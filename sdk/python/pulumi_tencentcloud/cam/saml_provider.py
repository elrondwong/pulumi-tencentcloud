# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SAMLProviderArgs', 'SAMLProvider']

@pulumi.input_type
class SAMLProviderArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 meta_data: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SAMLProvider resource.
        :param pulumi.Input[str] description: The description of the CAM SAML provider.
        :param pulumi.Input[str] meta_data: The meta data document of the CAM SAML provider.
        :param pulumi.Input[str] name: Name of CAM SAML provider.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "meta_data", meta_data)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The description of the CAM SAML provider.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="metaData")
    def meta_data(self) -> pulumi.Input[str]:
        """
        The meta data document of the CAM SAML provider.
        """
        return pulumi.get(self, "meta_data")

    @meta_data.setter
    def meta_data(self, value: pulumi.Input[str]):
        pulumi.set(self, "meta_data", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of CAM SAML provider.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _SAMLProviderState:
    def __init__(__self__, *,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 meta_data: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provider_arn: Optional[pulumi.Input[str]] = None,
                 update_time: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SAMLProvider resources.
        :param pulumi.Input[str] create_time: The create time of the CAM SAML provider.
        :param pulumi.Input[str] description: The description of the CAM SAML provider.
        :param pulumi.Input[str] meta_data: The meta data document of the CAM SAML provider.
        :param pulumi.Input[str] name: Name of CAM SAML provider.
        :param pulumi.Input[str] provider_arn: The ARN of the CAM SAML provider.
        :param pulumi.Input[str] update_time: The last update time of the CAM SAML provider.
        """
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if meta_data is not None:
            pulumi.set(__self__, "meta_data", meta_data)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provider_arn is not None:
            pulumi.set(__self__, "provider_arn", provider_arn)
        if update_time is not None:
            pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        The create time of the CAM SAML provider.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the CAM SAML provider.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="metaData")
    def meta_data(self) -> Optional[pulumi.Input[str]]:
        """
        The meta data document of the CAM SAML provider.
        """
        return pulumi.get(self, "meta_data")

    @meta_data.setter
    def meta_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "meta_data", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of CAM SAML provider.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="providerArn")
    def provider_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the CAM SAML provider.
        """
        return pulumi.get(self, "provider_arn")

    @provider_arn.setter
    def provider_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_arn", value)

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[str]]:
        """
        The last update time of the CAM SAML provider.
        """
        return pulumi.get(self, "update_time")

    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "update_time", value)


class SAMLProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 meta_data: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a SAMLProvider resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the CAM SAML provider.
        :param pulumi.Input[str] meta_data: The meta data document of the CAM SAML provider.
        :param pulumi.Input[str] name: Name of CAM SAML provider.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SAMLProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a SAMLProvider resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SAMLProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SAMLProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 meta_data: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = SAMLProviderArgs.__new__(SAMLProviderArgs)

            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if meta_data is None and not opts.urn:
                raise TypeError("Missing required property 'meta_data'")
            __props__.__dict__["meta_data"] = meta_data
            __props__.__dict__["name"] = name
            __props__.__dict__["create_time"] = None
            __props__.__dict__["provider_arn"] = None
            __props__.__dict__["update_time"] = None
        super(SAMLProvider, __self__).__init__(
            'tencentcloud:Cam/sAMLProvider:SAMLProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            meta_data: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            provider_arn: Optional[pulumi.Input[str]] = None,
            update_time: Optional[pulumi.Input[str]] = None) -> 'SAMLProvider':
        """
        Get an existing SAMLProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] create_time: The create time of the CAM SAML provider.
        :param pulumi.Input[str] description: The description of the CAM SAML provider.
        :param pulumi.Input[str] meta_data: The meta data document of the CAM SAML provider.
        :param pulumi.Input[str] name: Name of CAM SAML provider.
        :param pulumi.Input[str] provider_arn: The ARN of the CAM SAML provider.
        :param pulumi.Input[str] update_time: The last update time of the CAM SAML provider.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SAMLProviderState.__new__(_SAMLProviderState)

        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["meta_data"] = meta_data
        __props__.__dict__["name"] = name
        __props__.__dict__["provider_arn"] = provider_arn
        __props__.__dict__["update_time"] = update_time
        return SAMLProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The create time of the CAM SAML provider.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the CAM SAML provider.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="metaData")
    def meta_data(self) -> pulumi.Output[str]:
        """
        The meta data document of the CAM SAML provider.
        """
        return pulumi.get(self, "meta_data")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of CAM SAML provider.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="providerArn")
    def provider_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the CAM SAML provider.
        """
        return pulumi.get(self, "provider_arn")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The last update time of the CAM SAML provider.
        """
        return pulumi.get(self, "update_time")
