// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package tdmq

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-tencentcloud/sdk/go/tencentcloud"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "tencentcloud:Tdmq/instance:Instance":
		r = &Instance{}
	case "tencentcloud:Tdmq/namespace:Namespace":
		r = &Namespace{}
	case "tencentcloud:Tdmq/namespaceRoleAttachment:NamespaceRoleAttachment":
		r = &NamespaceRoleAttachment{}
	case "tencentcloud:Tdmq/role:Role":
		r = &Role{}
	case "tencentcloud:Tdmq/topic:Topic":
		r = &Topic{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := tencentcloud.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Tdmq/instance",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Tdmq/namespace",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Tdmq/namespaceRoleAttachment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Tdmq/role",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Tdmq/topic",
		&module{version},
	)
}