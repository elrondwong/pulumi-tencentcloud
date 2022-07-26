// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sqlserver

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Instance struct {
	pulumi.CustomResourceState

	// Automatic renewal sign. 0 for normal renewal, 1 for automatic renewal (Default). Only valid when purchasing a prepaid
	// instance.
	AutoRenew pulumi.IntPtrOutput `pulumi:"autoRenew"`
	// Whether to use the voucher automatically; 1 for yes, 0 for no, the default is 0.
	AutoVoucher pulumi.IntPtrOutput `pulumi:"autoVoucher"`
	// Availability zone.
	AvailabilityZone pulumi.StringOutput `pulumi:"availabilityZone"`
	// Pay type of the SQL Server instance. Available values `PREPAID`, `POSTPAID_BY_HOUR`.
	ChargeType pulumi.StringPtrOutput `pulumi:"chargeType"`
	// Create time of the SQL Server instance.
	CreateTime pulumi.StringOutput `pulumi:"createTime"`
	// Version of the SQL Server database engine. Allowed values are `2008R2`(SQL Server 2008 Enterprise), `2012SP3`(SQL Server
	// 2012 Enterprise), `2016SP1` (SQL Server 2016 Enterprise), `201602`(SQL Server 2016 Standard) and `2017`(SQL Server 2017
	// Enterprise). Default is `2008R2`.
	EngineVersion pulumi.StringPtrOutput `pulumi:"engineVersion"`
	// Instance type. `DUAL` (dual-server high availability), `CLUSTER` (cluster). Default is `DUAL`.
	HaType pulumi.StringPtrOutput `pulumi:"haType"`
	// Start time of the maintenance in one day, format like `HH:mm`.
	MaintenanceStartTime pulumi.StringOutput `pulumi:"maintenanceStartTime"`
	// The timespan of maintenance in one day, unit is hour.
	MaintenanceTimeSpan pulumi.IntOutput `pulumi:"maintenanceTimeSpan"`
	// A list of integer indicates weekly maintenance. For example, [2,7] presents do weekly maintenance on every Tuesday and
	// Sunday.
	MaintenanceWeekSets pulumi.IntArrayOutput `pulumi:"maintenanceWeekSets"`
	// Memory size (in GB). Allowed value must be larger than `memory` that data source `tencentcloud_sqlserver_specinfos`
	// provides.
	Memory pulumi.IntOutput `pulumi:"memory"`
	// Indicate whether to deploy across availability zones.
	MultiZones pulumi.BoolPtrOutput `pulumi:"multiZones"`
	// Name of the SQL Server instance.
	Name pulumi.StringOutput `pulumi:"name"`
	// Purchase instance period in month. The value does not exceed 48.
	Period pulumi.IntPtrOutput `pulumi:"period"`
	// Project ID, default value is 0.
	ProjectId pulumi.IntOutput `pulumi:"projectId"`
	// Readonly flag. `RO` (read-only instance), `MASTER` (primary instance with read-only instances). If it is left empty, it
	// refers to an instance which is not read-only and has no RO group.
	RoFlag pulumi.StringOutput `pulumi:"roFlag"`
	// Security group bound to the instance.
	SecurityGroups pulumi.StringArrayOutput `pulumi:"securityGroups"`
	// Status of the SQL Server instance. 1 for applying, 2 for running, 3 for running with limit, 4 for isolated, 5 for
	// recycling, 6 for recycled, 7 for running with task, 8 for off-line, 9 for expanding, 10 for migrating, 11 for readonly,
	// 12 for rebooting.
	Status pulumi.IntOutput `pulumi:"status"`
	// Disk size (in GB). Allowed value must be a multiple of 10. The storage must be set with the limit of `storage_min` and
	// `storage_max` which data source `tencentcloud_sqlserver_specinfos` provides.
	Storage pulumi.IntOutput `pulumi:"storage"`
	// ID of subnet.
	SubnetId pulumi.StringPtrOutput `pulumi:"subnetId"`
	// The tags of the SQL Server.
	Tags pulumi.MapOutput `pulumi:"tags"`
	// IP for private access.
	Vip pulumi.StringOutput `pulumi:"vip"`
	// An array of voucher IDs, currently only one can be used for a single order.
	VoucherIds pulumi.StringArrayOutput `pulumi:"voucherIds"`
	// ID of VPC.
	VpcId pulumi.StringPtrOutput `pulumi:"vpcId"`
	// Port for private access.
	Vport pulumi.IntOutput `pulumi:"vport"`
}

// NewInstance registers a new resource with the given unique name, arguments, and options.
func NewInstance(ctx *pulumi.Context,
	name string, args *InstanceArgs, opts ...pulumi.ResourceOption) (*Instance, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Memory == nil {
		return nil, errors.New("invalid value for required argument 'Memory'")
	}
	if args.Storage == nil {
		return nil, errors.New("invalid value for required argument 'Storage'")
	}
	var resource Instance
	err := ctx.RegisterResource("tencentcloud:Sqlserver/instance:Instance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstance gets an existing Instance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceState, opts ...pulumi.ResourceOption) (*Instance, error) {
	var resource Instance
	err := ctx.ReadResource("tencentcloud:Sqlserver/instance:Instance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Instance resources.
type instanceState struct {
	// Automatic renewal sign. 0 for normal renewal, 1 for automatic renewal (Default). Only valid when purchasing a prepaid
	// instance.
	AutoRenew *int `pulumi:"autoRenew"`
	// Whether to use the voucher automatically; 1 for yes, 0 for no, the default is 0.
	AutoVoucher *int `pulumi:"autoVoucher"`
	// Availability zone.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// Pay type of the SQL Server instance. Available values `PREPAID`, `POSTPAID_BY_HOUR`.
	ChargeType *string `pulumi:"chargeType"`
	// Create time of the SQL Server instance.
	CreateTime *string `pulumi:"createTime"`
	// Version of the SQL Server database engine. Allowed values are `2008R2`(SQL Server 2008 Enterprise), `2012SP3`(SQL Server
	// 2012 Enterprise), `2016SP1` (SQL Server 2016 Enterprise), `201602`(SQL Server 2016 Standard) and `2017`(SQL Server 2017
	// Enterprise). Default is `2008R2`.
	EngineVersion *string `pulumi:"engineVersion"`
	// Instance type. `DUAL` (dual-server high availability), `CLUSTER` (cluster). Default is `DUAL`.
	HaType *string `pulumi:"haType"`
	// Start time of the maintenance in one day, format like `HH:mm`.
	MaintenanceStartTime *string `pulumi:"maintenanceStartTime"`
	// The timespan of maintenance in one day, unit is hour.
	MaintenanceTimeSpan *int `pulumi:"maintenanceTimeSpan"`
	// A list of integer indicates weekly maintenance. For example, [2,7] presents do weekly maintenance on every Tuesday and
	// Sunday.
	MaintenanceWeekSets []int `pulumi:"maintenanceWeekSets"`
	// Memory size (in GB). Allowed value must be larger than `memory` that data source `tencentcloud_sqlserver_specinfos`
	// provides.
	Memory *int `pulumi:"memory"`
	// Indicate whether to deploy across availability zones.
	MultiZones *bool `pulumi:"multiZones"`
	// Name of the SQL Server instance.
	Name *string `pulumi:"name"`
	// Purchase instance period in month. The value does not exceed 48.
	Period *int `pulumi:"period"`
	// Project ID, default value is 0.
	ProjectId *int `pulumi:"projectId"`
	// Readonly flag. `RO` (read-only instance), `MASTER` (primary instance with read-only instances). If it is left empty, it
	// refers to an instance which is not read-only and has no RO group.
	RoFlag *string `pulumi:"roFlag"`
	// Security group bound to the instance.
	SecurityGroups []string `pulumi:"securityGroups"`
	// Status of the SQL Server instance. 1 for applying, 2 for running, 3 for running with limit, 4 for isolated, 5 for
	// recycling, 6 for recycled, 7 for running with task, 8 for off-line, 9 for expanding, 10 for migrating, 11 for readonly,
	// 12 for rebooting.
	Status *int `pulumi:"status"`
	// Disk size (in GB). Allowed value must be a multiple of 10. The storage must be set with the limit of `storage_min` and
	// `storage_max` which data source `tencentcloud_sqlserver_specinfos` provides.
	Storage *int `pulumi:"storage"`
	// ID of subnet.
	SubnetId *string `pulumi:"subnetId"`
	// The tags of the SQL Server.
	Tags map[string]interface{} `pulumi:"tags"`
	// IP for private access.
	Vip *string `pulumi:"vip"`
	// An array of voucher IDs, currently only one can be used for a single order.
	VoucherIds []string `pulumi:"voucherIds"`
	// ID of VPC.
	VpcId *string `pulumi:"vpcId"`
	// Port for private access.
	Vport *int `pulumi:"vport"`
}

type InstanceState struct {
	// Automatic renewal sign. 0 for normal renewal, 1 for automatic renewal (Default). Only valid when purchasing a prepaid
	// instance.
	AutoRenew pulumi.IntPtrInput
	// Whether to use the voucher automatically; 1 for yes, 0 for no, the default is 0.
	AutoVoucher pulumi.IntPtrInput
	// Availability zone.
	AvailabilityZone pulumi.StringPtrInput
	// Pay type of the SQL Server instance. Available values `PREPAID`, `POSTPAID_BY_HOUR`.
	ChargeType pulumi.StringPtrInput
	// Create time of the SQL Server instance.
	CreateTime pulumi.StringPtrInput
	// Version of the SQL Server database engine. Allowed values are `2008R2`(SQL Server 2008 Enterprise), `2012SP3`(SQL Server
	// 2012 Enterprise), `2016SP1` (SQL Server 2016 Enterprise), `201602`(SQL Server 2016 Standard) and `2017`(SQL Server 2017
	// Enterprise). Default is `2008R2`.
	EngineVersion pulumi.StringPtrInput
	// Instance type. `DUAL` (dual-server high availability), `CLUSTER` (cluster). Default is `DUAL`.
	HaType pulumi.StringPtrInput
	// Start time of the maintenance in one day, format like `HH:mm`.
	MaintenanceStartTime pulumi.StringPtrInput
	// The timespan of maintenance in one day, unit is hour.
	MaintenanceTimeSpan pulumi.IntPtrInput
	// A list of integer indicates weekly maintenance. For example, [2,7] presents do weekly maintenance on every Tuesday and
	// Sunday.
	MaintenanceWeekSets pulumi.IntArrayInput
	// Memory size (in GB). Allowed value must be larger than `memory` that data source `tencentcloud_sqlserver_specinfos`
	// provides.
	Memory pulumi.IntPtrInput
	// Indicate whether to deploy across availability zones.
	MultiZones pulumi.BoolPtrInput
	// Name of the SQL Server instance.
	Name pulumi.StringPtrInput
	// Purchase instance period in month. The value does not exceed 48.
	Period pulumi.IntPtrInput
	// Project ID, default value is 0.
	ProjectId pulumi.IntPtrInput
	// Readonly flag. `RO` (read-only instance), `MASTER` (primary instance with read-only instances). If it is left empty, it
	// refers to an instance which is not read-only and has no RO group.
	RoFlag pulumi.StringPtrInput
	// Security group bound to the instance.
	SecurityGroups pulumi.StringArrayInput
	// Status of the SQL Server instance. 1 for applying, 2 for running, 3 for running with limit, 4 for isolated, 5 for
	// recycling, 6 for recycled, 7 for running with task, 8 for off-line, 9 for expanding, 10 for migrating, 11 for readonly,
	// 12 for rebooting.
	Status pulumi.IntPtrInput
	// Disk size (in GB). Allowed value must be a multiple of 10. The storage must be set with the limit of `storage_min` and
	// `storage_max` which data source `tencentcloud_sqlserver_specinfos` provides.
	Storage pulumi.IntPtrInput
	// ID of subnet.
	SubnetId pulumi.StringPtrInput
	// The tags of the SQL Server.
	Tags pulumi.MapInput
	// IP for private access.
	Vip pulumi.StringPtrInput
	// An array of voucher IDs, currently only one can be used for a single order.
	VoucherIds pulumi.StringArrayInput
	// ID of VPC.
	VpcId pulumi.StringPtrInput
	// Port for private access.
	Vport pulumi.IntPtrInput
}

func (InstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceState)(nil)).Elem()
}

type instanceArgs struct {
	// Automatic renewal sign. 0 for normal renewal, 1 for automatic renewal (Default). Only valid when purchasing a prepaid
	// instance.
	AutoRenew *int `pulumi:"autoRenew"`
	// Whether to use the voucher automatically; 1 for yes, 0 for no, the default is 0.
	AutoVoucher *int `pulumi:"autoVoucher"`
	// Availability zone.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// Pay type of the SQL Server instance. Available values `PREPAID`, `POSTPAID_BY_HOUR`.
	ChargeType *string `pulumi:"chargeType"`
	// Version of the SQL Server database engine. Allowed values are `2008R2`(SQL Server 2008 Enterprise), `2012SP3`(SQL Server
	// 2012 Enterprise), `2016SP1` (SQL Server 2016 Enterprise), `201602`(SQL Server 2016 Standard) and `2017`(SQL Server 2017
	// Enterprise). Default is `2008R2`.
	EngineVersion *string `pulumi:"engineVersion"`
	// Instance type. `DUAL` (dual-server high availability), `CLUSTER` (cluster). Default is `DUAL`.
	HaType *string `pulumi:"haType"`
	// Start time of the maintenance in one day, format like `HH:mm`.
	MaintenanceStartTime *string `pulumi:"maintenanceStartTime"`
	// The timespan of maintenance in one day, unit is hour.
	MaintenanceTimeSpan *int `pulumi:"maintenanceTimeSpan"`
	// A list of integer indicates weekly maintenance. For example, [2,7] presents do weekly maintenance on every Tuesday and
	// Sunday.
	MaintenanceWeekSets []int `pulumi:"maintenanceWeekSets"`
	// Memory size (in GB). Allowed value must be larger than `memory` that data source `tencentcloud_sqlserver_specinfos`
	// provides.
	Memory int `pulumi:"memory"`
	// Indicate whether to deploy across availability zones.
	MultiZones *bool `pulumi:"multiZones"`
	// Name of the SQL Server instance.
	Name *string `pulumi:"name"`
	// Purchase instance period in month. The value does not exceed 48.
	Period *int `pulumi:"period"`
	// Project ID, default value is 0.
	ProjectId *int `pulumi:"projectId"`
	// Security group bound to the instance.
	SecurityGroups []string `pulumi:"securityGroups"`
	// Disk size (in GB). Allowed value must be a multiple of 10. The storage must be set with the limit of `storage_min` and
	// `storage_max` which data source `tencentcloud_sqlserver_specinfos` provides.
	Storage int `pulumi:"storage"`
	// ID of subnet.
	SubnetId *string `pulumi:"subnetId"`
	// The tags of the SQL Server.
	Tags map[string]interface{} `pulumi:"tags"`
	// An array of voucher IDs, currently only one can be used for a single order.
	VoucherIds []string `pulumi:"voucherIds"`
	// ID of VPC.
	VpcId *string `pulumi:"vpcId"`
}

// The set of arguments for constructing a Instance resource.
type InstanceArgs struct {
	// Automatic renewal sign. 0 for normal renewal, 1 for automatic renewal (Default). Only valid when purchasing a prepaid
	// instance.
	AutoRenew pulumi.IntPtrInput
	// Whether to use the voucher automatically; 1 for yes, 0 for no, the default is 0.
	AutoVoucher pulumi.IntPtrInput
	// Availability zone.
	AvailabilityZone pulumi.StringPtrInput
	// Pay type of the SQL Server instance. Available values `PREPAID`, `POSTPAID_BY_HOUR`.
	ChargeType pulumi.StringPtrInput
	// Version of the SQL Server database engine. Allowed values are `2008R2`(SQL Server 2008 Enterprise), `2012SP3`(SQL Server
	// 2012 Enterprise), `2016SP1` (SQL Server 2016 Enterprise), `201602`(SQL Server 2016 Standard) and `2017`(SQL Server 2017
	// Enterprise). Default is `2008R2`.
	EngineVersion pulumi.StringPtrInput
	// Instance type. `DUAL` (dual-server high availability), `CLUSTER` (cluster). Default is `DUAL`.
	HaType pulumi.StringPtrInput
	// Start time of the maintenance in one day, format like `HH:mm`.
	MaintenanceStartTime pulumi.StringPtrInput
	// The timespan of maintenance in one day, unit is hour.
	MaintenanceTimeSpan pulumi.IntPtrInput
	// A list of integer indicates weekly maintenance. For example, [2,7] presents do weekly maintenance on every Tuesday and
	// Sunday.
	MaintenanceWeekSets pulumi.IntArrayInput
	// Memory size (in GB). Allowed value must be larger than `memory` that data source `tencentcloud_sqlserver_specinfos`
	// provides.
	Memory pulumi.IntInput
	// Indicate whether to deploy across availability zones.
	MultiZones pulumi.BoolPtrInput
	// Name of the SQL Server instance.
	Name pulumi.StringPtrInput
	// Purchase instance period in month. The value does not exceed 48.
	Period pulumi.IntPtrInput
	// Project ID, default value is 0.
	ProjectId pulumi.IntPtrInput
	// Security group bound to the instance.
	SecurityGroups pulumi.StringArrayInput
	// Disk size (in GB). Allowed value must be a multiple of 10. The storage must be set with the limit of `storage_min` and
	// `storage_max` which data source `tencentcloud_sqlserver_specinfos` provides.
	Storage pulumi.IntInput
	// ID of subnet.
	SubnetId pulumi.StringPtrInput
	// The tags of the SQL Server.
	Tags pulumi.MapInput
	// An array of voucher IDs, currently only one can be used for a single order.
	VoucherIds pulumi.StringArrayInput
	// ID of VPC.
	VpcId pulumi.StringPtrInput
}

func (InstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceArgs)(nil)).Elem()
}

type InstanceInput interface {
	pulumi.Input

	ToInstanceOutput() InstanceOutput
	ToInstanceOutputWithContext(ctx context.Context) InstanceOutput
}

func (*Instance) ElementType() reflect.Type {
	return reflect.TypeOf((**Instance)(nil)).Elem()
}

func (i *Instance) ToInstanceOutput() InstanceOutput {
	return i.ToInstanceOutputWithContext(context.Background())
}

func (i *Instance) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceOutput)
}

// InstanceArrayInput is an input type that accepts InstanceArray and InstanceArrayOutput values.
// You can construct a concrete instance of `InstanceArrayInput` via:
//
//          InstanceArray{ InstanceArgs{...} }
type InstanceArrayInput interface {
	pulumi.Input

	ToInstanceArrayOutput() InstanceArrayOutput
	ToInstanceArrayOutputWithContext(context.Context) InstanceArrayOutput
}

type InstanceArray []InstanceInput

func (InstanceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Instance)(nil)).Elem()
}

func (i InstanceArray) ToInstanceArrayOutput() InstanceArrayOutput {
	return i.ToInstanceArrayOutputWithContext(context.Background())
}

func (i InstanceArray) ToInstanceArrayOutputWithContext(ctx context.Context) InstanceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceArrayOutput)
}

// InstanceMapInput is an input type that accepts InstanceMap and InstanceMapOutput values.
// You can construct a concrete instance of `InstanceMapInput` via:
//
//          InstanceMap{ "key": InstanceArgs{...} }
type InstanceMapInput interface {
	pulumi.Input

	ToInstanceMapOutput() InstanceMapOutput
	ToInstanceMapOutputWithContext(context.Context) InstanceMapOutput
}

type InstanceMap map[string]InstanceInput

func (InstanceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Instance)(nil)).Elem()
}

func (i InstanceMap) ToInstanceMapOutput() InstanceMapOutput {
	return i.ToInstanceMapOutputWithContext(context.Background())
}

func (i InstanceMap) ToInstanceMapOutputWithContext(ctx context.Context) InstanceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceMapOutput)
}

type InstanceOutput struct{ *pulumi.OutputState }

func (InstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Instance)(nil)).Elem()
}

func (o InstanceOutput) ToInstanceOutput() InstanceOutput {
	return o
}

func (o InstanceOutput) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return o
}

// Automatic renewal sign. 0 for normal renewal, 1 for automatic renewal (Default). Only valid when purchasing a prepaid
// instance.
func (o InstanceOutput) AutoRenew() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.IntPtrOutput { return v.AutoRenew }).(pulumi.IntPtrOutput)
}

// Whether to use the voucher automatically; 1 for yes, 0 for no, the default is 0.
func (o InstanceOutput) AutoVoucher() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.IntPtrOutput { return v.AutoVoucher }).(pulumi.IntPtrOutput)
}

// Availability zone.
func (o InstanceOutput) AvailabilityZone() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.AvailabilityZone }).(pulumi.StringOutput)
}

// Pay type of the SQL Server instance. Available values `PREPAID`, `POSTPAID_BY_HOUR`.
func (o InstanceOutput) ChargeType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringPtrOutput { return v.ChargeType }).(pulumi.StringPtrOutput)
}

// Create time of the SQL Server instance.
func (o InstanceOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.CreateTime }).(pulumi.StringOutput)
}

// Version of the SQL Server database engine. Allowed values are `2008R2`(SQL Server 2008 Enterprise), `2012SP3`(SQL Server
// 2012 Enterprise), `2016SP1` (SQL Server 2016 Enterprise), `201602`(SQL Server 2016 Standard) and `2017`(SQL Server 2017
// Enterprise). Default is `2008R2`.
func (o InstanceOutput) EngineVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringPtrOutput { return v.EngineVersion }).(pulumi.StringPtrOutput)
}

// Instance type. `DUAL` (dual-server high availability), `CLUSTER` (cluster). Default is `DUAL`.
func (o InstanceOutput) HaType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringPtrOutput { return v.HaType }).(pulumi.StringPtrOutput)
}

// Start time of the maintenance in one day, format like `HH:mm`.
func (o InstanceOutput) MaintenanceStartTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.MaintenanceStartTime }).(pulumi.StringOutput)
}

// The timespan of maintenance in one day, unit is hour.
func (o InstanceOutput) MaintenanceTimeSpan() pulumi.IntOutput {
	return o.ApplyT(func(v *Instance) pulumi.IntOutput { return v.MaintenanceTimeSpan }).(pulumi.IntOutput)
}

// A list of integer indicates weekly maintenance. For example, [2,7] presents do weekly maintenance on every Tuesday and
// Sunday.
func (o InstanceOutput) MaintenanceWeekSets() pulumi.IntArrayOutput {
	return o.ApplyT(func(v *Instance) pulumi.IntArrayOutput { return v.MaintenanceWeekSets }).(pulumi.IntArrayOutput)
}

// Memory size (in GB). Allowed value must be larger than `memory` that data source `tencentcloud_sqlserver_specinfos`
// provides.
func (o InstanceOutput) Memory() pulumi.IntOutput {
	return o.ApplyT(func(v *Instance) pulumi.IntOutput { return v.Memory }).(pulumi.IntOutput)
}

// Indicate whether to deploy across availability zones.
func (o InstanceOutput) MultiZones() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.BoolPtrOutput { return v.MultiZones }).(pulumi.BoolPtrOutput)
}

// Name of the SQL Server instance.
func (o InstanceOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Purchase instance period in month. The value does not exceed 48.
func (o InstanceOutput) Period() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.IntPtrOutput { return v.Period }).(pulumi.IntPtrOutput)
}

// Project ID, default value is 0.
func (o InstanceOutput) ProjectId() pulumi.IntOutput {
	return o.ApplyT(func(v *Instance) pulumi.IntOutput { return v.ProjectId }).(pulumi.IntOutput)
}

// Readonly flag. `RO` (read-only instance), `MASTER` (primary instance with read-only instances). If it is left empty, it
// refers to an instance which is not read-only and has no RO group.
func (o InstanceOutput) RoFlag() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.RoFlag }).(pulumi.StringOutput)
}

// Security group bound to the instance.
func (o InstanceOutput) SecurityGroups() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringArrayOutput { return v.SecurityGroups }).(pulumi.StringArrayOutput)
}

// Status of the SQL Server instance. 1 for applying, 2 for running, 3 for running with limit, 4 for isolated, 5 for
// recycling, 6 for recycled, 7 for running with task, 8 for off-line, 9 for expanding, 10 for migrating, 11 for readonly,
// 12 for rebooting.
func (o InstanceOutput) Status() pulumi.IntOutput {
	return o.ApplyT(func(v *Instance) pulumi.IntOutput { return v.Status }).(pulumi.IntOutput)
}

// Disk size (in GB). Allowed value must be a multiple of 10. The storage must be set with the limit of `storage_min` and
// `storage_max` which data source `tencentcloud_sqlserver_specinfos` provides.
func (o InstanceOutput) Storage() pulumi.IntOutput {
	return o.ApplyT(func(v *Instance) pulumi.IntOutput { return v.Storage }).(pulumi.IntOutput)
}

// ID of subnet.
func (o InstanceOutput) SubnetId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringPtrOutput { return v.SubnetId }).(pulumi.StringPtrOutput)
}

// The tags of the SQL Server.
func (o InstanceOutput) Tags() pulumi.MapOutput {
	return o.ApplyT(func(v *Instance) pulumi.MapOutput { return v.Tags }).(pulumi.MapOutput)
}

// IP for private access.
func (o InstanceOutput) Vip() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.Vip }).(pulumi.StringOutput)
}

// An array of voucher IDs, currently only one can be used for a single order.
func (o InstanceOutput) VoucherIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringArrayOutput { return v.VoucherIds }).(pulumi.StringArrayOutput)
}

// ID of VPC.
func (o InstanceOutput) VpcId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringPtrOutput { return v.VpcId }).(pulumi.StringPtrOutput)
}

// Port for private access.
func (o InstanceOutput) Vport() pulumi.IntOutput {
	return o.ApplyT(func(v *Instance) pulumi.IntOutput { return v.Vport }).(pulumi.IntOutput)
}

type InstanceArrayOutput struct{ *pulumi.OutputState }

func (InstanceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Instance)(nil)).Elem()
}

func (o InstanceArrayOutput) ToInstanceArrayOutput() InstanceArrayOutput {
	return o
}

func (o InstanceArrayOutput) ToInstanceArrayOutputWithContext(ctx context.Context) InstanceArrayOutput {
	return o
}

func (o InstanceArrayOutput) Index(i pulumi.IntInput) InstanceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Instance {
		return vs[0].([]*Instance)[vs[1].(int)]
	}).(InstanceOutput)
}

type InstanceMapOutput struct{ *pulumi.OutputState }

func (InstanceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Instance)(nil)).Elem()
}

func (o InstanceMapOutput) ToInstanceMapOutput() InstanceMapOutput {
	return o
}

func (o InstanceMapOutput) ToInstanceMapOutputWithContext(ctx context.Context) InstanceMapOutput {
	return o
}

func (o InstanceMapOutput) MapIndex(k pulumi.StringInput) InstanceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Instance {
		return vs[0].(map[string]*Instance)[vs[1].(string)]
	}).(InstanceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceInput)(nil)).Elem(), &Instance{})
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceArrayInput)(nil)).Elem(), InstanceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceMapInput)(nil)).Elem(), InstanceMap{})
	pulumi.RegisterOutputType(InstanceOutput{})
	pulumi.RegisterOutputType(InstanceArrayOutput{})
	pulumi.RegisterOutputType(InstanceMapOutput{})
}