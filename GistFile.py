from typing import Any, Dict

from github.GithubObject import Attribute, NonCompletableGithubObject, NotSet


class GistFile(NonCompletableGithubObject):
    """
    This class represents GistFiles.
    """

    def _initAttributes(self) -> None:
        self._content: Attribute[str] = NotSet
        self._filename: Attribute[str] = NotSet
        self._language: Attribute[str] = NotSet
        self._raw_url: Attribute[str] = NotSet
        self._size: Attribute[int] = NotSet
        self._type: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"filename": self._filename.value})

    @property
    def content(self) -> str:
        return self._content.value

    @property
    def filename(self) -> str:
        return self._filename.value

    @property
    def language(self) -> str:
        return self._language.value

    @property
    def raw_url(self) -> str:
        return self._raw_url.value

    @property
    def size(self) -> int:
        return self._size.value

    @property
    def type(self) -> str:
        return self._type.value

    def _useAttributes(self, attributes: Dict[str, Any]) -> None:
        if "content" in attributes:  # pragma no branch
            self._content = self._makeStringAttribute(attributes["content"])
        if "filename" in attributes:  # pragma no branch
            self._filename = self._makeStringAttribute(attributes["filename"])
        if "language" in attributes:  # pragma no branch
            self._language = self._makeStringAttribute(attributes["language"])
        if "raw_url" in attributes:  # pragma no branch
            self._raw_url = self._makeStringAttribute(attributes["raw_url"])
        if "size" in attributes:  # pragma no branch
            self._size = self._makeIntAttribute(attributes["size"])
        if "type" in attributes:  # pragma no branch
            self._type = self._makeStringAttribute(attributes["type"])
