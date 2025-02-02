# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GroupRuleAddressTemplate',
    'GroupRuleProtocolTemplate',
    'GetGroupsSecurityGroupResult',
]

@pulumi.output_type
class GroupRuleAddressTemplate(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "groupId":
            suggest = "group_id"
        elif key == "templateId":
            suggest = "template_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GroupRuleAddressTemplate. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GroupRuleAddressTemplate.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GroupRuleAddressTemplate.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 group_id: Optional[str] = None,
                 template_id: Optional[str] = None):
        """
        :param str group_id: Address template group ID, conflicts with `template_id`.
        :param str template_id: Address template ID, conflicts with `group_id`.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if template_id is not None:
            pulumi.set(__self__, "template_id", template_id)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[str]:
        """
        Address template group ID, conflicts with `template_id`.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[str]:
        """
        Address template ID, conflicts with `group_id`.
        """
        return pulumi.get(self, "template_id")


@pulumi.output_type
class GroupRuleProtocolTemplate(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "groupId":
            suggest = "group_id"
        elif key == "templateId":
            suggest = "template_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GroupRuleProtocolTemplate. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GroupRuleProtocolTemplate.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GroupRuleProtocolTemplate.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 group_id: Optional[str] = None,
                 template_id: Optional[str] = None):
        """
        :param str group_id: Address template group ID, conflicts with `template_id`.
        :param str template_id: Address template ID, conflicts with `group_id`.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if template_id is not None:
            pulumi.set(__self__, "template_id", template_id)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[str]:
        """
        Address template group ID, conflicts with `template_id`.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="templateId")
    def template_id(self) -> Optional[str]:
        """
        Address template ID, conflicts with `group_id`.
        """
        return pulumi.get(self, "template_id")


@pulumi.output_type
class GetGroupsSecurityGroupResult(dict):
    def __init__(__self__, *,
                 be_associate_count: int,
                 create_time: str,
                 description: str,
                 egresses: Sequence[str],
                 ingresses: Sequence[str],
                 name: str,
                 project_id: int,
                 security_group_id: str,
                 tags: Mapping[str, Any]):
        """
        :param int be_associate_count: Number of security group binding resources.
        :param str create_time: Creation time of security group.
        :param str description: Description of the security group.
        :param Sequence[str] egresses: Egress rules set. For items like `[action]#[cidr_ip]#[port]#[protocol]`, it means a regular rule; for items like `sg-XXXX`, it means a nested security group.
        :param Sequence[str] ingresses: Ingress rules set. For items like `[action]#[cidr_ip]#[port]#[protocol]`, it means a regular rule; for items like `sg-XXXX`, it means a nested security group.
        :param str name: Name of the security group to be queried. Conflict with `security_group_id`.
        :param int project_id: Project ID of the security group to be queried. Conflict with `security_group_id`.
        :param str security_group_id: ID of the security group to be queried. Conflict with `name` and `project_id`.
        :param Mapping[str, Any] tags: Tags of the security group to be queried. Conflict with `security_group_id`.
        """
        pulumi.set(__self__, "be_associate_count", be_associate_count)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "egresses", egresses)
        pulumi.set(__self__, "ingresses", ingresses)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "security_group_id", security_group_id)
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="beAssociateCount")
    def be_associate_count(self) -> int:
        """
        Number of security group binding resources.
        """
        return pulumi.get(self, "be_associate_count")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Creation time of security group.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the security group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def egresses(self) -> Sequence[str]:
        """
        Egress rules set. For items like `[action]#[cidr_ip]#[port]#[protocol]`, it means a regular rule; for items like `sg-XXXX`, it means a nested security group.
        """
        return pulumi.get(self, "egresses")

    @property
    @pulumi.getter
    def ingresses(self) -> Sequence[str]:
        """
        Ingress rules set. For items like `[action]#[cidr_ip]#[port]#[protocol]`, it means a regular rule; for items like `sg-XXXX`, it means a nested security group.
        """
        return pulumi.get(self, "ingresses")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the security group to be queried. Conflict with `security_group_id`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> int:
        """
        Project ID of the security group to be queried. Conflict with `security_group_id`.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> str:
        """
        ID of the security group to be queried. Conflict with `name` and `project_id`.
        """
        return pulumi.get(self, "security_group_id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, Any]:
        """
        Tags of the security group to be queried. Conflict with `security_group_id`.
        """
        return pulumi.get(self, "tags")


