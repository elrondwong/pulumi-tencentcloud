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

__all__ = ['CCHttpsPolicyArgs', 'CCHttpsPolicy']

@pulumi.input_type
class CCHttpsPolicyArgs:
    def __init__(__self__, *,
                 domain: pulumi.Input[str],
                 resource_id: pulumi.Input[str],
                 resource_type: pulumi.Input[str],
                 rule_id: pulumi.Input[str],
                 rule_lists: pulumi.Input[Sequence[pulumi.Input['CCHttpsPolicyRuleListArgs']]],
                 action: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 switch: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a CCHttpsPolicy resource.
        :param pulumi.Input[str] domain: Domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        :param pulumi.Input[str] resource_id: ID of the resource that the CC self-define https policy works for.
        :param pulumi.Input[str] resource_type: Type of the resource that the CC self-define https policy works for, valid value is `bgpip`.
        :param pulumi.Input[str] rule_id: Rule id of the domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        :param pulumi.Input[Sequence[pulumi.Input['CCHttpsPolicyRuleListArgs']]] rule_lists: Rule list of the CC self-define https policy.
        :param pulumi.Input[str] action: Action mode. Valid values are `alg` and `drop`.
        :param pulumi.Input[str] name: Name of the CC self-define https policy. Length should between 1 and 20.
        :param pulumi.Input[bool] switch: Indicate the CC self-define https policy takes effect or not.
        """
        pulumi.set(__self__, "domain", domain)
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "resource_type", resource_type)
        pulumi.set(__self__, "rule_id", rule_id)
        pulumi.set(__self__, "rule_lists", rule_lists)
        if action is not None:
            pulumi.set(__self__, "action", action)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if switch is not None:
            pulumi.set(__self__, "switch", switch)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        Domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        ID of the resource that the CC self-define https policy works for.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[str]:
        """
        Type of the resource that the CC self-define https policy works for, valid value is `bgpip`.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Input[str]:
        """
        Rule id of the domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        """
        return pulumi.get(self, "rule_id")

    @rule_id.setter
    def rule_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_id", value)

    @property
    @pulumi.getter(name="ruleLists")
    def rule_lists(self) -> pulumi.Input[Sequence[pulumi.Input['CCHttpsPolicyRuleListArgs']]]:
        """
        Rule list of the CC self-define https policy.
        """
        return pulumi.get(self, "rule_lists")

    @rule_lists.setter
    def rule_lists(self, value: pulumi.Input[Sequence[pulumi.Input['CCHttpsPolicyRuleListArgs']]]):
        pulumi.set(self, "rule_lists", value)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        Action mode. Valid values are `alg` and `drop`.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the CC self-define https policy. Length should between 1 and 20.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def switch(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicate the CC self-define https policy takes effect or not.
        """
        return pulumi.get(self, "switch")

    @switch.setter
    def switch(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "switch", value)


@pulumi.input_type
class _CCHttpsPolicyState:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 rule_id: Optional[pulumi.Input[str]] = None,
                 rule_lists: Optional[pulumi.Input[Sequence[pulumi.Input['CCHttpsPolicyRuleListArgs']]]] = None,
                 switch: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering CCHttpsPolicy resources.
        :param pulumi.Input[str] action: Action mode. Valid values are `alg` and `drop`.
        :param pulumi.Input[str] create_time: Create time of the CC self-define https policy.
        :param pulumi.Input[str] domain: Domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_lists: Ip of the CC self-define https policy.
        :param pulumi.Input[str] name: Name of the CC self-define https policy. Length should between 1 and 20.
        :param pulumi.Input[str] policy_id: Id of the CC self-define https policy.
        :param pulumi.Input[str] resource_id: ID of the resource that the CC self-define https policy works for.
        :param pulumi.Input[str] resource_type: Type of the resource that the CC self-define https policy works for, valid value is `bgpip`.
        :param pulumi.Input[str] rule_id: Rule id of the domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        :param pulumi.Input[Sequence[pulumi.Input['CCHttpsPolicyRuleListArgs']]] rule_lists: Rule list of the CC self-define https policy.
        :param pulumi.Input[bool] switch: Indicate the CC self-define https policy takes effect or not.
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if ip_lists is not None:
            pulumi.set(__self__, "ip_lists", ip_lists)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)
        if rule_id is not None:
            pulumi.set(__self__, "rule_id", rule_id)
        if rule_lists is not None:
            pulumi.set(__self__, "rule_lists", rule_lists)
        if switch is not None:
            pulumi.set(__self__, "switch", switch)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        Action mode. Valid values are `alg` and `drop`.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Create time of the CC self-define https policy.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        Domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="ipLists")
    def ip_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Ip of the CC self-define https policy.
        """
        return pulumi.get(self, "ip_lists")

    @ip_lists.setter
    def ip_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ip_lists", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the CC self-define https policy. Length should between 1 and 20.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of the CC self-define https policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the resource that the CC self-define https policy works for.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the resource that the CC self-define https policy works for, valid value is `bgpip`.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        Rule id of the domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        """
        return pulumi.get(self, "rule_id")

    @rule_id.setter
    def rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_id", value)

    @property
    @pulumi.getter(name="ruleLists")
    def rule_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CCHttpsPolicyRuleListArgs']]]]:
        """
        Rule list of the CC self-define https policy.
        """
        return pulumi.get(self, "rule_lists")

    @rule_lists.setter
    def rule_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CCHttpsPolicyRuleListArgs']]]]):
        pulumi.set(self, "rule_lists", value)

    @property
    @pulumi.getter
    def switch(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicate the CC self-define https policy takes effect or not.
        """
        return pulumi.get(self, "switch")

    @switch.setter
    def switch(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "switch", value)


class CCHttpsPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 rule_id: Optional[pulumi.Input[str]] = None,
                 rule_lists: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CCHttpsPolicyRuleListArgs']]]]] = None,
                 switch: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a CCHttpsPolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: Action mode. Valid values are `alg` and `drop`.
        :param pulumi.Input[str] domain: Domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        :param pulumi.Input[str] name: Name of the CC self-define https policy. Length should between 1 and 20.
        :param pulumi.Input[str] resource_id: ID of the resource that the CC self-define https policy works for.
        :param pulumi.Input[str] resource_type: Type of the resource that the CC self-define https policy works for, valid value is `bgpip`.
        :param pulumi.Input[str] rule_id: Rule id of the domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CCHttpsPolicyRuleListArgs']]]] rule_lists: Rule list of the CC self-define https policy.
        :param pulumi.Input[bool] switch: Indicate the CC self-define https policy takes effect or not.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CCHttpsPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CCHttpsPolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CCHttpsPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CCHttpsPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 rule_id: Optional[pulumi.Input[str]] = None,
                 rule_lists: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CCHttpsPolicyRuleListArgs']]]]] = None,
                 switch: Optional[pulumi.Input[bool]] = None,
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
            __props__ = CCHttpsPolicyArgs.__new__(CCHttpsPolicyArgs)

            __props__.__dict__["action"] = action
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            __props__.__dict__["name"] = name
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            if resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'resource_type'")
            __props__.__dict__["resource_type"] = resource_type
            if rule_id is None and not opts.urn:
                raise TypeError("Missing required property 'rule_id'")
            __props__.__dict__["rule_id"] = rule_id
            if rule_lists is None and not opts.urn:
                raise TypeError("Missing required property 'rule_lists'")
            __props__.__dict__["rule_lists"] = rule_lists
            __props__.__dict__["switch"] = switch
            __props__.__dict__["create_time"] = None
            __props__.__dict__["ip_lists"] = None
            __props__.__dict__["policy_id"] = None
        super(CCHttpsPolicy, __self__).__init__(
            'tencentcloud:Dayu/cCHttpsPolicy:CCHttpsPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            ip_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            policy_id: Optional[pulumi.Input[str]] = None,
            resource_id: Optional[pulumi.Input[str]] = None,
            resource_type: Optional[pulumi.Input[str]] = None,
            rule_id: Optional[pulumi.Input[str]] = None,
            rule_lists: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CCHttpsPolicyRuleListArgs']]]]] = None,
            switch: Optional[pulumi.Input[bool]] = None) -> 'CCHttpsPolicy':
        """
        Get an existing CCHttpsPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: Action mode. Valid values are `alg` and `drop`.
        :param pulumi.Input[str] create_time: Create time of the CC self-define https policy.
        :param pulumi.Input[str] domain: Domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_lists: Ip of the CC self-define https policy.
        :param pulumi.Input[str] name: Name of the CC self-define https policy. Length should between 1 and 20.
        :param pulumi.Input[str] policy_id: Id of the CC self-define https policy.
        :param pulumi.Input[str] resource_id: ID of the resource that the CC self-define https policy works for.
        :param pulumi.Input[str] resource_type: Type of the resource that the CC self-define https policy works for, valid value is `bgpip`.
        :param pulumi.Input[str] rule_id: Rule id of the domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CCHttpsPolicyRuleListArgs']]]] rule_lists: Rule list of the CC self-define https policy.
        :param pulumi.Input[bool] switch: Indicate the CC self-define https policy takes effect or not.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CCHttpsPolicyState.__new__(_CCHttpsPolicyState)

        __props__.__dict__["action"] = action
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["domain"] = domain
        __props__.__dict__["ip_lists"] = ip_lists
        __props__.__dict__["name"] = name
        __props__.__dict__["policy_id"] = policy_id
        __props__.__dict__["resource_id"] = resource_id
        __props__.__dict__["resource_type"] = resource_type
        __props__.__dict__["rule_id"] = rule_id
        __props__.__dict__["rule_lists"] = rule_lists
        __props__.__dict__["switch"] = switch
        return CCHttpsPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        """
        Action mode. Valid values are `alg` and `drop`.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Create time of the CC self-define https policy.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        Domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="ipLists")
    def ip_lists(self) -> pulumi.Output[Sequence[str]]:
        """
        Ip of the CC self-define https policy.
        """
        return pulumi.get(self, "ip_lists")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the CC self-define https policy. Length should between 1 and 20.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[str]:
        """
        Id of the CC self-define https policy.
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        ID of the resource that the CC self-define https policy works for.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[str]:
        """
        Type of the resource that the CC self-define https policy works for, valid value is `bgpip`.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Output[str]:
        """
        Rule id of the domain that the CC self-define https policy works for, only valid when `protocol` is `https`.
        """
        return pulumi.get(self, "rule_id")

    @property
    @pulumi.getter(name="ruleLists")
    def rule_lists(self) -> pulumi.Output[Sequence['outputs.CCHttpsPolicyRuleList']]:
        """
        Rule list of the CC self-define https policy.
        """
        return pulumi.get(self, "rule_lists")

    @property
    @pulumi.getter
    def switch(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicate the CC self-define https policy takes effect or not.
        """
        return pulumi.get(self, "switch")
