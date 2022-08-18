import re
import pandas as pd
import data_lib as lib
import data_tables as dt

# --------------- definitions -----------------
input_dir = "../resources/input/"
output_dir = "../resources/output/"
graph_output_dir = output_dir + "graphs/"


# --------------- helper functions --------------------

# replace all occurrences within 'str' of sub-strings in key col of a dictionary with val col string
def replace_strings(a_str, a_dict):
    for key, value in a_dict.items():
        # a_str = a_str.replace(key, value)
        a_str = re.sub(key, value, a_str, flags=re.IGNORECASE)
    return a_str


# generate an array containing every string in match_list that is found in a_str
# optionally insert a no-match value like 'NONE' or similar
def get_matches(a_str, match_list, no_match_value):
    result = []
    for term in match_list:
        if a_str.find(term) != -1:
            result.append(term)

    if no_match_value is not None and len(result) == 0:
        result.append(no_match_value)

    return result


# ----------- single argument lambdas based on above funcs ----------
def fix_strings(s):
    return replace_strings(s, dt.proj_name_replaces)


def get_domain_matches(a_str):
    return get_matches(a_str, dt.domains, 'NONE')


def get_supertopic_matches(a_str):
    super_topics = dt.domains.copy()
    super_topics.extend(dt.topics)
    super_topics.extend(dt.artefacts)
    return get_matches(a_str, super_topics, 'NONE')


def get_topic_matches(a_str):
    return get_matches(a_str, dt.topics, 'NONE')


def get_artefact_matches(a_str):
    return get_matches(a_str, dt.artefacts, 'NONE')


def get_funder_matches(a_str):
    return get_matches(a_str, dt.funders, 'NONE')


# -------------------- main --------------------
# Read the file
data = pd.read_csv(input_dir + "hl7_source.csv", sep=';', low_memory=False)

# fix some column names
data.rename(columns={'Number': 'Id'}, inplace=True)
data.rename(columns={'Sponsor(s)': 'Sponsors'}, inplace=True)
data.rename(columns={'Co-Sponsor(s)': 'Co_sponsors'}, inplace=True)
data.rename(columns={'Common Names / Keywords / Aliases': 'Aliases'}, inplace=True)
data.rename(columns={'Project Facilitator': 'Facilitator'}, inplace=True)

# Set Id col as index
data.set_index('Id')

# Output the number of rows
print("Total rows: {0}".format(len(data)))

# See which headers are available
print("Columns:", list(data))

# check the dtypes
print("Raw Dtypes:\n", data.dtypes)

# Convert Dtypes
data_typed = data.convert_dtypes()
print("Converted Dtypes:\n", data_typed.dtypes)

# archived projects
archived_projects = data_typed[data_typed.Status == "Archived"]
print("archived projects: {0}".format(len(archived_projects)))

# keep live projects only
lp = data_typed[data_typed.Status != "Archived"]
print("Live projects: {0}".format(len(lp)))

# Add a Label column that is the same as the project id, for use in Gephi,
# to avoid using looooong project names
labels = lp['Id'].copy()
lp.insert(loc=1, column="Label", value=labels)

# output whole data frame
lp.to_csv(output_dir + "hl7_out.csv", sep=';', index=False)

# ======== build data frames for specific relations of project x other col ========

# Generate dataframe {proj_id, sponsor}
proj_sponsors = lib.dataframe_view(source_data_frame=lp, col_name='Sponsors', string_dict=dt.org_unit_short_names)
proj_sponsors['Weight'] = 2.0

# Generate dataframe {proj_id, co-sponsor}
proj_co_sponsors = lib.dataframe_view(source_data_frame=lp, col_name='Co_sponsors', replace_empty=False,
                                      string_dict=dt.org_unit_short_names)
proj_co_sponsors['Weight'] = 1.0

# Generate dataframe {proj_id, products}
proj_products = lib.dataframe_view(source_data_frame=lp, col_name='Products', sep=';',
                                   string_dict=dt.product_short_names)
proj_products['Weight'] = 1.0

# Generate dataframe {proj_id, facilitator}
proj_facilitator = lib.dataframe_view(source_data_frame=lp, col_name='Facilitator')
proj_facilitator['Weight'] = 1.0

# Generate dataframe {proj_id, type}
proj_type = lib.dataframe_view(source_data_frame=lp, col_name='Type', explode=False)
proj_type['Weight'] = 1.0

# ========= generate various Nodes & Edges file sets ==========

# Projects as nodes, add a 'Cat' (category) field to mark them
# as projects
proj_nodes = lp[['Id', 'Label']].copy()
proj_nodes.drop_duplicates(inplace=True)
proj_nodes['Cat'] = 'project'

# Create a combined frame in which Co-sponsors are added in under Sponsors col
proj_sponsors_frame = proj_sponsors.copy()
proj_co_sponsors_frame = proj_co_sponsors.copy()
proj_co_sponsors_frame.rename(columns={'Co_sponsors': 'Sponsors'}, inplace=True)
all_proj_sponsors = pd.concat([proj_sponsors_frame, proj_co_sponsors_frame])

# Projs x Sponsors Nodes & Edges
lib.generate_nodes_edges(all_proj_sponsors, proj_nodes, graph_output_dir)

# Projs x Products Nodes & Edges
lib.generate_nodes_edges(proj_products, proj_nodes, graph_output_dir)

# Projs x Facilitator Nodes & Edges
lib.generate_nodes_edges(proj_facilitator, proj_nodes, graph_output_dir)

# Projs x Type Nodes & Edges
lib.generate_nodes_edges(proj_type, proj_nodes, graph_output_dir)

# ======== Topic analysis on project name field =========

# output just project names col, to create a text corpus
proj_names_df = lp[['Id', 'Name']].copy()
proj_names_df.to_csv(output_dir + "/proj_names.csv", sep=';', index=False)

# first do some string replacing to map variants to a single target
proj_names_df['Name'] = proj_names_df['Name'].transform(fix_strings)
proj_names_df.to_csv(output_dir + "proj_names_rep.csv", sep=';', index=False)

# create a topics DF -add a column for Topic and default to UNK
match_df = proj_names_df.copy()
match_df['Name'] = match_df['Name'].transform(get_supertopic_matches)
match_df = match_df.explode('Name')
match_df.rename(columns={'Name': 'Topic'}, inplace=True)
match_df['Weight'] = 1.0

match_df.to_csv(output_dir + "proj_names_topics.csv", sep=';', index=False)
# Projs x topics Nodes & Edges
lib.generate_nodes_edges(match_df, proj_nodes, graph_output_dir)


# ====== External funder (ONC / DaVinci / None) analysis on project name field =======

# create a external funder DF -add a column for Funder and default to NONE
match_df = proj_names_df.copy()
match_df['Name'] = match_df['Name'].transform(get_funder_matches)
match_df = match_df.explode('Name')
match_df.rename(columns={'Name': 'Funder'}, inplace=True)
match_df['Weight'] = 1.0

match_df.to_csv(output_dir + "proj_names_funders.csv", sep=';', index=False)
# Projs x funders Nodes & Edges
lib.generate_nodes_edges(match_df, proj_nodes, graph_output_dir)

