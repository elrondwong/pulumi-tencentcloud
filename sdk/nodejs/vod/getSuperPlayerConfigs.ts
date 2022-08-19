// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * Use this data source to query detailed information of VOD super player configs.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as tencentcloud from "@pulumi/tencentcloud";
 *
 * const fooSuperPlayerConfig = new tencentcloud.vod.SuperPlayerConfig("fooSuperPlayerConfig", {
 *     drmSwitch: true,
 *     drmStreamingInfo: {
 *         simpleAesDefinition: tencentcloud_vod_adaptive_dynamic_streaming_template.foo.id,
 *     },
 *     imageSpriteDefinition: tencentcloud_vod_image_sprite_template.foo.id,
 *     resolutionNames: [
 *         {
 *             minEdgeLength: 889,
 *             name: "test1",
 *         },
 *         {
 *             minEdgeLength: 890,
 *             name: "test2",
 *         },
 *     ],
 *     domain: "Default",
 *     scheme: "Default",
 *     comment: "test",
 * });
 * const fooSuperPlayerConfigs = tencentcloud.Vod.getSuperPlayerConfigs({
 *     type: "Custom",
 *     name: "tf-super-player",
 * });
 * ```
 */
export function getSuperPlayerConfigs(args?: GetSuperPlayerConfigsArgs, opts?: pulumi.InvokeOptions): Promise<GetSuperPlayerConfigsResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Vod/getSuperPlayerConfigs:getSuperPlayerConfigs", {
        "name": args.name,
        "resultOutputFile": args.resultOutputFile,
        "subAppId": args.subAppId,
        "type": args.type,
    }, opts);
}

/**
 * A collection of arguments for invoking getSuperPlayerConfigs.
 */
export interface GetSuperPlayerConfigsArgs {
    /**
     * Name of super player config.
     */
    name?: string;
    /**
     * Used to save results.
     */
    resultOutputFile?: string;
    /**
     * Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
     */
    subAppId?: number;
    /**
     * Config type filter. Valid values: `Preset`, `Custom`. `Preset`: preset template; `Custom`: custom template.
     */
    type?: string;
}

/**
 * A collection of values returned by getSuperPlayerConfigs.
 */
export interface GetSuperPlayerConfigsResult {
    /**
     * A list of super player configs. Each element contains the following attributes:
     */
    readonly configLists: outputs.Vod.GetSuperPlayerConfigsConfigList[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Display name.
     */
    readonly name?: string;
    readonly resultOutputFile?: string;
    readonly subAppId?: number;
    /**
     * Template type filter. Valid values: `Preset`, `Custom`. `Preset`: preset template; `Custom`: custom template.
     */
    readonly type?: string;
}

export function getSuperPlayerConfigsOutput(args?: GetSuperPlayerConfigsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSuperPlayerConfigsResult> {
    return pulumi.output(args).apply(a => getSuperPlayerConfigs(a, opts))
}

/**
 * A collection of arguments for invoking getSuperPlayerConfigs.
 */
export interface GetSuperPlayerConfigsOutputArgs {
    /**
     * Name of super player config.
     */
    name?: pulumi.Input<string>;
    /**
     * Used to save results.
     */
    resultOutputFile?: pulumi.Input<string>;
    /**
     * Subapplication ID in VOD. If you need to access a resource in a subapplication, enter the subapplication ID in this field; otherwise, leave it empty.
     */
    subAppId?: pulumi.Input<number>;
    /**
     * Config type filter. Valid values: `Preset`, `Custom`. `Preset`: preset template; `Custom`: custom template.
     */
    type?: pulumi.Input<string>;
}