// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to query detailed information of CBS storages.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const storages = pulumi.output(tencentcloud.Cbs.getStorages({
 *     resultOutputFile: "mytestpath",
 *     storageId: "disk-kdt0sq6m",
 * }));
 * ```
 *
 * The following snippet shows the new supported query params
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const whatsNew = pulumi.output(tencentcloud.Cbs.getStorages({
 *     chargeTypes: [
 *         "POSTPAID_BY_HOUR",
 *         "PREPAID",
 *     ],
 *     instanceIps: ["10.0.0.2"],
 *     instanceNames: ["my-instance"],
 *     portable: true,
 *     storageStates: ["ATTACHED"],
 *     tagKeys: ["foo"],
 *     tagValues: [
 *         "bar",
 *         "baz",
 *     ],
 * }));
 * ```
 */
export function getStorages(args?: GetStoragesArgs, opts?: pulumi.InvokeOptions): Promise<GetStoragesResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Cbs/getStorages:getStorages", {
        "availabilityZone": args.availabilityZone,
        "chargeTypes": args.chargeTypes,
        "instanceIps": args.instanceIps,
        "instanceNames": args.instanceNames,
        "portable": args.portable,
        "projectId": args.projectId,
        "resultOutputFile": args.resultOutputFile,
        "storageId": args.storageId,
        "storageName": args.storageName,
        "storageStates": args.storageStates,
        "storageType": args.storageType,
        "storageUsage": args.storageUsage,
        "tagKeys": args.tagKeys,
        "tagValues": args.tagValues,
    }, opts);
}

/**
 * A collection of arguments for invoking getStorages.
 */
export interface GetStoragesArgs {
    /**
     * The available zone that the CBS instance locates at.
     */
    availabilityZone?: string;
    /**
     * List filter by disk charge type (`POSTPAID_BY_HOUR` | `PREPAID`).
     */
    chargeTypes?: string[];
    /**
     * List filter by attached instance public or private IPs.
     */
    instanceIps?: string[];
    /**
     * List filter by attached instance name.
     */
    instanceNames?: string[];
    /**
     * Filter by whether the disk is portable (Boolean `true` or `false`).
     */
    portable?: boolean;
    /**
     * ID of the project with which the CBS is associated.
     */
    projectId?: number;
    /**
     * Used to save results.
     */
    resultOutputFile?: string;
    /**
     * ID of the CBS to be queried.
     */
    storageId?: string;
    /**
     * Name of the CBS to be queried.
     */
    storageName?: string;
    /**
     * List filter by disk state (`UNATTACHED` | `ATTACHING` | `ATTACHED` | `DETACHING` | `EXPANDING` | `ROLLBACKING` | `TORECYCLE`).
     */
    storageStates?: string[];
    /**
     * Filter by cloud disk media type (`CLOUD_BASIC`: HDD cloud disk | `CLOUD_PREMIUM`: Premium Cloud Storage | `CLOUD_SSD`: SSD cloud disk).
     */
    storageType?: string;
    /**
     * Filter by cloud disk type (`SYSTEM_DISK`: system disk | `DATA_DISK`: data disk).
     */
    storageUsage?: string;
    /**
     * List filter by tag keys.
     */
    tagKeys?: string[];
    /**
     * List filter by tag values.
     */
    tagValues?: string[];
}

/**
 * A collection of values returned by getStorages.
 */
export interface GetStoragesResult {
    /**
     * The zone of CBS.
     */
    readonly availabilityZone?: string;
    /**
     * Pay type of the CBS instance.
     */
    readonly chargeTypes?: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly instanceIps?: string[];
    readonly instanceNames?: string[];
    readonly portable?: boolean;
    /**
     * ID of the project.
     */
    readonly projectId?: number;
    readonly resultOutputFile?: string;
    /**
     * ID of CBS.
     */
    readonly storageId?: string;
    /**
     * A list of storage. Each element contains the following attributes:
     */
    readonly storageLists: outputs.Cbs.GetStoragesStorageList[];
    /**
     * Name of CBS.
     */
    readonly storageName?: string;
    readonly storageStates?: string[];
    /**
     * Types of storage medium.
     */
    readonly storageType?: string;
    /**
     * Types of CBS.
     */
    readonly storageUsage?: string;
    readonly tagKeys?: string[];
    readonly tagValues?: string[];
}

export function getStoragesOutput(args?: GetStoragesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetStoragesResult> {
    return pulumi.output(args).apply(a => getStorages(a, opts))
}

/**
 * A collection of arguments for invoking getStorages.
 */
export interface GetStoragesOutputArgs {
    /**
     * The available zone that the CBS instance locates at.
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * List filter by disk charge type (`POSTPAID_BY_HOUR` | `PREPAID`).
     */
    chargeTypes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List filter by attached instance public or private IPs.
     */
    instanceIps?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List filter by attached instance name.
     */
    instanceNames?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Filter by whether the disk is portable (Boolean `true` or `false`).
     */
    portable?: pulumi.Input<boolean>;
    /**
     * ID of the project with which the CBS is associated.
     */
    projectId?: pulumi.Input<number>;
    /**
     * Used to save results.
     */
    resultOutputFile?: pulumi.Input<string>;
    /**
     * ID of the CBS to be queried.
     */
    storageId?: pulumi.Input<string>;
    /**
     * Name of the CBS to be queried.
     */
    storageName?: pulumi.Input<string>;
    /**
     * List filter by disk state (`UNATTACHED` | `ATTACHING` | `ATTACHED` | `DETACHING` | `EXPANDING` | `ROLLBACKING` | `TORECYCLE`).
     */
    storageStates?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Filter by cloud disk media type (`CLOUD_BASIC`: HDD cloud disk | `CLOUD_PREMIUM`: Premium Cloud Storage | `CLOUD_SSD`: SSD cloud disk).
     */
    storageType?: pulumi.Input<string>;
    /**
     * Filter by cloud disk type (`SYSTEM_DISK`: system disk | `DATA_DISK`: data disk).
     */
    storageUsage?: pulumi.Input<string>;
    /**
     * List filter by tag keys.
     */
    tagKeys?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List filter by tag values.
     */
    tagValues?: pulumi.Input<pulumi.Input<string>[]>;
}