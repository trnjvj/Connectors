
from __future__ import annotations

from typing import TYPE_CHECKING, Any

import github.GitTreeElement
from github.GithubObject import Attribute, CompletableGithubObject, NotSet

if TYPE_CHECKING:
    from github.GitTreeElement import GitTreeElement


class GitTree(CompletableGithubObject):
    """
    This class represents GitTrees.

    The reference can be found here
    https://docs.github.com/en/rest/reference/git#trees

    """

    def _initAttributes(self) -> None:
        self._sha: Attribute[str] = NotSet
        self._tree: Attribute[list[GitTreeElement]] = NotSet
        self._url: Attribute[str] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"sha": self._sha.value})

    @property
    def sha(self) -> str:
        self._completeIfNotSet(self._sha)
        return self._sha.value

    @property
    def tree(self) -> list[GitTreeElement]:
        self._completeIfNotSet(self._tree)
        return self._tree.value

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def _identity(self) -> str:
        return self.sha

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "sha" in attributes:  # pragma no branch
            self._sha = self._makeStringAttribute(attributes["sha"])
        if "tree" in attributes:  # pragma no branch
            self._tree = self._makeListOfClassesAttribute(github.GitTreeElement.GitTreeElement, attributes["tree"])
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
