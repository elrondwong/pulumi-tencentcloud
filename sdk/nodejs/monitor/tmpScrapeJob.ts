// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a resource to create a monitor tmpScrapeJob
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const tmpScrapeJob = new tencentcloud.monitor.TmpScrapeJob("tmpScrapeJob", {
 *     instanceId: "prom-dko9d0nu",
 *     agentId: "agent-6a7g40k2",
 *     config: `job_name: demo-config
 * honor_timestamps: true
 * metrics_path: /metrics
 * scheme: https
 * `,
 * });
 * ```
 *
 * ## Import
 *
 * monitor tmpScrapeJob can be imported using the id, e.g.
 *
 * ```sh
 *  $ pulumi import tencentcloud:Monitor/tmpScrapeJob:TmpScrapeJob tmpScrapeJob tmpScrapeJob_id
 * ```
 */
export class TmpScrapeJob extends pulumi.CustomResource {
    /**
     * Get an existing TmpScrapeJob resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TmpScrapeJobState, opts?: pulumi.CustomResourceOptions): TmpScrapeJob {
        return new TmpScrapeJob(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'tencentcloud:Monitor/tmpScrapeJob:TmpScrapeJob';

    /**
     * Returns true if the given object is an instance of TmpScrapeJob.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TmpScrapeJob {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TmpScrapeJob.__pulumiType;
    }

    /**
     * Agent id.
     */
    public readonly agentId!: pulumi.Output<string>;
    /**
     * Job content.
     */
    public readonly config!: pulumi.Output<string | undefined>;
    /**
     * Instance id.
     */
    public readonly instanceId!: pulumi.Output<string>;

    /**
     * Create a TmpScrapeJob resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TmpScrapeJobArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TmpScrapeJobArgs | TmpScrapeJobState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TmpScrapeJobState | undefined;
            resourceInputs["agentId"] = state ? state.agentId : undefined;
            resourceInputs["config"] = state ? state.config : undefined;
            resourceInputs["instanceId"] = state ? state.instanceId : undefined;
        } else {
            const args = argsOrState as TmpScrapeJobArgs | undefined;
            if ((!args || args.agentId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'agentId'");
            }
            if ((!args || args.instanceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceId'");
            }
            resourceInputs["agentId"] = args ? args.agentId : undefined;
            resourceInputs["config"] = args ? args.config : undefined;
            resourceInputs["instanceId"] = args ? args.instanceId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(TmpScrapeJob.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TmpScrapeJob resources.
 */
export interface TmpScrapeJobState {
    /**
     * Agent id.
     */
    agentId?: pulumi.Input<string>;
    /**
     * Job content.
     */
    config?: pulumi.Input<string>;
    /**
     * Instance id.
     */
    instanceId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a TmpScrapeJob resource.
 */
export interface TmpScrapeJobArgs {
    /**
     * Agent id.
     */
    agentId: pulumi.Input<string>;
    /**
     * Job content.
     */
    config?: pulumi.Input<string>;
    /**
     * Instance id.
     */
    instanceId: pulumi.Input<string>;
}