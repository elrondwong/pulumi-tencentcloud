// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to query dayu layer 4 rules
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const nameTest = tencentcloud.Dayu.getL4Rules({
 *     resourceType: tencentcloud_dayu_l4_rule.test_rule.resource_type,
 *     resourceId: tencentcloud_dayu_l4_rule.test_rule.resource_id,
 *     name: tencentcloud_dayu_l4_rule.test_rule.name,
 * });
 * const idTest = tencentcloud.Dayu.getL4Rules({
 *     resourceType: tencentcloud_dayu_l4_rule.test_rule.resource_type,
 *     resourceId: tencentcloud_dayu_l4_rule.test_rule.resource_id,
 *     ruleId: tencentcloud_dayu_l4_rule.test_rule.rule_id,
 * });
 * ```
 */
export function getL4Rules(args: GetL4RulesArgs, opts?: pulumi.InvokeOptions): Promise<GetL4RulesResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Dayu/getL4Rules:getL4Rules", {
        "name": args.name,
        "resourceId": args.resourceId,
        "resourceType": args.resourceType,
        "resultOutputFile": args.resultOutputFile,
        "ruleId": args.ruleId,
    }, opts);
}

/**
 * A collection of arguments for invoking getL4Rules.
 */
export interface GetL4RulesArgs {
    /**
     * Name of the layer 4 rule to be queried.
     */
    name?: string;
    /**
     * Id of the resource that the layer 4 rule works for.
     */
    resourceId: string;
    /**
     * Type of the resource that the layer 4 rule works for, valid values are `bgpip`, `bgp`, `bgp-multip` and `net`.
     */
    resourceType: string;
    /**
     * Used to save results.
     */
    resultOutputFile?: string;
    /**
     * Id of the layer 4 rule to be queried.
     */
    ruleId?: string;
}

/**
 * A collection of values returned by getL4Rules.
 */
export interface GetL4RulesResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * A list of layer 4 rules. Each element contains the following attributes:
     */
    readonly lists: outputs.Dayu.GetL4RulesList[];
    /**
     * Name of the rule.
     */
    readonly name?: string;
    readonly resourceId: string;
    readonly resourceType: string;
    readonly resultOutputFile?: string;
    /**
     * ID of the 4 layer rule.
     */
    readonly ruleId?: string;
}

export function getL4RulesOutput(args: GetL4RulesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetL4RulesResult> {
    return pulumi.output(args).apply(a => getL4Rules(a, opts))
}

/**
 * A collection of arguments for invoking getL4Rules.
 */
export interface GetL4RulesOutputArgs {
    /**
     * Name of the layer 4 rule to be queried.
     */
    name?: pulumi.Input<string>;
    /**
     * Id of the resource that the layer 4 rule works for.
     */
    resourceId: pulumi.Input<string>;
    /**
     * Type of the resource that the layer 4 rule works for, valid values are `bgpip`, `bgp`, `bgp-multip` and `net`.
     */
    resourceType: pulumi.Input<string>;
    /**
     * Used to save results.
     */
    resultOutputFile?: pulumi.Input<string>;
    /**
     * Id of the layer 4 rule to be queried.
     */
    ruleId?: pulumi.Input<string>;
}