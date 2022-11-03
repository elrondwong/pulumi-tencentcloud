// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sqlserver

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a SQL Server PublishSubscribe resource belongs to SQL Server instance.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud/Sqlserver"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/tencentcloudstack/pulumi-tencentcloud/sdk/go/tencentcloud/Sqlserver"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := Sqlserver.NewPublishSubscribe(ctx, "example", &Sqlserver.PublishSubscribeArgs{
//				PublishInstanceId:    pulumi.Any(tencentcloud_sqlserver_instance.Publish_instance.Id),
//				SubscribeInstanceId:  pulumi.Any(tencentcloud_sqlserver_instance.Subscribe_instance.Id),
//				PublishSubscribeName: pulumi.String("example"),
//				DeleteSubscribeDb:    pulumi.Bool(false),
//				DatabaseTuples: sqlserver.PublishSubscribeDatabaseTupleArray{
//					&sqlserver.PublishSubscribeDatabaseTupleArgs{
//						PublishDatabase: pulumi.Any(tencentcloud_sqlserver_db.Test_publish_subscribe.Name),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// SQL Server PublishSubscribe can be imported using the publish_sqlserver_id#subscribe_sqlserver_id, e.g.
//
// ```sh
//
//	$ pulumi import tencentcloud:Sqlserver/publishSubscribe:PublishSubscribe foo publish_sqlserver_id#subscribe_sqlserver_id
//
// ```
type PublishSubscribe struct {
	pulumi.CustomResourceState

	// Database Publish and Publish relationship list. The elements inside can be deleted and added individually, but modification is not allowed.
	DatabaseTuples PublishSubscribeDatabaseTupleArrayOutput `pulumi:"databaseTuples"`
	// Whether to delete the subscriber database when deleting the Publish and Subscribe. `true` for deletes the subscribe database, `false` for does not delete the subscribe database. default is `false`.
	DeleteSubscribeDb pulumi.BoolPtrOutput `pulumi:"deleteSubscribeDb"`
	// ID of the SQL Server instance which publish.
	PublishInstanceId pulumi.StringOutput `pulumi:"publishInstanceId"`
	// ID of PubSub.
	PublishSubscribeId pulumi.IntOutput `pulumi:"publishSubscribeId"`
	// The name of the Publish and Subscribe. Default is `defaultName`.
	PublishSubscribeName pulumi.StringPtrOutput `pulumi:"publishSubscribeName"`
	// ID of the SQL Server instance which subscribe.
	SubscribeInstanceId pulumi.StringOutput `pulumi:"subscribeInstanceId"`
}

// NewPublishSubscribe registers a new resource with the given unique name, arguments, and options.
func NewPublishSubscribe(ctx *pulumi.Context,
	name string, args *PublishSubscribeArgs, opts ...pulumi.ResourceOption) (*PublishSubscribe, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DatabaseTuples == nil {
		return nil, errors.New("invalid value for required argument 'DatabaseTuples'")
	}
	if args.PublishInstanceId == nil {
		return nil, errors.New("invalid value for required argument 'PublishInstanceId'")
	}
	if args.SubscribeInstanceId == nil {
		return nil, errors.New("invalid value for required argument 'SubscribeInstanceId'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource PublishSubscribe
	err := ctx.RegisterResource("tencentcloud:Sqlserver/publishSubscribe:PublishSubscribe", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPublishSubscribe gets an existing PublishSubscribe resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPublishSubscribe(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PublishSubscribeState, opts ...pulumi.ResourceOption) (*PublishSubscribe, error) {
	var resource PublishSubscribe
	err := ctx.ReadResource("tencentcloud:Sqlserver/publishSubscribe:PublishSubscribe", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PublishSubscribe resources.
type publishSubscribeState struct {
	// Database Publish and Publish relationship list. The elements inside can be deleted and added individually, but modification is not allowed.
	DatabaseTuples []PublishSubscribeDatabaseTuple `pulumi:"databaseTuples"`
	// Whether to delete the subscriber database when deleting the Publish and Subscribe. `true` for deletes the subscribe database, `false` for does not delete the subscribe database. default is `false`.
	DeleteSubscribeDb *bool `pulumi:"deleteSubscribeDb"`
	// ID of the SQL Server instance which publish.
	PublishInstanceId *string `pulumi:"publishInstanceId"`
	// ID of PubSub.
	PublishSubscribeId *int `pulumi:"publishSubscribeId"`
	// The name of the Publish and Subscribe. Default is `defaultName`.
	PublishSubscribeName *string `pulumi:"publishSubscribeName"`
	// ID of the SQL Server instance which subscribe.
	SubscribeInstanceId *string `pulumi:"subscribeInstanceId"`
}

type PublishSubscribeState struct {
	// Database Publish and Publish relationship list. The elements inside can be deleted and added individually, but modification is not allowed.
	DatabaseTuples PublishSubscribeDatabaseTupleArrayInput
	// Whether to delete the subscriber database when deleting the Publish and Subscribe. `true` for deletes the subscribe database, `false` for does not delete the subscribe database. default is `false`.
	DeleteSubscribeDb pulumi.BoolPtrInput
	// ID of the SQL Server instance which publish.
	PublishInstanceId pulumi.StringPtrInput
	// ID of PubSub.
	PublishSubscribeId pulumi.IntPtrInput
	// The name of the Publish and Subscribe. Default is `defaultName`.
	PublishSubscribeName pulumi.StringPtrInput
	// ID of the SQL Server instance which subscribe.
	SubscribeInstanceId pulumi.StringPtrInput
}

func (PublishSubscribeState) ElementType() reflect.Type {
	return reflect.TypeOf((*publishSubscribeState)(nil)).Elem()
}

type publishSubscribeArgs struct {
	// Database Publish and Publish relationship list. The elements inside can be deleted and added individually, but modification is not allowed.
	DatabaseTuples []PublishSubscribeDatabaseTuple `pulumi:"databaseTuples"`
	// Whether to delete the subscriber database when deleting the Publish and Subscribe. `true` for deletes the subscribe database, `false` for does not delete the subscribe database. default is `false`.
	DeleteSubscribeDb *bool `pulumi:"deleteSubscribeDb"`
	// ID of the SQL Server instance which publish.
	PublishInstanceId string `pulumi:"publishInstanceId"`
	// The name of the Publish and Subscribe. Default is `defaultName`.
	PublishSubscribeName *string `pulumi:"publishSubscribeName"`
	// ID of the SQL Server instance which subscribe.
	SubscribeInstanceId string `pulumi:"subscribeInstanceId"`
}

// The set of arguments for constructing a PublishSubscribe resource.
type PublishSubscribeArgs struct {
	// Database Publish and Publish relationship list. The elements inside can be deleted and added individually, but modification is not allowed.
	DatabaseTuples PublishSubscribeDatabaseTupleArrayInput
	// Whether to delete the subscriber database when deleting the Publish and Subscribe. `true` for deletes the subscribe database, `false` for does not delete the subscribe database. default is `false`.
	DeleteSubscribeDb pulumi.BoolPtrInput
	// ID of the SQL Server instance which publish.
	PublishInstanceId pulumi.StringInput
	// The name of the Publish and Subscribe. Default is `defaultName`.
	PublishSubscribeName pulumi.StringPtrInput
	// ID of the SQL Server instance which subscribe.
	SubscribeInstanceId pulumi.StringInput
}

func (PublishSubscribeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*publishSubscribeArgs)(nil)).Elem()
}

type PublishSubscribeInput interface {
	pulumi.Input

	ToPublishSubscribeOutput() PublishSubscribeOutput
	ToPublishSubscribeOutputWithContext(ctx context.Context) PublishSubscribeOutput
}

func (*PublishSubscribe) ElementType() reflect.Type {
	return reflect.TypeOf((**PublishSubscribe)(nil)).Elem()
}

func (i *PublishSubscribe) ToPublishSubscribeOutput() PublishSubscribeOutput {
	return i.ToPublishSubscribeOutputWithContext(context.Background())
}

func (i *PublishSubscribe) ToPublishSubscribeOutputWithContext(ctx context.Context) PublishSubscribeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PublishSubscribeOutput)
}

// PublishSubscribeArrayInput is an input type that accepts PublishSubscribeArray and PublishSubscribeArrayOutput values.
// You can construct a concrete instance of `PublishSubscribeArrayInput` via:
//
//	PublishSubscribeArray{ PublishSubscribeArgs{...} }
type PublishSubscribeArrayInput interface {
	pulumi.Input

	ToPublishSubscribeArrayOutput() PublishSubscribeArrayOutput
	ToPublishSubscribeArrayOutputWithContext(context.Context) PublishSubscribeArrayOutput
}

type PublishSubscribeArray []PublishSubscribeInput

func (PublishSubscribeArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PublishSubscribe)(nil)).Elem()
}

func (i PublishSubscribeArray) ToPublishSubscribeArrayOutput() PublishSubscribeArrayOutput {
	return i.ToPublishSubscribeArrayOutputWithContext(context.Background())
}

func (i PublishSubscribeArray) ToPublishSubscribeArrayOutputWithContext(ctx context.Context) PublishSubscribeArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PublishSubscribeArrayOutput)
}

// PublishSubscribeMapInput is an input type that accepts PublishSubscribeMap and PublishSubscribeMapOutput values.
// You can construct a concrete instance of `PublishSubscribeMapInput` via:
//
//	PublishSubscribeMap{ "key": PublishSubscribeArgs{...} }
type PublishSubscribeMapInput interface {
	pulumi.Input

	ToPublishSubscribeMapOutput() PublishSubscribeMapOutput
	ToPublishSubscribeMapOutputWithContext(context.Context) PublishSubscribeMapOutput
}

type PublishSubscribeMap map[string]PublishSubscribeInput

func (PublishSubscribeMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PublishSubscribe)(nil)).Elem()
}

func (i PublishSubscribeMap) ToPublishSubscribeMapOutput() PublishSubscribeMapOutput {
	return i.ToPublishSubscribeMapOutputWithContext(context.Background())
}

func (i PublishSubscribeMap) ToPublishSubscribeMapOutputWithContext(ctx context.Context) PublishSubscribeMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PublishSubscribeMapOutput)
}

type PublishSubscribeOutput struct{ *pulumi.OutputState }

func (PublishSubscribeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PublishSubscribe)(nil)).Elem()
}

func (o PublishSubscribeOutput) ToPublishSubscribeOutput() PublishSubscribeOutput {
	return o
}

func (o PublishSubscribeOutput) ToPublishSubscribeOutputWithContext(ctx context.Context) PublishSubscribeOutput {
	return o
}

// Database Publish and Publish relationship list. The elements inside can be deleted and added individually, but modification is not allowed.
func (o PublishSubscribeOutput) DatabaseTuples() PublishSubscribeDatabaseTupleArrayOutput {
	return o.ApplyT(func(v *PublishSubscribe) PublishSubscribeDatabaseTupleArrayOutput { return v.DatabaseTuples }).(PublishSubscribeDatabaseTupleArrayOutput)
}

// Whether to delete the subscriber database when deleting the Publish and Subscribe. `true` for deletes the subscribe database, `false` for does not delete the subscribe database. default is `false`.
func (o PublishSubscribeOutput) DeleteSubscribeDb() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *PublishSubscribe) pulumi.BoolPtrOutput { return v.DeleteSubscribeDb }).(pulumi.BoolPtrOutput)
}

// ID of the SQL Server instance which publish.
func (o PublishSubscribeOutput) PublishInstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v *PublishSubscribe) pulumi.StringOutput { return v.PublishInstanceId }).(pulumi.StringOutput)
}

// ID of PubSub.
func (o PublishSubscribeOutput) PublishSubscribeId() pulumi.IntOutput {
	return o.ApplyT(func(v *PublishSubscribe) pulumi.IntOutput { return v.PublishSubscribeId }).(pulumi.IntOutput)
}

// The name of the Publish and Subscribe. Default is `defaultName`.
func (o PublishSubscribeOutput) PublishSubscribeName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *PublishSubscribe) pulumi.StringPtrOutput { return v.PublishSubscribeName }).(pulumi.StringPtrOutput)
}

// ID of the SQL Server instance which subscribe.
func (o PublishSubscribeOutput) SubscribeInstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v *PublishSubscribe) pulumi.StringOutput { return v.SubscribeInstanceId }).(pulumi.StringOutput)
}

type PublishSubscribeArrayOutput struct{ *pulumi.OutputState }

func (PublishSubscribeArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PublishSubscribe)(nil)).Elem()
}

func (o PublishSubscribeArrayOutput) ToPublishSubscribeArrayOutput() PublishSubscribeArrayOutput {
	return o
}

func (o PublishSubscribeArrayOutput) ToPublishSubscribeArrayOutputWithContext(ctx context.Context) PublishSubscribeArrayOutput {
	return o
}

func (o PublishSubscribeArrayOutput) Index(i pulumi.IntInput) PublishSubscribeOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *PublishSubscribe {
		return vs[0].([]*PublishSubscribe)[vs[1].(int)]
	}).(PublishSubscribeOutput)
}

type PublishSubscribeMapOutput struct{ *pulumi.OutputState }

func (PublishSubscribeMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PublishSubscribe)(nil)).Elem()
}

func (o PublishSubscribeMapOutput) ToPublishSubscribeMapOutput() PublishSubscribeMapOutput {
	return o
}

func (o PublishSubscribeMapOutput) ToPublishSubscribeMapOutputWithContext(ctx context.Context) PublishSubscribeMapOutput {
	return o
}

func (o PublishSubscribeMapOutput) MapIndex(k pulumi.StringInput) PublishSubscribeOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *PublishSubscribe {
		return vs[0].(map[string]*PublishSubscribe)[vs[1].(string)]
	}).(PublishSubscribeOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PublishSubscribeInput)(nil)).Elem(), &PublishSubscribe{})
	pulumi.RegisterInputType(reflect.TypeOf((*PublishSubscribeArrayInput)(nil)).Elem(), PublishSubscribeArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PublishSubscribeMapInput)(nil)).Elem(), PublishSubscribeMap{})
	pulumi.RegisterOutputType(PublishSubscribeOutput{})
	pulumi.RegisterOutputType(PublishSubscribeArrayOutput{})
	pulumi.RegisterOutputType(PublishSubscribeMapOutput{})
}
