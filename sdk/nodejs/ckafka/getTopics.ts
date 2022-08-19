// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to query detailed information of ckafka topic.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const foo = new tencentcloud.Ckafka.Topic("foo", {
 *     cleanUpPolicy: "delete",
 *     enableWhiteList: true,
 *     instanceId: "ckafka-f9ife4zz",
 *     ipWhiteLists: [
 *         "ip1",
 *         "ip2",
 *     ],
 *     maxMessageBytes: 0,
 *     note: "topic note",
 *     partitionNum: 1,
 *     replicaNum: 2,
 *     retention: 60000,
 *     segment: 3600000,
 *     syncReplicaMinNum: 1,
 *     topicName: "example",
 *     uncleanLeaderElectionEnable: false,
 * });
 * ```
 */
export function getTopics(args: GetTopicsArgs, opts?: pulumi.InvokeOptions): Promise<GetTopicsResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Ckafka/getTopics:getTopics", {
        "instanceId": args.instanceId,
        "resultOutputFile": args.resultOutputFile,
        "topicName": args.topicName,
    }, opts);
}

/**
 * A collection of arguments for invoking getTopics.
 */
export interface GetTopicsArgs {
    /**
     * Ckafka instance ID.
     */
    instanceId: string;
    /**
     * Used to store results.
     */
    resultOutputFile?: string;
    /**
     * Name of the CKafka topic. It must start with a letter, the rest can contain letters, numbers and dashes(-). The length range is from 1 to 64.
     */
    topicName?: string;
}

/**
 * A collection of values returned by getTopics.
 */
export interface GetTopicsResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly instanceId: string;
    /**
     * A list of instances. Each element contains the following attributes.
     */
    readonly instanceLists: outputs.Ckafka.GetTopicsInstanceList[];
    readonly resultOutputFile?: string;
    /**
     * Name of the CKafka topic.
     */
    readonly topicName?: string;
}

export function getTopicsOutput(args: GetTopicsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTopicsResult> {
    return pulumi.output(args).apply(a => getTopics(a, opts))
}

/**
 * A collection of arguments for invoking getTopics.
 */
export interface GetTopicsOutputArgs {
    /**
     * Ckafka instance ID.
     */
    instanceId: pulumi.Input<string>;
    /**
     * Used to store results.
     */
    resultOutputFile?: pulumi.Input<string>;
    /**
     * Name of the CKafka topic. It must start with a letter, the rest can contain letters, numbers and dashes(-). The length range is from 1 to 64.
     */
    topicName?: pulumi.Input<string>;
}