// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Provides a resource to create a lighthouse instance.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const lighthouse = new tencentcloud.Lighthouse.Instance("lighthouse", {
 *     blueprintId: "lhbp-f1lkcd41",
 *     bundleId: "bundle2022_gen_01",
 *     containers: [
 *         {
 *             command: "ls -l",
 *             containerImage: "ccr.ccs.tencentyun.com/qcloud/nginx",
 *             containerName: "nginx",
 *             envs: [
 *                 {
 *                     key: "key",
 *                     value: "value",
 *                 },
 *                 {
 *                     key: "key2",
 *                     value: "value2",
 *                 },
 *             ],
 *             publishPorts: [
 *                 {
 *                     containerPort: 80,
 *                     hostPort: 80,
 *                     ip: "127.0.0.1",
 *                     protocol: "tcp",
 *                 },
 *                 {
 *                     containerPort: 36000,
 *                     hostPort: 36000,
 *                     ip: "127.0.0.1",
 *                     protocol: "tcp",
 *                 },
 *             ],
 *             volumes: [
 *                 {
 *                     containerPath: "/data",
 *                     hostPath: "/tmp",
 *                 },
 *                 {
 *                     containerPath: "/var",
 *                     hostPath: "/tmp",
 *                 },
 *             ],
 *         },
 *         {
 *             command: "echo \"hello\"",
 *             containerImage: "ccr.ccs.tencentyun.com/qcloud/resty",
 *             containerName: "resty",
 *             envs: [{
 *                 key: "key2",
 *                 value: "value2",
 *             }],
 *             publishPorts: [{
 *                 containerPort: 80,
 *                 hostPort: 80,
 *                 ip: "127.0.0.1",
 *                 protocol: "udp",
 *             }],
 *             volumes: [{
 *                 containerPath: "/var",
 *                 hostPath: "/tmp",
 *             }],
 *         },
 *     ],
 *     instanceName: "hello world",
 *     period: 1,
 *     renewFlag: "NOTIFY_AND_AUTO_RENEW",
 *     zone: "ap-guangzhou-3",
 * });
 * ```
 */
export class Instance extends pulumi.CustomResource {
    /**
     * Get an existing Instance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState, opts?: pulumi.CustomResourceOptions): Instance {
        return new Instance(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:Lighthouse/instance:Instance';

    /**
     * Returns true if the given object is an instance of Instance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Instance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Instance.__pulumiType;
    }

    /**
     * ID of the Lighthouse image.
     */
    public readonly blueprintId!: pulumi.Output<string>;
    /**
     * ID of the Lighthouse package.
     */
    public readonly bundleId!: pulumi.Output<string>;
    /**
     * A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idem-potency of the request cannot be guaranteed.
     */
    public readonly clientToken!: pulumi.Output<string | undefined>;
    /**
     * Configuration of the containers to create.
     */
    public readonly containers!: pulumi.Output<outputs.Lighthouse.InstanceContainer[] | undefined>;
    /**
     * Whether the request is a dry run only.true: dry run only. The request will not create instance(s). A dry run can check whether all the required parameters are specified, whether the request format is right, whether the request exceeds service limits, and whether the specified CVMs are available. If the dry run fails, the corresponding error code will be returned.If the dry run succeeds, the RequestId will be returned.false (default value): send a normal request and create instance(s) if all the requirements are met.
     */
    public readonly dryRun!: pulumi.Output<boolean | undefined>;
    /**
     * The display name of the Lighthouse instance.
     */
    public readonly instanceName!: pulumi.Output<string>;
    /**
     * Login password of the instance. It is only available for Windows instances. If it is not specified, it means that the user choose to set the login password after the instance creation.
     */
    public readonly loginConfiguration!: pulumi.Output<outputs.Lighthouse.InstanceLoginConfiguration | undefined>;
    /**
     * Subscription period in months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60.
     */
    public readonly period!: pulumi.Output<number>;
    /**
     * Auto-Renewal flag. Valid values: NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically; NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically. You need to manually renew DISABLE_NOTIFY_AND_AUTO_RENEW: neither notify upon expiration nor renew automatically. Default value: NOTIFY_AND_MANUAL_RENEW.
     */
    public readonly renewFlag!: pulumi.Output<string>;
    /**
     * List of availability zones. A random AZ is selected by default.
     */
    public readonly zone!: pulumi.Output<string | undefined>;

    /**
     * Create a Instance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: InstanceArgs | InstanceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as InstanceState | undefined;
            resourceInputs["blueprintId"] = state ? state.blueprintId : undefined;
            resourceInputs["bundleId"] = state ? state.bundleId : undefined;
            resourceInputs["clientToken"] = state ? state.clientToken : undefined;
            resourceInputs["containers"] = state ? state.containers : undefined;
            resourceInputs["dryRun"] = state ? state.dryRun : undefined;
            resourceInputs["instanceName"] = state ? state.instanceName : undefined;
            resourceInputs["loginConfiguration"] = state ? state.loginConfiguration : undefined;
            resourceInputs["period"] = state ? state.period : undefined;
            resourceInputs["renewFlag"] = state ? state.renewFlag : undefined;
            resourceInputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as InstanceArgs | undefined;
            if ((!args || args.blueprintId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'blueprintId'");
            }
            if ((!args || args.bundleId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'bundleId'");
            }
            if ((!args || args.instanceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceName'");
            }
            if ((!args || args.period === undefined) && !opts.urn) {
                throw new Error("Missing required property 'period'");
            }
            if ((!args || args.renewFlag === undefined) && !opts.urn) {
                throw new Error("Missing required property 'renewFlag'");
            }
            resourceInputs["blueprintId"] = args ? args.blueprintId : undefined;
            resourceInputs["bundleId"] = args ? args.bundleId : undefined;
            resourceInputs["clientToken"] = args ? args.clientToken : undefined;
            resourceInputs["containers"] = args ? args.containers : undefined;
            resourceInputs["dryRun"] = args ? args.dryRun : undefined;
            resourceInputs["instanceName"] = args ? args.instanceName : undefined;
            resourceInputs["loginConfiguration"] = args ? args.loginConfiguration : undefined;
            resourceInputs["period"] = args ? args.period : undefined;
            resourceInputs["renewFlag"] = args ? args.renewFlag : undefined;
            resourceInputs["zone"] = args ? args.zone : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Instance.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Instance resources.
 */
export interface InstanceState {
    /**
     * ID of the Lighthouse image.
     */
    blueprintId?: pulumi.Input<string>;
    /**
     * ID of the Lighthouse package.
     */
    bundleId?: pulumi.Input<string>;
    /**
     * A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idem-potency of the request cannot be guaranteed.
     */
    clientToken?: pulumi.Input<string>;
    /**
     * Configuration of the containers to create.
     */
    containers?: pulumi.Input<pulumi.Input<inputs.Lighthouse.InstanceContainer>[]>;
    /**
     * Whether the request is a dry run only.true: dry run only. The request will not create instance(s). A dry run can check whether all the required parameters are specified, whether the request format is right, whether the request exceeds service limits, and whether the specified CVMs are available. If the dry run fails, the corresponding error code will be returned.If the dry run succeeds, the RequestId will be returned.false (default value): send a normal request and create instance(s) if all the requirements are met.
     */
    dryRun?: pulumi.Input<boolean>;
    /**
     * The display name of the Lighthouse instance.
     */
    instanceName?: pulumi.Input<string>;
    /**
     * Login password of the instance. It is only available for Windows instances. If it is not specified, it means that the user choose to set the login password after the instance creation.
     */
    loginConfiguration?: pulumi.Input<inputs.Lighthouse.InstanceLoginConfiguration>;
    /**
     * Subscription period in months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60.
     */
    period?: pulumi.Input<number>;
    /**
     * Auto-Renewal flag. Valid values: NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically; NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically. You need to manually renew DISABLE_NOTIFY_AND_AUTO_RENEW: neither notify upon expiration nor renew automatically. Default value: NOTIFY_AND_MANUAL_RENEW.
     */
    renewFlag?: pulumi.Input<string>;
    /**
     * List of availability zones. A random AZ is selected by default.
     */
    zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Instance resource.
 */
export interface InstanceArgs {
    /**
     * ID of the Lighthouse image.
     */
    blueprintId: pulumi.Input<string>;
    /**
     * ID of the Lighthouse package.
     */
    bundleId: pulumi.Input<string>;
    /**
     * A unique string supplied by the client to ensure that the request is idempotent. Its maximum length is 64 ASCII characters. If this parameter is not specified, the idem-potency of the request cannot be guaranteed.
     */
    clientToken?: pulumi.Input<string>;
    /**
     * Configuration of the containers to create.
     */
    containers?: pulumi.Input<pulumi.Input<inputs.Lighthouse.InstanceContainer>[]>;
    /**
     * Whether the request is a dry run only.true: dry run only. The request will not create instance(s). A dry run can check whether all the required parameters are specified, whether the request format is right, whether the request exceeds service limits, and whether the specified CVMs are available. If the dry run fails, the corresponding error code will be returned.If the dry run succeeds, the RequestId will be returned.false (default value): send a normal request and create instance(s) if all the requirements are met.
     */
    dryRun?: pulumi.Input<boolean>;
    /**
     * The display name of the Lighthouse instance.
     */
    instanceName: pulumi.Input<string>;
    /**
     * Login password of the instance. It is only available for Windows instances. If it is not specified, it means that the user choose to set the login password after the instance creation.
     */
    loginConfiguration?: pulumi.Input<inputs.Lighthouse.InstanceLoginConfiguration>;
    /**
     * Subscription period in months. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60.
     */
    period: pulumi.Input<number>;
    /**
     * Auto-Renewal flag. Valid values: NOTIFY_AND_AUTO_RENEW: notify upon expiration and renew automatically; NOTIFY_AND_MANUAL_RENEW: notify upon expiration but do not renew automatically. You need to manually renew DISABLE_NOTIFY_AND_AUTO_RENEW: neither notify upon expiration nor renew automatically. Default value: NOTIFY_AND_MANUAL_RENEW.
     */
    renewFlag: pulumi.Input<string>;
    /**
     * List of availability zones. A random AZ is selected by default.
     */
    zone?: pulumi.Input<string>;
}