// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export class L7RuleV2 extends pulumi.CustomResource {
    /**
     * Get an existing L7RuleV2 resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: L7RuleV2State, opts?: pulumi.CustomResourceOptions): L7RuleV2 {
        return new L7RuleV2(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:Dayu/l7RuleV2:L7RuleV2';

    /**
     * Returns true if the given object is an instance of L7RuleV2.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is L7RuleV2 {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === L7RuleV2.__pulumiType;
    }

    /**
     * ID of the resource that the layer 7 rule works for.
     */
    public readonly resourceId!: pulumi.Output<string>;
    /**
     * Ip of the resource that the layer 7 rule works for.
     */
    public readonly resourceIp!: pulumi.Output<string>;
    /**
     * Type of the resource that the layer 7 rule works for, valid value is `bgpip`.
     */
    public readonly resourceType!: pulumi.Output<string>;
    /**
     * A list of layer 7 rules. Each element contains the following attributes:
     */
    public readonly rule!: pulumi.Output<outputs.Dayu.L7RuleV2Rule>;

    /**
     * Create a L7RuleV2 resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: L7RuleV2Args, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: L7RuleV2Args | L7RuleV2State, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as L7RuleV2State | undefined;
            resourceInputs["resourceId"] = state ? state.resourceId : undefined;
            resourceInputs["resourceIp"] = state ? state.resourceIp : undefined;
            resourceInputs["resourceType"] = state ? state.resourceType : undefined;
            resourceInputs["rule"] = state ? state.rule : undefined;
        } else {
            const args = argsOrState as L7RuleV2Args | undefined;
            if ((!args || args.resourceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceId'");
            }
            if ((!args || args.resourceIp === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceIp'");
            }
            if ((!args || args.resourceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceType'");
            }
            if ((!args || args.rule === undefined) && !opts.urn) {
                throw new Error("Missing required property 'rule'");
            }
            resourceInputs["resourceId"] = args ? args.resourceId : undefined;
            resourceInputs["resourceIp"] = args ? args.resourceIp : undefined;
            resourceInputs["resourceType"] = args ? args.resourceType : undefined;
            resourceInputs["rule"] = args ? args.rule : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(L7RuleV2.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering L7RuleV2 resources.
 */
export interface L7RuleV2State {
    /**
     * ID of the resource that the layer 7 rule works for.
     */
    resourceId?: pulumi.Input<string>;
    /**
     * Ip of the resource that the layer 7 rule works for.
     */
    resourceIp?: pulumi.Input<string>;
    /**
     * Type of the resource that the layer 7 rule works for, valid value is `bgpip`.
     */
    resourceType?: pulumi.Input<string>;
    /**
     * A list of layer 7 rules. Each element contains the following attributes:
     */
    rule?: pulumi.Input<inputs.Dayu.L7RuleV2Rule>;
}

/**
 * The set of arguments for constructing a L7RuleV2 resource.
 */
export interface L7RuleV2Args {
    /**
     * ID of the resource that the layer 7 rule works for.
     */
    resourceId: pulumi.Input<string>;
    /**
     * Ip of the resource that the layer 7 rule works for.
     */
    resourceIp: pulumi.Input<string>;
    /**
     * Type of the resource that the layer 7 rule works for, valid value is `bgpip`.
     */
    resourceType: pulumi.Input<string>;
    /**
     * A list of layer 7 rules. Each element contains the following attributes:
     */
    rule: pulumi.Input<inputs.Dayu.L7RuleV2Rule>;
}