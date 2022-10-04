from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_plant_list import PaginatedPlantList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedPlantList]:
    if response.status_code == 200:
        response_200 = PaginatedPlantList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedPlantList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedPlantList]:
    """List all plants

    Args:
        cursor (Union[Unset, None, str]):

    Returns:
        Response[PaginatedPlantList]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedPlantList]:
    """List all plants

    Args:
        cursor (Union[Unset, None, str]):

    Returns:
        Response[PaginatedPlantList]
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedPlantList]:
    """List all plants

    Args:
        cursor (Union[Unset, None, str]):

    Returns:
        Response[PaginatedPlantList]
    """

    kwargs = _get_kwargs(
        client=client,
        cursor=cursor,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedPlantList]:
    """List all plants

    Args:
        cursor (Union[Unset, None, str]):

    Returns:
        Response[PaginatedPlantList]
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
        )
    ).parsed
