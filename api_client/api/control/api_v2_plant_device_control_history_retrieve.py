import datetime
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.api_v2_plant_device_control_history_retrieve_period import ApiV2PlantDeviceControlHistoryRetrievePeriod
from ...models.api_v2_plant_device_control_history_retrieve_response_format import (
    ApiV2PlantDeviceControlHistoryRetrieveResponseFormat,
)
from ...models.history_response import HistoryResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    plant_uuid: str,
    *,
    client: AuthenticatedClient,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    format_: Union[
        Unset, None, ApiV2PlantDeviceControlHistoryRetrieveResponseFormat
    ] = ApiV2PlantDeviceControlHistoryRetrieveResponseFormat.JSON,
    period: Union[
        Unset, None, ApiV2PlantDeviceControlHistoryRetrievePeriod
    ] = ApiV2PlantDeviceControlHistoryRetrievePeriod.VALUE_1,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/{plant_uuid}/device/control/history/".format(client.base_url, plant_uuid=plant_uuid)

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


def _parse_response(*, response: httpx.Response) -> Optional[HistoryResponse]:
    if response.status_code == 200:
        response_200 = HistoryResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[HistoryResponse]:
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
    end: Union[Unset, None, datetime.datetime] = UNSET,
    format_: Union[
        Unset, None, ApiV2PlantDeviceControlHistoryRetrieveResponseFormat
    ] = ApiV2PlantDeviceControlHistoryRetrieveResponseFormat.JSON,
    period: Union[
        Unset, None, ApiV2PlantDeviceControlHistoryRetrievePeriod
    ] = ApiV2PlantDeviceControlHistoryRetrievePeriod.VALUE_1,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[HistoryResponse]:
    """Fetch control history

     Fetches control history. 0 = unknown, 1 = off, 2 = on

    Args:
        plant_uuid (str):
        end (Union[Unset, None, datetime.datetime]):
        format_ (Union[Unset, None, ApiV2PlantDeviceControlHistoryRetrieveResponseFormat]):
            Default: ApiV2PlantDeviceControlHistoryRetrieveResponseFormat.JSON.
        period (Union[Unset, None, ApiV2PlantDeviceControlHistoryRetrievePeriod]):  Default:
            ApiV2PlantDeviceControlHistoryRetrievePeriod.VALUE_1.
        start (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[HistoryResponse]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
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
    *,
    client: AuthenticatedClient,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    format_: Union[
        Unset, None, ApiV2PlantDeviceControlHistoryRetrieveResponseFormat
    ] = ApiV2PlantDeviceControlHistoryRetrieveResponseFormat.JSON,
    period: Union[
        Unset, None, ApiV2PlantDeviceControlHistoryRetrievePeriod
    ] = ApiV2PlantDeviceControlHistoryRetrievePeriod.VALUE_1,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[HistoryResponse]:
    """Fetch control history

     Fetches control history. 0 = unknown, 1 = off, 2 = on

    Args:
        plant_uuid (str):
        end (Union[Unset, None, datetime.datetime]):
        format_ (Union[Unset, None, ApiV2PlantDeviceControlHistoryRetrieveResponseFormat]):
            Default: ApiV2PlantDeviceControlHistoryRetrieveResponseFormat.JSON.
        period (Union[Unset, None, ApiV2PlantDeviceControlHistoryRetrievePeriod]):  Default:
            ApiV2PlantDeviceControlHistoryRetrievePeriod.VALUE_1.
        start (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[HistoryResponse]
    """

    return sync_detailed(
        plant_uuid=plant_uuid,
        client=client,
        end=end,
        format_=format_,
        period=period,
        start=start,
    ).parsed


async def asyncio_detailed(
    plant_uuid: str,
    *,
    client: AuthenticatedClient,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    format_: Union[
        Unset, None, ApiV2PlantDeviceControlHistoryRetrieveResponseFormat
    ] = ApiV2PlantDeviceControlHistoryRetrieveResponseFormat.JSON,
    period: Union[
        Unset, None, ApiV2PlantDeviceControlHistoryRetrievePeriod
    ] = ApiV2PlantDeviceControlHistoryRetrievePeriod.VALUE_1,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[HistoryResponse]:
    """Fetch control history

     Fetches control history. 0 = unknown, 1 = off, 2 = on

    Args:
        plant_uuid (str):
        end (Union[Unset, None, datetime.datetime]):
        format_ (Union[Unset, None, ApiV2PlantDeviceControlHistoryRetrieveResponseFormat]):
            Default: ApiV2PlantDeviceControlHistoryRetrieveResponseFormat.JSON.
        period (Union[Unset, None, ApiV2PlantDeviceControlHistoryRetrievePeriod]):  Default:
            ApiV2PlantDeviceControlHistoryRetrievePeriod.VALUE_1.
        start (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[HistoryResponse]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
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
    *,
    client: AuthenticatedClient,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    format_: Union[
        Unset, None, ApiV2PlantDeviceControlHistoryRetrieveResponseFormat
    ] = ApiV2PlantDeviceControlHistoryRetrieveResponseFormat.JSON,
    period: Union[
        Unset, None, ApiV2PlantDeviceControlHistoryRetrievePeriod
    ] = ApiV2PlantDeviceControlHistoryRetrievePeriod.VALUE_1,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[HistoryResponse]:
    """Fetch control history

     Fetches control history. 0 = unknown, 1 = off, 2 = on

    Args:
        plant_uuid (str):
        end (Union[Unset, None, datetime.datetime]):
        format_ (Union[Unset, None, ApiV2PlantDeviceControlHistoryRetrieveResponseFormat]):
            Default: ApiV2PlantDeviceControlHistoryRetrieveResponseFormat.JSON.
        period (Union[Unset, None, ApiV2PlantDeviceControlHistoryRetrievePeriod]):  Default:
            ApiV2PlantDeviceControlHistoryRetrievePeriod.VALUE_1.
        start (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[HistoryResponse]
    """

    return (
        await asyncio_detailed(
            plant_uuid=plant_uuid,
            client=client,
            end=end,
            format_=format_,
            period=period,
            start=start,
        )
    ).parsed
