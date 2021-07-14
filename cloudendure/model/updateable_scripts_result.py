"""
    CloudEndure API documentation

    © 2021 CloudEndure All rights reserved  # General Request authentication in CloudEndure's API is done using session cookies. A session cookie is returned upon successful execution of the \"login\" method. This value must then be provided within the request headers of all subsequent API requests.  ## Errors Some errors are not specifically written in every method since they may always return. Those are: 1) 401 (Unauthorized) - for unauthenticated requests. 2) 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET). 3) 403 (Forbidden) - request is authenticated, but the user is not allowed to access. 4) 422 (Unprocessable Entity) - for invalid input.  ## Formats All strings with date-time format are according to RFC3339.  All strings with \"duration\" format are according to ISO8601. For example, a full day duration can be specified with \"PNNNND\".   # noqa: E501

    The version of the OpenAPI document: 5
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cloudendure.model_utils import ModelComposed  # noqa: F401
from cloudendure.model_utils import (
    ApiTypeError,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


def lazy_import():
    from cloudendure.model.updateable_scripts_result_on_premise_volumes import (
        UpdateableScriptsResultOnPremiseVolumes,
    )

    globals()[
        "UpdateableScriptsResultOnPremiseVolumes"
    ] = UpdateableScriptsResultOnPremiseVolumes


class UpdateableScriptsResult(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            "migration": (str,),  # noqa: E501
            "custom_preboot_timeout": (int,),  # noqa: E501
            "mount_points": ([str],),  # noqa: E501
            "postboot_auto_copy_datetime": (str,),  # noqa: E501
            "lvm_vgs": ([str],),  # noqa: E501
            "preboot_environment": ({str: (str,)},),  # noqa: E501
            "postboot": ([str],),  # noqa: E501
            "converter_ami": (str,),  # noqa: E501
            "postboot_uninstall_disable": (bool,),  # noqa: E501
            "volume_id": (str,),  # noqa: E501
            "preboot_auto_copy_datetime": (str,),  # noqa: E501
            "partitions": ([int],),  # noqa: E501
            "preboot": ([str],),  # noqa: E501
            "on_premise_root_device": (str,),  # noqa: E501
            "on_premise_volumes": (
                [UpdateableScriptsResultOnPremiseVolumes],
            ),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "migration": "migration",  # noqa: E501
        "custom_preboot_timeout": "custom_preboot_timeout",  # noqa: E501
        "mount_points": "mount_points",  # noqa: E501
        "postboot_auto_copy_datetime": "postboot_auto_copy_datetime",  # noqa: E501
        "lvm_vgs": "lvm_vgs",  # noqa: E501
        "preboot_environment": "preboot_environment",  # noqa: E501
        "postboot": "postboot",  # noqa: E501
        "converter_ami": "converter_ami",  # noqa: E501
        "postboot_uninstall_disable": "postboot_uninstall_disable",  # noqa: E501
        "volume_id": "volume_id",  # noqa: E501
        "preboot_auto_copy_datetime": "preboot_auto_copy_datetime",  # noqa: E501
        "partitions": "partitions",  # noqa: E501
        "preboot": "preboot",  # noqa: E501
        "on_premise_root_device": "on_premise_root_device",  # noqa: E501
        "on_premise_volumes": "on_premise_volumes",  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """UpdateableScriptsResult - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            migration (str): [optional]  # noqa: E501
            custom_preboot_timeout (int): [optional]  # noqa: E501
            mount_points ([str]): [optional]  # noqa: E501
            postboot_auto_copy_datetime (str): [optional]  # noqa: E501
            lvm_vgs ([str]): [optional]  # noqa: E501
            preboot_environment ({str: (str,)}): [optional]  # noqa: E501
            postboot ([str]): [optional]  # noqa: E501
            converter_ami (str): [optional]  # noqa: E501
            postboot_uninstall_disable (bool): [optional]  # noqa: E501
            volume_id (str): [optional]  # noqa: E501
            preboot_auto_copy_datetime (str): [optional]  # noqa: E501
            partitions ([int]): [optional]  # noqa: E501
            preboot ([str]): [optional]  # noqa: E501
            on_premise_root_device (str): [optional]  # noqa: E501
            on_premise_volumes ([UpdateableScriptsResultOnPremiseVolumes]): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
