import json
from typing import Any, Dict, List, Optional, Tuple, Type, Union


class GithubException(Exception):
    """
    Error handling in PyGithub is done with exceptions. This class is the base of all exceptions raised by PyGithub
    (but :class:`github.GithubException.BadAttributeException`).

    Some other types of exceptions might be raised by underlying libraries, for example for network-related issues.

    """

    def __init__(
        self,
        status: int,
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        message: Optional[str] = None,
    ):
        super().__init__()
        self.__status = status
        self.__data = data
        self.__headers = headers
        self.__message = message
        self.args = (status, data, headers, message)

    @property
    def message(self) -> Optional[str]:
        return self.__message

    @property
    def status(self) -> int:
        """
        The status returned by the Github API.
        """
        return self.__status

    @property
    def data(self) -> Any:
        """
        The (decoded) data returned by the Github API.
        """
        return self.__data

    @property
    def headers(self) -> Optional[Dict[str, str]]:
        """
        The headers returned by the Github API.
        """
        return self.__headers

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__str__()})"

    def __str__(self) -> str:
        if self.__message:
            msg = f"{self.__message}: {self.status}"
        else:
            msg = f"{self.status}"

        if self.data is not None:
            msg += " " + json.dumps(self.data)

        return msg


class BadCredentialsException(GithubException):
    """
    Exception raised in case of bad credentials (when Github API replies with a 401 or 403 HTML status)
    """


class UnknownObjectException(GithubException):
    """
    Exception raised when a non-existing object is requested (when Github API replies with a 404 HTML status)
    """


class BadUserAgentException(GithubException):
    """
    Exception raised when request is sent with a bad user agent header (when Github API replies with a 403 bad user
    agent HTML status)
    """


class RateLimitExceededException(GithubException):
    """
    Exception raised when the rate limit is exceeded (when Github API replies with a 403 rate limit exceeded HTML
    status)
    """


class BadAttributeException(Exception):
    """
    Exception raised when Github returns an attribute with the wrong type.
    """

    def __init__(
        self,
        actualValue: Any,
        expectedType: Union[
            Dict[Tuple[Type[str], Type[str]], Type[dict]],
            Tuple[Type[str], Type[str]],
            List[Type[dict]],
            List[Tuple[Type[str], Type[str]]],
        ],
        transformationException: Optional[Exception],
    ):
        self.__actualValue = actualValue
        self.__expectedType = expectedType
        self.__transformationException = transformationException

    @property
    def actual_value(self) -> Any:
        """
        The value returned by Github.
        """
        return self.__actualValue

    @property
    def expected_type(
        self,
    ) -> Union[
        List[Type[dict]],
        Tuple[Type[str], Type[str]],
        Dict[Tuple[Type[str], Type[str]], Type[dict]],
        List[Tuple[Type[str], Type[str]]],
    ]:
        """
        The type PyGithub expected.
        """
        return self.__expectedType

    @property
    def transformation_exception(self) -> Optional[Exception]:
        """
        The exception raised when PyGithub tried to parse the value.
        """
        return self.__transformationException


class TwoFactorException(GithubException):
    """
    Exception raised when Github requires a onetime password for two-factor authentication.
    """


class IncompletableObject(GithubException):
    """
    Exception raised when we can not request an object from Github because the data returned did not include a URL.
    """
