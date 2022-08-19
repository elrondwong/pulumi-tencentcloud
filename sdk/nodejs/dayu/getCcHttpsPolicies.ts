// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to query dayu CC https policies
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const nameTest = tencentcloud.Dayu.getCcHttpsPolicies({
 *     resourceType: tencentcloud_dayu_cc_https_policy.test_policy.resource_type,
 *     resourceId: tencentcloud_dayu_cc_https_policy.test_policy.resource_id,
 *     name: tencentcloud_dayu_cc_https_policy.test_policy.name,
 * });
 * const idTest = tencentcloud.Dayu.getCcHttpsPolicies({
 *     resourceType: tencentcloud_dayu_cc_https_policy.test_policy.resource_type,
 *     resourceId: tencentcloud_dayu_cc_https_policy.test_policy.resource_id,
 *     policyId: tencentcloud_dayu_cc_https_policy.test_policy.policy_id,
 * });
 * ```
 */
export function getCcHttpsPolicies(args: GetCcHttpsPoliciesArgs, opts?: pulumi.InvokeOptions): Promise<GetCcHttpsPoliciesResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Dayu/getCcHttpsPolicies:getCcHttpsPolicies", {
        "name": args.name,
        "policyId": args.policyId,
        "resourceId": args.resourceId,
        "resourceType": args.resourceType,
        "resultOutputFile": args.resultOutputFile,
    }, opts);
}

/**
 * A collection of arguments for invoking getCcHttpsPolicies.
 */
export interface GetCcHttpsPoliciesArgs {
    /**
     * Name of the CC https policy to be queried.
     */
    name?: string;
    /**
     * Id of the CC https policy to be queried.
     */
    policyId?: string;
    /**
     * Id of the resource that the CC https policy works for.
     */
    resourceId: string;
    /**
     * Type of the resource that the CC https policy works for, valid value is `bgpip`.
     */
    resourceType: string;
    /**
     * Used to save results.
     */
    resultOutputFile?: string;
}

/**
 * A collection of values returned by getCcHttpsPolicies.
 */
export interface GetCcHttpsPoliciesResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * A list of CC https policies. Each element contains the following attributes:
     */
    readonly lists: outputs.Dayu.GetCcHttpsPoliciesList[];
    /**
     * Name of the CC self-define https policy.
     */
    readonly name?: string;
    /**
     * Id of the CC self-define https policy.
     */
    readonly policyId?: string;
    /**
     * ID of the resource that the CC self-define https policy works for.
     */
    readonly resourceId: string;
    /**
     * Type of the resource that the CC self-define https policy works for.
     */
    readonly resourceType: string;
    readonly resultOutputFile?: string;
}

export function getCcHttpsPoliciesOutput(args: GetCcHttpsPoliciesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCcHttpsPoliciesResult> {
    return pulumi.output(args).apply(a => getCcHttpsPolicies(a, opts))
}

/**
 * A collection of arguments for invoking getCcHttpsPolicies.
 */
export interface GetCcHttpsPoliciesOutputArgs {
    /**
     * Name of the CC https policy to be queried.
     */
    name?: pulumi.Input<string>;
    /**
     * Id of the CC https policy to be queried.
     */
    policyId?: pulumi.Input<string>;
    /**
     * Id of the resource that the CC https policy works for.
     */
    resourceId: pulumi.Input<string>;
    /**
     * Type of the resource that the CC https policy works for, valid value is `bgpip`.
     */
    resourceType: pulumi.Input<string>;
    /**
     * Used to save results.
     */
    resultOutputFile?: pulumi.Input<string>;
}