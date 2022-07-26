// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

export function keyAlias(args: KeyAliasArgs, opts?: pulumi.InvokeOptions): Promise<KeyAliasResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("tencentcloud:Audit/keyAlias:KeyAlias", {
        "region": args.region,
        "resultOutputFile": args.resultOutputFile,
    }, opts);
}

/**
 * A collection of arguments for invoking KeyAlias.
 */
export interface KeyAliasArgs {
    region: string;
    resultOutputFile?: string;
}

/**
 * A collection of values returned by KeyAlias.
 */
export interface KeyAliasResult {
    readonly auditKeyAliasLists: outputs.Audit.KeyAliasAuditKeyAliasList[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly region: string;
    readonly resultOutputFile?: string;
}

export function keyAliasOutput(args: KeyAliasOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<KeyAliasResult> {
    return pulumi.output(args).apply(a => keyAlias(a, opts))
}

/**
 * A collection of arguments for invoking KeyAlias.
 */
export interface KeyAliasOutputArgs {
    region: pulumi.Input<string>;
    resultOutputFile?: pulumi.Input<string>;
}