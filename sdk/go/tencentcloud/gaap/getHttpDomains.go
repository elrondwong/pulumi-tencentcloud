// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package gaap

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to query forward domain of layer7 listeners.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/Gaap"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Gaap"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		fooProxy, err := Gaap.NewProxy(ctx, "fooProxy", &Gaap.ProxyArgs{
// 			Bandwidth:        pulumi.Int(10),
// 			Concurrent:       pulumi.Int(2),
// 			AccessRegion:     pulumi.String("SouthChina"),
// 			RealserverRegion: pulumi.String("NorthChina"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		fooLayer7Listener, err := Gaap.NewLayer7Listener(ctx, "fooLayer7Listener", &Gaap.Layer7ListenerArgs{
// 			Protocol: pulumi.String("HTTP"),
// 			Port:     pulumi.Int(80),
// 			ProxyId:  fooProxy.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		fooHttpDomain, err := Gaap.NewHttpDomain(ctx, "fooHttpDomain", &Gaap.HttpDomainArgs{
// 			ListenerId: fooLayer7Listener.ID(),
// 			Domain:     pulumi.String("www.qq.com"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_ = Gaap.GetHttpDomainsOutput(ctx, gaap.GetHttpDomainsOutputArgs{
// 			ListenerId: fooLayer7Listener.ID(),
// 			Domain:     fooHttpDomain.Domain,
// 		}, nil)
// 		return nil
// 	})
// }
// ```
func GetHttpDomains(ctx *pulumi.Context, args *GetHttpDomainsArgs, opts ...pulumi.InvokeOption) (*GetHttpDomainsResult, error) {
	var rv GetHttpDomainsResult
	err := ctx.Invoke("tencentcloud:Gaap/getHttpDomains:getHttpDomains", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getHttpDomains.
type GetHttpDomainsArgs struct {
	// Forward domain of the layer7 listener to be queried.
	Domain string `pulumi:"domain"`
	// ID of the layer7 listener to be queried.
	ListenerId string `pulumi:"listenerId"`
	// Used to save results.
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

// A collection of values returned by getHttpDomains.
type GetHttpDomainsResult struct {
	// Forward domain of the layer7 listener.
	Domain string `pulumi:"domain"`
	// An information list of forward domain of the layer7 listeners. Each element contains the following attributes:
	Domains []GetHttpDomainsDomain `pulumi:"domains"`
	// The provider-assigned unique ID for this managed resource.
	Id               string  `pulumi:"id"`
	ListenerId       string  `pulumi:"listenerId"`
	ResultOutputFile *string `pulumi:"resultOutputFile"`
}

func GetHttpDomainsOutput(ctx *pulumi.Context, args GetHttpDomainsOutputArgs, opts ...pulumi.InvokeOption) GetHttpDomainsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetHttpDomainsResult, error) {
			args := v.(GetHttpDomainsArgs)
			r, err := GetHttpDomains(ctx, &args, opts...)
			var s GetHttpDomainsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetHttpDomainsResultOutput)
}

// A collection of arguments for invoking getHttpDomains.
type GetHttpDomainsOutputArgs struct {
	// Forward domain of the layer7 listener to be queried.
	Domain pulumi.StringInput `pulumi:"domain"`
	// ID of the layer7 listener to be queried.
	ListenerId pulumi.StringInput `pulumi:"listenerId"`
	// Used to save results.
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
}

func (GetHttpDomainsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetHttpDomainsArgs)(nil)).Elem()
}

// A collection of values returned by getHttpDomains.
type GetHttpDomainsResultOutput struct{ *pulumi.OutputState }

func (GetHttpDomainsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetHttpDomainsResult)(nil)).Elem()
}

func (o GetHttpDomainsResultOutput) ToGetHttpDomainsResultOutput() GetHttpDomainsResultOutput {
	return o
}

func (o GetHttpDomainsResultOutput) ToGetHttpDomainsResultOutputWithContext(ctx context.Context) GetHttpDomainsResultOutput {
	return o
}

// Forward domain of the layer7 listener.
func (o GetHttpDomainsResultOutput) Domain() pulumi.StringOutput {
	return o.ApplyT(func(v GetHttpDomainsResult) string { return v.Domain }).(pulumi.StringOutput)
}

// An information list of forward domain of the layer7 listeners. Each element contains the following attributes:
func (o GetHttpDomainsResultOutput) Domains() GetHttpDomainsDomainArrayOutput {
	return o.ApplyT(func(v GetHttpDomainsResult) []GetHttpDomainsDomain { return v.Domains }).(GetHttpDomainsDomainArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetHttpDomainsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetHttpDomainsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetHttpDomainsResultOutput) ListenerId() pulumi.StringOutput {
	return o.ApplyT(func(v GetHttpDomainsResult) string { return v.ListenerId }).(pulumi.StringOutput)
}

func (o GetHttpDomainsResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetHttpDomainsResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetHttpDomainsResultOutput{})
}