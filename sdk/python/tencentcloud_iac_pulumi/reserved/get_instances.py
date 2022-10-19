# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetInstancesResult',
    'AwaitableGetInstancesResult',
    'get_instances',
    'get_instances_output',
]

@pulumi.output_type
class GetInstancesResult:
    """
    A collection of values returned by getInstances.
    """
    def __init__(__self__, availability_zone=None, id=None, instance_type=None, reserved_instance_id=None, reserved_instance_lists=None, result_output_file=None):
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_type and not isinstance(instance_type, str):
            raise TypeError("Expected argument 'instance_type' to be a str")
        pulumi.set(__self__, "instance_type", instance_type)
        if reserved_instance_id and not isinstance(reserved_instance_id, str):
            raise TypeError("Expected argument 'reserved_instance_id' to be a str")
        pulumi.set(__self__, "reserved_instance_id", reserved_instance_id)
        if reserved_instance_lists and not isinstance(reserved_instance_lists, list):
            raise TypeError("Expected argument 'reserved_instance_lists' to be a list")
        pulumi.set(__self__, "reserved_instance_lists", reserved_instance_lists)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[str]:
        """
        Availability zone of the reserved instance.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[str]:
        """
        The type of reserved instance.
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="reservedInstanceId")
    def reserved_instance_id(self) -> Optional[str]:
        """
        ID of the reserved instance.
        """
        return pulumi.get(self, "reserved_instance_id")

    @property
    @pulumi.getter(name="reservedInstanceLists")
    def reserved_instance_lists(self) -> Sequence['outputs.GetInstancesReservedInstanceListResult']:
        """
        An information list of reserved instance. Each element contains the following attributes:
        """
        return pulumi.get(self, "reserved_instance_lists")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")


class AwaitableGetInstancesResult(GetInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstancesResult(
            availability_zone=self.availability_zone,
            id=self.id,
            instance_type=self.instance_type,
            reserved_instance_id=self.reserved_instance_id,
            reserved_instance_lists=self.reserved_instance_lists,
            result_output_file=self.result_output_file)


def get_instances(availability_zone: Optional[str] = None,
                  instance_type: Optional[str] = None,
                  reserved_instance_id: Optional[str] = None,
                  result_output_file: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstancesResult:
    """
    Use this data source to query reserved instances.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    instances = tencentcloud.Reserved.get_instances(availability_zone="na-siliconvalley-1",
        instance_type="S2.MEDIUM8")
    ```


    :param str availability_zone: The available zone that the reserved instance locates at.
    :param str instance_type: The type of reserved instance.
    :param str reserved_instance_id: ID of the reserved instance to be query.
    :param str result_output_file: Used to save results.
    """
    __args__ = dict()
    __args__['availabilityZone'] = availability_zone
    __args__['instanceType'] = instance_type
    __args__['reservedInstanceId'] = reserved_instance_id
    __args__['resultOutputFile'] = result_output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Reserved/getInstances:getInstances', __args__, opts=opts, typ=GetInstancesResult).value

    return AwaitableGetInstancesResult(
        availability_zone=__ret__.availability_zone,
        id=__ret__.id,
        instance_type=__ret__.instance_type,
        reserved_instance_id=__ret__.reserved_instance_id,
        reserved_instance_lists=__ret__.reserved_instance_lists,
        result_output_file=__ret__.result_output_file)


@_utilities.lift_output_func(get_instances)
def get_instances_output(availability_zone: Optional[pulumi.Input[Optional[str]]] = None,
                         instance_type: Optional[pulumi.Input[Optional[str]]] = None,
                         reserved_instance_id: Optional[pulumi.Input[Optional[str]]] = None,
                         result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstancesResult]:
    """
    Use this data source to query reserved instances.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    instances = tencentcloud.Reserved.get_instances(availability_zone="na-siliconvalley-1",
        instance_type="S2.MEDIUM8")
    ```


    :param str availability_zone: The available zone that the reserved instance locates at.
    :param str instance_type: The type of reserved instance.
    :param str reserved_instance_id: ID of the reserved instance to be query.
    :param str result_output_file: Used to save results.
    """
    ...