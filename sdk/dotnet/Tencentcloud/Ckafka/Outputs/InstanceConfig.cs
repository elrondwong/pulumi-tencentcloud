// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace TencentCloudIAC.PulumiPackage.Tencentcloud.Ckafka.Outputs
{

    [OutputType]
    public sealed class InstanceConfig
    {
        /// <summary>
        /// Automatic creation. true: enabled, false: not enabled.
        /// </summary>
        public readonly bool AutoCreateTopicEnable;
        /// <summary>
        /// If auto.create.topic.enable is set to true and this value is not set, 3 will be used by default.
        /// </summary>
        public readonly int DefaultNumPartitions;
        /// <summary>
        /// If auto.create.topic.enable is set to true but this value is not set, 2 will be used by default.
        /// </summary>
        public readonly int DefaultReplicationFactor;

        [OutputConstructor]
        private InstanceConfig(
            bool autoCreateTopicEnable,

            int defaultNumPartitions,

            int defaultReplicationFactor)
        {
            AutoCreateTopicEnable = autoCreateTopicEnable;
            DefaultNumPartitions = defaultNumPartitions;
            DefaultReplicationFactor = defaultReplicationFactor;
        }
    }
}