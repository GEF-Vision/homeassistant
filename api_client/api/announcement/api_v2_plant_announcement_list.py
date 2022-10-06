from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.exception import Exception_
from ...models.paginated_announcement_list import PaginatedAnnouncementList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/{uuid}/announcement/".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Exception_, PaginatedAnnouncementList]]:
    if response.status_code == 200:
        response_200 = PaginatedAnnouncementList.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = Exception_.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Exception_.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Exception_, PaginatedAnnouncementList]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, str] = UNSET,
) -> Response[Union[Exception_, PaginatedAnnouncementList]]:
    """Fetch announcements related to the plant

    Args:
        uuid (str):
        cursor (Union[Unset, None, str]):

    Returns:
        Response[Union[Exception_, PaginatedAnnouncementList]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        cursor=cursor,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Exception_, PaginatedAnnouncementList]]:
    """Fetch announcements related to the plant

    Args:
        uuid (str):
        cursor (Union[Unset, None, str]):

    Returns:
        Response[Union[Exception_, PaginatedAnnouncementList]]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, str] = UNSET,
) -> Response[Union[Exception_, PaginatedAnnouncementList]]:
    """Fetch announcements related to the plant

    Args:
        uuid (str):
        cursor (Union[Unset, None, str]):

    Returns:
        Response[Union[Exception_, PaginatedAnnouncementList]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        cursor=cursor,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Exception_, PaginatedAnnouncementList]]:
    """Fetch announcements related to the plant

    Args:
        uuid (str):
        cursor (Union[Unset, None, str]):

    Returns:
        Response[Union[Exception_, PaginatedAnnouncementList]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            cursor=cursor,
        )
    ).parsed
