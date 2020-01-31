"""
This type stub file was generated by pyright.
"""

from ..language import component

@component("merge_noun_chunks", requires=["token.dep", "token.tag", "token.pos"], retokenizes=True)
def merge_noun_chunks(doc):
    """Merge noun chunks into a single token.

    doc (Doc): The Doc object.
    RETURNS (Doc): The Doc object with merged noun chunks.

    DOCS: https://spacy.io/api/pipeline-functions#merge_noun_chunks
    """
    ...

@component("merge_entities", requires=["doc.ents", "token.ent_iob", "token.ent_type"], retokenizes=True)
def merge_entities(doc):
    """Merge entities into a single token.

    doc (Doc): The Doc object.
    RETURNS (Doc): The Doc object with merged entities.

    DOCS: https://spacy.io/api/pipeline-functions#merge_entities
    """
    ...

@component("merge_subtokens", requires=["token.dep"], retokenizes=True)
def merge_subtokens(doc, label=...):
    """Merge subtokens into a single token.

    doc (Doc): The Doc object.
    label (unicode): The subtoken dependency label.
    RETURNS (Doc): The Doc object with merged subtokens.

    DOCS: https://spacy.io/api/pipeline-functions#merge_subtokens
    """
    ...

