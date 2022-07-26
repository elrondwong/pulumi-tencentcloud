// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./instance";
export * from "./instances";
export * from "./shardingInstance";
export * from "./standbyInstance";
export * from "./zoneConfig";

// Import resources to register:
import { Instance } from "./instance";
import { ShardingInstance } from "./shardingInstance";
import { StandbyInstance } from "./standbyInstance";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "tencentcloud:Mongodb/instance:Instance":
                return new Instance(name, <any>undefined, { urn })
            case "tencentcloud:Mongodb/shardingInstance:ShardingInstance":
                return new ShardingInstance(name, <any>undefined, { urn })
            case "tencentcloud:Mongodb/standbyInstance:StandbyInstance":
                return new StandbyInstance(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("tencentcloud", "Mongodb/instance", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Mongodb/shardingInstance", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Mongodb/standbyInstance", _module)