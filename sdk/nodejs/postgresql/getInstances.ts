// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to query postgresql instances
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const name = pulumi.output(tencentcloud.Postgresql.getInstances({
 *     name: "test",
 * }));
 * const project = pulumi.output(tencentcloud.Postgresql.getInstances({
 *     projectId: 0,
 * }));
 * const id = pulumi.output(tencentcloud.Postgresql.getInstances({
 *     id: "postgres-h9t4fde1",
 * }));
 * ```
 */
export function getInstances(args?: GetInstancesArgs, opts?: pulumi.InvokeOptions): Promise<GetInstancesResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Postgresql/getInstances:getInstances", {
        "id": args.id,
        "name": args.name,
        "projectId": args.projectId,
        "resultOutputFile": args.resultOutputFile,
    }, opts);
}

/**
 * A collection of arguments for invoking getInstances.
 */
export interface GetInstancesArgs {
    /**
     * ID of the postgresql instance to be query.
     */
    id?: string;
    /**
     * Name of the postgresql instance to be query.
     */
    name?: string;
    /**
     * Project ID of the postgresql instance to be query.
     */
    projectId?: number;
    /**
     * Used to save results.
     */
    resultOutputFile?: string;
}

/**
 * A collection of values returned by getInstances.
 */
export interface GetInstancesResult {
    /**
     * ID of the postgresql instance.
     */
    readonly id?: string;
    /**
     * A list of postgresql instances. Each element contains the following attributes.
     */
    readonly instanceLists: outputs.Postgresql.GetInstancesInstanceList[];
    /**
     * Name of the postgresql instance.
     */
    readonly name?: string;
    /**
     * Project id, default value is 0.
     */
    readonly projectId?: number;
    readonly resultOutputFile?: string;
}

export function getInstancesOutput(args?: GetInstancesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetInstancesResult> {
    return pulumi.output(args).apply(a => getInstances(a, opts))
}

/**
 * A collection of arguments for invoking getInstances.
 */
export interface GetInstancesOutputArgs {
    /**
     * ID of the postgresql instance to be query.
     */
    id?: pulumi.Input<string>;
    /**
     * Name of the postgresql instance to be query.
     */
    name?: pulumi.Input<string>;
    /**
     * Project ID of the postgresql instance to be query.
     */
    projectId?: pulumi.Input<number>;
    /**
     * Used to save results.
     */
    resultOutputFile?: pulumi.Input<string>;
}