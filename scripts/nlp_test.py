#
# Some very rough NLP processing, mostly stolen from https://realpython.com/nltk-nlp-python/
#

import nltk
nltk.download('punkt')
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")

from nltk.tokenize import word_tokenize

ignore_set = {'(', ')', 'and', 'in', 'of', 'for', 'on', ',', '.', ';', '-', ':'}


# -------------- simple NLP experiments ------------

proj_name = """
FHIR DSTU Ballot (Jira PSS-1955)
V3 Nutrition Order Clinical Messages
HL7 Care Coordination Service (CCS)
Laboratory Order Interface IG (LOI IG) DSTU
"""

proj_words = word_tokenize(proj_name)
print("Project words:\n")
print(proj_words)
word_set = set(proj_words)
significant_words = word_set.difference(ignore_set)
print("Significant words:\n")
print(significant_words)

# Tag parts of speech
proj_tags = nltk.pos_tag(proj_words)

print(proj_tags)

grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(proj_tags)

tree = nltk.ne_chunk(proj_tags)
print(tree)
