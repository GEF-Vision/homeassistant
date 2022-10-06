from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.inverter import Inverter
from ...models.patched_inverter import PatchedInverter
from ...types import Response


def _get_kwargs(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedInverter,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/{plant_uuid}/device/inverter/{id}/".format(client.base_url, plant_uuid=plant_uuid, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Inverter]:
    if response.status_code == 200:
        response_200 = Inverter.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Inverter]:
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
    json_body: PatchedInverter,
) -> Response[Inverter]:
    """Update inverter information

    Args:
        plant_uuid (str):
        id (int):
        json_body (PatchedInverter):

    Returns:
        Response[Inverter]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        id=id,
        client=client,
        json_body=json_body,
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
    json_body: PatchedInverter,
) -> Optional[Inverter]:
    """Update inverter information

    Args:
        plant_uuid (str):
        id (int):
        json_body (PatchedInverter):

    Returns:
        Response[Inverter]
    """

    return sync_detailed(
        plant_uuid=plant_uuid,
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedInverter,
) -> Response[Inverter]:
    """Update inverter information

    Args:
        plant_uuid (str):
        id (int):
        json_body (PatchedInverter):

    Returns:
        Response[Inverter]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedInverter,
) -> Optional[Inverter]:
    """Update inverter information

    Args:
        plant_uuid (str):
        id (int):
        json_body (PatchedInverter):

    Returns:
        Response[Inverter]
    """

    return (
        await asyncio_detailed(
            plant_uuid=plant_uuid,
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
