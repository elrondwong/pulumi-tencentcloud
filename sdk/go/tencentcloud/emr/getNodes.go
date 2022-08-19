// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package emr

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides an available EMR for the user.
//
// The EMR data source obtain the hardware node information by using the emr cluster ID.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/Emr"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Emr"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := Emr.GetNodes(ctx, &emr.GetNodesArgs{
// 			InstanceId: "emr-rnzqrleq",
// 			NodeFlag:   "master",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetNodes(ctx *pulumi.Context, args *GetNodesArgs, opts ...pulumi.InvokeOption) (*GetNodesResult, error) {
	var rv GetNodesResult
	err := ctx.Invoke("tencentcloud:Emr/getNodes:getNodes", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNodes.
type GetNodesArgs struct {
	// Resource type: Support all/host/pod, default is all.
	HardwareResourceType *string `pulumi:"hardwareResourceType"`
	// Cluster instance ID, the instance ID is as follows: emr-xxxxxxxx.
	InstanceId string `pulumi:"instanceId"`
	// The number returned per page, the default value is 100, and the maximum value is 100.
	Limit *int `pulumi:"limit"`
	// Node ID, the value is:
	// - all: Means to get all type nodes, except cdb information.
	// - master: Indicates that the master node information is obtained.
	// - core: Indicates that the core node information is obtained.
	// - task: indicates obtaining task node information.
	// - common: means to get common node information.
	// - router: Indicates obtaining router node information.
	// - db: Indicates that the cdb information for the normal state is obtained.
	// - recyle: Indicates that the node information in the Recycle Bin isolation, including the cdb information, is obtained.
	// - renew: Indicates that all node information to be renewed, including cddb information, is obtained, and the auto-renewal node will not be returned.
	NodeFlag string `pulumi:"nodeFlag"`
	// Page number, with a default value of 0, represents the first page.
	Offset *int `pulumi:"offset"`
	// Used to save results.
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by getNodes.
type GetNodesResult struct {
	// Resource type, host/pod.
	HardwareResourceType *string `pulumi:"hardwareResourceType"`
	// The provider-assigned unique ID for this managed resource.
	Id         string `pulumi:"id"`
	InstanceId string `pulumi:"instanceId"`
	Limit      *int   `pulumi:"limit"`
	NodeFlag   string `pulumi:"nodeFlag"`
	// List of node details.
	Nodes            []GetNodesNode `pulumi:"nodes"`
	Offset           *int           `pulumi:"offset"`
	ResultOutputFile *string        `pulumi:"resultOutputFile"`
}

func GetNodesOutput(ctx *pulumi.Context, args GetNodesOutputArgs, opts ...pulumi.InvokeOption) GetNodesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetNodesResult, error) {
			args := v.(GetNodesArgs)
			r, err := GetNodes(ctx, &args, opts...)
			var s GetNodesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetNodesResultOutput)
}

// A collection of arguments for invoking getNodes.
type GetNodesOutputArgs struct {
	// Resource type: Support all/host/pod, default is all.
	HardwareResourceType pulumi.StringPtrInput `pulumi:"hardwareResourceType"`
	// Cluster instance ID, the instance ID is as follows: emr-xxxxxxxx.
	InstanceId pulumi.StringInput `pulumi:"instanceId"`
	// The number returned per page, the default value is 100, and the maximum value is 100.
	Limit pulumi.IntPtrInput `pulumi:"limit"`
	// Node ID, the value is:
	// - all: Means to get all type nodes, except cdb information.
	// - master: Indicates that the master node information is obtained.
	// - core: Indicates that the core node information is obtained.
	// - task: indicates obtaining task node information.
	// - common: means to get common node information.
	// - router: Indicates obtaining router node information.
	// - db: Indicates that the cdb information for the normal state is obtained.
	// - recyle: Indicates that the node information in the Recycle Bin isolation, including the cdb information, is obtained.
	// - renew: Indicates that all node information to be renewed, including cddb information, is obtained, and the auto-renewal node will not be returned.
	NodeFlag pulumi.StringInput `pulumi:"nodeFlag"`
	// Page number, with a default value of 0, represents the first page.
	Offset pulumi.IntPtrInput `pulumi:"offset"`
	// Used to save results.
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (GetNodesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetNodesArgs)(nil)).Elem()
}

// A collection of values returned by getNodes.
type GetNodesResultOutput struct{ *pulumi.OutputState }

func (GetNodesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetNodesResult)(nil)).Elem()
}

func (o GetNodesResultOutput) ToGetNodesResultOutput() GetNodesResultOutput {
	return o
}

func (o GetNodesResultOutput) ToGetNodesResultOutputWithContext(ctx context.Context) GetNodesResultOutput {
	return o
}

// Resource type, host/pod.
func (o GetNodesResultOutput) HardwareResourceType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetNodesResult) *string { return v.HardwareResourceType }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetNodesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetNodesResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetNodesResultOutput) InstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v GetNodesResult) string { return v.InstanceId }).(pulumi.StringOutput)
}

func (o GetNodesResultOutput) Limit() pulumi.IntPtrOutput {
	return o.ApplyT(func(v GetNodesResult) *int { return v.Limit }).(pulumi.IntPtrOutput)
}

func (o GetNodesResultOutput) NodeFlag() pulumi.StringOutput {
	return o.ApplyT(func(v GetNodesResult) string { return v.NodeFlag }).(pulumi.StringOutput)
}

// List of node details.
func (o GetNodesResultOutput) Nodes() GetNodesNodeArrayOutput {
	return o.ApplyT(func(v GetNodesResult) []GetNodesNode { return v.Nodes }).(GetNodesNodeArrayOutput)
}

func (o GetNodesResultOutput) Offset() pulumi.IntPtrOutput {
	return o.ApplyT(func(v GetNodesResult) *int { return v.Offset }).(pulumi.IntPtrOutput)
}

func (o GetNodesResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetNodesResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetNodesResultOutput{})
}