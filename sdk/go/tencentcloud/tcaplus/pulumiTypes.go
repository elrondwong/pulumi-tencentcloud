// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package tcaplus

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type IdlTableInfo struct {
	// Error messages for creating IDL file.
	Error *string `pulumi:"error"`
	// Index key set of the TcaplusDB table.
	IndexKeySet *string `pulumi:"indexKeySet"`
	// Primary key fields of the TcaplusDB table.
	KeyFields *string `pulumi:"keyFields"`
	// Total size of primary key field of the TcaplusDB table.
	SumKeyFieldSize *int `pulumi:"sumKeyFieldSize"`
	// Total size of non-primary key fields of the TcaplusDB table.
	SumValueFieldSize *int `pulumi:"sumValueFieldSize"`
	// Name of the TcaplusDB table.
	TableName *string `pulumi:"tableName"`
	// Non-primary key fields of the TcaplusDB table.
	ValueFields *string `pulumi:"valueFields"`
}

// IdlTableInfoInput is an input type that accepts IdlTableInfoArgs and IdlTableInfoOutput values.
// You can construct a concrete instance of `IdlTableInfoInput` via:
//
//	IdlTableInfoArgs{...}
type IdlTableInfoInput interface {
	pulumi.Input

	ToIdlTableInfoOutput() IdlTableInfoOutput
	ToIdlTableInfoOutputWithContext(context.Context) IdlTableInfoOutput
}

type IdlTableInfoArgs struct {
	// Error messages for creating IDL file.
	Error pulumi.StringPtrInput `pulumi:"error"`
	// Index key set of the TcaplusDB table.
	IndexKeySet pulumi.StringPtrInput `pulumi:"indexKeySet"`
	// Primary key fields of the TcaplusDB table.
	KeyFields pulumi.StringPtrInput `pulumi:"keyFields"`
	// Total size of primary key field of the TcaplusDB table.
	SumKeyFieldSize pulumi.IntPtrInput `pulumi:"sumKeyFieldSize"`
	// Total size of non-primary key fields of the TcaplusDB table.
	SumValueFieldSize pulumi.IntPtrInput `pulumi:"sumValueFieldSize"`
	// Name of the TcaplusDB table.
	TableName pulumi.StringPtrInput `pulumi:"tableName"`
	// Non-primary key fields of the TcaplusDB table.
	ValueFields pulumi.StringPtrInput `pulumi:"valueFields"`
}

func (IdlTableInfoArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*IdlTableInfo)(nil)).Elem()
}

func (i IdlTableInfoArgs) ToIdlTableInfoOutput() IdlTableInfoOutput {
	return i.ToIdlTableInfoOutputWithContext(context.Background())
}

func (i IdlTableInfoArgs) ToIdlTableInfoOutputWithContext(ctx context.Context) IdlTableInfoOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IdlTableInfoOutput)
}

// IdlTableInfoArrayInput is an input type that accepts IdlTableInfoArray and IdlTableInfoArrayOutput values.
// You can construct a concrete instance of `IdlTableInfoArrayInput` via:
//
//	IdlTableInfoArray{ IdlTableInfoArgs{...} }
type IdlTableInfoArrayInput interface {
	pulumi.Input

	ToIdlTableInfoArrayOutput() IdlTableInfoArrayOutput
	ToIdlTableInfoArrayOutputWithContext(context.Context) IdlTableInfoArrayOutput
}

type IdlTableInfoArray []IdlTableInfoInput

func (IdlTableInfoArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]IdlTableInfo)(nil)).Elem()
}

func (i IdlTableInfoArray) ToIdlTableInfoArrayOutput() IdlTableInfoArrayOutput {
	return i.ToIdlTableInfoArrayOutputWithContext(context.Background())
}

func (i IdlTableInfoArray) ToIdlTableInfoArrayOutputWithContext(ctx context.Context) IdlTableInfoArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IdlTableInfoArrayOutput)
}

type IdlTableInfoOutput struct{ *pulumi.OutputState }

func (IdlTableInfoOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*IdlTableInfo)(nil)).Elem()
}

func (o IdlTableInfoOutput) ToIdlTableInfoOutput() IdlTableInfoOutput {
	return o
}

func (o IdlTableInfoOutput) ToIdlTableInfoOutputWithContext(ctx context.Context) IdlTableInfoOutput {
	return o
}

// Error messages for creating IDL file.
func (o IdlTableInfoOutput) Error() pulumi.StringPtrOutput {
	return o.ApplyT(func(v IdlTableInfo) *string { return v.Error }).(pulumi.StringPtrOutput)
}

// Index key set of the TcaplusDB table.
func (o IdlTableInfoOutput) IndexKeySet() pulumi.StringPtrOutput {
	return o.ApplyT(func(v IdlTableInfo) *string { return v.IndexKeySet }).(pulumi.StringPtrOutput)
}

// Primary key fields of the TcaplusDB table.
func (o IdlTableInfoOutput) KeyFields() pulumi.StringPtrOutput {
	return o.ApplyT(func(v IdlTableInfo) *string { return v.KeyFields }).(pulumi.StringPtrOutput)
}

// Total size of primary key field of the TcaplusDB table.
func (o IdlTableInfoOutput) SumKeyFieldSize() pulumi.IntPtrOutput {
	return o.ApplyT(func(v IdlTableInfo) *int { return v.SumKeyFieldSize }).(pulumi.IntPtrOutput)
}

// Total size of non-primary key fields of the TcaplusDB table.
func (o IdlTableInfoOutput) SumValueFieldSize() pulumi.IntPtrOutput {
	return o.ApplyT(func(v IdlTableInfo) *int { return v.SumValueFieldSize }).(pulumi.IntPtrOutput)
}

// Name of the TcaplusDB table.
func (o IdlTableInfoOutput) TableName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v IdlTableInfo) *string { return v.TableName }).(pulumi.StringPtrOutput)
}

// Non-primary key fields of the TcaplusDB table.
func (o IdlTableInfoOutput) ValueFields() pulumi.StringPtrOutput {
	return o.ApplyT(func(v IdlTableInfo) *string { return v.ValueFields }).(pulumi.StringPtrOutput)
}

type IdlTableInfoArrayOutput struct{ *pulumi.OutputState }

func (IdlTableInfoArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]IdlTableInfo)(nil)).Elem()
}

func (o IdlTableInfoArrayOutput) ToIdlTableInfoArrayOutput() IdlTableInfoArrayOutput {
	return o
}

func (o IdlTableInfoArrayOutput) ToIdlTableInfoArrayOutputWithContext(ctx context.Context) IdlTableInfoArrayOutput {
	return o
}

func (o IdlTableInfoArrayOutput) Index(i pulumi.IntInput) IdlTableInfoOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) IdlTableInfo {
		return vs[0].([]IdlTableInfo)[vs[1].(int)]
	}).(IdlTableInfoOutput)
}

type GetClustersList struct {
	// Access id of the TcaplusDB cluster.For TcaplusDB SDK connect.
	ApiAccessId string `pulumi:"apiAccessId"`
	// Access ip of the TcaplusDB cluster.For TcaplusDB SDK connect.
	ApiAccessIp string `pulumi:"apiAccessIp"`
	// Access port of the TcaplusDB cluster.For TcaplusDB SDK connect.
	ApiAccessPort int `pulumi:"apiAccessPort"`
	// ID of the TcaplusDB cluster to be query.
	ClusterId string `pulumi:"clusterId"`
	// Name of the TcaplusDB cluster to be query.
	ClusterName string `pulumi:"clusterName"`
	// Create time of the TcaplusDB cluster.
	CreateTime string `pulumi:"createTime"`
	// IDL type of the TcaplusDB cluster.
	IdlType string `pulumi:"idlType"`
	// Network type of the TcaplusDB cluster.
	NetworkType string `pulumi:"networkType"`
	// Expiration time of the old password. If `passwordStatus` is `unmodifiable`, it means the old password has not yet expired.
	OldPasswordExpireTime string `pulumi:"oldPasswordExpireTime"`
	// Access password of the TcaplusDB cluster.
	Password string `pulumi:"password"`
	// Password status of the TcaplusDB cluster. Valid values: `unmodifiable`, `modifiable`. `unmodifiable` means the password can not be changed in this moment; `modifiable` means the password can be changed in this moment.
	PasswordStatus string `pulumi:"passwordStatus"`
	// Subnet ID of the TcaplusDB cluster.
	SubnetId string `pulumi:"subnetId"`
	// VPC ID of the TcaplusDB cluster.
	VpcId string `pulumi:"vpcId"`
}

// GetClustersListInput is an input type that accepts GetClustersListArgs and GetClustersListOutput values.
// You can construct a concrete instance of `GetClustersListInput` via:
//
//	GetClustersListArgs{...}
type GetClustersListInput interface {
	pulumi.Input

	ToGetClustersListOutput() GetClustersListOutput
	ToGetClustersListOutputWithContext(context.Context) GetClustersListOutput
}

type GetClustersListArgs struct {
	// Access id of the TcaplusDB cluster.For TcaplusDB SDK connect.
	ApiAccessId pulumi.StringInput `pulumi:"apiAccessId"`
	// Access ip of the TcaplusDB cluster.For TcaplusDB SDK connect.
	ApiAccessIp pulumi.StringInput `pulumi:"apiAccessIp"`
	// Access port of the TcaplusDB cluster.For TcaplusDB SDK connect.
	ApiAccessPort pulumi.IntInput `pulumi:"apiAccessPort"`
	// ID of the TcaplusDB cluster to be query.
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	// Name of the TcaplusDB cluster to be query.
	ClusterName pulumi.StringInput `pulumi:"clusterName"`
	// Create time of the TcaplusDB cluster.
	CreateTime pulumi.StringInput `pulumi:"createTime"`
	// IDL type of the TcaplusDB cluster.
	IdlType pulumi.StringInput `pulumi:"idlType"`
	// Network type of the TcaplusDB cluster.
	NetworkType pulumi.StringInput `pulumi:"networkType"`
	// Expiration time of the old password. If `passwordStatus` is `unmodifiable`, it means the old password has not yet expired.
	OldPasswordExpireTime pulumi.StringInput `pulumi:"oldPasswordExpireTime"`
	// Access password of the TcaplusDB cluster.
	Password pulumi.StringInput `pulumi:"password"`
	// Password status of the TcaplusDB cluster. Valid values: `unmodifiable`, `modifiable`. `unmodifiable` means the password can not be changed in this moment; `modifiable` means the password can be changed in this moment.
	PasswordStatus pulumi.StringInput `pulumi:"passwordStatus"`
	// Subnet ID of the TcaplusDB cluster.
	SubnetId pulumi.StringInput `pulumi:"subnetId"`
	// VPC ID of the TcaplusDB cluster.
	VpcId pulumi.StringInput `pulumi:"vpcId"`
}

func (GetClustersListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetClustersList)(nil)).Elem()
}

func (i GetClustersListArgs) ToGetClustersListOutput() GetClustersListOutput {
	return i.ToGetClustersListOutputWithContext(context.Background())
}

func (i GetClustersListArgs) ToGetClustersListOutputWithContext(ctx context.Context) GetClustersListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetClustersListOutput)
}

// GetClustersListArrayInput is an input type that accepts GetClustersListArray and GetClustersListArrayOutput values.
// You can construct a concrete instance of `GetClustersListArrayInput` via:
//
//	GetClustersListArray{ GetClustersListArgs{...} }
type GetClustersListArrayInput interface {
	pulumi.Input

	ToGetClustersListArrayOutput() GetClustersListArrayOutput
	ToGetClustersListArrayOutputWithContext(context.Context) GetClustersListArrayOutput
}

type GetClustersListArray []GetClustersListInput

func (GetClustersListArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetClustersList)(nil)).Elem()
}

func (i GetClustersListArray) ToGetClustersListArrayOutput() GetClustersListArrayOutput {
	return i.ToGetClustersListArrayOutputWithContext(context.Background())
}

func (i GetClustersListArray) ToGetClustersListArrayOutputWithContext(ctx context.Context) GetClustersListArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetClustersListArrayOutput)
}

type GetClustersListOutput struct{ *pulumi.OutputState }

func (GetClustersListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetClustersList)(nil)).Elem()
}

func (o GetClustersListOutput) ToGetClustersListOutput() GetClustersListOutput {
	return o
}

func (o GetClustersListOutput) ToGetClustersListOutputWithContext(ctx context.Context) GetClustersListOutput {
	return o
}

// Access id of the TcaplusDB cluster.For TcaplusDB SDK connect.
func (o GetClustersListOutput) ApiAccessId() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersList) string { return v.ApiAccessId }).(pulumi.StringOutput)
}

// Access ip of the TcaplusDB cluster.For TcaplusDB SDK connect.
func (o GetClustersListOutput) ApiAccessIp() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersList) string { return v.ApiAccessIp }).(pulumi.StringOutput)
}

// Access port of the TcaplusDB cluster.For TcaplusDB SDK connect.
func (o GetClustersListOutput) ApiAccessPort() pulumi.IntOutput {
	return o.ApplyT(func(v GetClustersList) int { return v.ApiAccessPort }).(pulumi.IntOutput)
}

// ID of the TcaplusDB cluster to be query.
func (o GetClustersListOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersList) string { return v.ClusterId }).(pulumi.StringOutput)
}

// Name of the TcaplusDB cluster to be query.
func (o GetClustersListOutput) ClusterName() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersList) string { return v.ClusterName }).(pulumi.StringOutput)
}

// Create time of the TcaplusDB cluster.
func (o GetClustersListOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersList) string { return v.CreateTime }).(pulumi.StringOutput)
}

// IDL type of the TcaplusDB cluster.
func (o GetClustersListOutput) IdlType() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersList) string { return v.IdlType }).(pulumi.StringOutput)
}

// Network type of the TcaplusDB cluster.
func (o GetClustersListOutput) NetworkType() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersList) string { return v.NetworkType }).(pulumi.StringOutput)
}

// Expiration time of the old password. If `passwordStatus` is `unmodifiable`, it means the old password has not yet expired.
func (o GetClustersListOutput) OldPasswordExpireTime() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersList) string { return v.OldPasswordExpireTime }).(pulumi.StringOutput)
}

// Access password of the TcaplusDB cluster.
func (o GetClustersListOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersList) string { return v.Password }).(pulumi.StringOutput)
}

// Password status of the TcaplusDB cluster. Valid values: `unmodifiable`, `modifiable`. `unmodifiable` means the password can not be changed in this moment; `modifiable` means the password can be changed in this moment.
func (o GetClustersListOutput) PasswordStatus() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersList) string { return v.PasswordStatus }).(pulumi.StringOutput)
}

// Subnet ID of the TcaplusDB cluster.
func (o GetClustersListOutput) SubnetId() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersList) string { return v.SubnetId }).(pulumi.StringOutput)
}

// VPC ID of the TcaplusDB cluster.
func (o GetClustersListOutput) VpcId() pulumi.StringOutput {
	return o.ApplyT(func(v GetClustersList) string { return v.VpcId }).(pulumi.StringOutput)
}

type GetClustersListArrayOutput struct{ *pulumi.OutputState }

func (GetClustersListArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetClustersList)(nil)).Elem()
}

func (o GetClustersListArrayOutput) ToGetClustersListArrayOutput() GetClustersListArrayOutput {
	return o
}

func (o GetClustersListArrayOutput) ToGetClustersListArrayOutputWithContext(ctx context.Context) GetClustersListArrayOutput {
	return o
}

func (o GetClustersListArrayOutput) Index(i pulumi.IntInput) GetClustersListOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetClustersList {
		return vs[0].([]GetClustersList)[vs[1].(int)]
	}).(GetClustersListOutput)
}

type GetIdlsList struct {
	// ID of the IDL.
	IdlId string `pulumi:"idlId"`
}

// GetIdlsListInput is an input type that accepts GetIdlsListArgs and GetIdlsListOutput values.
// You can construct a concrete instance of `GetIdlsListInput` via:
//
//	GetIdlsListArgs{...}
type GetIdlsListInput interface {
	pulumi.Input

	ToGetIdlsListOutput() GetIdlsListOutput
	ToGetIdlsListOutputWithContext(context.Context) GetIdlsListOutput
}

type GetIdlsListArgs struct {
	// ID of the IDL.
	IdlId pulumi.StringInput `pulumi:"idlId"`
}

func (GetIdlsListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetIdlsList)(nil)).Elem()
}

func (i GetIdlsListArgs) ToGetIdlsListOutput() GetIdlsListOutput {
	return i.ToGetIdlsListOutputWithContext(context.Background())
}

func (i GetIdlsListArgs) ToGetIdlsListOutputWithContext(ctx context.Context) GetIdlsListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetIdlsListOutput)
}

// GetIdlsListArrayInput is an input type that accepts GetIdlsListArray and GetIdlsListArrayOutput values.
// You can construct a concrete instance of `GetIdlsListArrayInput` via:
//
//	GetIdlsListArray{ GetIdlsListArgs{...} }
type GetIdlsListArrayInput interface {
	pulumi.Input

	ToGetIdlsListArrayOutput() GetIdlsListArrayOutput
	ToGetIdlsListArrayOutputWithContext(context.Context) GetIdlsListArrayOutput
}

type GetIdlsListArray []GetIdlsListInput

func (GetIdlsListArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetIdlsList)(nil)).Elem()
}

func (i GetIdlsListArray) ToGetIdlsListArrayOutput() GetIdlsListArrayOutput {
	return i.ToGetIdlsListArrayOutputWithContext(context.Background())
}

func (i GetIdlsListArray) ToGetIdlsListArrayOutputWithContext(ctx context.Context) GetIdlsListArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetIdlsListArrayOutput)
}

type GetIdlsListOutput struct{ *pulumi.OutputState }

func (GetIdlsListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetIdlsList)(nil)).Elem()
}

func (o GetIdlsListOutput) ToGetIdlsListOutput() GetIdlsListOutput {
	return o
}

func (o GetIdlsListOutput) ToGetIdlsListOutputWithContext(ctx context.Context) GetIdlsListOutput {
	return o
}

// ID of the IDL.
func (o GetIdlsListOutput) IdlId() pulumi.StringOutput {
	return o.ApplyT(func(v GetIdlsList) string { return v.IdlId }).(pulumi.StringOutput)
}

type GetIdlsListArrayOutput struct{ *pulumi.OutputState }

func (GetIdlsListArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetIdlsList)(nil)).Elem()
}

func (o GetIdlsListArrayOutput) ToGetIdlsListArrayOutput() GetIdlsListArrayOutput {
	return o
}

func (o GetIdlsListArrayOutput) ToGetIdlsListArrayOutputWithContext(ctx context.Context) GetIdlsListArrayOutput {
	return o
}

func (o GetIdlsListArrayOutput) Index(i pulumi.IntInput) GetIdlsListOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetIdlsList {
		return vs[0].([]GetIdlsList)[vs[1].(int)]
	}).(GetIdlsListOutput)
}

type GetTablegroupsList struct {
	// Create time of the table group..
	CreateTime string `pulumi:"createTime"`
	// Number of tables.
	TableCount int `pulumi:"tableCount"`
	// Id of the table group to be query.
	TablegroupId string `pulumi:"tablegroupId"`
	// Name of the table group to be query.
	TablegroupName string `pulumi:"tablegroupName"`
	// Total storage size (MB).
	TotalSize int `pulumi:"totalSize"`
}

// GetTablegroupsListInput is an input type that accepts GetTablegroupsListArgs and GetTablegroupsListOutput values.
// You can construct a concrete instance of `GetTablegroupsListInput` via:
//
//	GetTablegroupsListArgs{...}
type GetTablegroupsListInput interface {
	pulumi.Input

	ToGetTablegroupsListOutput() GetTablegroupsListOutput
	ToGetTablegroupsListOutputWithContext(context.Context) GetTablegroupsListOutput
}

type GetTablegroupsListArgs struct {
	// Create time of the table group..
	CreateTime pulumi.StringInput `pulumi:"createTime"`
	// Number of tables.
	TableCount pulumi.IntInput `pulumi:"tableCount"`
	// Id of the table group to be query.
	TablegroupId pulumi.StringInput `pulumi:"tablegroupId"`
	// Name of the table group to be query.
	TablegroupName pulumi.StringInput `pulumi:"tablegroupName"`
	// Total storage size (MB).
	TotalSize pulumi.IntInput `pulumi:"totalSize"`
}

func (GetTablegroupsListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTablegroupsList)(nil)).Elem()
}

func (i GetTablegroupsListArgs) ToGetTablegroupsListOutput() GetTablegroupsListOutput {
	return i.ToGetTablegroupsListOutputWithContext(context.Background())
}

func (i GetTablegroupsListArgs) ToGetTablegroupsListOutputWithContext(ctx context.Context) GetTablegroupsListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetTablegroupsListOutput)
}

// GetTablegroupsListArrayInput is an input type that accepts GetTablegroupsListArray and GetTablegroupsListArrayOutput values.
// You can construct a concrete instance of `GetTablegroupsListArrayInput` via:
//
//	GetTablegroupsListArray{ GetTablegroupsListArgs{...} }
type GetTablegroupsListArrayInput interface {
	pulumi.Input

	ToGetTablegroupsListArrayOutput() GetTablegroupsListArrayOutput
	ToGetTablegroupsListArrayOutputWithContext(context.Context) GetTablegroupsListArrayOutput
}

type GetTablegroupsListArray []GetTablegroupsListInput

func (GetTablegroupsListArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetTablegroupsList)(nil)).Elem()
}

func (i GetTablegroupsListArray) ToGetTablegroupsListArrayOutput() GetTablegroupsListArrayOutput {
	return i.ToGetTablegroupsListArrayOutputWithContext(context.Background())
}

func (i GetTablegroupsListArray) ToGetTablegroupsListArrayOutputWithContext(ctx context.Context) GetTablegroupsListArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetTablegroupsListArrayOutput)
}

type GetTablegroupsListOutput struct{ *pulumi.OutputState }

func (GetTablegroupsListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTablegroupsList)(nil)).Elem()
}

func (o GetTablegroupsListOutput) ToGetTablegroupsListOutput() GetTablegroupsListOutput {
	return o
}

func (o GetTablegroupsListOutput) ToGetTablegroupsListOutputWithContext(ctx context.Context) GetTablegroupsListOutput {
	return o
}

// Create time of the table group..
func (o GetTablegroupsListOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablegroupsList) string { return v.CreateTime }).(pulumi.StringOutput)
}

// Number of tables.
func (o GetTablegroupsListOutput) TableCount() pulumi.IntOutput {
	return o.ApplyT(func(v GetTablegroupsList) int { return v.TableCount }).(pulumi.IntOutput)
}

// Id of the table group to be query.
func (o GetTablegroupsListOutput) TablegroupId() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablegroupsList) string { return v.TablegroupId }).(pulumi.StringOutput)
}

// Name of the table group to be query.
func (o GetTablegroupsListOutput) TablegroupName() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablegroupsList) string { return v.TablegroupName }).(pulumi.StringOutput)
}

// Total storage size (MB).
func (o GetTablegroupsListOutput) TotalSize() pulumi.IntOutput {
	return o.ApplyT(func(v GetTablegroupsList) int { return v.TotalSize }).(pulumi.IntOutput)
}

type GetTablegroupsListArrayOutput struct{ *pulumi.OutputState }

func (GetTablegroupsListArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetTablegroupsList)(nil)).Elem()
}

func (o GetTablegroupsListArrayOutput) ToGetTablegroupsListArrayOutput() GetTablegroupsListArrayOutput {
	return o
}

func (o GetTablegroupsListArrayOutput) ToGetTablegroupsListArrayOutputWithContext(ctx context.Context) GetTablegroupsListArrayOutput {
	return o
}

func (o GetTablegroupsListArrayOutput) Index(i pulumi.IntInput) GetTablegroupsListOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetTablegroupsList {
		return vs[0].([]GetTablegroupsList)[vs[1].(int)]
	}).(GetTablegroupsListOutput)
}

type GetTablesList struct {
	// Create time of the TcaplusDB table.
	CreateTime string `pulumi:"createTime"`
	// Description of the TcaplusDB table.
	Description string `pulumi:"description"`
	// Error message for creating TcaplusDB table.
	Error string `pulumi:"error"`
	// IDL file id of the TcaplusDB table.
	IdlId string `pulumi:"idlId"`
	// Reserved read capacity units of the TcaplusDB table.
	ReservedReadCu int `pulumi:"reservedReadCu"`
	// Reserved storage capacity of the TcaplusDB table (unit:GB).
	ReservedVolume int `pulumi:"reservedVolume"`
	// Reserved write capacity units of the TcaplusDB table.
	ReservedWriteCu int `pulumi:"reservedWriteCu"`
	// Status of the TcaplusDB table.
	Status string `pulumi:"status"`
	// Table ID to be query.
	TableId string `pulumi:"tableId"`
	// IDL type of  the TcaplusDB table.
	TableIdlType string `pulumi:"tableIdlType"`
	// Table name to be query.
	TableName string `pulumi:"tableName"`
	// Size of the TcaplusDB table.
	TableSize int `pulumi:"tableSize"`
	// Type of the TcaplusDB table.
	TableType string `pulumi:"tableType"`
	// ID of the table group to be query.
	TablegroupId string `pulumi:"tablegroupId"`
}

// GetTablesListInput is an input type that accepts GetTablesListArgs and GetTablesListOutput values.
// You can construct a concrete instance of `GetTablesListInput` via:
//
//	GetTablesListArgs{...}
type GetTablesListInput interface {
	pulumi.Input

	ToGetTablesListOutput() GetTablesListOutput
	ToGetTablesListOutputWithContext(context.Context) GetTablesListOutput
}

type GetTablesListArgs struct {
	// Create time of the TcaplusDB table.
	CreateTime pulumi.StringInput `pulumi:"createTime"`
	// Description of the TcaplusDB table.
	Description pulumi.StringInput `pulumi:"description"`
	// Error message for creating TcaplusDB table.
	Error pulumi.StringInput `pulumi:"error"`
	// IDL file id of the TcaplusDB table.
	IdlId pulumi.StringInput `pulumi:"idlId"`
	// Reserved read capacity units of the TcaplusDB table.
	ReservedReadCu pulumi.IntInput `pulumi:"reservedReadCu"`
	// Reserved storage capacity of the TcaplusDB table (unit:GB).
	ReservedVolume pulumi.IntInput `pulumi:"reservedVolume"`
	// Reserved write capacity units of the TcaplusDB table.
	ReservedWriteCu pulumi.IntInput `pulumi:"reservedWriteCu"`
	// Status of the TcaplusDB table.
	Status pulumi.StringInput `pulumi:"status"`
	// Table ID to be query.
	TableId pulumi.StringInput `pulumi:"tableId"`
	// IDL type of  the TcaplusDB table.
	TableIdlType pulumi.StringInput `pulumi:"tableIdlType"`
	// Table name to be query.
	TableName pulumi.StringInput `pulumi:"tableName"`
	// Size of the TcaplusDB table.
	TableSize pulumi.IntInput `pulumi:"tableSize"`
	// Type of the TcaplusDB table.
	TableType pulumi.StringInput `pulumi:"tableType"`
	// ID of the table group to be query.
	TablegroupId pulumi.StringInput `pulumi:"tablegroupId"`
}

func (GetTablesListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTablesList)(nil)).Elem()
}

func (i GetTablesListArgs) ToGetTablesListOutput() GetTablesListOutput {
	return i.ToGetTablesListOutputWithContext(context.Background())
}

func (i GetTablesListArgs) ToGetTablesListOutputWithContext(ctx context.Context) GetTablesListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetTablesListOutput)
}

// GetTablesListArrayInput is an input type that accepts GetTablesListArray and GetTablesListArrayOutput values.
// You can construct a concrete instance of `GetTablesListArrayInput` via:
//
//	GetTablesListArray{ GetTablesListArgs{...} }
type GetTablesListArrayInput interface {
	pulumi.Input

	ToGetTablesListArrayOutput() GetTablesListArrayOutput
	ToGetTablesListArrayOutputWithContext(context.Context) GetTablesListArrayOutput
}

type GetTablesListArray []GetTablesListInput

func (GetTablesListArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetTablesList)(nil)).Elem()
}

func (i GetTablesListArray) ToGetTablesListArrayOutput() GetTablesListArrayOutput {
	return i.ToGetTablesListArrayOutputWithContext(context.Background())
}

func (i GetTablesListArray) ToGetTablesListArrayOutputWithContext(ctx context.Context) GetTablesListArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetTablesListArrayOutput)
}

type GetTablesListOutput struct{ *pulumi.OutputState }

func (GetTablesListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTablesList)(nil)).Elem()
}

func (o GetTablesListOutput) ToGetTablesListOutput() GetTablesListOutput {
	return o
}

func (o GetTablesListOutput) ToGetTablesListOutputWithContext(ctx context.Context) GetTablesListOutput {
	return o
}

// Create time of the TcaplusDB table.
func (o GetTablesListOutput) CreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesList) string { return v.CreateTime }).(pulumi.StringOutput)
}

// Description of the TcaplusDB table.
func (o GetTablesListOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesList) string { return v.Description }).(pulumi.StringOutput)
}

// Error message for creating TcaplusDB table.
func (o GetTablesListOutput) Error() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesList) string { return v.Error }).(pulumi.StringOutput)
}

// IDL file id of the TcaplusDB table.
func (o GetTablesListOutput) IdlId() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesList) string { return v.IdlId }).(pulumi.StringOutput)
}

// Reserved read capacity units of the TcaplusDB table.
func (o GetTablesListOutput) ReservedReadCu() pulumi.IntOutput {
	return o.ApplyT(func(v GetTablesList) int { return v.ReservedReadCu }).(pulumi.IntOutput)
}

// Reserved storage capacity of the TcaplusDB table (unit:GB).
func (o GetTablesListOutput) ReservedVolume() pulumi.IntOutput {
	return o.ApplyT(func(v GetTablesList) int { return v.ReservedVolume }).(pulumi.IntOutput)
}

// Reserved write capacity units of the TcaplusDB table.
func (o GetTablesListOutput) ReservedWriteCu() pulumi.IntOutput {
	return o.ApplyT(func(v GetTablesList) int { return v.ReservedWriteCu }).(pulumi.IntOutput)
}

// Status of the TcaplusDB table.
func (o GetTablesListOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesList) string { return v.Status }).(pulumi.StringOutput)
}

// Table ID to be query.
func (o GetTablesListOutput) TableId() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesList) string { return v.TableId }).(pulumi.StringOutput)
}

// IDL type of  the TcaplusDB table.
func (o GetTablesListOutput) TableIdlType() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesList) string { return v.TableIdlType }).(pulumi.StringOutput)
}

// Table name to be query.
func (o GetTablesListOutput) TableName() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesList) string { return v.TableName }).(pulumi.StringOutput)
}

// Size of the TcaplusDB table.
func (o GetTablesListOutput) TableSize() pulumi.IntOutput {
	return o.ApplyT(func(v GetTablesList) int { return v.TableSize }).(pulumi.IntOutput)
}

// Type of the TcaplusDB table.
func (o GetTablesListOutput) TableType() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesList) string { return v.TableType }).(pulumi.StringOutput)
}

// ID of the table group to be query.
func (o GetTablesListOutput) TablegroupId() pulumi.StringOutput {
	return o.ApplyT(func(v GetTablesList) string { return v.TablegroupId }).(pulumi.StringOutput)
}

type GetTablesListArrayOutput struct{ *pulumi.OutputState }

func (GetTablesListArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetTablesList)(nil)).Elem()
}

func (o GetTablesListArrayOutput) ToGetTablesListArrayOutput() GetTablesListArrayOutput {
	return o
}

func (o GetTablesListArrayOutput) ToGetTablesListArrayOutputWithContext(ctx context.Context) GetTablesListArrayOutput {
	return o
}

func (o GetTablesListArrayOutput) Index(i pulumi.IntInput) GetTablesListOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetTablesList {
		return vs[0].([]GetTablesList)[vs[1].(int)]
	}).(GetTablesListOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IdlTableInfoInput)(nil)).Elem(), IdlTableInfoArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*IdlTableInfoArrayInput)(nil)).Elem(), IdlTableInfoArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetClustersListInput)(nil)).Elem(), GetClustersListArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetClustersListArrayInput)(nil)).Elem(), GetClustersListArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetIdlsListInput)(nil)).Elem(), GetIdlsListArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetIdlsListArrayInput)(nil)).Elem(), GetIdlsListArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetTablegroupsListInput)(nil)).Elem(), GetTablegroupsListArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetTablegroupsListArrayInput)(nil)).Elem(), GetTablegroupsListArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetTablesListInput)(nil)).Elem(), GetTablesListArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetTablesListArrayInput)(nil)).Elem(), GetTablesListArray{})
	pulumi.RegisterOutputType(IdlTableInfoOutput{})
	pulumi.RegisterOutputType(IdlTableInfoArrayOutput{})
	pulumi.RegisterOutputType(GetClustersListOutput{})
	pulumi.RegisterOutputType(GetClustersListArrayOutput{})
	pulumi.RegisterOutputType(GetIdlsListOutput{})
	pulumi.RegisterOutputType(GetIdlsListArrayOutput{})
	pulumi.RegisterOutputType(GetTablegroupsListOutput{})
	pulumi.RegisterOutputType(GetTablegroupsListArrayOutput{})
	pulumi.RegisterOutputType(GetTablesListOutput{})
	pulumi.RegisterOutputType(GetTablesListArrayOutput{})
}
