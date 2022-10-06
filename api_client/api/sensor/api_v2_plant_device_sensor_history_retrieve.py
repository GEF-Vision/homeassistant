import datetime
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.api_v2_plant_device_sensor_history_retrieve_period import ApiV2PlantDeviceSensorHistoryRetrievePeriod
from ...models.api_v2_plant_device_sensor_history_retrieve_response_format import (
    ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat,
)
from ...models.exception import Exception_
from ...models.history_response import HistoryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    plant_uuid: str,
    sensor_type: str,
    id: int,
    *,
    client: AuthenticatedClient,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    format_: Union[
        Unset, None, ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat
    ] = ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat.JSON,
    period: Union[
        Unset, None, ApiV2PlantDeviceSensorHistoryRetrievePeriod
    ] = ApiV2PlantDeviceSensorHistoryRetrievePeriod.VALUE_1,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/{plant_uuid}/device/sensor/{sensor_type}/{id}/history/".format(
        client.base_url, plant_uuid=plant_uuid, sensor_type=sensor_type, id=id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_end: Union[Unset, None, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat() if end else None

    params["end"] = json_end

    json_format_: Union[Unset, None, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value if format_ else None

    params["format"] = json_format_

    json_period: Union[Unset, None, str] = UNSET
    if not isinstance(period, Unset):
        json_period = period.value if period else None

    params["period"] = json_period

    json_start: Union[Unset, None, str] = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat() if start else None

    params["start"] = json_start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Exception_, HistoryResponse]]:
    if response.status_code == 200:
        response_200 = HistoryResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = Exception_.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Exception_.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Exception_, HistoryResponse]]:
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
    end: Union[Unset, None, datetime.datetime] = UNSET,
    format_: Union[
        Unset, None, ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat
    ] = ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat.JSON,
    period: Union[
        Unset, None, ApiV2PlantDeviceSensorHistoryRetrievePeriod
    ] = ApiV2PlantDeviceSensorHistoryRetrievePeriod.VALUE_1,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Union[Exception_, HistoryResponse]]:
    """Fetch sensor history

    Args:
        plant_uuid (str):
        sensor_type (str):
        id (int):
        end (Union[Unset, None, datetime.datetime]):
        format_ (Union[Unset, None, ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat]):
            Default: ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat.JSON.
        period (Union[Unset, None, ApiV2PlantDeviceSensorHistoryRetrievePeriod]):  Default:
            ApiV2PlantDeviceSensorHistoryRetrievePeriod.VALUE_1.
        start (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[Union[Exception_, HistoryResponse]]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        sensor_type=sensor_type,
        id=id,
        client=client,
        end=end,
        format_=format_,
        period=period,
        start=start,
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
    end: Union[Unset, None, datetime.datetime] = UNSET,
    format_: Union[
        Unset, None, ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat
    ] = ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat.JSON,
    period: Union[
        Unset, None, ApiV2PlantDeviceSensorHistoryRetrievePeriod
    ] = ApiV2PlantDeviceSensorHistoryRetrievePeriod.VALUE_1,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Union[Exception_, HistoryResponse]]:
    """Fetch sensor history

    Args:
        plant_uuid (str):
        sensor_type (str):
        id (int):
        end (Union[Unset, None, datetime.datetime]):
        format_ (Union[Unset, None, ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat]):
            Default: ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat.JSON.
        period (Union[Unset, None, ApiV2PlantDeviceSensorHistoryRetrievePeriod]):  Default:
            ApiV2PlantDeviceSensorHistoryRetrievePeriod.VALUE_1.
        start (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[Union[Exception_, HistoryResponse]]
    """

    return sync_detailed(
        plant_uuid=plant_uuid,
        sensor_type=sensor_type,
        id=id,
        client=client,
        end=end,
        format_=format_,
        period=period,
        start=start,
    ).parsed


async def asyncio_detailed(
    plant_uuid: str,
    sensor_type: str,
    id: int,
    *,
    client: AuthenticatedClient,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    format_: Union[
        Unset, None, ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat
    ] = ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat.JSON,
    period: Union[
        Unset, None, ApiV2PlantDeviceSensorHistoryRetrievePeriod
    ] = ApiV2PlantDeviceSensorHistoryRetrievePeriod.VALUE_1,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Union[Exception_, HistoryResponse]]:
    """Fetch sensor history

    Args:
        plant_uuid (str):
        sensor_type (str):
        id (int):
        end (Union[Unset, None, datetime.datetime]):
        format_ (Union[Unset, None, ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat]):
            Default: ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat.JSON.
        period (Union[Unset, None, ApiV2PlantDeviceSensorHistoryRetrievePeriod]):  Default:
            ApiV2PlantDeviceSensorHistoryRetrievePeriod.VALUE_1.
        start (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[Union[Exception_, HistoryResponse]]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        sensor_type=sensor_type,
        id=id,
        client=client,
        end=end,
        format_=format_,
        period=period,
        start=start,
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
    end: Union[Unset, None, datetime.datetime] = UNSET,
    format_: Union[
        Unset, None, ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat
    ] = ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat.JSON,
    period: Union[
        Unset, None, ApiV2PlantDeviceSensorHistoryRetrievePeriod
    ] = ApiV2PlantDeviceSensorHistoryRetrievePeriod.VALUE_1,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Union[Exception_, HistoryResponse]]:
    """Fetch sensor history

    Args:
        plant_uuid (str):
        sensor_type (str):
        id (int):
        end (Union[Unset, None, datetime.datetime]):
        format_ (Union[Unset, None, ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat]):
            Default: ApiV2PlantDeviceSensorHistoryRetrieveResponseFormat.JSON.
        period (Union[Unset, None, ApiV2PlantDeviceSensorHistoryRetrievePeriod]):  Default:
            ApiV2PlantDeviceSensorHistoryRetrievePeriod.VALUE_1.
        start (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[Union[Exception_, HistoryResponse]]
    """

    return (
        await asyncio_detailed(
            plant_uuid=plant_uuid,
            sensor_type=sensor_type,
            id=id,
            client=client,
            end=end,
            format_=format_,
            period=period,
            start=start,
        )
    ).parsed
