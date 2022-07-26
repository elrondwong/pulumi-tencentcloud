// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cls

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
	case "tencentcloud:Cls/config:Config":
		r = &Config{}
	case "tencentcloud:Cls/configAttachment:ConfigAttachment":
		r = &ConfigAttachment{}
	case "tencentcloud:Cls/configExtra:ConfigExtra":
		r = &ConfigExtra{}
	case "tencentcloud:Cls/cosShipper:CosShipper":
		r = &CosShipper{}
	case "tencentcloud:Cls/logset:Logset":
		r = &Logset{}
	case "tencentcloud:Cls/machineGroup:MachineGroup":
		r = &MachineGroup{}
	case "tencentcloud:Cls/topic:Topic":
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
		"Cls/config",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Cls/configAttachment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Cls/configExtra",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Cls/cosShipper",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Cls/logset",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Cls/machineGroup",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Cls/topic",
		&module{version},
	)
}