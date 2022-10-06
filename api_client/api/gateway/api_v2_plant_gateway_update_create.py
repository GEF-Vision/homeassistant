from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.exception import Exception_
from ...types import Response


def _get_kwargs(
    plant_uuid: str,
    serial_number: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/{plant_uuid}/gateway/{serial_number}/update/".format(
        client.base_url, plant_uuid=plant_uuid, serial_number=serial_number
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Exception_]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 404:
        response_404 = Exception_.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Exception_]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    plant_uuid: str,
    serial_number: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Exception_]]:
    """Update gateway

     Initiates gateway firmware update, if newer is available.

    Args:
        plant_uuid (str):
        serial_number (str):

    Returns:
        Response[Union[Any, Exception_]]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        serial_number=serial_number,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    plant_uuid: str,
    serial_number: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Exception_]]:
    """Update gateway

     Initiates gateway firmware update, if newer is available.

    Args:
        plant_uuid (str):
        serial_number (str):

    Returns:
        Response[Union[Any, Exception_]]
    """

    return sync_detailed(
        plant_uuid=plant_uuid,
        serial_number=serial_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    plant_uuid: str,
    serial_number: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, Exception_]]:
    """Update gateway

     Initiates gateway firmware update, if newer is available.

    Args:
        plant_uuid (str):
        serial_number (str):

    Returns:
        Response[Union[Any, Exception_]]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        serial_number=serial_number,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    plant_uuid: str,
    serial_number: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, Exception_]]:
    """Update gateway

     Initiates gateway firmware update, if newer is available.

    Args:
        plant_uuid (str):
        serial_number (str):

    Returns:
        Response[Union[Any, Exception_]]
    """

    return (
        await asyncio_detailed(
            plant_uuid=plant_uuid,
            serial_number=serial_number,
            client=client,
        )
    ).parsed
