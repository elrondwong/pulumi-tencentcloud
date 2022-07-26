// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Availability
{
    public static class Zones
    {
        public static Task<ZonesResult> InvokeAsync(ZonesArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<ZonesResult>("tencentcloud:Availability/zones:Zones", args ?? new ZonesArgs(), options.WithDefaults());

        public static Output<ZonesResult> Invoke(ZonesInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<ZonesResult>("tencentcloud:Availability/zones:Zones", args ?? new ZonesInvokeArgs(), options.WithDefaults());
    }


    public sealed class ZonesArgs : Pulumi.InvokeArgs
    {
        [Input("includeUnavailable")]
        public bool? IncludeUnavailable { get; set; }

        [Input("name")]
        public string? Name { get; set; }

        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public ZonesArgs()
        {
        }
    }

    public sealed class ZonesInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("includeUnavailable")]
        public Input<bool>? IncludeUnavailable { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public ZonesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class ZonesResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly bool? IncludeUnavailable;
        public readonly string? Name;
        public readonly string? ResultOutputFile;
        public readonly ImmutableArray<Outputs.ZonesZoneResult> Zones;

        [OutputConstructor]
        private ZonesResult(
            string id,

            bool? includeUnavailable,

            string? name,

            string? resultOutputFile,

            ImmutableArray<Outputs.ZonesZoneResult> zones)
        {
            Id = id;
            IncludeUnavailable = includeUnavailable;
            Name = name;
            ResultOutputFile = resultOutputFile;
            Zones = zones;
        }
    }
}