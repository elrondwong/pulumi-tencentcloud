// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export function templates(args?: TemplatesArgs, opts?: pulumi.InvokeOptions): Promise<TemplatesResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Protocol/templates:Templates", {
        "id": args.id,
        "name": args.name,
        "resultOutputFile": args.resultOutputFile,
    }, opts);
}

/**
 * A collection of arguments for invoking Templates.
 */
export interface TemplatesArgs {
    id?: string;
    name?: string;
    resultOutputFile?: string;
}

/**
 * A collection of values returned by Templates.
 */
export interface TemplatesResult {
    readonly id?: string;
    readonly name?: string;
    readonly resultOutputFile?: string;
    readonly templateLists: outputs.Protocol.TemplatesTemplateList[];
}

export function templatesOutput(args?: TemplatesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<TemplatesResult> {
    return pulumi.output(args).apply(a => templates(a, opts))
}

/**
 * A collection of arguments for invoking Templates.
 */
export interface TemplatesOutputArgs {
    id?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    resultOutputFile?: pulumi.Input<string>;
}