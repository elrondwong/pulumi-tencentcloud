// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sqlserver

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func BasicInstances(ctx *pulumi.Context, args *BasicInstancesArgs, opts ...pulumi.InvokeOption) (*BasicInstancesResult, error) {
	var rv BasicInstancesResult
	err := ctx.Invoke("tencentcloud:Sqlserver/basicInstances:BasicInstances", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking BasicInstances.
type BasicInstancesArgs struct {
	Id               *string `pulumi:"id"`
	Name             *string `pulumi:"name"`
	ProjectId        *int    `pulumi:"projectId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	SubnetId         *string `pulumi:"subnetId"`
	VpcId            *string `pulumi:"vpcId"`
}

// A collection of values returned by BasicInstances.
type BasicInstancesResult struct {
	Id               *string                      `pulumi:"id"`
	InstanceLists    []BasicInstancesInstanceList `pulumi:"instanceLists"`
	Name             *string                      `pulumi:"name"`
	ProjectId        *int                         `pulumi:"projectId"`
	ResultOutputFile *string                      `pulumi:"resultOutputFile"`
	SubnetId         *string                      `pulumi:"subnetId"`
	VpcId            *string                      `pulumi:"vpcId"`
}

func BasicInstancesOutput(ctx *pulumi.Context, args BasicInstancesOutputArgs, opts ...pulumi.InvokeOption) BasicInstancesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (BasicInstancesResult, error) {
			args := v.(BasicInstancesArgs)
			r, err := BasicInstances(ctx, &args, opts...)
			var s BasicInstancesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(BasicInstancesResultOutput)
}

// A collection of arguments for invoking BasicInstances.
type BasicInstancesOutputArgs struct {
	Id               pulumi.StringPtrInput `pulumi:"id"`
	Name             pulumi.StringPtrInput `pulumi:"name"`
	ProjectId        pulumi.IntPtrInput    `pulumi:"projectId"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	SubnetId         pulumi.StringPtrInput `pulumi:"subnetId"`
	VpcId            pulumi.StringPtrInput `pulumi:"vpcId"`
}

func (BasicInstancesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*BasicInstancesArgs)(nil)).Elem()
}

// A collection of values returned by BasicInstances.
type BasicInstancesResultOutput struct{ *pulumi.OutputState }

func (BasicInstancesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*BasicInstancesResult)(nil)).Elem()
}

func (o BasicInstancesResultOutput) ToBasicInstancesResultOutput() BasicInstancesResultOutput {
	return o
}

func (o BasicInstancesResultOutput) ToBasicInstancesResultOutputWithContext(ctx context.Context) BasicInstancesResultOutput {
	return o
}

func (o BasicInstancesResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v BasicInstancesResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o BasicInstancesResultOutput) InstanceLists() BasicInstancesInstanceListArrayOutput {
	return o.ApplyT(func(v BasicInstancesResult) []BasicInstancesInstanceList { return v.InstanceLists }).(BasicInstancesInstanceListArrayOutput)
}

func (o BasicInstancesResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v BasicInstancesResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o BasicInstancesResultOutput) ProjectId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v BasicInstancesResult) *int { return v.ProjectId }).(pulumi.IntPtrOutput)
}

func (o BasicInstancesResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v BasicInstancesResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o BasicInstancesResultOutput) SubnetId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v BasicInstancesResult) *string { return v.SubnetId }).(pulumi.StringPtrOutput)
}

func (o BasicInstancesResultOutput) VpcId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v BasicInstancesResult) *string { return v.VpcId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(BasicInstancesResultOutput{})
}