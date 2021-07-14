"""
    CloudEndure API documentation

    © 2021 CloudEndure All rights reserved  # General Request authentication in CloudEndure's API is done using session cookies. A session cookie is returned upon successful execution of the \"login\" method. This value must then be provided within the request headers of all subsequent API requests.  ## Errors Some errors are not specifically written in every method since they may always return. Those are: 1) 401 (Unauthorized) - for unauthenticated requests. 2) 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET). 3) 403 (Forbidden) - request is authenticated, but the user is not allowed to access. 4) 422 (Unprocessable Entity) - for invalid input.  ## Formats All strings with date-time format are according to RFC3339.  All strings with \"duration\" format are according to ISO8601. For example, a full day duration can be specified with \"PNNNND\".   # noqa: E501

    The version of the OpenAPI document: 5
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cloudendure.api_client import ApiClient
from cloudendure.api_client import Endpoint as _Endpoint
from cloudendure.model.cloud_credentials import CloudCredentials
from cloudendure.model.cloud_credentials_list import CloudCredentialsList
from cloudendure.model.cloud_credentials_request import CloudCredentialsRequest
from cloudendure.model_utils import check_allowed_values  # noqa: F401
from cloudendure.model_utils import (
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class CloudCredentialsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __cloud_credentials_creds_id_get(self, creds_id, **kwargs):
            """Get Credentials  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.cloud_credentials_creds_id_get(creds_id, async_req=True)
            >>> result = thread.get()

            Args:
                creds_id (str): UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\".

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CloudCredentials
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["creds_id"] = creds_id
            return self.call_with_http_info(**kwargs)

        self.cloud_credentials_creds_id_get = _Endpoint(
            settings={
                "response_type": (CloudCredentials,),
                "auth": [],
                "endpoint_path": "/cloudCredentials/{credsId}",
                "operation_id": "cloud_credentials_creds_id_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "creds_id",
                ],
                "required": [
                    "creds_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "creds_id": (str,),
                },
                "attribute_map": {
                    "creds_id": "credsId",
                },
                "location_map": {
                    "creds_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__cloud_credentials_creds_id_get,
        )

        def __cloud_credentials_creds_id_patch(
            self, creds_id, cloud_credentials, **kwargs
        ):
            """Change Credentials  # noqa: E501

            Changes the cloud credentials.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.cloud_credentials_creds_id_patch(creds_id, cloud_credentials, async_req=True)
            >>> result = thread.get()

            Args:
                creds_id (str): UUID of the credentials to use. In case of on-premise, you should use the null UUID \"00000000-0000-0000-0000-000000000000\".
                cloud_credentials (CloudCredentialsRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CloudCredentials
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["creds_id"] = creds_id
            kwargs["cloud_credentials"] = cloud_credentials
            return self.call_with_http_info(**kwargs)

        self.cloud_credentials_creds_id_patch = _Endpoint(
            settings={
                "response_type": (CloudCredentials,),
                "auth": [],
                "endpoint_path": "/cloudCredentials/{credsId}",
                "operation_id": "cloud_credentials_creds_id_patch",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "all": [
                    "creds_id",
                    "cloud_credentials",
                ],
                "required": [
                    "creds_id",
                    "cloud_credentials",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "creds_id": (str,),
                    "cloud_credentials": (CloudCredentialsRequest,),
                },
                "attribute_map": {
                    "creds_id": "credsId",
                },
                "location_map": {
                    "creds_id": "path",
                    "cloud_credentials": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
            callable=__cloud_credentials_creds_id_patch,
        )

        def __cloud_credentials_get(self, **kwargs):
            """List Credentials  # noqa: E501

            Returns the list of cloudCredentials in the account.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.cloud_credentials_get(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                offset (int): With which item to start (0 based).. [optional] if omitted the server will use the default value of 0
                limit (int): A number specifying how many entries to return.. [optional] if omitted the server will use the default value of 1500
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CloudCredentialsList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.cloud_credentials_get = _Endpoint(
            settings={
                "response_type": (CloudCredentialsList,),
                "auth": [],
                "endpoint_path": "/cloudCredentials",
                "operation_id": "cloud_credentials_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "offset",
                    "limit",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [
                    "offset",
                    "limit",
                ],
            },
            root_map={
                "validations": {
                    ("offset",): {
                        "inclusive_minimum": 0,
                    },
                    ("limit",): {
                        "inclusive_maximum": 1500,
                        "inclusive_minimum": 0,
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "offset": (int,),
                    "limit": (int,),
                },
                "attribute_map": {
                    "offset": "offset",
                    "limit": "limit",
                },
                "location_map": {
                    "offset": "query",
                    "limit": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__cloud_credentials_get,
        )

        def __cloud_credentials_post(self, cloud_credentials, **kwargs):
            """Create Credentials  # noqa: E501

            Provide the credentials with which to access the cloud API. Returns the newly created object.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.cloud_credentials_post(cloud_credentials, async_req=True)
            >>> result = thread.get()

            Args:
                cloud_credentials (CloudCredentialsRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                CloudCredentials
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["cloud_credentials"] = cloud_credentials
            return self.call_with_http_info(**kwargs)

        self.cloud_credentials_post = _Endpoint(
            settings={
                "response_type": (CloudCredentials,),
                "auth": [],
                "endpoint_path": "/cloudCredentials",
                "operation_id": "cloud_credentials_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "cloud_credentials",
                ],
                "required": [
                    "cloud_credentials",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "cloud_credentials": (CloudCredentialsRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "cloud_credentials": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
            callable=__cloud_credentials_post,
        )
