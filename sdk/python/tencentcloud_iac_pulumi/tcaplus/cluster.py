# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 idl_type: pulumi.Input[str],
                 password: pulumi.Input[str],
                 subnet_id: pulumi.Input[str],
                 vpc_id: pulumi.Input[str],
                 old_password_expire_last: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] cluster_name: Name of the TcaplusDB cluster. Name length should be between 1 and 30.
        :param pulumi.Input[str] idl_type: IDL type of the TcaplusDB cluster. Valid values: `PROTO` and `TDR`.
        :param pulumi.Input[str] password: Password of the TcaplusDB cluster. Password length should be between 12 and 16. The password must be a *mix* of uppercase letters (A-Z), lowercase *letters* (a-z) and *numbers* (0-9).
        :param pulumi.Input[str] subnet_id: Subnet id of the TcaplusDB cluster.
        :param pulumi.Input[str] vpc_id: VPC id of the TcaplusDB cluster.
        :param pulumi.Input[int] old_password_expire_last: Expiration time of old password after password update, unit: second.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "idl_type", idl_type)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "subnet_id", subnet_id)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if old_password_expire_last is not None:
            pulumi.set(__self__, "old_password_expire_last", old_password_expire_last)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        Name of the TcaplusDB cluster. Name length should be between 1 and 30.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="idlType")
    def idl_type(self) -> pulumi.Input[str]:
        """
        IDL type of the TcaplusDB cluster. Valid values: `PROTO` and `TDR`.
        """
        return pulumi.get(self, "idl_type")

    @idl_type.setter
    def idl_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "idl_type", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        Password of the TcaplusDB cluster. Password length should be between 12 and 16. The password must be a *mix* of uppercase letters (A-Z), lowercase *letters* (a-z) and *numbers* (0-9).
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        Subnet id of the TcaplusDB cluster.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        VPC id of the TcaplusDB cluster.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="oldPasswordExpireLast")
    def old_password_expire_last(self) -> Optional[pulumi.Input[int]]:
        """
        Expiration time of old password after password update, unit: second.
        """
        return pulumi.get(self, "old_password_expire_last")

    @old_password_expire_last.setter
    def old_password_expire_last(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "old_password_expire_last", value)


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *,
                 api_access_id: Optional[pulumi.Input[str]] = None,
                 api_access_ip: Optional[pulumi.Input[str]] = None,
                 api_access_port: Optional[pulumi.Input[int]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 idl_type: Optional[pulumi.Input[str]] = None,
                 network_type: Optional[pulumi.Input[str]] = None,
                 old_password_expire_last: Optional[pulumi.Input[int]] = None,
                 old_password_expire_time: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 password_status: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Cluster resources.
        :param pulumi.Input[str] api_access_id: Access ID of the TcaplusDB cluster.For TcaplusDB SDK connect.
        :param pulumi.Input[str] api_access_ip: Access IP of the TcaplusDB cluster.For TcaplusDB SDK connect.
        :param pulumi.Input[int] api_access_port: Access port of the TcaplusDB cluster.For TcaplusDB SDK connect.
        :param pulumi.Input[str] cluster_name: Name of the TcaplusDB cluster. Name length should be between 1 and 30.
        :param pulumi.Input[str] create_time: Create time of the TcaplusDB cluster.
        :param pulumi.Input[str] idl_type: IDL type of the TcaplusDB cluster. Valid values: `PROTO` and `TDR`.
        :param pulumi.Input[str] network_type: Network type of the TcaplusDB cluster.
        :param pulumi.Input[int] old_password_expire_last: Expiration time of old password after password update, unit: second.
        :param pulumi.Input[str] old_password_expire_time: Expiration time of the old password. If `password_status` is `unmodifiable`, it means the old password has not yet expired.
        :param pulumi.Input[str] password: Password of the TcaplusDB cluster. Password length should be between 12 and 16. The password must be a *mix* of uppercase letters (A-Z), lowercase *letters* (a-z) and *numbers* (0-9).
        :param pulumi.Input[str] password_status: Password status of the TcaplusDB cluster. Valid values: `unmodifiable`, `modifiable`. `unmodifiable`. which means the password can not be changed in this moment; `modifiable`, which means the password can be changed in this moment.
        :param pulumi.Input[str] subnet_id: Subnet id of the TcaplusDB cluster.
        :param pulumi.Input[str] vpc_id: VPC id of the TcaplusDB cluster.
        """
        if api_access_id is not None:
            pulumi.set(__self__, "api_access_id", api_access_id)
        if api_access_ip is not None:
            pulumi.set(__self__, "api_access_ip", api_access_ip)
        if api_access_port is not None:
            pulumi.set(__self__, "api_access_port", api_access_port)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if idl_type is not None:
            pulumi.set(__self__, "idl_type", idl_type)
        if network_type is not None:
            pulumi.set(__self__, "network_type", network_type)
        if old_password_expire_last is not None:
            pulumi.set(__self__, "old_password_expire_last", old_password_expire_last)
        if old_password_expire_time is not None:
            pulumi.set(__self__, "old_password_expire_time", old_password_expire_time)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if password_status is not None:
            pulumi.set(__self__, "password_status", password_status)
        if subnet_id is not None:
            pulumi.set(__self__, "subnet_id", subnet_id)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="apiAccessId")
    def api_access_id(self) -> Optional[pulumi.Input[str]]:
        """
        Access ID of the TcaplusDB cluster.For TcaplusDB SDK connect.
        """
        return pulumi.get(self, "api_access_id")

    @api_access_id.setter
    def api_access_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_access_id", value)

    @property
    @pulumi.getter(name="apiAccessIp")
    def api_access_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Access IP of the TcaplusDB cluster.For TcaplusDB SDK connect.
        """
        return pulumi.get(self, "api_access_ip")

    @api_access_ip.setter
    def api_access_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_access_ip", value)

    @property
    @pulumi.getter(name="apiAccessPort")
    def api_access_port(self) -> Optional[pulumi.Input[int]]:
        """
        Access port of the TcaplusDB cluster.For TcaplusDB SDK connect.
        """
        return pulumi.get(self, "api_access_port")

    @api_access_port.setter
    def api_access_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "api_access_port", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the TcaplusDB cluster. Name length should be between 1 and 30.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Create time of the TcaplusDB cluster.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="idlType")
    def idl_type(self) -> Optional[pulumi.Input[str]]:
        """
        IDL type of the TcaplusDB cluster. Valid values: `PROTO` and `TDR`.
        """
        return pulumi.get(self, "idl_type")

    @idl_type.setter
    def idl_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "idl_type", value)

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[str]]:
        """
        Network type of the TcaplusDB cluster.
        """
        return pulumi.get(self, "network_type")

    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_type", value)

    @property
    @pulumi.getter(name="oldPasswordExpireLast")
    def old_password_expire_last(self) -> Optional[pulumi.Input[int]]:
        """
        Expiration time of old password after password update, unit: second.
        """
        return pulumi.get(self, "old_password_expire_last")

    @old_password_expire_last.setter
    def old_password_expire_last(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "old_password_expire_last", value)

    @property
    @pulumi.getter(name="oldPasswordExpireTime")
    def old_password_expire_time(self) -> Optional[pulumi.Input[str]]:
        """
        Expiration time of the old password. If `password_status` is `unmodifiable`, it means the old password has not yet expired.
        """
        return pulumi.get(self, "old_password_expire_time")

    @old_password_expire_time.setter
    def old_password_expire_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "old_password_expire_time", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password of the TcaplusDB cluster. Password length should be between 12 and 16. The password must be a *mix* of uppercase letters (A-Z), lowercase *letters* (a-z) and *numbers* (0-9).
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="passwordStatus")
    def password_status(self) -> Optional[pulumi.Input[str]]:
        """
        Password status of the TcaplusDB cluster. Valid values: `unmodifiable`, `modifiable`. `unmodifiable`. which means the password can not be changed in this moment; `modifiable`, which means the password can be changed in this moment.
        """
        return pulumi.get(self, "password_status")

    @password_status.setter
    def password_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_status", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[str]]:
        """
        Subnet id of the TcaplusDB cluster.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        """
        VPC id of the TcaplusDB cluster.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 idl_type: Optional[pulumi.Input[str]] = None,
                 old_password_expire_last: Optional[pulumi.Input[int]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Use this resource to create TcaplusDB cluster.

        > **NOTE:** TcaplusDB now only supports the following regions: `ap-shanghai,ap-hongkong,na-siliconvalley,ap-singapore,ap-seoul,ap-tokyo,eu-frankfurt, and na-ashburn`.

        ## Example Usage

        ```python
        import pulumi
        import tencentcloud_iac_pulumi as tencentcloud

        test = tencentcloud.tcaplus.Cluster("test",
            cluster_name="tf_tcaplus_cluster_test",
            idl_type="PROTO",
            old_password_expire_last=3600,
            password="1qaA2k1wgvfa3ZZZ",
            subnet_id="subnet-akwgvfa3",
            vpc_id="vpc-7k6gzox6")
        ```

        ## Import

        tcaplus cluster can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Tcaplus/cluster:Cluster test 26655801
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: Name of the TcaplusDB cluster. Name length should be between 1 and 30.
        :param pulumi.Input[str] idl_type: IDL type of the TcaplusDB cluster. Valid values: `PROTO` and `TDR`.
        :param pulumi.Input[int] old_password_expire_last: Expiration time of old password after password update, unit: second.
        :param pulumi.Input[str] password: Password of the TcaplusDB cluster. Password length should be between 12 and 16. The password must be a *mix* of uppercase letters (A-Z), lowercase *letters* (a-z) and *numbers* (0-9).
        :param pulumi.Input[str] subnet_id: Subnet id of the TcaplusDB cluster.
        :param pulumi.Input[str] vpc_id: VPC id of the TcaplusDB cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Use this resource to create TcaplusDB cluster.

        > **NOTE:** TcaplusDB now only supports the following regions: `ap-shanghai,ap-hongkong,na-siliconvalley,ap-singapore,ap-seoul,ap-tokyo,eu-frankfurt, and na-ashburn`.

        ## Example Usage

        ```python
        import pulumi
        import tencentcloud_iac_pulumi as tencentcloud

        test = tencentcloud.tcaplus.Cluster("test",
            cluster_name="tf_tcaplus_cluster_test",
            idl_type="PROTO",
            old_password_expire_last=3600,
            password="1qaA2k1wgvfa3ZZZ",
            subnet_id="subnet-akwgvfa3",
            vpc_id="vpc-7k6gzox6")
        ```

        ## Import

        tcaplus cluster can be imported using the id, e.g.

        ```sh
         $ pulumi import tencentcloud:Tcaplus/cluster:Cluster test 26655801
        ```

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 idl_type: Optional[pulumi.Input[str]] = None,
                 old_password_expire_last: Optional[pulumi.Input[int]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = ClusterArgs.__new__(ClusterArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if idl_type is None and not opts.urn:
                raise TypeError("Missing required property 'idl_type'")
            __props__.__dict__["idl_type"] = idl_type
            __props__.__dict__["old_password_expire_last"] = old_password_expire_last
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = password
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["api_access_id"] = None
            __props__.__dict__["api_access_ip"] = None
            __props__.__dict__["api_access_port"] = None
            __props__.__dict__["create_time"] = None
            __props__.__dict__["network_type"] = None
            __props__.__dict__["old_password_expire_time"] = None
            __props__.__dict__["password_status"] = None
        super(Cluster, __self__).__init__(
            'tencentcloud:Tcaplus/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_access_id: Optional[pulumi.Input[str]] = None,
            api_access_ip: Optional[pulumi.Input[str]] = None,
            api_access_port: Optional[pulumi.Input[int]] = None,
            cluster_name: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            idl_type: Optional[pulumi.Input[str]] = None,
            network_type: Optional[pulumi.Input[str]] = None,
            old_password_expire_last: Optional[pulumi.Input[int]] = None,
            old_password_expire_time: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            password_status: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_access_id: Access ID of the TcaplusDB cluster.For TcaplusDB SDK connect.
        :param pulumi.Input[str] api_access_ip: Access IP of the TcaplusDB cluster.For TcaplusDB SDK connect.
        :param pulumi.Input[int] api_access_port: Access port of the TcaplusDB cluster.For TcaplusDB SDK connect.
        :param pulumi.Input[str] cluster_name: Name of the TcaplusDB cluster. Name length should be between 1 and 30.
        :param pulumi.Input[str] create_time: Create time of the TcaplusDB cluster.
        :param pulumi.Input[str] idl_type: IDL type of the TcaplusDB cluster. Valid values: `PROTO` and `TDR`.
        :param pulumi.Input[str] network_type: Network type of the TcaplusDB cluster.
        :param pulumi.Input[int] old_password_expire_last: Expiration time of old password after password update, unit: second.
        :param pulumi.Input[str] old_password_expire_time: Expiration time of the old password. If `password_status` is `unmodifiable`, it means the old password has not yet expired.
        :param pulumi.Input[str] password: Password of the TcaplusDB cluster. Password length should be between 12 and 16. The password must be a *mix* of uppercase letters (A-Z), lowercase *letters* (a-z) and *numbers* (0-9).
        :param pulumi.Input[str] password_status: Password status of the TcaplusDB cluster. Valid values: `unmodifiable`, `modifiable`. `unmodifiable`. which means the password can not be changed in this moment; `modifiable`, which means the password can be changed in this moment.
        :param pulumi.Input[str] subnet_id: Subnet id of the TcaplusDB cluster.
        :param pulumi.Input[str] vpc_id: VPC id of the TcaplusDB cluster.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterState.__new__(_ClusterState)

        __props__.__dict__["api_access_id"] = api_access_id
        __props__.__dict__["api_access_ip"] = api_access_ip
        __props__.__dict__["api_access_port"] = api_access_port
        __props__.__dict__["cluster_name"] = cluster_name
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["idl_type"] = idl_type
        __props__.__dict__["network_type"] = network_type
        __props__.__dict__["old_password_expire_last"] = old_password_expire_last
        __props__.__dict__["old_password_expire_time"] = old_password_expire_time
        __props__.__dict__["password"] = password
        __props__.__dict__["password_status"] = password_status
        __props__.__dict__["subnet_id"] = subnet_id
        __props__.__dict__["vpc_id"] = vpc_id
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiAccessId")
    def api_access_id(self) -> pulumi.Output[str]:
        """
        Access ID of the TcaplusDB cluster.For TcaplusDB SDK connect.
        """
        return pulumi.get(self, "api_access_id")

    @property
    @pulumi.getter(name="apiAccessIp")
    def api_access_ip(self) -> pulumi.Output[str]:
        """
        Access IP of the TcaplusDB cluster.For TcaplusDB SDK connect.
        """
        return pulumi.get(self, "api_access_ip")

    @property
    @pulumi.getter(name="apiAccessPort")
    def api_access_port(self) -> pulumi.Output[int]:
        """
        Access port of the TcaplusDB cluster.For TcaplusDB SDK connect.
        """
        return pulumi.get(self, "api_access_port")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        Name of the TcaplusDB cluster. Name length should be between 1 and 30.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Create time of the TcaplusDB cluster.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="idlType")
    def idl_type(self) -> pulumi.Output[str]:
        """
        IDL type of the TcaplusDB cluster. Valid values: `PROTO` and `TDR`.
        """
        return pulumi.get(self, "idl_type")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[str]:
        """
        Network type of the TcaplusDB cluster.
        """
        return pulumi.get(self, "network_type")

    @property
    @pulumi.getter(name="oldPasswordExpireLast")
    def old_password_expire_last(self) -> pulumi.Output[Optional[int]]:
        """
        Expiration time of old password after password update, unit: second.
        """
        return pulumi.get(self, "old_password_expire_last")

    @property
    @pulumi.getter(name="oldPasswordExpireTime")
    def old_password_expire_time(self) -> pulumi.Output[str]:
        """
        Expiration time of the old password. If `password_status` is `unmodifiable`, it means the old password has not yet expired.
        """
        return pulumi.get(self, "old_password_expire_time")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        Password of the TcaplusDB cluster. Password length should be between 12 and 16. The password must be a *mix* of uppercase letters (A-Z), lowercase *letters* (a-z) and *numbers* (0-9).
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="passwordStatus")
    def password_status(self) -> pulumi.Output[str]:
        """
        Password status of the TcaplusDB cluster. Valid values: `unmodifiable`, `modifiable`. `unmodifiable`. which means the password can not be changed in this moment; `modifiable`, which means the password can be changed in this moment.
        """
        return pulumi.get(self, "password_status")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        Subnet id of the TcaplusDB cluster.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        VPC id of the TcaplusDB cluster.
        """
        return pulumi.get(self, "vpc_id")
