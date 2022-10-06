from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.exception import Exception_
from ...models.panel_installation import PanelInstallation
from ...types import Response


def _get_kwargs(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/{plant_uuid}/panel/{id}/".format(client.base_url, plant_uuid=plant_uuid, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Exception_, PanelInstallation]]:
    if response.status_code == 200:
        response_200 = PanelInstallation.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = Exception_.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Exception_.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = Exception_.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Exception_, PanelInstallation]]:
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
) -> Response[Union[Exception_, PanelInstallation]]:
    """Get single panel group

    Args:
        plant_uuid (str):
        id (int):

    Returns:
        Response[Union[Exception_, PanelInstallation]]
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
) -> Optional[Union[Exception_, PanelInstallation]]:
    """Get single panel group

    Args:
        plant_uuid (str):
        id (int):

    Returns:
        Response[Union[Exception_, PanelInstallation]]
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
) -> Response[Union[Exception_, PanelInstallation]]:
    """Get single panel group

    Args:
        plant_uuid (str):
        id (int):

    Returns:
        Response[Union[Exception_, PanelInstallation]]
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
) -> Optional[Union[Exception_, PanelInstallation]]:
    """Get single panel group

    Args:
        plant_uuid (str):
        id (int):

    Returns:
        Response[Union[Exception_, PanelInstallation]]
    """

    return (
        await asyncio_detailed(
            plant_uuid=plant_uuid,
            id=id,
            client=client,
        )
    ).parsed
