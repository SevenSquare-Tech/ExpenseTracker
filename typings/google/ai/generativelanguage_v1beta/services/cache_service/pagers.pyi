"""
This type stub file was generated by pyright.
"""

from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence, Tuple, Union
from google.ai.generativelanguage_v1beta.types import cache_service, cached_content

"""
This type stub file was generated by pyright.
"""
OptionalRetry = ...
OptionalAsyncRetry = ...
class ListCachedContentsPager:
    """A pager for iterating through ``list_cached_contents`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListCachedContentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``cached_contents`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCachedContents`` requests and continue to iterate
    through the ``cached_contents`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListCachedContentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., cache_service.ListCachedContentsResponse], request: cache_service.ListCachedContentsRequest, response: cache_service.ListCachedContentsResponse, *, retry: OptionalRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListCachedContentsRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListCachedContentsResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    def pages(self) -> Iterator[cache_service.ListCachedContentsResponse]:
        ...
    
    def __iter__(self) -> Iterator[cached_content.CachedContent]:
        ...
    
    def __repr__(self) -> str:
        ...
    


class ListCachedContentsAsyncPager:
    """A pager for iterating through ``list_cached_contents`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListCachedContentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``cached_contents`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCachedContents`` requests and continue to iterate
    through the ``cached_contents`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListCachedContentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., Awaitable[cache_service.ListCachedContentsResponse]], request: cache_service.ListCachedContentsRequest, response: cache_service.ListCachedContentsResponse, *, retry: OptionalAsyncRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListCachedContentsRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListCachedContentsResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    async def pages(self) -> AsyncIterator[cache_service.ListCachedContentsResponse]:
        ...
    
    def __aiter__(self) -> AsyncIterator[cached_content.CachedContent]:
        ...
    
    def __repr__(self) -> str:
        ...
    


