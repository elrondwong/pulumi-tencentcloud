// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Kubernetes.Outputs
{

    [OutputType]
    public sealed class GetClusterLevelsListResult
    {
        /// <summary>
        /// Alias used for pass to cluster level arguments.
        /// </summary>
        public readonly string Alias;
        /// <summary>
        /// Number of ConfigMaps.
        /// </summary>
        public readonly int ConfigMapCount;
        /// <summary>
        /// Number of CRDs.
        /// </summary>
        public readonly int CrdCount;
        /// <summary>
        /// Indicates whether the current level enabled.
        /// </summary>
        public readonly bool Enable;
        /// <summary>
        /// Level name.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Number of nodes.
        /// </summary>
        public readonly int NodeCount;
        /// <summary>
        /// Number of others.
        /// </summary>
        public readonly int OtherCount;
        /// <summary>
        /// Number of pods.
        /// </summary>
        public readonly int PodCount;

        [OutputConstructor]
        private GetClusterLevelsListResult(
            string alias,

            int configMapCount,

            int crdCount,

            bool enable,

            string name,

            int nodeCount,

            int otherCount,

            int podCount)
        {
            Alias = alias;
            ConfigMapCount = configMapCount;
            CrdCount = crdCount;
            Enable = enable;
            Name = name;
            NodeCount = nodeCount;
            OtherCount = otherCount;
            PodCount = podCount;
        }
    }
}