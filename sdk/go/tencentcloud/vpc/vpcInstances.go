// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vpc

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func VpcInstances(ctx *pulumi.Context, args *VpcInstancesArgs, opts ...pulumi.InvokeOption) (*VpcInstancesResult, error) {
	var rv VpcInstancesResult
	err := ctx.Invoke("tencentcloud:Vpc/vpcInstances:VpcInstances", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking VpcInstances.
type VpcInstancesArgs struct {
	CidrBlock        *string                `pulumi:"cidrBlock"`
	IsDefault        *bool                  `pulumi:"isDefault"`
	Name             *string                `pulumi:"name"`
	ResultOutputFile *string                `pulumi:"resultOutputFile"`
	TagKey           *string                `pulumi:"tagKey"`
	Tags             map[string]interface{} `pulumi:"tags"`
	VpcId            *string                `pulumi:"vpcId"`
}

// A collection of values returned by VpcInstances.
type VpcInstancesResult struct {
	CidrBlock *string `pulumi:"cidrBlock"`
	// The provider-assigned unique ID for this managed resource.
	Id               string                     `pulumi:"id"`
	InstanceLists    []VpcInstancesInstanceList `pulumi:"instanceLists"`
	IsDefault        *bool                      `pulumi:"isDefault"`
	Name             *string                    `pulumi:"name"`
	ResultOutputFile *string                    `pulumi:"resultOutputFile"`
	TagKey           *string                    `pulumi:"tagKey"`
	Tags             map[string]interface{}     `pulumi:"tags"`
	VpcId            *string                    `pulumi:"vpcId"`
}

func VpcInstancesOutput(ctx *pulumi.Context, args VpcInstancesOutputArgs, opts ...pulumi.InvokeOption) VpcInstancesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (VpcInstancesResult, error) {
			args := v.(VpcInstancesArgs)
			r, err := VpcInstances(ctx, &args, opts...)
			var s VpcInstancesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(VpcInstancesResultOutput)
}

// A collection of arguments for invoking VpcInstances.
type VpcInstancesOutputArgs struct {
	CidrBlock        pulumi.StringPtrInput `pulumi:"cidrBlock"`
	IsDefault        pulumi.BoolPtrInput   `pulumi:"isDefault"`
	Name             pulumi.StringPtrInput `pulumi:"name"`
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	TagKey           pulumi.StringPtrInput `pulumi:"tagKey"`
	Tags             pulumi.MapInput       `pulumi:"tags"`
	VpcId            pulumi.StringPtrInput `pulumi:"vpcId"`
}

func (VpcInstancesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*VpcInstancesArgs)(nil)).Elem()
}

// A collection of values returned by VpcInstances.
type VpcInstancesResultOutput struct{ *pulumi.OutputState }

func (VpcInstancesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*VpcInstancesResult)(nil)).Elem()
}

func (o VpcInstancesResultOutput) ToVpcInstancesResultOutput() VpcInstancesResultOutput {
	return o
}

func (o VpcInstancesResultOutput) ToVpcInstancesResultOutputWithContext(ctx context.Context) VpcInstancesResultOutput {
	return o
}

func (o VpcInstancesResultOutput) CidrBlock() pulumi.StringPtrOutput {
	return o.ApplyT(func(v VpcInstancesResult) *string { return v.CidrBlock }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o VpcInstancesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v VpcInstancesResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o VpcInstancesResultOutput) InstanceLists() VpcInstancesInstanceListArrayOutput {
	return o.ApplyT(func(v VpcInstancesResult) []VpcInstancesInstanceList { return v.InstanceLists }).(VpcInstancesInstanceListArrayOutput)
}

func (o VpcInstancesResultOutput) IsDefault() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v VpcInstancesResult) *bool { return v.IsDefault }).(pulumi.BoolPtrOutput)
}

func (o VpcInstancesResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v VpcInstancesResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o VpcInstancesResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v VpcInstancesResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func (o VpcInstancesResultOutput) TagKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v VpcInstancesResult) *string { return v.TagKey }).(pulumi.StringPtrOutput)
}

func (o VpcInstancesResultOutput) Tags() pulumi.MapOutput {
	return o.ApplyT(func(v VpcInstancesResult) map[string]interface{} { return v.Tags }).(pulumi.MapOutput)
}

func (o VpcInstancesResultOutput) VpcId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v VpcInstancesResult) *string { return v.VpcId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(VpcInstancesResultOutput{})
}