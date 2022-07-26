// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Cdn.Outputs
{

    [OutputType]
    public sealed class CdnDomainStatusCodeCache
    {
        public readonly ImmutableArray<Outputs.CdnDomainStatusCodeCacheCacheRule> CacheRules;
        public readonly string Switch;

        [OutputConstructor]
        private CdnDomainStatusCodeCache(
            ImmutableArray<Outputs.CdnDomainStatusCodeCacheCacheRule> cacheRules,

            string @switch)
        {
            CacheRules = cacheRules;
            Switch = @switch;
        }
    }
}