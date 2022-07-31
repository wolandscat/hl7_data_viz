import pandas as pd

#
# Generate dataframe {proj_id, X}
# This extracts a view from a source data-frame representing the full data-set
# into a data-frame consisting only of the Id column, and one other
# nominated column. The latter column may contain comma- or semicolon-
# separated multiple values, so we may need to 'explode' those values
# out into separate rows; controlled by the 'explode' flag.
#
# We can also do some string replacements as well, to make the data
# less voluminous in the visualisation tool - the string_dict parameter
# may be supplied in this case
#
def dataframe_view(source_data_frame, col_name, replace_empty=True, explode=True, sep=',', string_dict=None):
    # initial extract
    result = source_data_frame[['Id', col_name]].copy()

    # fill right-hand col with 'UNK' if empty, ,or else remove rows with empty RH col
    if replace_empty:
        result.fillna(value='UNK', inplace=True)
    else:
        result.dropna(axis=0, how='any', inplace=True)

    if explode:
        # convert values of form String 'x, y, z' into [x, y, z]
        result[col_name] = result[col_name].str.split(sep)

        # generate row per item from those arrays
        result = result.explode(col_name)

    # get rid of leading and trailing space
    result[col_name] = result[col_name].str.strip()

    if string_dict is not None:
        result.replace({col_name: string_dict}, inplace=True)

    return result


#
# generate 2-mode Projs x Col Nodes & Edges CSV files for a tool such as Gephi.
# '2-mode' means that there are 2 kinds of entities, here, projects and one other
# that is in the right-hand column of the 'col_frame'.
#
# col_frame is a data frame of {Id, xxx, Weight}, where xxx is some
# other column from original data set.
#
# Nodes file is of form {Id, Label, cat}, where Id and Label are made identical
#     and 'cat' marks each node as either 'project' or the other kind of entity
#     It will contain project rows and rows of another entity kind.
#
# Edges file is of form {Source, Target, Weight}
#
def generate_nodes_edges(col_frame, ref_nodes_frame, output_dir):
    # get the col name of interest
    col_name = col_frame.columns[1]

    # extract col X and duplicate it into 'Id' and 'Label' cols,
    # then add a 'Cat' col
    col_nodes = col_frame[col_name].copy()
    col_nodes_unique = col_nodes.unique()
    col_nodes_frame = pd.DataFrame(data={'Id': col_nodes_unique,
                                         'Label': col_nodes_unique.copy()})
    col_nodes_frame['Cat'] = col_name

    # append these nodes to the reference nodes, i.e. 'Project'
    node_frame = pd.concat([ref_nodes_frame, col_nodes_frame])
    node_frame.to_csv(output_dir + "nodes_" + col_name.lower() + ".csv", sep=';', index=False)

    edges_frame = col_frame.copy()
    edges_frame.rename(columns={'Id': 'Source'}, inplace=True)
    edges_frame.rename(columns={col_name: 'Target'}, inplace=True)
    edges_frame.drop_duplicates(inplace=True)
    edges_frame.to_csv(output_dir + "edges_" + col_name.lower() + ".csv", sep=';', index=False)
