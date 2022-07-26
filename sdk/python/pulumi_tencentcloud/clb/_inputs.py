# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'InstanceSnatIpArgs',
    'ServerAttachmentTargetArgs',
    'TargetGroupTargetGroupInstanceArgs',
]

@pulumi.input_type
class InstanceSnatIpArgs:
    def __init__(__self__, *,
                 subnet_id: pulumi.Input[str],
                 ip: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "subnet_id", subnet_id)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)


@pulumi.input_type
class ServerAttachmentTargetArgs:
    def __init__(__self__, *,
                 port: pulumi.Input[int],
                 eni_ip: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        pulumi.set(__self__, "port", port)
        if eni_ip is not None:
            pulumi.set(__self__, "eni_ip", eni_ip)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="eniIp")
    def eni_ip(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "eni_ip")

    @eni_ip.setter
    def eni_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eni_ip", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class TargetGroupTargetGroupInstanceArgs:
    def __init__(__self__, *,
                 bind_ip: pulumi.Input[str],
                 port: pulumi.Input[int],
                 new_port: Optional[pulumi.Input[int]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        pulumi.set(__self__, "bind_ip", bind_ip)
        pulumi.set(__self__, "port", port)
        if new_port is not None:
            pulumi.set(__self__, "new_port", new_port)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="bindIp")
    def bind_ip(self) -> pulumi.Input[str]:
        return pulumi.get(self, "bind_ip")

    @bind_ip.setter
    def bind_ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "bind_ip", value)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="newPort")
    def new_port(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "new_port")

    @new_port.setter
    def new_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "new_port", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)

