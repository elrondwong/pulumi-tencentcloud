// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kms

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type KmsKey struct {
	pulumi.CustomResourceState

	// Name of CMK. The name can only contain English letters, numbers, underscore and hyphen '-'. The first character must be
	// a letter or number.
	Alias pulumi.StringOutput `pulumi:"alias"`
	// Description of CMK. The maximum is 1024 bytes.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Specify whether to archive key. Default value is `false`. This field is conflict with `is_enabled`, valid when key_state
	// is `Enabled`, `Disabled`, `Archived`.
	IsArchived pulumi.BoolPtrOutput `pulumi:"isArchived"`
	// Specify whether to enable key. Default value is `false`. This field is conflict with `is_archived`, valid when key_state
	// is `Enabled`, `Disabled`, `Archived`.
	IsEnabled pulumi.BoolPtrOutput `pulumi:"isEnabled"`
	// Specify whether to enable key rotation, valid when key_usage is `ENCRYPT_DECRYPT`. Default value is `false`.
	KeyRotationEnabled pulumi.BoolPtrOutput `pulumi:"keyRotationEnabled"`
	// State of CMK.
	KeyState pulumi.StringOutput `pulumi:"keyState"`
	// Usage of CMK. Available values include `ENCRYPT_DECRYPT`, `ASYMMETRIC_DECRYPT_RSA_2048`, `ASYMMETRIC_DECRYPT_SM2`,
	// `ASYMMETRIC_SIGN_VERIFY_SM2`, `ASYMMETRIC_SIGN_VERIFY_RSA_2048`, `ASYMMETRIC_SIGN_VERIFY_ECC`. Default value is
	// `ENCRYPT_DECRYPT`.
	KeyUsage pulumi.StringPtrOutput `pulumi:"keyUsage"`
	// Duration in days after which the key is deleted after destruction of the resource, must be between 7 and 30 days.
	// Defaults to 7 days.
	PendingDeleteWindowInDays pulumi.IntPtrOutput `pulumi:"pendingDeleteWindowInDays"`
	// Tags of CMK.
	Tags pulumi.MapOutput `pulumi:"tags"`
}

// NewKmsKey registers a new resource with the given unique name, arguments, and options.
func NewKmsKey(ctx *pulumi.Context,
	name string, args *KmsKeyArgs, opts ...pulumi.ResourceOption) (*KmsKey, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Alias == nil {
		return nil, errors.New("invalid value for required argument 'Alias'")
	}
	var resource KmsKey
	err := ctx.RegisterResource("tencentcloud:Kms/kmsKey:KmsKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetKmsKey gets an existing KmsKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetKmsKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *KmsKeyState, opts ...pulumi.ResourceOption) (*KmsKey, error) {
	var resource KmsKey
	err := ctx.ReadResource("tencentcloud:Kms/kmsKey:KmsKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering KmsKey resources.
type kmsKeyState struct {
	// Name of CMK. The name can only contain English letters, numbers, underscore and hyphen '-'. The first character must be
	// a letter or number.
	Alias *string `pulumi:"alias"`
	// Description of CMK. The maximum is 1024 bytes.
	Description *string `pulumi:"description"`
	// Specify whether to archive key. Default value is `false`. This field is conflict with `is_enabled`, valid when key_state
	// is `Enabled`, `Disabled`, `Archived`.
	IsArchived *bool `pulumi:"isArchived"`
	// Specify whether to enable key. Default value is `false`. This field is conflict with `is_archived`, valid when key_state
	// is `Enabled`, `Disabled`, `Archived`.
	IsEnabled *bool `pulumi:"isEnabled"`
	// Specify whether to enable key rotation, valid when key_usage is `ENCRYPT_DECRYPT`. Default value is `false`.
	KeyRotationEnabled *bool `pulumi:"keyRotationEnabled"`
	// State of CMK.
	KeyState *string `pulumi:"keyState"`
	// Usage of CMK. Available values include `ENCRYPT_DECRYPT`, `ASYMMETRIC_DECRYPT_RSA_2048`, `ASYMMETRIC_DECRYPT_SM2`,
	// `ASYMMETRIC_SIGN_VERIFY_SM2`, `ASYMMETRIC_SIGN_VERIFY_RSA_2048`, `ASYMMETRIC_SIGN_VERIFY_ECC`. Default value is
	// `ENCRYPT_DECRYPT`.
	KeyUsage *string `pulumi:"keyUsage"`
	// Duration in days after which the key is deleted after destruction of the resource, must be between 7 and 30 days.
	// Defaults to 7 days.
	PendingDeleteWindowInDays *int `pulumi:"pendingDeleteWindowInDays"`
	// Tags of CMK.
	Tags map[string]interface{} `pulumi:"tags"`
}

type KmsKeyState struct {
	// Name of CMK. The name can only contain English letters, numbers, underscore and hyphen '-'. The first character must be
	// a letter or number.
	Alias pulumi.StringPtrInput
	// Description of CMK. The maximum is 1024 bytes.
	Description pulumi.StringPtrInput
	// Specify whether to archive key. Default value is `false`. This field is conflict with `is_enabled`, valid when key_state
	// is `Enabled`, `Disabled`, `Archived`.
	IsArchived pulumi.BoolPtrInput
	// Specify whether to enable key. Default value is `false`. This field is conflict with `is_archived`, valid when key_state
	// is `Enabled`, `Disabled`, `Archived`.
	IsEnabled pulumi.BoolPtrInput
	// Specify whether to enable key rotation, valid when key_usage is `ENCRYPT_DECRYPT`. Default value is `false`.
	KeyRotationEnabled pulumi.BoolPtrInput
	// State of CMK.
	KeyState pulumi.StringPtrInput
	// Usage of CMK. Available values include `ENCRYPT_DECRYPT`, `ASYMMETRIC_DECRYPT_RSA_2048`, `ASYMMETRIC_DECRYPT_SM2`,
	// `ASYMMETRIC_SIGN_VERIFY_SM2`, `ASYMMETRIC_SIGN_VERIFY_RSA_2048`, `ASYMMETRIC_SIGN_VERIFY_ECC`. Default value is
	// `ENCRYPT_DECRYPT`.
	KeyUsage pulumi.StringPtrInput
	// Duration in days after which the key is deleted after destruction of the resource, must be between 7 and 30 days.
	// Defaults to 7 days.
	PendingDeleteWindowInDays pulumi.IntPtrInput
	// Tags of CMK.
	Tags pulumi.MapInput
}

func (KmsKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*kmsKeyState)(nil)).Elem()
}

type kmsKeyArgs struct {
	// Name of CMK. The name can only contain English letters, numbers, underscore and hyphen '-'. The first character must be
	// a letter or number.
	Alias string `pulumi:"alias"`
	// Description of CMK. The maximum is 1024 bytes.
	Description *string `pulumi:"description"`
	// Specify whether to archive key. Default value is `false`. This field is conflict with `is_enabled`, valid when key_state
	// is `Enabled`, `Disabled`, `Archived`.
	IsArchived *bool `pulumi:"isArchived"`
	// Specify whether to enable key. Default value is `false`. This field is conflict with `is_archived`, valid when key_state
	// is `Enabled`, `Disabled`, `Archived`.
	IsEnabled *bool `pulumi:"isEnabled"`
	// Specify whether to enable key rotation, valid when key_usage is `ENCRYPT_DECRYPT`. Default value is `false`.
	KeyRotationEnabled *bool `pulumi:"keyRotationEnabled"`
	// Usage of CMK. Available values include `ENCRYPT_DECRYPT`, `ASYMMETRIC_DECRYPT_RSA_2048`, `ASYMMETRIC_DECRYPT_SM2`,
	// `ASYMMETRIC_SIGN_VERIFY_SM2`, `ASYMMETRIC_SIGN_VERIFY_RSA_2048`, `ASYMMETRIC_SIGN_VERIFY_ECC`. Default value is
	// `ENCRYPT_DECRYPT`.
	KeyUsage *string `pulumi:"keyUsage"`
	// Duration in days after which the key is deleted after destruction of the resource, must be between 7 and 30 days.
	// Defaults to 7 days.
	PendingDeleteWindowInDays *int `pulumi:"pendingDeleteWindowInDays"`
	// Tags of CMK.
	Tags map[string]interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a KmsKey resource.
type KmsKeyArgs struct {
	// Name of CMK. The name can only contain English letters, numbers, underscore and hyphen '-'. The first character must be
	// a letter or number.
	Alias pulumi.StringInput
	// Description of CMK. The maximum is 1024 bytes.
	Description pulumi.StringPtrInput
	// Specify whether to archive key. Default value is `false`. This field is conflict with `is_enabled`, valid when key_state
	// is `Enabled`, `Disabled`, `Archived`.
	IsArchived pulumi.BoolPtrInput
	// Specify whether to enable key. Default value is `false`. This field is conflict with `is_archived`, valid when key_state
	// is `Enabled`, `Disabled`, `Archived`.
	IsEnabled pulumi.BoolPtrInput
	// Specify whether to enable key rotation, valid when key_usage is `ENCRYPT_DECRYPT`. Default value is `false`.
	KeyRotationEnabled pulumi.BoolPtrInput
	// Usage of CMK. Available values include `ENCRYPT_DECRYPT`, `ASYMMETRIC_DECRYPT_RSA_2048`, `ASYMMETRIC_DECRYPT_SM2`,
	// `ASYMMETRIC_SIGN_VERIFY_SM2`, `ASYMMETRIC_SIGN_VERIFY_RSA_2048`, `ASYMMETRIC_SIGN_VERIFY_ECC`. Default value is
	// `ENCRYPT_DECRYPT`.
	KeyUsage pulumi.StringPtrInput
	// Duration in days after which the key is deleted after destruction of the resource, must be between 7 and 30 days.
	// Defaults to 7 days.
	PendingDeleteWindowInDays pulumi.IntPtrInput
	// Tags of CMK.
	Tags pulumi.MapInput
}

func (KmsKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*kmsKeyArgs)(nil)).Elem()
}

type KmsKeyInput interface {
	pulumi.Input

	ToKmsKeyOutput() KmsKeyOutput
	ToKmsKeyOutputWithContext(ctx context.Context) KmsKeyOutput
}

func (*KmsKey) ElementType() reflect.Type {
	return reflect.TypeOf((**KmsKey)(nil)).Elem()
}

func (i *KmsKey) ToKmsKeyOutput() KmsKeyOutput {
	return i.ToKmsKeyOutputWithContext(context.Background())
}

func (i *KmsKey) ToKmsKeyOutputWithContext(ctx context.Context) KmsKeyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KmsKeyOutput)
}

// KmsKeyArrayInput is an input type that accepts KmsKeyArray and KmsKeyArrayOutput values.
// You can construct a concrete instance of `KmsKeyArrayInput` via:
//
//          KmsKeyArray{ KmsKeyArgs{...} }
type KmsKeyArrayInput interface {
	pulumi.Input

	ToKmsKeyArrayOutput() KmsKeyArrayOutput
	ToKmsKeyArrayOutputWithContext(context.Context) KmsKeyArrayOutput
}

type KmsKeyArray []KmsKeyInput

func (KmsKeyArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*KmsKey)(nil)).Elem()
}

func (i KmsKeyArray) ToKmsKeyArrayOutput() KmsKeyArrayOutput {
	return i.ToKmsKeyArrayOutputWithContext(context.Background())
}

func (i KmsKeyArray) ToKmsKeyArrayOutputWithContext(ctx context.Context) KmsKeyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KmsKeyArrayOutput)
}

// KmsKeyMapInput is an input type that accepts KmsKeyMap and KmsKeyMapOutput values.
// You can construct a concrete instance of `KmsKeyMapInput` via:
//
//          KmsKeyMap{ "key": KmsKeyArgs{...} }
type KmsKeyMapInput interface {
	pulumi.Input

	ToKmsKeyMapOutput() KmsKeyMapOutput
	ToKmsKeyMapOutputWithContext(context.Context) KmsKeyMapOutput
}

type KmsKeyMap map[string]KmsKeyInput

func (KmsKeyMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*KmsKey)(nil)).Elem()
}

func (i KmsKeyMap) ToKmsKeyMapOutput() KmsKeyMapOutput {
	return i.ToKmsKeyMapOutputWithContext(context.Background())
}

func (i KmsKeyMap) ToKmsKeyMapOutputWithContext(ctx context.Context) KmsKeyMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KmsKeyMapOutput)
}

type KmsKeyOutput struct{ *pulumi.OutputState }

func (KmsKeyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**KmsKey)(nil)).Elem()
}

func (o KmsKeyOutput) ToKmsKeyOutput() KmsKeyOutput {
	return o
}

func (o KmsKeyOutput) ToKmsKeyOutputWithContext(ctx context.Context) KmsKeyOutput {
	return o
}

// Name of CMK. The name can only contain English letters, numbers, underscore and hyphen '-'. The first character must be
// a letter or number.
func (o KmsKeyOutput) Alias() pulumi.StringOutput {
	return o.ApplyT(func(v *KmsKey) pulumi.StringOutput { return v.Alias }).(pulumi.StringOutput)
}

// Description of CMK. The maximum is 1024 bytes.
func (o KmsKeyOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *KmsKey) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Specify whether to archive key. Default value is `false`. This field is conflict with `is_enabled`, valid when key_state
// is `Enabled`, `Disabled`, `Archived`.
func (o KmsKeyOutput) IsArchived() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *KmsKey) pulumi.BoolPtrOutput { return v.IsArchived }).(pulumi.BoolPtrOutput)
}

// Specify whether to enable key. Default value is `false`. This field is conflict with `is_archived`, valid when key_state
// is `Enabled`, `Disabled`, `Archived`.
func (o KmsKeyOutput) IsEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *KmsKey) pulumi.BoolPtrOutput { return v.IsEnabled }).(pulumi.BoolPtrOutput)
}

// Specify whether to enable key rotation, valid when key_usage is `ENCRYPT_DECRYPT`. Default value is `false`.
func (o KmsKeyOutput) KeyRotationEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *KmsKey) pulumi.BoolPtrOutput { return v.KeyRotationEnabled }).(pulumi.BoolPtrOutput)
}

// State of CMK.
func (o KmsKeyOutput) KeyState() pulumi.StringOutput {
	return o.ApplyT(func(v *KmsKey) pulumi.StringOutput { return v.KeyState }).(pulumi.StringOutput)
}

// Usage of CMK. Available values include `ENCRYPT_DECRYPT`, `ASYMMETRIC_DECRYPT_RSA_2048`, `ASYMMETRIC_DECRYPT_SM2`,
// `ASYMMETRIC_SIGN_VERIFY_SM2`, `ASYMMETRIC_SIGN_VERIFY_RSA_2048`, `ASYMMETRIC_SIGN_VERIFY_ECC`. Default value is
// `ENCRYPT_DECRYPT`.
func (o KmsKeyOutput) KeyUsage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *KmsKey) pulumi.StringPtrOutput { return v.KeyUsage }).(pulumi.StringPtrOutput)
}

// Duration in days after which the key is deleted after destruction of the resource, must be between 7 and 30 days.
// Defaults to 7 days.
func (o KmsKeyOutput) PendingDeleteWindowInDays() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *KmsKey) pulumi.IntPtrOutput { return v.PendingDeleteWindowInDays }).(pulumi.IntPtrOutput)
}

// Tags of CMK.
func (o KmsKeyOutput) Tags() pulumi.MapOutput {
	return o.ApplyT(func(v *KmsKey) pulumi.MapOutput { return v.Tags }).(pulumi.MapOutput)
}

type KmsKeyArrayOutput struct{ *pulumi.OutputState }

func (KmsKeyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*KmsKey)(nil)).Elem()
}

func (o KmsKeyArrayOutput) ToKmsKeyArrayOutput() KmsKeyArrayOutput {
	return o
}

func (o KmsKeyArrayOutput) ToKmsKeyArrayOutputWithContext(ctx context.Context) KmsKeyArrayOutput {
	return o
}

func (o KmsKeyArrayOutput) Index(i pulumi.IntInput) KmsKeyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *KmsKey {
		return vs[0].([]*KmsKey)[vs[1].(int)]
	}).(KmsKeyOutput)
}

type KmsKeyMapOutput struct{ *pulumi.OutputState }

func (KmsKeyMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*KmsKey)(nil)).Elem()
}

func (o KmsKeyMapOutput) ToKmsKeyMapOutput() KmsKeyMapOutput {
	return o
}

func (o KmsKeyMapOutput) ToKmsKeyMapOutputWithContext(ctx context.Context) KmsKeyMapOutput {
	return o
}

func (o KmsKeyMapOutput) MapIndex(k pulumi.StringInput) KmsKeyOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *KmsKey {
		return vs[0].(map[string]*KmsKey)[vs[1].(string)]
	}).(KmsKeyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*KmsKeyInput)(nil)).Elem(), &KmsKey{})
	pulumi.RegisterInputType(reflect.TypeOf((*KmsKeyArrayInput)(nil)).Elem(), KmsKeyArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*KmsKeyMapInput)(nil)).Elem(), KmsKeyMap{})
	pulumi.RegisterOutputType(KmsKeyOutput{})
	pulumi.RegisterOutputType(KmsKeyArrayOutput{})
	pulumi.RegisterOutputType(KmsKeyMapOutput{})
}