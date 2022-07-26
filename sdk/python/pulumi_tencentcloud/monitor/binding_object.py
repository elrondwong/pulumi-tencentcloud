# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['BindingObjectArgs', 'BindingObject']

@pulumi.input_type
class BindingObjectArgs:
    def __init__(__self__, *,
                 dimensions: pulumi.Input[Sequence[pulumi.Input['BindingObjectDimensionArgs']]],
                 group_id: pulumi.Input[int]):
        """
        The set of arguments for constructing a BindingObject resource.
        :param pulumi.Input[Sequence[pulumi.Input['BindingObjectDimensionArgs']]] dimensions: A list objects. Each element contains the following attributes:
        :param pulumi.Input[int] group_id: Policy group ID for binding objects.
        """
        pulumi.set(__self__, "dimensions", dimensions)
        pulumi.set(__self__, "group_id", group_id)

    @property
    @pulumi.getter
    def dimensions(self) -> pulumi.Input[Sequence[pulumi.Input['BindingObjectDimensionArgs']]]:
        """
        A list objects. Each element contains the following attributes:
        """
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: pulumi.Input[Sequence[pulumi.Input['BindingObjectDimensionArgs']]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[int]:
        """
        Policy group ID for binding objects.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "group_id", value)


@pulumi.input_type
class _BindingObjectState:
    def __init__(__self__, *,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['BindingObjectDimensionArgs']]]] = None,
                 group_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering BindingObject resources.
        :param pulumi.Input[Sequence[pulumi.Input['BindingObjectDimensionArgs']]] dimensions: A list objects. Each element contains the following attributes:
        :param pulumi.Input[int] group_id: Policy group ID for binding objects.
        """
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BindingObjectDimensionArgs']]]]:
        """
        A list objects. Each element contains the following attributes:
        """
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BindingObjectDimensionArgs']]]]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[int]]:
        """
        Policy group ID for binding objects.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "group_id", value)


class BindingObject(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BindingObjectDimensionArgs']]]]] = None,
                 group_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a BindingObject resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BindingObjectDimensionArgs']]]] dimensions: A list objects. Each element contains the following attributes:
        :param pulumi.Input[int] group_id: Policy group ID for binding objects.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BindingObjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a BindingObject resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param BindingObjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BindingObjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BindingObjectDimensionArgs']]]]] = None,
                 group_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BindingObjectArgs.__new__(BindingObjectArgs)

            if dimensions is None and not opts.urn:
                raise TypeError("Missing required property 'dimensions'")
            __props__.__dict__["dimensions"] = dimensions
            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
        super(BindingObject, __self__).__init__(
            'tencentcloud:Monitor/bindingObject:BindingObject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BindingObjectDimensionArgs']]]]] = None,
            group_id: Optional[pulumi.Input[int]] = None) -> 'BindingObject':
        """
        Get an existing BindingObject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BindingObjectDimensionArgs']]]] dimensions: A list objects. Each element contains the following attributes:
        :param pulumi.Input[int] group_id: Policy group ID for binding objects.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BindingObjectState.__new__(_BindingObjectState)

        __props__.__dict__["dimensions"] = dimensions
        __props__.__dict__["group_id"] = group_id
        return BindingObject(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def dimensions(self) -> pulumi.Output[Sequence['outputs.BindingObjectDimension']]:
        """
        A list objects. Each element contains the following attributes:
        """
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[int]:
        """
        Policy group ID for binding objects.
        """
        return pulumi.get(self, "group_id")
