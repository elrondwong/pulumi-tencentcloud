// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cdn.Inputs
{

    public sealed class CdnDomainStatusCodeCacheArgs : Pulumi.ResourceArgs
    {
        [Input("cacheRules")]
        private InputList<Inputs.CdnDomainStatusCodeCacheCacheRuleArgs>? _cacheRules;
        public InputList<Inputs.CdnDomainStatusCodeCacheCacheRuleArgs> CacheRules
        {
            get => _cacheRules ?? (_cacheRules = new InputList<Inputs.CdnDomainStatusCodeCacheCacheRuleArgs>());
            set => _cacheRules = value;
        }

        [Input("switch", required: true)]
        public Input<string> Switch { get; set; } = null!;

        public CdnDomainStatusCodeCacheArgs()
        {
        }
    }
}