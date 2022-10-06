from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.energymeter import Energymeter
from ...models.exception import Exception_
from ...models.patched_energymeter import PatchedEnergymeter
from ...types import Response


def _get_kwargs(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedEnergymeter,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/{plant_uuid}/device/energymeter/{id}/".format(client.base_url, plant_uuid=plant_uuid, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Energymeter, Exception_]]:
    if response.status_code == 200:
        response_200 = Energymeter.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = Exception_.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Exception_.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Energymeter, Exception_]]:
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
    json_body: PatchedEnergymeter,
) -> Response[Union[Energymeter, Exception_]]:
    """Update energymeter information

    Args:
        plant_uuid (str):
        id (int):
        json_body (PatchedEnergymeter):

    Returns:
        Response[Union[Energymeter, Exception_]]
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
    json_body: PatchedEnergymeter,
) -> Optional[Union[Energymeter, Exception_]]:
    """Update energymeter information

    Args:
        plant_uuid (str):
        id (int):
        json_body (PatchedEnergymeter):

    Returns:
        Response[Union[Energymeter, Exception_]]
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
    json_body: PatchedEnergymeter,
) -> Response[Union[Energymeter, Exception_]]:
    """Update energymeter information

    Args:
        plant_uuid (str):
        id (int):
        json_body (PatchedEnergymeter):

    Returns:
        Response[Union[Energymeter, Exception_]]
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
    json_body: PatchedEnergymeter,
) -> Optional[Union[Energymeter, Exception_]]:
    """Update energymeter information

    Args:
        plant_uuid (str):
        id (int):
        json_body (PatchedEnergymeter):

    Returns:
        Response[Union[Energymeter, Exception_]]
    """

    return (
        await asyncio_detailed(
            plant_uuid=plant_uuid,
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
