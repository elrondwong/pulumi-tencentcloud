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
    def __init__(__self__, id=None, instance_lists=None, name=None, project_id=None, result_output_file=None, subnet_id=None, vpc_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_lists and not isinstance(instance_lists, list):
            raise TypeError("Expected argument 'instance_lists' to be a list")
        pulumi.set(__self__, "instance_lists", instance_lists)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if project_id and not isinstance(project_id, int):
            raise TypeError("Expected argument 'project_id' to be a int")
        pulumi.set(__self__, "project_id", project_id)
        if result_output_file and not isinstance(result_output_file, str):
            raise TypeError("Expected argument 'result_output_file' to be a str")
        pulumi.set(__self__, "result_output_file", result_output_file)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        ID of the SQL Server instance.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceLists")
    def instance_lists(self) -> Sequence['outputs.GetInstancesInstanceListResult']:
        """
        A list of SQL Server instances. Each element contains the following attributes.
        """
        return pulumi.get(self, "instance_lists")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the SQL Server instance.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[int]:
        """
        Project ID, default value is 0.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="resultOutputFile")
    def result_output_file(self) -> Optional[str]:
        return pulumi.get(self, "result_output_file")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[str]:
        """
        ID of subnet.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        """
        ID of VPC.
        """
        return pulumi.get(self, "vpc_id")


class AwaitableGetInstancesResult(GetInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstancesResult(
            id=self.id,
            instance_lists=self.instance_lists,
            name=self.name,
            project_id=self.project_id,
            result_output_file=self.result_output_file,
            subnet_id=self.subnet_id,
            vpc_id=self.vpc_id)


def get_instances(id: Optional[str] = None,
                  name: Optional[str] = None,
                  project_id: Optional[int] = None,
                  result_output_file: Optional[str] = None,
                  subnet_id: Optional[str] = None,
                  vpc_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstancesResult:
    """
    Use this data source to query SQL Server instances

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    vpc = tencentcloud.Sqlserver.get_instances(subnet_id="subnet-nf9n81ps",
        vpc_id="vpc-409mvdvv")
    project = tencentcloud.Sqlserver.get_instances(project_id=0)
    id = tencentcloud.Sqlserver.get_instances(id="postgres-h9t4fde1")
    ```


    :param str id: ID of the SQL Server instance to be query.
    :param str name: Name of the SQL Server instance to be query.
    :param int project_id: Project ID of the SQL Server instance to be query.
    :param str result_output_file: Used to save results.
    :param str subnet_id: Subnet ID of the SQL Server instance to be query.
    :param str vpc_id: Vpc ID of the SQL Server instance to be query.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['projectId'] = project_id
    __args__['resultOutputFile'] = result_output_file
    __args__['subnetId'] = subnet_id
    __args__['vpcId'] = vpc_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('tencentcloud:Sqlserver/getInstances:getInstances', __args__, opts=opts, typ=GetInstancesResult).value

    return AwaitableGetInstancesResult(
        id=__ret__.id,
        instance_lists=__ret__.instance_lists,
        name=__ret__.name,
        project_id=__ret__.project_id,
        result_output_file=__ret__.result_output_file,
        subnet_id=__ret__.subnet_id,
        vpc_id=__ret__.vpc_id)


@_utilities.lift_output_func(get_instances)
def get_instances_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                         name: Optional[pulumi.Input[Optional[str]]] = None,
                         project_id: Optional[pulumi.Input[Optional[int]]] = None,
                         result_output_file: Optional[pulumi.Input[Optional[str]]] = None,
                         subnet_id: Optional[pulumi.Input[Optional[str]]] = None,
                         vpc_id: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstancesResult]:
    """
    Use this data source to query SQL Server instances

    ## Example Usage

    ```python
    import pulumi
    import pulumi_tencentcloud as tencentcloud

    vpc = tencentcloud.Sqlserver.get_instances(subnet_id="subnet-nf9n81ps",
        vpc_id="vpc-409mvdvv")
    project = tencentcloud.Sqlserver.get_instances(project_id=0)
    id = tencentcloud.Sqlserver.get_instances(id="postgres-h9t4fde1")
    ```


    :param str id: ID of the SQL Server instance to be query.
    :param str name: Name of the SQL Server instance to be query.
    :param int project_id: Project ID of the SQL Server instance to be query.
    :param str result_output_file: Used to save results.
    :param str subnet_id: Subnet ID of the SQL Server instance to be query.
    :param str vpc_id: Vpc ID of the SQL Server instance to be query.
    """
    ...