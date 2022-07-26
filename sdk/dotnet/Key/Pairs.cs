// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Key
{
    public static class Pairs
    {
        public static Task<PairsResult> InvokeAsync(PairsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<PairsResult>("tencentcloud:Key/pairs:Pairs", args ?? new PairsArgs(), options.WithDefaults());

        public static Output<PairsResult> Invoke(PairsInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<PairsResult>("tencentcloud:Key/pairs:Pairs", args ?? new PairsInvokeArgs(), options.WithDefaults());
    }


    public sealed class PairsArgs : Pulumi.InvokeArgs
    {
        [Input("keyId")]
        public string? KeyId { get; set; }

        [Input("keyName")]
        public string? KeyName { get; set; }

        [Input("projectId")]
        public int? ProjectId { get; set; }

        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public PairsArgs()
        {
        }
    }

    public sealed class PairsInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("keyId")]
        public Input<string>? KeyId { get; set; }

        [Input("keyName")]
        public Input<string>? KeyName { get; set; }

        [Input("projectId")]
        public Input<int>? ProjectId { get; set; }

        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public PairsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class PairsResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string? KeyId;
        public readonly string? KeyName;
        public readonly ImmutableArray<Outputs.PairsKeyPairListResult> KeyPairLists;
        public readonly int? ProjectId;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private PairsResult(
            string id,

            string? keyId,

            string? keyName,

            ImmutableArray<Outputs.PairsKeyPairListResult> keyPairLists,

            int? projectId,

            string? resultOutputFile)
        {
            Id = id;
            KeyId = keyId;
            KeyName = keyName;
            KeyPairLists = keyPairLists;
            ProjectId = projectId;
            ResultOutputFile = resultOutputFile;
        }
    }
}