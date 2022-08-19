// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to query API gateway throttling APIs.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/ApiGateway"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/ApiGateway"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		service, err := ApiGateway.NewService(ctx, "service", &ApiGateway.ServiceArgs{
// 			ServiceName: pulumi.String("niceservice"),
// 			Protocol:    pulumi.String("http&https"),
// 			ServiceDesc: pulumi.String("your nice service"),
// 			NetTypes: pulumi.StringArray{
// 				pulumi.String("INNER"),
// 				pulumi.String("OUTER"),
// 			},
// 			IpVersion: pulumi.String("IPv4"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ApiGateway.NewApi(ctx, "api", &ApiGateway.ApiArgs{
// 			ServiceId:           service.ID(),
// 			ApiName:             pulumi.String("hello_update"),
// 			ApiDesc:             pulumi.String("my hello api update"),
// 			AuthType:            pulumi.String("SECRET"),
// 			Protocol:            pulumi.String("HTTP"),
// 			EnableCors:          pulumi.Bool(true),
// 			RequestConfigPath:   pulumi.String("/user/info"),
// 			RequestConfigMethod: pulumi.String("POST"),
// 			RequestParameters: apigateway.ApiRequestParameterArray{
// 				&apigateway.ApiRequestParameterArgs{
// 					Name:         pulumi.String("email"),
// 					Position:     pulumi.String("QUERY"),
// 					Type:         pulumi.String("string"),
// 					Desc:         pulumi.String("your email please?"),
// 					DefaultValue: pulumi.String("tom@qq.com"),
// 					Required:     pulumi.Bool(true),
// 				},
// 			},
// 			ServiceConfigType:      pulumi.String("HTTP"),
// 			ServiceConfigTimeout:   pulumi.Int(10),
// 			ServiceConfigUrl:       pulumi.String("http://www.tencent.com"),
// 			ServiceConfigPath:      pulumi.String("/user"),
// 			ServiceConfigMethod:    pulumi.String("POST"),
// 			ResponseType:           pulumi.String("XML"),
// 			ResponseSuccessExample: pulumi.String("<note>success</note>"),
// 			ResponseFailExample:    pulumi.String("<note>fail</note>"),
// 			ResponseErrorCodes: apigateway.ApiResponseErrorCodeArray{
// 				&apigateway.ApiResponseErrorCodeArgs{
// 					Code:          pulumi.Int(10),
// 					Msg:           pulumi.String("system error"),
// 					Desc:          pulumi.String("system error code"),
// 					ConvertedCode: -10,
// 					NeedConvert:   pulumi.Bool(true),
// 				},
// 			},
// 			ReleaseLimit: pulumi.Int(100),
// 			PreLimit:     pulumi.Int(100),
// 			TestLimit:    pulumi.Int(100),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ApiGateway.GetThrottlingApis(ctx, &apigateway.GetThrottlingApisArgs{
// 			ServiceId: pulumi.StringRef(tencentcloud_api_gateway_api.Service_id),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ApiGateway.GetThrottlingApis(ctx, &apigateway.GetThrottlingApisArgs{
// 			ServiceId: pulumi.StringRef(tencentcloud_api_gateway_api.Service.Service_id),
// 			EnvironmentNames: []string{
// 				"release",
// 				"test",
// 			},
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetThrottlingApis(ctx *pulumi.Context, args *GetThrottlingApisArgs, opts ...pulumi.InvokeOption) (*GetThrottlingApisResult, error) {
	var rv GetThrottlingApisResult
	err := ctx.Invoke("tencentcloud:ApiGateway/getThrottlingApis:getThrottlingApis", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getThrottlingApis.
type GetThrottlingApisArgs struct {
	// Environment list.
	EnvironmentNames []string `pulumi:"environmentNames"`
	// Used to save results.
	ResultOutputFile *string `pulumi:"resultOutputFile"`
	// Unique service ID of API.
	ServiceId *string `pulumi:"serviceId"`
}

// A collection of values returned by getThrottlingApis.
type GetThrottlingApisResult struct {
	EnvironmentNames []string `pulumi:"environmentNames"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// A list of policies bound to API.
	Lists            []GetThrottlingApisList `pulumi:"lists"`
	ResultOutputFile *string                 `pulumi:"resultOutputFile"`
	// Unique service ID of API.
	ServiceId *string `pulumi:"serviceId"`
}

func GetThrottlingApisOutput(ctx *pulumi.Context, args GetThrottlingApisOutputArgs, opts ...pulumi.InvokeOption) GetThrottlingApisResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetThrottlingApisResult, error) {
			args := v.(GetThrottlingApisArgs)
			r, err := GetThrottlingApis(ctx, &args, opts...)
			var s GetThrottlingApisResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetThrottlingApisResultOutput)
}

// A collection of arguments for invoking getThrottlingApis.
type GetThrottlingApisOutputArgs struct {
	// Environment list.
	EnvironmentNames pulumi.StringArrayInput `pulumi:"environmentNames"`
	// Used to save results.
	ResultOutputFile pulumi.StringPtrInput `pulumi:"resultOutputFile"`
	// Unique service ID of API.
	ServiceId pulumi.StringPtrInput `pulumi:"serviceId"`
}

func (GetThrottlingApisOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetThrottlingApisArgs)(nil)).Elem()
}

// A collection of values returned by getThrottlingApis.
type GetThrottlingApisResultOutput struct{ *pulumi.OutputState }

func (GetThrottlingApisResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetThrottlingApisResult)(nil)).Elem()
}

func (o GetThrottlingApisResultOutput) ToGetThrottlingApisResultOutput() GetThrottlingApisResultOutput {
	return o
}

func (o GetThrottlingApisResultOutput) ToGetThrottlingApisResultOutputWithContext(ctx context.Context) GetThrottlingApisResultOutput {
	return o
}

func (o GetThrottlingApisResultOutput) EnvironmentNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetThrottlingApisResult) []string { return v.EnvironmentNames }).(pulumi.StringArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetThrottlingApisResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetThrottlingApisResult) string { return v.Id }).(pulumi.StringOutput)
}

// A list of policies bound to API.
func (o GetThrottlingApisResultOutput) Lists() GetThrottlingApisListArrayOutput {
	return o.ApplyT(func(v GetThrottlingApisResult) []GetThrottlingApisList { return v.Lists }).(GetThrottlingApisListArrayOutput)
}

func (o GetThrottlingApisResultOutput) ResultOutputFile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetThrottlingApisResult) *string { return v.ResultOutputFile }).(pulumi.StringPtrOutput)
}

// Unique service ID of API.
func (o GetThrottlingApisResultOutput) ServiceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetThrottlingApisResult) *string { return v.ServiceId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetThrottlingApisResultOutput{})
}