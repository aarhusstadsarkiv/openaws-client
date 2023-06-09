from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.schema_read import SchemaRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    client: AuthenticatedClient,
    version: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/schemas/{name}".format(client.base_url, name=name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, SchemaRead]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SchemaRead.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, SchemaRead]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    version: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, HTTPValidationError, SchemaRead]]:
    """Entity:Get Schema

    Args:
        name (str):
        version (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, SchemaRead]]
    """

    kwargs = _get_kwargs(
        name=name,
        client=client,
        version=version,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    version: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, SchemaRead]]:
    """Entity:Get Schema

    Args:
        name (str):
        version (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, SchemaRead]
    """

    return sync_detailed(
        name=name,
        client=client,
        version=version,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    version: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, HTTPValidationError, SchemaRead]]:
    """Entity:Get Schema

    Args:
        name (str):
        version (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, SchemaRead]]
    """

    kwargs = _get_kwargs(
        name=name,
        client=client,
        version=version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    version: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, SchemaRead]]:
    """Entity:Get Schema

    Args:
        name (str):
        version (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, SchemaRead]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            version=version,
        )
    ).parsed
