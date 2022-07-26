# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'InstanceBackupPlan',
    'InstanceDbNodeSet',
    'InstancesInstanceListResult',
    'SpecinfosListResult',
    'XlogsListResult',
]

@pulumi.output_type
class InstanceBackupPlan(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "backupPeriods":
            suggest = "backup_periods"
        elif key == "baseBackupRetentionPeriod":
            suggest = "base_backup_retention_period"
        elif key == "maxBackupStartTime":
            suggest = "max_backup_start_time"
        elif key == "minBackupStartTime":
            suggest = "min_backup_start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceBackupPlan. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceBackupPlan.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceBackupPlan.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 backup_periods: Optional[Sequence[str]] = None,
                 base_backup_retention_period: Optional[int] = None,
                 max_backup_start_time: Optional[str] = None,
                 min_backup_start_time: Optional[str] = None):
        if backup_periods is not None:
            pulumi.set(__self__, "backup_periods", backup_periods)
        if base_backup_retention_period is not None:
            pulumi.set(__self__, "base_backup_retention_period", base_backup_retention_period)
        if max_backup_start_time is not None:
            pulumi.set(__self__, "max_backup_start_time", max_backup_start_time)
        if min_backup_start_time is not None:
            pulumi.set(__self__, "min_backup_start_time", min_backup_start_time)

    @property
    @pulumi.getter(name="backupPeriods")
    def backup_periods(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "backup_periods")

    @property
    @pulumi.getter(name="baseBackupRetentionPeriod")
    def base_backup_retention_period(self) -> Optional[int]:
        return pulumi.get(self, "base_backup_retention_period")

    @property
    @pulumi.getter(name="maxBackupStartTime")
    def max_backup_start_time(self) -> Optional[str]:
        return pulumi.get(self, "max_backup_start_time")

    @property
    @pulumi.getter(name="minBackupStartTime")
    def min_backup_start_time(self) -> Optional[str]:
        return pulumi.get(self, "min_backup_start_time")


@pulumi.output_type
class InstanceDbNodeSet(dict):
    def __init__(__self__, *,
                 zone: str,
                 role: Optional[str] = None):
        pulumi.set(__self__, "zone", zone)
        if role is not None:
            pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter
    def zone(self) -> str:
        return pulumi.get(self, "zone")

    @property
    @pulumi.getter
    def role(self) -> Optional[str]:
        return pulumi.get(self, "role")


@pulumi.output_type
class InstancesInstanceListResult(dict):
    def __init__(__self__, *,
                 auto_renew_flag: int,
                 availability_zone: str,
                 charge_type: str,
                 charset: str,
                 create_time: str,
                 engine_version: str,
                 id: str,
                 memory: int,
                 name: str,
                 private_access_ip: str,
                 private_access_port: int,
                 project_id: int,
                 public_access_host: str,
                 public_access_port: int,
                 public_access_switch: bool,
                 root_user: str,
                 storage: int,
                 subnet_id: str,
                 tags: Mapping[str, Any],
                 vpc_id: str):
        pulumi.set(__self__, "auto_renew_flag", auto_renew_flag)
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "charge_type", charge_type)
        pulumi.set(__self__, "charset", charset)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "engine_version", engine_version)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "memory", memory)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "private_access_ip", private_access_ip)
        pulumi.set(__self__, "private_access_port", private_access_port)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "public_access_host", public_access_host)
        pulumi.set(__self__, "public_access_port", public_access_port)
        pulumi.set(__self__, "public_access_switch", public_access_switch)
        pulumi.set(__self__, "root_user", root_user)
        pulumi.set(__self__, "storage", storage)
        pulumi.set(__self__, "subnet_id", subnet_id)
        pulumi.set(__self__, "tags", tags)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="autoRenewFlag")
    def auto_renew_flag(self) -> int:
        return pulumi.get(self, "auto_renew_flag")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> str:
        return pulumi.get(self, "charge_type")

    @property
    @pulumi.getter
    def charset(self) -> str:
        return pulumi.get(self, "charset")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> str:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def memory(self) -> int:
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateAccessIp")
    def private_access_ip(self) -> str:
        return pulumi.get(self, "private_access_ip")

    @property
    @pulumi.getter(name="privateAccessPort")
    def private_access_port(self) -> int:
        return pulumi.get(self, "private_access_port")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> int:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="publicAccessHost")
    def public_access_host(self) -> str:
        return pulumi.get(self, "public_access_host")

    @property
    @pulumi.getter(name="publicAccessPort")
    def public_access_port(self) -> int:
        return pulumi.get(self, "public_access_port")

    @property
    @pulumi.getter(name="publicAccessSwitch")
    def public_access_switch(self) -> bool:
        return pulumi.get(self, "public_access_switch")

    @property
    @pulumi.getter(name="rootUser")
    def root_user(self) -> str:
        return pulumi.get(self, "root_user")

    @property
    @pulumi.getter
    def storage(self) -> int:
        return pulumi.get(self, "storage")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, Any]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        return pulumi.get(self, "vpc_id")


@pulumi.output_type
class SpecinfosListResult(dict):
    def __init__(__self__, *,
                 cpu: int,
                 engine_version: str,
                 engine_version_name: str,
                 id: str,
                 memory: int,
                 qps: int,
                 storage_max: int,
                 storage_min: int):
        pulumi.set(__self__, "cpu", cpu)
        pulumi.set(__self__, "engine_version", engine_version)
        pulumi.set(__self__, "engine_version_name", engine_version_name)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "memory", memory)
        pulumi.set(__self__, "qps", qps)
        pulumi.set(__self__, "storage_max", storage_max)
        pulumi.set(__self__, "storage_min", storage_min)

    @property
    @pulumi.getter
    def cpu(self) -> int:
        return pulumi.get(self, "cpu")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> str:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="engineVersionName")
    def engine_version_name(self) -> str:
        return pulumi.get(self, "engine_version_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def memory(self) -> int:
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter
    def qps(self) -> int:
        return pulumi.get(self, "qps")

    @property
    @pulumi.getter(name="storageMax")
    def storage_max(self) -> int:
        return pulumi.get(self, "storage_max")

    @property
    @pulumi.getter(name="storageMin")
    def storage_min(self) -> int:
        return pulumi.get(self, "storage_min")


@pulumi.output_type
class XlogsListResult(dict):
    def __init__(__self__, *,
                 end_time: str,
                 external_addr: str,
                 id: int,
                 internal_addr: str,
                 size: int,
                 start_time: str):
        pulumi.set(__self__, "end_time", end_time)
        pulumi.set(__self__, "external_addr", external_addr)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "internal_addr", internal_addr)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="externalAddr")
    def external_addr(self) -> str:
        return pulumi.get(self, "external_addr")

    @property
    @pulumi.getter
    def id(self) -> int:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="internalAddr")
    def internal_addr(self) -> str:
        return pulumi.get(self, "internal_addr")

    @property
    @pulumi.getter
    def size(self) -> int:
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        return pulumi.get(self, "start_time")

