from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.sensor import Sensor
from ...types import Response


def _get_kwargs(
    plant_uuid: str,
    sensor_type: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/{plant_uuid}/device/sensor/{sensor_type}/{id}/".format(
        client.base_url, plant_uuid=plant_uuid, sensor_type=sensor_type, id=id
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


def _parse_response(*, response: httpx.Response) -> Optional[Sensor]:
    if response.status_code == 200:
        response_200 = Sensor.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Sensor]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    plant_uuid: str,
    sensor_type: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Sensor]:
    """Get single sensor

    Args:
        plant_uuid (str):
        sensor_type (str):
        id (int):

    Returns:
        Response[Sensor]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        sensor_type=sensor_type,
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
    sensor_type: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Sensor]:
    """Get single sensor

    Args:
        plant_uuid (str):
        sensor_type (str):
        id (int):

    Returns:
        Response[Sensor]
    """

    return sync_detailed(
        plant_uuid=plant_uuid,
        sensor_type=sensor_type,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    plant_uuid: str,
    sensor_type: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Sensor]:
    """Get single sensor

    Args:
        plant_uuid (str):
        sensor_type (str):
        id (int):

    Returns:
        Response[Sensor]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        sensor_type=sensor_type,
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    plant_uuid: str,
    sensor_type: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Sensor]:
    """Get single sensor

    Args:
        plant_uuid (str):
        sensor_type (str):
        id (int):

    Returns:
        Response[Sensor]
    """

    return (
        await asyncio_detailed(
            plant_uuid=plant_uuid,
            sensor_type=sensor_type,
            id=id,
            client=client,
        )
    ).parsed
