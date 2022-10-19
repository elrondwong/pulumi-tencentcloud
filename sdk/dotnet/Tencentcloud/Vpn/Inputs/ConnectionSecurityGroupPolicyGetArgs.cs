// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace TencentCloudIAC.PulumiPackage.Tencentcloud.Vpn.Inputs
{

    public sealed class ConnectionSecurityGroupPolicyGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Local cidr block.
        /// </summary>
        [Input("localCidrBlock", required: true)]
        public Input<string> LocalCidrBlock { get; set; } = null!;

        [Input("remoteCidrBlocks", required: true)]
        private InputList<string>? _remoteCidrBlocks;

        /// <summary>
        /// Remote cidr block list.
        /// </summary>
        public InputList<string> RemoteCidrBlocks
        {
            get => _remoteCidrBlocks ?? (_remoteCidrBlocks = new InputList<string>());
            set => _remoteCidrBlocks = value;
        }

        public ConnectionSecurityGroupPolicyGetArgs()
        {
        }
    }
}