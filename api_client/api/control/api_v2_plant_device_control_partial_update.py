from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.control import Control
from ...models.patched_control import PatchedControl
from ...types import Response


def _get_kwargs(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
    json_body: PatchedControl,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/{plant_uuid}/device/control/{id}/".format(client.base_url, plant_uuid=plant_uuid, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Control]:
    if response.status_code == 200:
        response_200 = Control.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Control]:
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
    json_body: PatchedControl,
) -> Response[Control]:
    """Update control information

    Args:
        plant_uuid (str):
        id (int):
        json_body (PatchedControl):

    Returns:
        Response[Control]
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
    json_body: PatchedControl,
) -> Optional[Control]:
    """Update control information

    Args:
        plant_uuid (str):
        id (int):
        json_body (PatchedControl):

    Returns:
        Response[Control]
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
    json_body: PatchedControl,
) -> Response[Control]:
    """Update control information

    Args:
        plant_uuid (str):
        id (int):
        json_body (PatchedControl):

    Returns:
        Response[Control]
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
    json_body: PatchedControl,
) -> Optional[Control]:
    """Update control information

    Args:
        plant_uuid (str):
        id (int):
        json_body (PatchedControl):

    Returns:
        Response[Control]
    """

    return (
        await asyncio_detailed(
            plant_uuid=plant_uuid,
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
