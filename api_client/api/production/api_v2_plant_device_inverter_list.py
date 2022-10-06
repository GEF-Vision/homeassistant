from typing import Any, Dict, List, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.inverter import Inverter
from ...types import Response


def _get_kwargs(
    plant_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/{plant_uuid}/device/inverter/".format(client.base_url, plant_uuid=plant_uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Inverter]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Inverter.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Inverter]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    plant_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[List[Inverter]]:
    """List all inverters

    Args:
        plant_uuid (str):

    Returns:
        Response[List[Inverter]]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    plant_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List[Inverter]]:
    """List all inverters

    Args:
        plant_uuid (str):

    Returns:
        Response[List[Inverter]]
    """

    return sync_detailed(
        plant_uuid=plant_uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    plant_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[List[Inverter]]:
    """List all inverters

    Args:
        plant_uuid (str):

    Returns:
        Response[List[Inverter]]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    plant_uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List[Inverter]]:
    """List all inverters

    Args:
        plant_uuid (str):

    Returns:
        Response[List[Inverter]]
    """

    return (
        await asyncio_detailed(
            plant_uuid=plant_uuid,
            client=client,
        )
    ).parsed
