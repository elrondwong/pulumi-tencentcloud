// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Postgresql
{
    public static class Specinfos
    {
        public static Task<SpecinfosResult> InvokeAsync(SpecinfosArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<SpecinfosResult>("tencentcloud:Postgresql/specinfos:Specinfos", args ?? new SpecinfosArgs(), options.WithDefaults());

        public static Output<SpecinfosResult> Invoke(SpecinfosInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<SpecinfosResult>("tencentcloud:Postgresql/specinfos:Specinfos", args ?? new SpecinfosInvokeArgs(), options.WithDefaults());
    }


    public sealed class SpecinfosArgs : Pulumi.InvokeArgs
    {
        [Input("availabilityZone", required: true)]
        public string AvailabilityZone { get; set; } = null!;

        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public SpecinfosArgs()
        {
        }
    }

    public sealed class SpecinfosInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("availabilityZone", required: true)]
        public Input<string> AvailabilityZone { get; set; } = null!;

        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public SpecinfosInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class SpecinfosResult
    {
        public readonly string AvailabilityZone;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.SpecinfosListResult> Lists;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private SpecinfosResult(
            string availabilityZone,

            string id,

            ImmutableArray<Outputs.SpecinfosListResult> lists,

            string? resultOutputFile)
        {
            AvailabilityZone = availabilityZone;
            Id = id;
            Lists = lists;
            ResultOutputFile = resultOutputFile;
        }
    }
}