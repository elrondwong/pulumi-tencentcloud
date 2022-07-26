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

__all__ = ['CosShipperArgs', 'CosShipper']

@pulumi.input_type
class CosShipperArgs:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 prefix: pulumi.Input[str],
                 shipper_name: pulumi.Input[str],
                 topic_id: pulumi.Input[str],
                 compress: Optional[pulumi.Input['CosShipperCompressArgs']] = None,
                 content: Optional[pulumi.Input['CosShipperContentArgs']] = None,
                 filter_rules: Optional[pulumi.Input[Sequence[pulumi.Input['CosShipperFilterRuleArgs']]]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 max_size: Optional[pulumi.Input[int]] = None,
                 partition: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CosShipper resource.
        :param pulumi.Input[str] bucket: Destination bucket in the shipping rule to be created.
        :param pulumi.Input[str] prefix: Prefix of the shipping directory in the shipping rule to be created.
        :param pulumi.Input[str] shipper_name: Shipping rule name.
        :param pulumi.Input[str] topic_id: ID of the log topic to which the shipping rule to be created belongs.
        :param pulumi.Input['CosShipperCompressArgs'] compress: Compression configuration of shipped log.
        :param pulumi.Input['CosShipperContentArgs'] content: Format configuration of shipped log content.
        :param pulumi.Input[Sequence[pulumi.Input['CosShipperFilterRuleArgs']]] filter_rules: Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and
               up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        :param pulumi.Input[int] interval: Shipping time interval in seconds. Default value: 300. Value range: 300~900.
        :param pulumi.Input[int] max_size: Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
        :param pulumi.Input[str] partition: Partition rule of shipped log, which can be represented in strftime time format.
        """
        pulumi.set(__self__, "bucket", bucket)
        pulumi.set(__self__, "prefix", prefix)
        pulumi.set(__self__, "shipper_name", shipper_name)
        pulumi.set(__self__, "topic_id", topic_id)
        if compress is not None:
            pulumi.set(__self__, "compress", compress)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if filter_rules is not None:
            pulumi.set(__self__, "filter_rules", filter_rules)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if max_size is not None:
            pulumi.set(__self__, "max_size", max_size)
        if partition is not None:
            pulumi.set(__self__, "partition", partition)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        Destination bucket in the shipping rule to be created.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[str]:
        """
        Prefix of the shipping directory in the shipping rule to be created.
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "prefix", value)

    @property
    @pulumi.getter(name="shipperName")
    def shipper_name(self) -> pulumi.Input[str]:
        """
        Shipping rule name.
        """
        return pulumi.get(self, "shipper_name")

    @shipper_name.setter
    def shipper_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "shipper_name", value)

    @property
    @pulumi.getter(name="topicId")
    def topic_id(self) -> pulumi.Input[str]:
        """
        ID of the log topic to which the shipping rule to be created belongs.
        """
        return pulumi.get(self, "topic_id")

    @topic_id.setter
    def topic_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "topic_id", value)

    @property
    @pulumi.getter
    def compress(self) -> Optional[pulumi.Input['CosShipperCompressArgs']]:
        """
        Compression configuration of shipped log.
        """
        return pulumi.get(self, "compress")

    @compress.setter
    def compress(self, value: Optional[pulumi.Input['CosShipperCompressArgs']]):
        pulumi.set(self, "compress", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input['CosShipperContentArgs']]:
        """
        Format configuration of shipped log content.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input['CosShipperContentArgs']]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="filterRules")
    def filter_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CosShipperFilterRuleArgs']]]]:
        """
        Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and
        up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        """
        return pulumi.get(self, "filter_rules")

    @filter_rules.setter
    def filter_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CosShipperFilterRuleArgs']]]]):
        pulumi.set(self, "filter_rules", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[int]]:
        """
        Shipping time interval in seconds. Default value: 300. Value range: 300~900.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "interval", value)

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
        """
        return pulumi.get(self, "max_size")

    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_size", value)

    @property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[str]]:
        """
        Partition rule of shipped log, which can be represented in strftime time format.
        """
        return pulumi.get(self, "partition")

    @partition.setter
    def partition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partition", value)


@pulumi.input_type
class _CosShipperState:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 compress: Optional[pulumi.Input['CosShipperCompressArgs']] = None,
                 content: Optional[pulumi.Input['CosShipperContentArgs']] = None,
                 filter_rules: Optional[pulumi.Input[Sequence[pulumi.Input['CosShipperFilterRuleArgs']]]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 max_size: Optional[pulumi.Input[int]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 shipper_name: Optional[pulumi.Input[str]] = None,
                 topic_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CosShipper resources.
        :param pulumi.Input[str] bucket: Destination bucket in the shipping rule to be created.
        :param pulumi.Input['CosShipperCompressArgs'] compress: Compression configuration of shipped log.
        :param pulumi.Input['CosShipperContentArgs'] content: Format configuration of shipped log content.
        :param pulumi.Input[Sequence[pulumi.Input['CosShipperFilterRuleArgs']]] filter_rules: Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and
               up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        :param pulumi.Input[int] interval: Shipping time interval in seconds. Default value: 300. Value range: 300~900.
        :param pulumi.Input[int] max_size: Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
        :param pulumi.Input[str] partition: Partition rule of shipped log, which can be represented in strftime time format.
        :param pulumi.Input[str] prefix: Prefix of the shipping directory in the shipping rule to be created.
        :param pulumi.Input[str] shipper_name: Shipping rule name.
        :param pulumi.Input[str] topic_id: ID of the log topic to which the shipping rule to be created belongs.
        """
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if compress is not None:
            pulumi.set(__self__, "compress", compress)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if filter_rules is not None:
            pulumi.set(__self__, "filter_rules", filter_rules)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if max_size is not None:
            pulumi.set(__self__, "max_size", max_size)
        if partition is not None:
            pulumi.set(__self__, "partition", partition)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)
        if shipper_name is not None:
            pulumi.set(__self__, "shipper_name", shipper_name)
        if topic_id is not None:
            pulumi.set(__self__, "topic_id", topic_id)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        Destination bucket in the shipping rule to be created.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def compress(self) -> Optional[pulumi.Input['CosShipperCompressArgs']]:
        """
        Compression configuration of shipped log.
        """
        return pulumi.get(self, "compress")

    @compress.setter
    def compress(self, value: Optional[pulumi.Input['CosShipperCompressArgs']]):
        pulumi.set(self, "compress", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input['CosShipperContentArgs']]:
        """
        Format configuration of shipped log content.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input['CosShipperContentArgs']]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="filterRules")
    def filter_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CosShipperFilterRuleArgs']]]]:
        """
        Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and
        up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        """
        return pulumi.get(self, "filter_rules")

    @filter_rules.setter
    def filter_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CosShipperFilterRuleArgs']]]]):
        pulumi.set(self, "filter_rules", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[int]]:
        """
        Shipping time interval in seconds. Default value: 300. Value range: 300~900.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "interval", value)

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
        """
        return pulumi.get(self, "max_size")

    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_size", value)

    @property
    @pulumi.getter
    def partition(self) -> Optional[pulumi.Input[str]]:
        """
        Partition rule of shipped log, which can be represented in strftime time format.
        """
        return pulumi.get(self, "partition")

    @partition.setter
    def partition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partition", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Prefix of the shipping directory in the shipping rule to be created.
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)

    @property
    @pulumi.getter(name="shipperName")
    def shipper_name(self) -> Optional[pulumi.Input[str]]:
        """
        Shipping rule name.
        """
        return pulumi.get(self, "shipper_name")

    @shipper_name.setter
    def shipper_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shipper_name", value)

    @property
    @pulumi.getter(name="topicId")
    def topic_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the log topic to which the shipping rule to be created belongs.
        """
        return pulumi.get(self, "topic_id")

    @topic_id.setter
    def topic_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic_id", value)


class CosShipper(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 compress: Optional[pulumi.Input[pulumi.InputType['CosShipperCompressArgs']]] = None,
                 content: Optional[pulumi.Input[pulumi.InputType['CosShipperContentArgs']]] = None,
                 filter_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CosShipperFilterRuleArgs']]]]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 max_size: Optional[pulumi.Input[int]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 shipper_name: Optional[pulumi.Input[str]] = None,
                 topic_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a CosShipper resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: Destination bucket in the shipping rule to be created.
        :param pulumi.Input[pulumi.InputType['CosShipperCompressArgs']] compress: Compression configuration of shipped log.
        :param pulumi.Input[pulumi.InputType['CosShipperContentArgs']] content: Format configuration of shipped log content.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CosShipperFilterRuleArgs']]]] filter_rules: Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and
               up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        :param pulumi.Input[int] interval: Shipping time interval in seconds. Default value: 300. Value range: 300~900.
        :param pulumi.Input[int] max_size: Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
        :param pulumi.Input[str] partition: Partition rule of shipped log, which can be represented in strftime time format.
        :param pulumi.Input[str] prefix: Prefix of the shipping directory in the shipping rule to be created.
        :param pulumi.Input[str] shipper_name: Shipping rule name.
        :param pulumi.Input[str] topic_id: ID of the log topic to which the shipping rule to be created belongs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CosShipperArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CosShipper resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CosShipperArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CosShipperArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 compress: Optional[pulumi.Input[pulumi.InputType['CosShipperCompressArgs']]] = None,
                 content: Optional[pulumi.Input[pulumi.InputType['CosShipperContentArgs']]] = None,
                 filter_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CosShipperFilterRuleArgs']]]]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 max_size: Optional[pulumi.Input[int]] = None,
                 partition: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 shipper_name: Optional[pulumi.Input[str]] = None,
                 topic_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = CosShipperArgs.__new__(CosShipperArgs)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["compress"] = compress
            __props__.__dict__["content"] = content
            __props__.__dict__["filter_rules"] = filter_rules
            __props__.__dict__["interval"] = interval
            __props__.__dict__["max_size"] = max_size
            __props__.__dict__["partition"] = partition
            if prefix is None and not opts.urn:
                raise TypeError("Missing required property 'prefix'")
            __props__.__dict__["prefix"] = prefix
            if shipper_name is None and not opts.urn:
                raise TypeError("Missing required property 'shipper_name'")
            __props__.__dict__["shipper_name"] = shipper_name
            if topic_id is None and not opts.urn:
                raise TypeError("Missing required property 'topic_id'")
            __props__.__dict__["topic_id"] = topic_id
        super(CosShipper, __self__).__init__(
            'tencentcloud:Cls/cosShipper:CosShipper',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            compress: Optional[pulumi.Input[pulumi.InputType['CosShipperCompressArgs']]] = None,
            content: Optional[pulumi.Input[pulumi.InputType['CosShipperContentArgs']]] = None,
            filter_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CosShipperFilterRuleArgs']]]]] = None,
            interval: Optional[pulumi.Input[int]] = None,
            max_size: Optional[pulumi.Input[int]] = None,
            partition: Optional[pulumi.Input[str]] = None,
            prefix: Optional[pulumi.Input[str]] = None,
            shipper_name: Optional[pulumi.Input[str]] = None,
            topic_id: Optional[pulumi.Input[str]] = None) -> 'CosShipper':
        """
        Get an existing CosShipper resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: Destination bucket in the shipping rule to be created.
        :param pulumi.Input[pulumi.InputType['CosShipperCompressArgs']] compress: Compression configuration of shipped log.
        :param pulumi.Input[pulumi.InputType['CosShipperContentArgs']] content: Format configuration of shipped log content.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CosShipperFilterRuleArgs']]]] filter_rules: Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and
               up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        :param pulumi.Input[int] interval: Shipping time interval in seconds. Default value: 300. Value range: 300~900.
        :param pulumi.Input[int] max_size: Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
        :param pulumi.Input[str] partition: Partition rule of shipped log, which can be represented in strftime time format.
        :param pulumi.Input[str] prefix: Prefix of the shipping directory in the shipping rule to be created.
        :param pulumi.Input[str] shipper_name: Shipping rule name.
        :param pulumi.Input[str] topic_id: ID of the log topic to which the shipping rule to be created belongs.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CosShipperState.__new__(_CosShipperState)

        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["compress"] = compress
        __props__.__dict__["content"] = content
        __props__.__dict__["filter_rules"] = filter_rules
        __props__.__dict__["interval"] = interval
        __props__.__dict__["max_size"] = max_size
        __props__.__dict__["partition"] = partition
        __props__.__dict__["prefix"] = prefix
        __props__.__dict__["shipper_name"] = shipper_name
        __props__.__dict__["topic_id"] = topic_id
        return CosShipper(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        Destination bucket in the shipping rule to be created.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter
    def compress(self) -> pulumi.Output[Optional['outputs.CosShipperCompress']]:
        """
        Compression configuration of shipped log.
        """
        return pulumi.get(self, "compress")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[Optional['outputs.CosShipperContent']]:
        """
        Format configuration of shipped log content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="filterRules")
    def filter_rules(self) -> pulumi.Output[Optional[Sequence['outputs.CosShipperFilterRule']]]:
        """
        Filter rules for shipped logs. Only logs matching the rules can be shipped. All rules are in the AND relationship, and
        up to five rules can be added. If the array is empty, no filtering will be performed, and all logs will be shipped.
        """
        return pulumi.get(self, "filter_rules")

    @property
    @pulumi.getter
    def interval(self) -> pulumi.Output[Optional[int]]:
        """
        Shipping time interval in seconds. Default value: 300. Value range: 300~900.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum size of a file to be shipped, in MB. Default value: 256. Value range: 100~256.
        """
        return pulumi.get(self, "max_size")

    @property
    @pulumi.getter
    def partition(self) -> pulumi.Output[Optional[str]]:
        """
        Partition rule of shipped log, which can be represented in strftime time format.
        """
        return pulumi.get(self, "partition")

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Output[str]:
        """
        Prefix of the shipping directory in the shipping rule to be created.
        """
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter(name="shipperName")
    def shipper_name(self) -> pulumi.Output[str]:
        """
        Shipping rule name.
        """
        return pulumi.get(self, "shipper_name")

    @property
    @pulumi.getter(name="topicId")
    def topic_id(self) -> pulumi.Output[str]:
        """
        ID of the log topic to which the shipping rule to be created belongs.
        """
        return pulumi.get(self, "topic_id")
