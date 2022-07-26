// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export function policyConditions(args?: PolicyConditionsArgs, opts?: pulumi.InvokeOptions): Promise<PolicyConditionsResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Monitor/policyConditions:PolicyConditions", {
        "name": args.name,
        "resultOutputFile": args.resultOutputFile,
    }, opts);
}

/**
 * A collection of arguments for invoking PolicyConditions.
 */
export interface PolicyConditionsArgs {
    name?: string;
    resultOutputFile?: string;
}

/**
 * A collection of values returned by PolicyConditions.
 */
export interface PolicyConditionsResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly lists: outputs.Monitor.PolicyConditionsList[];
    readonly name?: string;
    readonly resultOutputFile?: string;
}

export function policyConditionsOutput(args?: PolicyConditionsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<PolicyConditionsResult> {
    return pulumi.output(args).apply(a => policyConditions(a, opts))
}

/**
 * A collection of arguments for invoking PolicyConditions.
 */
export interface PolicyConditionsOutputArgs {
    name?: pulumi.Input<string>;
    resultOutputFile?: pulumi.Input<string>;
}