// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dayu

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to query dayu DDoS policy cases
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/Dayu"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Dayu"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := Dayu.GetDdosPolicyCases(ctx, &dayu.GetDdosPolicyCasesArgs{
// 			ResourceType: tencentcloud_dayu_ddos_policy_case.Test_policy_case.Resource_type,
// 			SceneId:      tencentcloud_dayu_ddos_policy_case.Test_policy_case.Scene_id,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetDdosPolicyCases(ctx *pulumi.Context, args *GetDdosPolicyCasesArgs, opts ...pulumi.InvokeOption) (*GetDdosPolicyCasesResult, error) {
	var rv GetDdosPolicyCasesResult
	err := ctx.Invoke("tencentcloud:Dayu/getDdosPolicyCases:getDdosPolicyCases", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDdosPolicyCases.
type GetDdosPolicyCasesArgs struct {
	// Type of the resource that the DDoS policy case works for, valid values are `bgpip`, `bgp`, `bgp-multip` and `net`.
	ResourceType string `pulumi:"resourceType"`
	// Used to save results.
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	// ID of the DDoS policy case to be query.
	SceneId string `pulumi:"sceneId"`
}

// A collection of values returned by getDdosPolicyCases.
type GetDdosPolicyCasesResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// A list of DDoS policy cases. Each element contains the following attributes:
	Lists []GetDdosPolicyCasesList `pulumi:"lists"`
	// Type of the resource that the DDoS policy case works for.
	ResourceType     string  `pulumi:"resourceType"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	// ID of the DDoS policy case.
	SceneId string `pulumi:"sceneId"`
}

func GetDdosPolicyCasesOutput(ctx *pulumi.Context, args GetDdosPolicyCasesOutputArgs, opts ...pulumi.InvokeOption) GetDdosPolicyCasesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetDdosPolicyCasesResult, error) {
			args := v.(GetDdosPolicyCasesArgs)
			r, err := GetDdosPolicyCases(ctx, &args, opts...)
			var s GetDdosPolicyCasesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetDdosPolicyCasesResultOutput)
}

// A collection of arguments for invoking getDdosPolicyCases.
type GetDdosPolicyCasesOutputArgs struct {
	// Type of the resource that the DDoS policy case works for, valid values are `bgpip`, `bgp`, `bgp-multip` and `net`.
	ResourceType pulumi.StringInput `pulumi:"resourceType"`
	// Used to save results.
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	// ID of the DDoS policy case to be query.
	SceneId pulumi.StringInput `pulumi:"sceneId"`
}

func (GetDdosPolicyCasesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDdosPolicyCasesArgs)(nil)).Elem()
}

// A collection of values returned by getDdosPolicyCases.
type GetDdosPolicyCasesResultOutput struct{ *pulumi.OutputState }

func (GetDdosPolicyCasesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDdosPolicyCasesResult)(nil)).Elem()
}

func (o GetDdosPolicyCasesResultOutput) ToGetDdosPolicyCasesResultOutput() GetDdosPolicyCasesResultOutput {
	return o
}

func (o GetDdosPolicyCasesResultOutput) ToGetDdosPolicyCasesResultOutputWithContext(ctx context.Context) GetDdosPolicyCasesResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetDdosPolicyCasesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetDdosPolicyCasesResult) string { return v.Id }).(pulumi.StringOutput)
}

// A list of DDoS policy cases. Each element contains the following attributes:
func (o GetDdosPolicyCasesResultOutput) Lists() GetDdosPolicyCasesListArrayOutput {
	return o.ApplyT(func(v GetDdosPolicyCasesResult) []GetDdosPolicyCasesList { return v.Lists }).(GetDdosPolicyCasesListArrayOutput)
}

// Type of the resource that the DDoS policy case works for.
func (o GetDdosPolicyCasesResultOutput) ResourceType() pulumi.StringOutput {
	return o.ApplyT(func(v GetDdosPolicyCasesResult) string { return v.ResourceType }).(pulumi.StringOutput)
}

func (o GetDdosPolicyCasesResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetDdosPolicyCasesResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

// ID of the DDoS policy case.
func (o GetDdosPolicyCasesResultOutput) SceneId() pulumi.StringOutput {
	return o.ApplyT(func(v GetDdosPolicyCasesResult) string { return v.SceneId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetDdosPolicyCasesResultOutput{})
}