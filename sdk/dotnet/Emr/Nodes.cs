// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Emr
{
    public static class Nodes
    {
        public static Task<NodesResult> InvokeAsync(NodesArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<NodesResult>("tencentcloud:Emr/nodes:Nodes", args ?? new NodesArgs(), options.WithDefaults());

        public static Output<NodesResult> Invoke(NodesInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<NodesResult>("tencentcloud:Emr/nodes:Nodes", args ?? new NodesInvokeArgs(), options.WithDefaults());
    }


    public sealed class NodesArgs : Pulumi.InvokeArgs
    {
        [Input("hardwareResourceType")]
        public string? HardwareResourceType { get; set; }

        [Input("instanceId", required: true)]
        public string InstanceId { get; set; } = null!;

        [Input("limit")]
        public int? Limit { get; set; }

        [Input("nodeFlag", required: true)]
        public string NodeFlag { get; set; } = null!;

        [Input("offset")]
        public int? Offset { get; set; }

        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public NodesArgs()
        {
        }
    }

    public sealed class NodesInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("hardwareResourceType")]
        public Input<string>? HardwareResourceType { get; set; }

        [Input("instanceId", required: true)]
        public Input<string> InstanceId { get; set; } = null!;

        [Input("limit")]
        public Input<int>? Limit { get; set; }

        [Input("nodeFlag", required: true)]
        public Input<string> NodeFlag { get; set; } = null!;

        [Input("offset")]
        public Input<int>? Offset { get; set; }

        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public NodesInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class NodesResult
    {
        public readonly string? HardwareResourceType;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string InstanceId;
        public readonly int? Limit;
        public readonly string NodeFlag;
        public readonly ImmutableArray<Outputs.NodesNodeResult> Nodes;
        public readonly int? Offset;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private NodesResult(
            string? hardwareResourceType,

            string id,

            string instanceId,

            int? limit,

            string nodeFlag,

            ImmutableArray<Outputs.NodesNodeResult> nodes,

            int? offset,

            string? resultOutputFile)
        {
            HardwareResourceType = hardwareResourceType;
            Id = id;
            InstanceId = instanceId;
            Limit = limit;
            NodeFlag = nodeFlag;
            Nodes = nodes;
            Offset = offset;
            ResultOutputFile = resultOutputFile;
        }
    }
}