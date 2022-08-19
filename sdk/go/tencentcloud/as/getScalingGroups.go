// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package as

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to query the detail information of an existing autoscaling group.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/As"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/As"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := As.GetScalingGroups(ctx, &as.GetScalingGroupsArgs{
// 			ConfigurationId:  pulumi.StringRef("asc-oqio4yyj"),
// 			ResultOutputFile: pulumi.StringRef("my_test_path"),
// 			ScalingGroupName: pulumi.StringRef("myasgroup"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetScalingGroups(ctx *pulumi.Context, args *GetScalingGroupsArgs, opts ...pulumi.InvokeOption) (*GetScalingGroupsResult, error) {
	var rv GetScalingGroupsResult
	err := ctx.Invoke("tencentcloud:As/getScalingGroups:getScalingGroups", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getScalingGroups.
type GetScalingGroupsArgs struct {
	// Filter results by launch configuration ID.
	ConfigurationId *string `pulumi:"configurationId"`
	// Used to save results.
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	// A specified scaling group ID used to query.
	ScalingGroupId *string `pulumi:"scalingGroupId"`
	// A scaling group name used to query.
	ScalingGroupName *string `pulumi:"scalingGroupName"`
	// Tags used to query.
	Tags map[string]interface{} `pulumi:"tags"`
}

// A collection of values returned by getScalingGroups.
type GetScalingGroupsResult struct {
	// Launch configuration ID.
	ConfigurationId *string `pulumi:"configurationId"`
	// The provider-assigned unique ID for this managed resource.
	Id               string  `pulumi:"id"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	// Auto scaling group ID.
	ScalingGroupId *string `pulumi:"scalingGroupId"`
	// A list of scaling group. Each element contains the following attributes:
	ScalingGroupLists []GetScalingGroupsScalingGroupList `pulumi:"scalingGroupLists"`
	// Auto scaling group name.
	ScalingGroupName *string `pulumi:"scalingGroupName"`
	// Tags of the scaling group.
	Tags map[string]interface{} `pulumi:"tags"`
}

func GetScalingGroupsOutput(ctx *pulumi.Context, args GetScalingGroupsOutputArgs, opts ...pulumi.InvokeOption) GetScalingGroupsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetScalingGroupsResult, error) {
			args := v.(GetScalingGroupsArgs)
			r, err := GetScalingGroups(ctx, &args, opts...)
			var s GetScalingGroupsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetScalingGroupsResultOutput)
}

// A collection of arguments for invoking getScalingGroups.
type GetScalingGroupsOutputArgs struct {
	// Filter results by launch configuration ID.
	ConfigurationId pulumi.StringPtrInput `pulumi:"configurationId"`
	// Used to save results.
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	// A specified scaling group ID used to query.
	ScalingGroupId pulumi.StringPtrInput `pulumi:"scalingGroupId"`
	// A scaling group name used to query.
	ScalingGroupName pulumi.StringPtrInput `pulumi:"scalingGroupName"`
	// Tags used to query.
	Tags pulumi.MapInput `pulumi:"tags"`
}

func (GetScalingGroupsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetScalingGroupsArgs)(nil)).Elem()
}

// A collection of values returned by getScalingGroups.
type GetScalingGroupsResultOutput struct{ *pulumi.OutputState }

func (GetScalingGroupsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetScalingGroupsResult)(nil)).Elem()
}

func (o GetScalingGroupsResultOutput) ToGetScalingGroupsResultOutput() GetScalingGroupsResultOutput {
	return o
}

func (o GetScalingGroupsResultOutput) ToGetScalingGroupsResultOutputWithContext(ctx context.Context) GetScalingGroupsResultOutput {
	return o
}

// Launch configuration ID.
func (o GetScalingGroupsResultOutput) ConfigurationId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetScalingGroupsResult) *string { return v.ConfigurationId }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetScalingGroupsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetScalingGroupsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetScalingGroupsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetScalingGroupsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

// Auto scaling group ID.
func (o GetScalingGroupsResultOutput) ScalingGroupId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetScalingGroupsResult) *string { return v.ScalingGroupId }).(pulumi.StringPtrOutput)
}

// A list of scaling group. Each element contains the following attributes:
func (o GetScalingGroupsResultOutput) ScalingGroupLists() GetScalingGroupsScalingGroupListArrayOutput {
	return o.ApplyT(func(v GetScalingGroupsResult) []GetScalingGroupsScalingGroupList { return v.ScalingGroupLists }).(GetScalingGroupsScalingGroupListArrayOutput)
}

// Auto scaling group name.
func (o GetScalingGroupsResultOutput) ScalingGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetScalingGroupsResult) *string { return v.ScalingGroupName }).(pulumi.StringPtrOutput)
}

// Tags of the scaling group.
func (o GetScalingGroupsResultOutput) Tags() pulumi.MapOutput {
	return o.ApplyT(func(v GetScalingGroupsResult) map[string]interface{} { return v.Tags }).(pulumi.MapOutput)
}

func init() {
	pulumi.RegisterOutputType(GetScalingGroupsResultOutput{})
}