// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cdn.Inputs
{

    public sealed class CdnDomainCompressionArgs : Pulumi.ResourceArgs
    {
        [Input("compressionRules")]
        private InputList<Inputs.CdnDomainCompressionCompressionRuleArgs>? _compressionRules;
        public InputList<Inputs.CdnDomainCompressionCompressionRuleArgs> CompressionRules
        {
            get => _compressionRules ?? (_compressionRules = new InputList<Inputs.CdnDomainCompressionCompressionRuleArgs>());
            set => _compressionRules = value;
        }

        [Input("switch", required: true)]
        public Input<string> Switch { get; set; } = null!;

        public CdnDomainCompressionArgs()
        {
        }
    }
}