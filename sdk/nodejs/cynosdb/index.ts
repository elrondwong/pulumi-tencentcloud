// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./cluster";
export * from "./getClusters";
export * from "./getInstances";
export * from "./readonlyInstance";

// Import resources to register:
import { Cluster } from "./cluster";
import { ReadonlyInstance } from "./readonlyInstance";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "tencentcloud:Cynosdb/cluster:Cluster":
                return new Cluster(name, <any>undefined, { urn })
            case "tencentcloud:Cynosdb/readonlyInstance:ReadonlyInstance":
                return new ReadonlyInstance(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("tencentcloud", "Cynosdb/cluster", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Cynosdb/readonlyInstance", _module)
