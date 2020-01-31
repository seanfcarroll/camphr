from pathlib import Path
from typing import Any, Callable, Iterable, Iterator, List, Optional, Sequence, Union

from spacy.gold import GoldParse
from spacy.tokens.doc import Doc

from spacy.vocab import Vocab

from spacy.language import Language

class Pipe:
    name: Union[str]
    @classmethod
    def from_nlp(cls, nlp: Language, **cfg) -> "Pipe": ...
    def __init__(self, vocab: Vocab, model=True, **cfg): ...
    def __call__(self, doc: Doc): ...
    def require_model(self): ...
    def update(self, docs: Iterable[Doc], golds: Iterable[GoldParse], **kwargs): ...

class DependencyParser: ...
class EntityLinker: ...
class EntityRecognizer: ...

class Sentencizer:
    def __init__(self, punct_chars: Optional[List[str]] = None) -> None: ...

class Tagger: ...
class Tensorizer: ...
class TextCategorizer: ...

