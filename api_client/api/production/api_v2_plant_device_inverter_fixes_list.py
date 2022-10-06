from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.exception import Exception_
from ...models.fix_suggestion import FixSuggestion
from ...types import Response


def _get_kwargs(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/{plant_uuid}/device/inverter/{id}/fixes/".format(
        client.base_url, plant_uuid=plant_uuid, id=id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Exception_, List[FixSuggestion]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FixSuggestion.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 404:
        response_404 = Exception_.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Exception_, List[FixSuggestion]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Exception_, List[FixSuggestion]]]:
    """Suggested fixes

     Get suggested fixes for issues with inverter.

    Args:
        plant_uuid (str):
        id (int):

    Returns:
        Response[Union[Exception_, List[FixSuggestion]]]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Exception_, List[FixSuggestion]]]:
    """Suggested fixes

     Get suggested fixes for issues with inverter.

    Args:
        plant_uuid (str):
        id (int):

    Returns:
        Response[Union[Exception_, List[FixSuggestion]]]
    """

    return sync_detailed(
        plant_uuid=plant_uuid,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Exception_, List[FixSuggestion]]]:
    """Suggested fixes

     Get suggested fixes for issues with inverter.

    Args:
        plant_uuid (str):
        id (int):

    Returns:
        Response[Union[Exception_, List[FixSuggestion]]]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Exception_, List[FixSuggestion]]]:
    """Suggested fixes

     Get suggested fixes for issues with inverter.

    Args:
        plant_uuid (str):
        id (int):

    Returns:
        Response[Union[Exception_, List[FixSuggestion]]]
    """

    return (
        await asyncio_detailed(
            plant_uuid=plant_uuid,
            id=id,
            client=client,
        )
    ).parsed
