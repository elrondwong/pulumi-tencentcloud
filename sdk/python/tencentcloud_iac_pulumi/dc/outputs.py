# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetGatewayCcnRoutesInstanceListResult',
    'GetGatewayInstancesInstanceListResult',
    'GetInstancesInstanceListResult',
]

@pulumi.output_type
class GetGatewayCcnRoutesInstanceListResult(dict):
    def __init__(__self__, *,
                 as_paths: Sequence[str],
                 cidr_block: str,
                 dcg_id: str,
                 route_id: str):
        """
        :param Sequence[str] as_paths: As path list of the BGP.
        :param str cidr_block: A network address segment of IDC.
        :param str dcg_id: ID of the DCG to be queried.
        :param str route_id: ID of the DCG route.
        """
        pulumi.set(__self__, "as_paths", as_paths)
        pulumi.set(__self__, "cidr_block", cidr_block)
        pulumi.set(__self__, "dcg_id", dcg_id)
        pulumi.set(__self__, "route_id", route_id)

    @property
    @pulumi.getter(name="asPaths")
    def as_paths(self) -> Sequence[str]:
        """
        As path list of the BGP.
        """
        return pulumi.get(self, "as_paths")

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> str:
        """
        A network address segment of IDC.
        """
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter(name="dcgId")
    def dcg_id(self) -> str:
        """
        ID of the DCG to be queried.
        """
        return pulumi.get(self, "dcg_id")

    @property
    @pulumi.getter(name="routeId")
    def route_id(self) -> str:
        """
        ID of the DCG route.
        """
        return pulumi.get(self, "route_id")


@pulumi.output_type
class GetGatewayInstancesInstanceListResult(dict):
    def __init__(__self__, *,
                 cnn_route_type: str,
                 create_time: str,
                 dcg_id: str,
                 dcg_ip: str,
                 enable_bgp: bool,
                 gateway_type: str,
                 name: str,
                 network_instance_id: str,
                 network_type: str):
        """
        :param str cnn_route_type: Type of CCN route. Valid values: `BGP` and `STATIC`.
        :param str create_time: Creation time of resource.
        :param str dcg_id: ID of the DCG to be queried.
        :param str dcg_ip: IP of the DCG.
        :param bool enable_bgp: Indicates whether the BGP is enabled.
        :param str gateway_type: Type of the gateway. Valid values: `NORMAL` and `NAT`. Default is `NORMAL`.
        :param str name: Name of the DCG to be queried.
        :param str network_instance_id: Type of associated network. Valid values: `VPC` and `CCN`.
        :param str network_type: IP of the DCG.
        """
        pulumi.set(__self__, "cnn_route_type", cnn_route_type)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "dcg_id", dcg_id)
        pulumi.set(__self__, "dcg_ip", dcg_ip)
        pulumi.set(__self__, "enable_bgp", enable_bgp)
        pulumi.set(__self__, "gateway_type", gateway_type)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "network_instance_id", network_instance_id)
        pulumi.set(__self__, "network_type", network_type)

    @property
    @pulumi.getter(name="cnnRouteType")
    def cnn_route_type(self) -> str:
        """
        Type of CCN route. Valid values: `BGP` and `STATIC`.
        """
        return pulumi.get(self, "cnn_route_type")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Creation time of resource.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="dcgId")
    def dcg_id(self) -> str:
        """
        ID of the DCG to be queried.
        """
        return pulumi.get(self, "dcg_id")

    @property
    @pulumi.getter(name="dcgIp")
    def dcg_ip(self) -> str:
        """
        IP of the DCG.
        """
        return pulumi.get(self, "dcg_ip")

    @property
    @pulumi.getter(name="enableBgp")
    def enable_bgp(self) -> bool:
        """
        Indicates whether the BGP is enabled.
        """
        return pulumi.get(self, "enable_bgp")

    @property
    @pulumi.getter(name="gatewayType")
    def gateway_type(self) -> str:
        """
        Type of the gateway. Valid values: `NORMAL` and `NAT`. Default is `NORMAL`.
        """
        return pulumi.get(self, "gateway_type")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the DCG to be queried.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInstanceId")
    def network_instance_id(self) -> str:
        """
        Type of associated network. Valid values: `VPC` and `CCN`.
        """
        return pulumi.get(self, "network_instance_id")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> str:
        """
        IP of the DCG.
        """
        return pulumi.get(self, "network_type")


@pulumi.output_type
class GetInstancesInstanceListResult(dict):
    def __init__(__self__, *,
                 access_point_id: str,
                 bandwidth: int,
                 circuit_code: str,
                 create_time: str,
                 customer_address: str,
                 customer_email: str,
                 customer_name: str,
                 customer_phone: str,
                 dc_id: str,
                 enabled_time: str,
                 expired_time: str,
                 fault_report_contact_person: str,
                 fault_report_contact_phone: str,
                 line_operator: str,
                 location: str,
                 name: str,
                 port_type: str,
                 redundant_dc_id: str,
                 state: str,
                 tencent_address: str):
        """
        :param str access_point_id: Access point ID of tne DC.
        :param int bandwidth: Bandwidth of the DC.
        :param str circuit_code: The circuit code provided by the operator for the DC.
        :param str create_time: Creation time of resource.
        :param str customer_address: Interconnect IP of the DC within client. Note: This field may return null, indicating that no valid values are taken.
        :param str customer_email: Applicant email of the DC, the default is obtained from the account. Note: This field may return null, indicating that no valid values are taken.
        :param str customer_name: Applicant name of the DC, the default is obtained from the account. Note: This field may return null, indicating that no valid values are taken.
        :param str customer_phone: Applicant phone number of the DC, the default is obtained from the account. Note: This field may return null, indicating that no valid values are taken.
        :param str dc_id: ID of the DC to be queried.
        :param str enabled_time: Enable time of resource.
        :param str expired_time: Expire date of resource.
        :param str fault_report_contact_person: Contact of reporting a faulty. Note: This field may return null, indicating that no valid values are taken.
        :param str fault_report_contact_phone: Phone number of reporting a faulty. Note: This field may return null, indicating that no valid values are taken.
        :param str line_operator: Operator of the DC, and available values include `ChinaTelecom`, `ChinaMobile`, `ChinaUnicom`, `In-houseWiring`, `ChinaOther` and `InternationalOperator`.
        :param str location: The DC location where the connection is located.
        :param str name: Name of the DC to be queried.
        :param str port_type: Port type of the DC in client, and available values include `100Base-T`, `1000Base-T`, `1000Base-LX`, `10GBase-T` and `10GBase-LR`. The default value is `1000Base-LX`.
        :param str redundant_dc_id: ID of the redundant DC.
        :param str state: State of the DC, and available values include `REJECTED`, `TOPAY`, `PAID`, `ALLOCATED`, `AVAILABLE`, `DELETING` and `DELETED`.
        :param str tencent_address: Interconnect IP of the DC within Tencent. Note: This field may return null, indicating that no valid values are taken.
        """
        pulumi.set(__self__, "access_point_id", access_point_id)
        pulumi.set(__self__, "bandwidth", bandwidth)
        pulumi.set(__self__, "circuit_code", circuit_code)
        pulumi.set(__self__, "create_time", create_time)
        pulumi.set(__self__, "customer_address", customer_address)
        pulumi.set(__self__, "customer_email", customer_email)
        pulumi.set(__self__, "customer_name", customer_name)
        pulumi.set(__self__, "customer_phone", customer_phone)
        pulumi.set(__self__, "dc_id", dc_id)
        pulumi.set(__self__, "enabled_time", enabled_time)
        pulumi.set(__self__, "expired_time", expired_time)
        pulumi.set(__self__, "fault_report_contact_person", fault_report_contact_person)
        pulumi.set(__self__, "fault_report_contact_phone", fault_report_contact_phone)
        pulumi.set(__self__, "line_operator", line_operator)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "port_type", port_type)
        pulumi.set(__self__, "redundant_dc_id", redundant_dc_id)
        pulumi.set(__self__, "state", state)
        pulumi.set(__self__, "tencent_address", tencent_address)

    @property
    @pulumi.getter(name="accessPointId")
    def access_point_id(self) -> str:
        """
        Access point ID of tne DC.
        """
        return pulumi.get(self, "access_point_id")

    @property
    @pulumi.getter
    def bandwidth(self) -> int:
        """
        Bandwidth of the DC.
        """
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter(name="circuitCode")
    def circuit_code(self) -> str:
        """
        The circuit code provided by the operator for the DC.
        """
        return pulumi.get(self, "circuit_code")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Creation time of resource.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="customerAddress")
    def customer_address(self) -> str:
        """
        Interconnect IP of the DC within client. Note: This field may return null, indicating that no valid values are taken.
        """
        return pulumi.get(self, "customer_address")

    @property
    @pulumi.getter(name="customerEmail")
    def customer_email(self) -> str:
        """
        Applicant email of the DC, the default is obtained from the account. Note: This field may return null, indicating that no valid values are taken.
        """
        return pulumi.get(self, "customer_email")

    @property
    @pulumi.getter(name="customerName")
    def customer_name(self) -> str:
        """
        Applicant name of the DC, the default is obtained from the account. Note: This field may return null, indicating that no valid values are taken.
        """
        return pulumi.get(self, "customer_name")

    @property
    @pulumi.getter(name="customerPhone")
    def customer_phone(self) -> str:
        """
        Applicant phone number of the DC, the default is obtained from the account. Note: This field may return null, indicating that no valid values are taken.
        """
        return pulumi.get(self, "customer_phone")

    @property
    @pulumi.getter(name="dcId")
    def dc_id(self) -> str:
        """
        ID of the DC to be queried.
        """
        return pulumi.get(self, "dc_id")

    @property
    @pulumi.getter(name="enabledTime")
    def enabled_time(self) -> str:
        """
        Enable time of resource.
        """
        return pulumi.get(self, "enabled_time")

    @property
    @pulumi.getter(name="expiredTime")
    def expired_time(self) -> str:
        """
        Expire date of resource.
        """
        return pulumi.get(self, "expired_time")

    @property
    @pulumi.getter(name="faultReportContactPerson")
    def fault_report_contact_person(self) -> str:
        """
        Contact of reporting a faulty. Note: This field may return null, indicating that no valid values are taken.
        """
        return pulumi.get(self, "fault_report_contact_person")

    @property
    @pulumi.getter(name="faultReportContactPhone")
    def fault_report_contact_phone(self) -> str:
        """
        Phone number of reporting a faulty. Note: This field may return null, indicating that no valid values are taken.
        """
        return pulumi.get(self, "fault_report_contact_phone")

    @property
    @pulumi.getter(name="lineOperator")
    def line_operator(self) -> str:
        """
        Operator of the DC, and available values include `ChinaTelecom`, `ChinaMobile`, `ChinaUnicom`, `In-houseWiring`, `ChinaOther` and `InternationalOperator`.
        """
        return pulumi.get(self, "line_operator")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The DC location where the connection is located.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the DC to be queried.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="portType")
    def port_type(self) -> str:
        """
        Port type of the DC in client, and available values include `100Base-T`, `1000Base-T`, `1000Base-LX`, `10GBase-T` and `10GBase-LR`. The default value is `1000Base-LX`.
        """
        return pulumi.get(self, "port_type")

    @property
    @pulumi.getter(name="redundantDcId")
    def redundant_dc_id(self) -> str:
        """
        ID of the redundant DC.
        """
        return pulumi.get(self, "redundant_dc_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the DC, and available values include `REJECTED`, `TOPAY`, `PAID`, `ALLOCATED`, `AVAILABLE`, `DELETING` and `DELETED`.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="tencentAddress")
    def tencent_address(self) -> str:
        """
        Interconnect IP of the DC within Tencent. Note: This field may return null, indicating that no valid values are taken.
        """
        return pulumi.get(self, "tencent_address")


