// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./gateway";
export * from "./gatewaySnat";
export * from "./gatewaySnats";
export * from "./gateways";

// Import resources to register:
import { Gateway } from "./gateway";
import { GatewaySnat } from "./gatewaySnat";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "tencentcloud:Nat/gateway:Gateway":
                return new Gateway(name, <any>undefined, { urn })
            case "tencentcloud:Nat/gatewaySnat:GatewaySnat":
                return new GatewaySnat(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("tencentcloud", "Nat/gateway", _module)
pulumi.runtime.registerResourceModule("tencentcloud", "Nat/gatewaySnat", _module)