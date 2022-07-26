# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'InstanceSecurityPolicyArgs',
]

@pulumi.input_type
class InstanceSecurityPolicyArgs:
    def __init__(__self__, *,
                 cidr_block: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 index: Optional[pulumi.Input[int]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        if cidr_block is not None:
            pulumi.set(__self__, "cidr_block", cidr_block)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if index is not None:
            pulumi.set(__self__, "index", index)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cidr_block")

    @cidr_block.setter
    def cidr_block(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_block", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def index(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "index")

    @index.setter
    def index(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "index", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)

