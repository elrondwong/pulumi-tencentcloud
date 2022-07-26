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
    'InstancesResult',
    'AwaitableInstancesResult',
    'instances',
    'instances_output',
]

@pulumi.output_type
class InstancesResult:
    """
    A collection of values returned by Instances.
    """
    def __init__(__self__, bandwidth=None, id=None, max_concurrent=None, name=None, nats=None, state=None, vpc_id=None):
        if bandwidth and not isinstance(bandwidth, int):
            raise TypeError("Expected argument 'bandwidth' to be a int")
        pulumi.set(__self__, "bandwidth", bandwidth)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_concurrent and not isinstance(max_concurrent, int):
            raise TypeError("Expected argument 'max_concurrent' to be a int")
        pulumi.set(__self__, "max_concurrent", max_concurrent)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nats and not isinstance(nats, list):
            raise TypeError("Expected argument 'nats' to be a list")
        pulumi.set(__self__, "nats", nats)
        if state and not isinstance(state, int):
            raise TypeError("Expected argument 'state' to be a int")
        pulumi.set(__self__, "state", state)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter
    def bandwidth(self) -> Optional[int]:
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxConcurrent")
    def max_concurrent(self) -> Optional[int]:
        return pulumi.get(self, "max_concurrent")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nats(self) -> Sequence['outputs.InstancesNatResult']:
        return pulumi.get(self, "nats")

    @property
    @pulumi.getter
    def state(self) -> Optional[int]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        return pulumi.get(self, "vpc_id")


class AwaitableInstancesResult(InstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return InstancesResult(
            bandwidth=self.bandwidth,
            id=self.id,
            max_concurrent=self.max_concurrent,
            name=self.name,
            nats=self.nats,
            state=self.state,
            vpc_id=self.vpc_id)


def instances(bandwidth: Optional[int] = None,
              id: Optional[str] = None,
              max_concurrent: Optional[int] = None,
              name: Optional[str] = None,
              state: Optional[int] = None,
              vpc_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableInstancesResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['bandwidth'] = bandwidth
    __args__['id'] = id
    __args__['maxConcurrent'] = max_concurrent
    __args__['name'] = name
    __args__['state'] = state
    __args__['vpcId'] = vpc_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Nats/instances:Instances', __args__, opts=opts, typ=InstancesResult).value

    return AwaitableInstancesResult(
        bandwidth=__ret__.bandwidth,
        id=__ret__.id,
        max_concurrent=__ret__.max_concurrent,
        name=__ret__.name,
        nats=__ret__.nats,
        state=__ret__.state,
        vpc_id=__ret__.vpc_id)


@_utilities.lift_output_func(instances)
def instances_output(bandwidth: Optional[pulumi.Input[Optional[int]]] = None,
                     id: Optional[pulumi.Input[Optional[str]]] = None,
                     max_concurrent: Optional[pulumi.Input[Optional[int]]] = None,
                     name: Optional[pulumi.Input[Optional[str]]] = None,
                     state: Optional[pulumi.Input[Optional[int]]] = None,
                     vpc_id: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[InstancesResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...