// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dayu

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
	case "tencentcloud:Dayu/cCHttpPolicy:CCHttpPolicy":
		r = &CCHttpPolicy{}
	case "tencentcloud:Dayu/cCHttpsPolicy:CCHttpsPolicy":
		r = &CCHttpsPolicy{}
	case "tencentcloud:Dayu/cCPolicyV2:CCPolicyV2":
		r = &CCPolicyV2{}
	case "tencentcloud:Dayu/dayuEipEip:DayuEipEip":
		r = &DayuEipEip{}
	case "tencentcloud:Dayu/ddosPolicy:DdosPolicy":
		r = &DdosPolicy{}
	case "tencentcloud:Dayu/ddosPolicyAttachment:DdosPolicyAttachment":
		r = &DdosPolicyAttachment{}
	case "tencentcloud:Dayu/ddosPolicyCase:DdosPolicyCase":
		r = &DdosPolicyCase{}
	case "tencentcloud:Dayu/ddosPolicyV2:DdosPolicyV2":
		r = &DdosPolicyV2{}
	case "tencentcloud:Dayu/l4Rule:L4Rule":
		r = &L4Rule{}
	case "tencentcloud:Dayu/l4RuleV2:L4RuleV2":
		r = &L4RuleV2{}
	case "tencentcloud:Dayu/l7Rule:L7Rule":
		r = &L7Rule{}
	case "tencentcloud:Dayu/l7RuleV2:L7RuleV2":
		r = &L7RuleV2{}
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
		"Dayu/cCHttpPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Dayu/cCHttpsPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Dayu/cCPolicyV2",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Dayu/dayuEipEip",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Dayu/ddosPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Dayu/ddosPolicyAttachment",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Dayu/ddosPolicyCase",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Dayu/ddosPolicyV2",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Dayu/l4Rule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Dayu/l4RuleV2",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Dayu/l7Rule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"tencentcloud",
		"Dayu/l7RuleV2",
		&module{version},
	)
}