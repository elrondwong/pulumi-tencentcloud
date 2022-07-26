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
    'ConfigExcludePath',
    'ConfigExtraContainerFile',
    'ConfigExtraContainerFileWorkload',
    'ConfigExtraContainerStdout',
    'ConfigExtraContainerStdoutWorkload',
    'ConfigExtraExcludePath',
    'ConfigExtraExtractRule',
    'ConfigExtraExtractRuleFilterKeyRegex',
    'ConfigExtraHostFile',
    'ConfigExtractRule',
    'ConfigExtractRuleFilterKeyRegex',
    'CosShipperCompress',
    'CosShipperContent',
    'CosShipperContentCsv',
    'CosShipperContentJson',
    'CosShipperFilterRule',
    'MachineGroupMachineGroupType',
]

@pulumi.output_type
class ConfigExcludePath(dict):
    def __init__(__self__, *,
                 type: Optional[str] = None,
                 value: Optional[str] = None):
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class ConfigExtraContainerFile(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "filePattern":
            suggest = "file_pattern"
        elif key == "logPath":
            suggest = "log_path"
        elif key == "excludeLabels":
            suggest = "exclude_labels"
        elif key == "excludeNamespace":
            suggest = "exclude_namespace"
        elif key == "includeLabels":
            suggest = "include_labels"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigExtraContainerFile. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigExtraContainerFile.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigExtraContainerFile.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 container: str,
                 file_pattern: str,
                 log_path: str,
                 namespace: str,
                 exclude_labels: Optional[Sequence[str]] = None,
                 exclude_namespace: Optional[str] = None,
                 include_labels: Optional[Sequence[str]] = None,
                 workload: Optional['outputs.ConfigExtraContainerFileWorkload'] = None):
        pulumi.set(__self__, "container", container)
        pulumi.set(__self__, "file_pattern", file_pattern)
        pulumi.set(__self__, "log_path", log_path)
        pulumi.set(__self__, "namespace", namespace)
        if exclude_labels is not None:
            pulumi.set(__self__, "exclude_labels", exclude_labels)
        if exclude_namespace is not None:
            pulumi.set(__self__, "exclude_namespace", exclude_namespace)
        if include_labels is not None:
            pulumi.set(__self__, "include_labels", include_labels)
        if workload is not None:
            pulumi.set(__self__, "workload", workload)

    @property
    @pulumi.getter
    def container(self) -> str:
        return pulumi.get(self, "container")

    @property
    @pulumi.getter(name="filePattern")
    def file_pattern(self) -> str:
        return pulumi.get(self, "file_pattern")

    @property
    @pulumi.getter(name="logPath")
    def log_path(self) -> str:
        return pulumi.get(self, "log_path")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="excludeLabels")
    def exclude_labels(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "exclude_labels")

    @property
    @pulumi.getter(name="excludeNamespace")
    def exclude_namespace(self) -> Optional[str]:
        return pulumi.get(self, "exclude_namespace")

    @property
    @pulumi.getter(name="includeLabels")
    def include_labels(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "include_labels")

    @property
    @pulumi.getter
    def workload(self) -> Optional['outputs.ConfigExtraContainerFileWorkload']:
        return pulumi.get(self, "workload")


@pulumi.output_type
class ConfigExtraContainerFileWorkload(dict):
    def __init__(__self__, *,
                 kind: str,
                 name: str,
                 container: Optional[str] = None,
                 namespace: Optional[str] = None):
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "name", name)
        if container is not None:
            pulumi.set(__self__, "container", container)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def kind(self) -> str:
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def container(self) -> Optional[str]:
        return pulumi.get(self, "container")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        return pulumi.get(self, "namespace")


@pulumi.output_type
class ConfigExtraContainerStdout(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allContainers":
            suggest = "all_containers"
        elif key == "excludeLabels":
            suggest = "exclude_labels"
        elif key == "excludeNamespace":
            suggest = "exclude_namespace"
        elif key == "includeLabels":
            suggest = "include_labels"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigExtraContainerStdout. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigExtraContainerStdout.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigExtraContainerStdout.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 all_containers: bool,
                 exclude_labels: Optional[Sequence[str]] = None,
                 exclude_namespace: Optional[str] = None,
                 include_labels: Optional[Sequence[str]] = None,
                 namespace: Optional[str] = None,
                 workloads: Optional[Sequence['outputs.ConfigExtraContainerStdoutWorkload']] = None):
        pulumi.set(__self__, "all_containers", all_containers)
        if exclude_labels is not None:
            pulumi.set(__self__, "exclude_labels", exclude_labels)
        if exclude_namespace is not None:
            pulumi.set(__self__, "exclude_namespace", exclude_namespace)
        if include_labels is not None:
            pulumi.set(__self__, "include_labels", include_labels)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if workloads is not None:
            pulumi.set(__self__, "workloads", workloads)

    @property
    @pulumi.getter(name="allContainers")
    def all_containers(self) -> bool:
        return pulumi.get(self, "all_containers")

    @property
    @pulumi.getter(name="excludeLabels")
    def exclude_labels(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "exclude_labels")

    @property
    @pulumi.getter(name="excludeNamespace")
    def exclude_namespace(self) -> Optional[str]:
        return pulumi.get(self, "exclude_namespace")

    @property
    @pulumi.getter(name="includeLabels")
    def include_labels(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "include_labels")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def workloads(self) -> Optional[Sequence['outputs.ConfigExtraContainerStdoutWorkload']]:
        return pulumi.get(self, "workloads")


@pulumi.output_type
class ConfigExtraContainerStdoutWorkload(dict):
    def __init__(__self__, *,
                 kind: str,
                 name: str,
                 container: Optional[str] = None,
                 namespace: Optional[str] = None):
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "name", name)
        if container is not None:
            pulumi.set(__self__, "container", container)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def kind(self) -> str:
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def container(self) -> Optional[str]:
        return pulumi.get(self, "container")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        return pulumi.get(self, "namespace")


@pulumi.output_type
class ConfigExtraExcludePath(dict):
    def __init__(__self__, *,
                 type: Optional[str] = None,
                 value: Optional[str] = None):
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class ConfigExtraExtractRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "beginRegex":
            suggest = "begin_regex"
        elif key == "filterKeyRegexes":
            suggest = "filter_key_regexes"
        elif key == "logRegex":
            suggest = "log_regex"
        elif key == "timeFormat":
            suggest = "time_format"
        elif key == "timeKey":
            suggest = "time_key"
        elif key == "unMatchLogKey":
            suggest = "un_match_log_key"
        elif key == "unMatchUpLoadSwitch":
            suggest = "un_match_up_load_switch"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigExtraExtractRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigExtraExtractRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigExtraExtractRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 backtracking: Optional[int] = None,
                 begin_regex: Optional[str] = None,
                 delimiter: Optional[str] = None,
                 filter_key_regexes: Optional[Sequence['outputs.ConfigExtraExtractRuleFilterKeyRegex']] = None,
                 keys: Optional[Sequence[str]] = None,
                 log_regex: Optional[str] = None,
                 time_format: Optional[str] = None,
                 time_key: Optional[str] = None,
                 un_match_log_key: Optional[str] = None,
                 un_match_up_load_switch: Optional[bool] = None):
        if backtracking is not None:
            pulumi.set(__self__, "backtracking", backtracking)
        if begin_regex is not None:
            pulumi.set(__self__, "begin_regex", begin_regex)
        if delimiter is not None:
            pulumi.set(__self__, "delimiter", delimiter)
        if filter_key_regexes is not None:
            pulumi.set(__self__, "filter_key_regexes", filter_key_regexes)
        if keys is not None:
            pulumi.set(__self__, "keys", keys)
        if log_regex is not None:
            pulumi.set(__self__, "log_regex", log_regex)
        if time_format is not None:
            pulumi.set(__self__, "time_format", time_format)
        if time_key is not None:
            pulumi.set(__self__, "time_key", time_key)
        if un_match_log_key is not None:
            pulumi.set(__self__, "un_match_log_key", un_match_log_key)
        if un_match_up_load_switch is not None:
            pulumi.set(__self__, "un_match_up_load_switch", un_match_up_load_switch)

    @property
    @pulumi.getter
    def backtracking(self) -> Optional[int]:
        return pulumi.get(self, "backtracking")

    @property
    @pulumi.getter(name="beginRegex")
    def begin_regex(self) -> Optional[str]:
        return pulumi.get(self, "begin_regex")

    @property
    @pulumi.getter
    def delimiter(self) -> Optional[str]:
        return pulumi.get(self, "delimiter")

    @property
    @pulumi.getter(name="filterKeyRegexes")
    def filter_key_regexes(self) -> Optional[Sequence['outputs.ConfigExtraExtractRuleFilterKeyRegex']]:
        return pulumi.get(self, "filter_key_regexes")

    @property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter(name="logRegex")
    def log_regex(self) -> Optional[str]:
        return pulumi.get(self, "log_regex")

    @property
    @pulumi.getter(name="timeFormat")
    def time_format(self) -> Optional[str]:
        return pulumi.get(self, "time_format")

    @property
    @pulumi.getter(name="timeKey")
    def time_key(self) -> Optional[str]:
        return pulumi.get(self, "time_key")

    @property
    @pulumi.getter(name="unMatchLogKey")
    def un_match_log_key(self) -> Optional[str]:
        return pulumi.get(self, "un_match_log_key")

    @property
    @pulumi.getter(name="unMatchUpLoadSwitch")
    def un_match_up_load_switch(self) -> Optional[bool]:
        return pulumi.get(self, "un_match_up_load_switch")


@pulumi.output_type
class ConfigExtraExtractRuleFilterKeyRegex(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 regex: Optional[str] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def regex(self) -> Optional[str]:
        return pulumi.get(self, "regex")


@pulumi.output_type
class ConfigExtraHostFile(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "filePattern":
            suggest = "file_pattern"
        elif key == "logPath":
            suggest = "log_path"
        elif key == "customLabels":
            suggest = "custom_labels"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigExtraHostFile. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigExtraHostFile.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigExtraHostFile.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 file_pattern: str,
                 log_path: str,
                 custom_labels: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "file_pattern", file_pattern)
        pulumi.set(__self__, "log_path", log_path)
        if custom_labels is not None:
            pulumi.set(__self__, "custom_labels", custom_labels)

    @property
    @pulumi.getter(name="filePattern")
    def file_pattern(self) -> str:
        return pulumi.get(self, "file_pattern")

    @property
    @pulumi.getter(name="logPath")
    def log_path(self) -> str:
        return pulumi.get(self, "log_path")

    @property
    @pulumi.getter(name="customLabels")
    def custom_labels(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "custom_labels")


@pulumi.output_type
class ConfigExtractRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "beginRegex":
            suggest = "begin_regex"
        elif key == "filterKeyRegexes":
            suggest = "filter_key_regexes"
        elif key == "logRegex":
            suggest = "log_regex"
        elif key == "timeFormat":
            suggest = "time_format"
        elif key == "timeKey":
            suggest = "time_key"
        elif key == "unMatchLogKey":
            suggest = "un_match_log_key"
        elif key == "unMatchUpLoadSwitch":
            suggest = "un_match_up_load_switch"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigExtractRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigExtractRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigExtractRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 backtracking: Optional[int] = None,
                 begin_regex: Optional[str] = None,
                 delimiter: Optional[str] = None,
                 filter_key_regexes: Optional[Sequence['outputs.ConfigExtractRuleFilterKeyRegex']] = None,
                 keys: Optional[Sequence[str]] = None,
                 log_regex: Optional[str] = None,
                 time_format: Optional[str] = None,
                 time_key: Optional[str] = None,
                 un_match_log_key: Optional[str] = None,
                 un_match_up_load_switch: Optional[bool] = None):
        if backtracking is not None:
            pulumi.set(__self__, "backtracking", backtracking)
        if begin_regex is not None:
            pulumi.set(__self__, "begin_regex", begin_regex)
        if delimiter is not None:
            pulumi.set(__self__, "delimiter", delimiter)
        if filter_key_regexes is not None:
            pulumi.set(__self__, "filter_key_regexes", filter_key_regexes)
        if keys is not None:
            pulumi.set(__self__, "keys", keys)
        if log_regex is not None:
            pulumi.set(__self__, "log_regex", log_regex)
        if time_format is not None:
            pulumi.set(__self__, "time_format", time_format)
        if time_key is not None:
            pulumi.set(__self__, "time_key", time_key)
        if un_match_log_key is not None:
            pulumi.set(__self__, "un_match_log_key", un_match_log_key)
        if un_match_up_load_switch is not None:
            pulumi.set(__self__, "un_match_up_load_switch", un_match_up_load_switch)

    @property
    @pulumi.getter
    def backtracking(self) -> Optional[int]:
        return pulumi.get(self, "backtracking")

    @property
    @pulumi.getter(name="beginRegex")
    def begin_regex(self) -> Optional[str]:
        return pulumi.get(self, "begin_regex")

    @property
    @pulumi.getter
    def delimiter(self) -> Optional[str]:
        return pulumi.get(self, "delimiter")

    @property
    @pulumi.getter(name="filterKeyRegexes")
    def filter_key_regexes(self) -> Optional[Sequence['outputs.ConfigExtractRuleFilterKeyRegex']]:
        return pulumi.get(self, "filter_key_regexes")

    @property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter(name="logRegex")
    def log_regex(self) -> Optional[str]:
        return pulumi.get(self, "log_regex")

    @property
    @pulumi.getter(name="timeFormat")
    def time_format(self) -> Optional[str]:
        return pulumi.get(self, "time_format")

    @property
    @pulumi.getter(name="timeKey")
    def time_key(self) -> Optional[str]:
        return pulumi.get(self, "time_key")

    @property
    @pulumi.getter(name="unMatchLogKey")
    def un_match_log_key(self) -> Optional[str]:
        return pulumi.get(self, "un_match_log_key")

    @property
    @pulumi.getter(name="unMatchUpLoadSwitch")
    def un_match_up_load_switch(self) -> Optional[bool]:
        return pulumi.get(self, "un_match_up_load_switch")


@pulumi.output_type
class ConfigExtractRuleFilterKeyRegex(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 regex: Optional[str] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def regex(self) -> Optional[str]:
        return pulumi.get(self, "regex")


@pulumi.output_type
class CosShipperCompress(dict):
    def __init__(__self__, *,
                 format: str):
        pulumi.set(__self__, "format", format)

    @property
    @pulumi.getter
    def format(self) -> str:
        return pulumi.get(self, "format")


@pulumi.output_type
class CosShipperContent(dict):
    def __init__(__self__, *,
                 format: str,
                 csv: Optional['outputs.CosShipperContentCsv'] = None,
                 json: Optional['outputs.CosShipperContentJson'] = None):
        pulumi.set(__self__, "format", format)
        if csv is not None:
            pulumi.set(__self__, "csv", csv)
        if json is not None:
            pulumi.set(__self__, "json", json)

    @property
    @pulumi.getter
    def format(self) -> str:
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def csv(self) -> Optional['outputs.CosShipperContentCsv']:
        return pulumi.get(self, "csv")

    @property
    @pulumi.getter
    def json(self) -> Optional['outputs.CosShipperContentJson']:
        return pulumi.get(self, "json")


@pulumi.output_type
class CosShipperContentCsv(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "escapeChar":
            suggest = "escape_char"
        elif key == "nonExistingField":
            suggest = "non_existing_field"
        elif key == "printKey":
            suggest = "print_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CosShipperContentCsv. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CosShipperContentCsv.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CosShipperContentCsv.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 delimiter: str,
                 escape_char: str,
                 keys: Sequence[str],
                 non_existing_field: str,
                 print_key: bool):
        pulumi.set(__self__, "delimiter", delimiter)
        pulumi.set(__self__, "escape_char", escape_char)
        pulumi.set(__self__, "keys", keys)
        pulumi.set(__self__, "non_existing_field", non_existing_field)
        pulumi.set(__self__, "print_key", print_key)

    @property
    @pulumi.getter
    def delimiter(self) -> str:
        return pulumi.get(self, "delimiter")

    @property
    @pulumi.getter(name="escapeChar")
    def escape_char(self) -> str:
        return pulumi.get(self, "escape_char")

    @property
    @pulumi.getter
    def keys(self) -> Sequence[str]:
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter(name="nonExistingField")
    def non_existing_field(self) -> str:
        return pulumi.get(self, "non_existing_field")

    @property
    @pulumi.getter(name="printKey")
    def print_key(self) -> bool:
        return pulumi.get(self, "print_key")


@pulumi.output_type
class CosShipperContentJson(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "enableTag":
            suggest = "enable_tag"
        elif key == "metaFields":
            suggest = "meta_fields"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CosShipperContentJson. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CosShipperContentJson.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CosShipperContentJson.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enable_tag: bool,
                 meta_fields: Sequence[str]):
        pulumi.set(__self__, "enable_tag", enable_tag)
        pulumi.set(__self__, "meta_fields", meta_fields)

    @property
    @pulumi.getter(name="enableTag")
    def enable_tag(self) -> bool:
        return pulumi.get(self, "enable_tag")

    @property
    @pulumi.getter(name="metaFields")
    def meta_fields(self) -> Sequence[str]:
        return pulumi.get(self, "meta_fields")


@pulumi.output_type
class CosShipperFilterRule(dict):
    def __init__(__self__, *,
                 key: str,
                 regex: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "regex", regex)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def regex(self) -> str:
        return pulumi.get(self, "regex")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class MachineGroupMachineGroupType(dict):
    def __init__(__self__, *,
                 type: str,
                 values: Sequence[str]):
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

