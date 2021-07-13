"""
    CloudEndure API documentation

    © 2021 CloudEndure All rights reserved  # General Request authentication in CloudEndure's API is done using session cookies. A session cookie is returned upon successful execution of the \"login\" method. This value must then be provided within the request headers of all subsequent API requests.  ## Errors Some errors are not specifically written in every method since they may always return. Those are: 1) 401 (Unauthorized) - for unauthenticated requests. 2) 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET). 3) 403 (Forbidden) - request is authenticated, but the user is not allowed to access. 4) 422 (Unprocessable Entity) - for invalid input.  ## Formats All strings with date-time format are according to RFC3339.  All strings with \"duration\" format are according to ISO8601. For example, a full day duration can be specified with \"PNNNND\".   # noqa: E501

    The version of the OpenAPI document: 5
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cloudendure.api_client import ApiClient, Endpoint as _Endpoint
from cloudendure.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from cloudendure.model.error import Error
from cloudendure.model.inline_object8 import InlineObject8
from cloudendure.model.machine import Machine
from cloudendure.model.machines_list import MachinesList
from cloudendure.model.replica import Replica


class MachinesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __projects_project_id_machines_delete(
            self, project_id, machine_ids, **kwargs
        ):
            """Uninstall multiple agents  # noqa: E501

            Stops replication and removes the cloudendure agent from the specified machines. All cloud artifacts associated with those machines with the exception of launched target machines are deleted.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.projects_project_id_machines_delete(project_id, machine_ids, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str):
                machine_ids (InlineObject8):

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
                None
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
            kwargs["project_id"] = project_id
            kwargs["machine_ids"] = machine_ids
            return self.call_with_http_info(**kwargs)

        self.projects_project_id_machines_delete = _Endpoint(
            settings={
                "response_type": None,
                "auth": [],
                "endpoint_path": "/projects/{projectId}/machines",
                "operation_id": "projects_project_id_machines_delete",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": ["project_id", "machine_ids",],
                "required": ["project_id", "machine_ids",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "project_id": (str,),
                    "machine_ids": (InlineObject8,),
                },
                "attribute_map": {"project_id": "projectId",},
                "location_map": {"project_id": "path", "machine_ids": "body",},
                "collection_format_map": {},
            },
            headers_map={"accept": [], "content_type": ["application/json"]},
            api_client=api_client,
            callable=__projects_project_id_machines_delete,
        )

        def __projects_project_id_machines_get(self, project_id, **kwargs):
            """List Machines  # noqa: E501

            Returns the list of all source machines in the Project (i.e. machines that have an Agent installed).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.projects_project_id_machines_get(project_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str):

            Keyword Args:
                offset (int): With which item to start (0 based).. [optional] if omitted the server will use the default value of 0
                limit (int): A number specifying how many entries to return.. [optional] if omitted the server will use the default value of 1500
                all (bool): When set to false, returns only currently replicating machines. When set to true, returns all machines in the project regardless of replications status. machines are consuming/ have consumed licenses.  Note that some license types are transferable and therefore once you remove the and set to true false, returns only currently replicating machines. When set to true, returns all machines in the project regardless of replications status. . [optional] if omitted the server will use the default value of False
                types (str): Use this url query param to control which machines are returned when doing GET.  If you do not include the \\\"types\\\" query param, you will only get source machines . [optional]
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
                MachinesList
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
            kwargs["project_id"] = project_id
            return self.call_with_http_info(**kwargs)

        self.projects_project_id_machines_get = _Endpoint(
            settings={
                "response_type": (MachinesList,),
                "auth": [],
                "endpoint_path": "/projects/{projectId}/machines",
                "operation_id": "projects_project_id_machines_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["project_id", "offset", "limit", "all", "types",],
                "required": ["project_id",],
                "nullable": [],
                "enum": [],
                "validation": ["offset", "limit",],
            },
            root_map={
                "validations": {
                    ("offset",): {"inclusive_minimum": 0,},
                    ("limit",): {"inclusive_maximum": 1500, "inclusive_minimum": 0,},
                },
                "allowed_values": {},
                "openapi_types": {
                    "project_id": (str,),
                    "offset": (int,),
                    "limit": (int,),
                    "all": (bool,),
                    "types": (str,),
                },
                "attribute_map": {
                    "project_id": "projectId",
                    "offset": "offset",
                    "limit": "limit",
                    "all": "all",
                    "types": "types",
                },
                "location_map": {
                    "project_id": "path",
                    "offset": "query",
                    "limit": "query",
                    "all": "query",
                    "types": "query",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
            callable=__projects_project_id_machines_get,
        )

        def __projects_project_id_machines_machine_id_delete(
            self, project_id, machine_id, **kwargs
        ):
            """Uninstall agent  # noqa: E501

            Stops replication and removes the cloudendure agent from this machine. All cloud artifacts associated with those machines with the exception of launched target machine are deleted.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.projects_project_id_machines_machine_id_delete(project_id, machine_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str):
                machine_id (str):

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
                None
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
            kwargs["project_id"] = project_id
            kwargs["machine_id"] = machine_id
            return self.call_with_http_info(**kwargs)

        self.projects_project_id_machines_machine_id_delete = _Endpoint(
            settings={
                "response_type": None,
                "auth": [],
                "endpoint_path": "/projects/{projectId}/machines/{machineId}",
                "operation_id": "projects_project_id_machines_machine_id_delete",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": ["project_id", "machine_id",],
                "required": ["project_id", "machine_id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"project_id": (str,), "machine_id": (str,),},
                "attribute_map": {
                    "project_id": "projectId",
                    "machine_id": "machineId",
                },
                "location_map": {"project_id": "path", "machine_id": "path",},
                "collection_format_map": {},
            },
            headers_map={"accept": [], "content_type": [],},
            api_client=api_client,
            callable=__projects_project_id_machines_machine_id_delete,
        )

        def __projects_project_id_machines_machine_id_get(
            self, project_id, machine_id, **kwargs
        ):
            """Get a specific machine.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.projects_project_id_machines_machine_id_get(project_id, machine_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str):
                machine_id (str):

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
                Machine
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
            kwargs["project_id"] = project_id
            kwargs["machine_id"] = machine_id
            return self.call_with_http_info(**kwargs)

        self.projects_project_id_machines_machine_id_get = _Endpoint(
            settings={
                "response_type": (Machine,),
                "auth": [],
                "endpoint_path": "/projects/{projectId}/machines/{machineId}",
                "operation_id": "projects_project_id_machines_machine_id_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["project_id", "machine_id",],
                "required": ["project_id", "machine_id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"project_id": (str,), "machine_id": (str,),},
                "attribute_map": {
                    "project_id": "projectId",
                    "machine_id": "machineId",
                },
                "location_map": {"project_id": "path", "machine_id": "path",},
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
            callable=__projects_project_id_machines_machine_id_get,
        )

        def __projects_project_id_machines_machine_id_patch(
            self, project_id, machine_id, machine, **kwargs
        ):
            """Update a machine. Accepts only Launch time updates.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.projects_project_id_machines_machine_id_patch(project_id, machine_id, machine, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str):
                machine_id (str):
                machine (Machine):

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
                Machine
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
            kwargs["project_id"] = project_id
            kwargs["machine_id"] = machine_id
            kwargs["machine"] = machine
            return self.call_with_http_info(**kwargs)

        self.projects_project_id_machines_machine_id_patch = _Endpoint(
            settings={
                "response_type": (Machine,),
                "auth": [],
                "endpoint_path": "/projects/{projectId}/machines/{machineId}",
                "operation_id": "projects_project_id_machines_machine_id_patch",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "all": ["project_id", "machine_id", "machine",],
                "required": ["project_id", "machine_id", "machine",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "project_id": (str,),
                    "machine_id": (str,),
                    "machine": (Machine,),
                },
                "attribute_map": {
                    "project_id": "projectId",
                    "machine_id": "machineId",
                },
                "location_map": {
                    "project_id": "path",
                    "machine_id": "path",
                    "machine": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
            callable=__projects_project_id_machines_machine_id_patch,
        )

        def __projects_project_id_machines_patch(
            self, project_id, machines_list, **kwargs
        ):
            """Batch-update multiple machines  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.projects_project_id_machines_patch(project_id, machines_list, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str):
                machines_list (MachinesList):

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
                MachinesList
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
            kwargs["project_id"] = project_id
            kwargs["machines_list"] = machines_list
            return self.call_with_http_info(**kwargs)

        self.projects_project_id_machines_patch = _Endpoint(
            settings={
                "response_type": (MachinesList,),
                "auth": [],
                "endpoint_path": "/projects/{projectId}/machines",
                "operation_id": "projects_project_id_machines_patch",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "all": ["project_id", "machines_list",],
                "required": ["project_id", "machines_list",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "project_id": (str,),
                    "machines_list": (MachinesList,),
                },
                "attribute_map": {"project_id": "projectId",},
                "location_map": {"project_id": "path", "machines_list": "body",},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
            callable=__projects_project_id_machines_patch,
        )

        def __projects_project_id_replicas_replica_id_get(
            self, project_id, replica_id, **kwargs
        ):
            """Get Target Machine  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.projects_project_id_replicas_replica_id_get(project_id, replica_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str):
                replica_id (str):

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
                Replica
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
            kwargs["project_id"] = project_id
            kwargs["replica_id"] = replica_id
            return self.call_with_http_info(**kwargs)

        self.projects_project_id_replicas_replica_id_get = _Endpoint(
            settings={
                "response_type": (Replica,),
                "auth": [],
                "endpoint_path": "/projects/{projectId}/replicas/{replicaId}",
                "operation_id": "projects_project_id_replicas_replica_id_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": ["project_id", "replica_id",],
                "required": ["project_id", "replica_id",],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {"project_id": (str,), "replica_id": (str,),},
                "attribute_map": {
                    "project_id": "projectId",
                    "replica_id": "replicaId",
                },
                "location_map": {"project_id": "path", "replica_id": "path",},
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": [],},
            api_client=api_client,
            callable=__projects_project_id_replicas_replica_id_get,
        )
