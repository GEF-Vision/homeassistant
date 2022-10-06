import datetime
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.exception import Exception_
from ...types import UNSET, Response, Unset


def _get_kwargs(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v2/plant/{plant_uuid}/device/inverter/{id}/history/state/".format(
        client.base_url, plant_uuid=plant_uuid, id=id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_end: Union[Unset, None, str] = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat() if end else None

    params["end"] = json_end

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


def _parse_response(*, response: httpx.Response) -> Optional[Exception_]:
    if response.status_code == 404:
        response_404 = Exception_.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Exception_]:
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
    end: Union[Unset, None, datetime.datetime] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Exception_]:
    """Inverter state history

     Fetch inverter state history.

    Args:
        plant_uuid (str):
        id (int):
        end (Union[Unset, None, datetime.datetime]):
        start (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[Exception_]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        id=id,
        client=client,
        end=end,
        start=start,
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
    end: Union[Unset, None, datetime.datetime] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Exception_]:
    """Inverter state history

     Fetch inverter state history.

    Args:
        plant_uuid (str):
        id (int):
        end (Union[Unset, None, datetime.datetime]):
        start (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[Exception_]
    """

    return sync_detailed(
        plant_uuid=plant_uuid,
        id=id,
        client=client,
        end=end,
        start=start,
    ).parsed


async def asyncio_detailed(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Exception_]:
    """Inverter state history

     Fetch inverter state history.

    Args:
        plant_uuid (str):
        id (int):
        end (Union[Unset, None, datetime.datetime]):
        start (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[Exception_]
    """

    kwargs = _get_kwargs(
        plant_uuid=plant_uuid,
        id=id,
        client=client,
        end=end,
        start=start,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    plant_uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
    end: Union[Unset, None, datetime.datetime] = UNSET,
    start: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Exception_]:
    """Inverter state history

     Fetch inverter state history.

    Args:
        plant_uuid (str):
        id (int):
        end (Union[Unset, None, datetime.datetime]):
        start (Union[Unset, None, datetime.datetime]):

    Returns:
        Response[Exception_]
    """

    return (
        await asyncio_detailed(
            plant_uuid=plant_uuid,
            id=id,
            client=client,
            end=end,
            start=start,
        )
    ).parsed
