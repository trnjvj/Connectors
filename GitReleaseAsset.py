from __future__ import annotations

from datetime import datetime
from typing import Any

import github.NamedUser
from github.GithubObject import Attribute, CompletableGithubObject, NotSet


class GitReleaseAsset(CompletableGithubObject):
    """
    This class represents GitReleaseAssets.

    The reference can be found here
    https://docs.github.com/en/rest/reference/repos#releases

    """

    def _initAttributes(self) -> None:
        self._url: Attribute[str] = NotSet
        self._id: Attribute[int] = NotSet
        self._name: Attribute[str] = NotSet
        self._label: Attribute[str] = NotSet
        self._content_type: Attribute[str] = NotSet
        self._state: Attribute[str] = NotSet
        self._size: Attribute[int] = NotSet
        self._download_count: Attribute[int] = NotSet
        self._created_at: Attribute[datetime] = NotSet
        self._updated_at: Attribute[datetime] = NotSet
        self._browser_download_url: Attribute[str] = NotSet
        self._uploader: Attribute[github.NamedUser.NamedUser] = NotSet

    def __repr__(self) -> str:
        return self.get__repr__({"url": self.url})

    @property
    def url(self) -> str:
        self._completeIfNotSet(self._url)
        return self._url.value

    @property
    def id(self) -> int:
        self._completeIfNotSet(self._id)
        return self._id.value

    @property
    def name(self) -> str:
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def label(self) -> str:
        self._completeIfNotSet(self._label)
        return self._label.value

    @property
    def content_type(self) -> str:
        self._completeIfNotSet(self._content_type)
        return self._content_type.value

    @property
    def state(self) -> str:
        self._completeIfNotSet(self._state)
        return self._state.value

    @property
    def size(self) -> int:
        self._completeIfNotSet(self._size)
        return self._size.value

    @property
    def download_count(self) -> int:
        self._completeIfNotSet(self._download_count)
        return self._download_count.value

    @property
    def created_at(self) -> datetime:
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def updated_at(self) -> datetime:
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def browser_download_url(self) -> str:
        self._completeIfNotSet(self._browser_download_url)
        return self._browser_download_url.value

    @property
    def uploader(self) -> github.NamedUser.NamedUser:
        self._completeIfNotSet(self._uploader)
        return self._uploader.value

    def delete_asset(self) -> bool:
        """
        Delete asset from the release.
        """
        headers, data = self._requester.requestJsonAndCheck("DELETE", self.url)
        return True

    def update_asset(self, name: str, label: str = "") -> GitReleaseAsset:
        """
        Update asset metadata.
        """
        assert isinstance(name, str), name
        assert isinstance(label, str), label
        post_parameters = {"name": name, "label": label}
        headers, data = self._requester.requestJsonAndCheck("PATCH", self.url, input=post_parameters)
        return GitReleaseAsset(self._requester, headers, data, completed=True)

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        if "url" in attributes:  # pragma no branch
            self._url = self._makeStringAttribute(attributes["url"])
        if "id" in attributes:  # pragma no branch
            self._id = self._makeIntAttribute(attributes["id"])
        if "name" in attributes:  # pragma no branch
            self._name = self._makeStringAttribute(attributes["name"])
        if "label" in attributes:  # pragma no branch
            self._label = self._makeStringAttribute(attributes["label"])
        if "uploader" in attributes:  # pragma no branch
            self._uploader = self._makeClassAttribute(github.NamedUser.NamedUser, attributes["uploader"])
        if "content_type" in attributes:  # pragma no branch
            self._content_type = self._makeStringAttribute(attributes["content_type"])
        if "state" in attributes:  # pragma no branch
            self._state = self._makeStringAttribute(attributes["state"])
        if "size" in attributes:  # pragma no branch
            self._size = self._makeIntAttribute(attributes["size"])
        if "download_count" in attributes:  # pragma no branch
            self._download_count = self._makeIntAttribute(attributes["download_count"])
        if "created_at" in attributes:  # pragma no branch
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "updated_at" in attributes:  # pragma no branch
            self._updated_at = self._makeDatetimeAttribute(attributes["updated_at"])
        if "browser_download_url" in attributes:  # pragma no branch
            self._browser_download_url = self._makeStringAttribute(attributes["browser_download_url"])
