// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Mysql.Outputs
{

    [OutputType]
    public sealed class GetZoneConfigListResult
    {
        /// <summary>
        /// Information about available zones of recovery.
        /// </summary>
        public readonly ImmutableArray<string> DisasterRecoveryZones;
        /// <summary>
        /// The version number of the database engine to use. Supported versions include `5.5`/`5.6`/`5.7`.
        /// </summary>
        public readonly ImmutableArray<string> EngineVersions;
        /// <summary>
        /// Zone information about first slave instance.
        /// </summary>
        public readonly ImmutableArray<string> FirstSlaveZones;
        public readonly int HourInstanceSaleMaxNum;
        /// <summary>
        /// Indicates whether the current DC is the default DC for the region. Possible returned values: `0` - no; `1` - yes.
        /// </summary>
        public readonly int IsDefault;
        /// <summary>
        /// Indicates whether recovery is supported: `0` - No; `1` - Yes.
        /// </summary>
        public readonly int IsSupportDisasterRecovery;
        /// <summary>
        /// Indicates whether VPC is supported: `0` - No; `1` - Yes.
        /// </summary>
        public readonly int IsSupportVpc;
        /// <summary>
        /// The name of available zone which is equal to a specific datacenter.
        /// </summary>
        public readonly string Name;
        public readonly ImmutableArray<int> PayTypes;
        /// <summary>
        /// Zone information about remote ro instance.
        /// </summary>
        public readonly ImmutableArray<string> RemoteRoZones;
        /// <summary>
        /// Zone information about second slave instance.
        /// </summary>
        public readonly ImmutableArray<string> SecondSlaveZones;
        /// <summary>
        /// A list of supported instance types for sell:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetZoneConfigListSellResult> Sells;
        /// <summary>
        /// Availability zone deployment method. Available values: `0` - Single availability zone; `1` - Multiple availability zones.
        /// </summary>
        public readonly ImmutableArray<int> SlaveDeployModes;
        /// <summary>
        /// Data replication mode. `0` - Async replication; `1` - Semisync replication; `2` - Strongsync replication.
        /// </summary>
        public readonly ImmutableArray<int> SupportSlaveSyncModes;

        [OutputConstructor]
        private GetZoneConfigListResult(
            ImmutableArray<string> disasterRecoveryZones,

            ImmutableArray<string> engineVersions,

            ImmutableArray<string> firstSlaveZones,

            int hourInstanceSaleMaxNum,

            int isDefault,

            int isSupportDisasterRecovery,

            int isSupportVpc,

            string name,

            ImmutableArray<int> payTypes,

            ImmutableArray<string> remoteRoZones,

            ImmutableArray<string> secondSlaveZones,

            ImmutableArray<Outputs.GetZoneConfigListSellResult> sells,

            ImmutableArray<int> slaveDeployModes,

            ImmutableArray<int> supportSlaveSyncModes)
        {
            DisasterRecoveryZones = disasterRecoveryZones;
            EngineVersions = engineVersions;
            FirstSlaveZones = firstSlaveZones;
            HourInstanceSaleMaxNum = hourInstanceSaleMaxNum;
            IsDefault = isDefault;
            IsSupportDisasterRecovery = isSupportDisasterRecovery;
            IsSupportVpc = isSupportVpc;
            Name = name;
            PayTypes = payTypes;
            RemoteRoZones = remoteRoZones;
            SecondSlaveZones = secondSlaveZones;
            Sells = sells;
            SlaveDeployModes = slaveDeployModes;
            SupportSlaveSyncModes = supportSlaveSyncModes;
        }
    }
}