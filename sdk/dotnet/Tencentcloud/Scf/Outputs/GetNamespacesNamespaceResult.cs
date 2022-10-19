// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace TencentCloudIAC.PulumiPackage.Tencentcloud.Scf.Outputs
{

    [OutputType]
    public sealed class GetNamespacesNamespaceResult
    {
        /// <summary>
        /// Create time of the SCF namespace.
        /// </summary>
        public readonly string CreateTime;
        /// <summary>
        /// Description of the SCF namespace to be queried.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Modify time of the SCF namespace.
        /// </summary>
        public readonly string ModifyTime;
        /// <summary>
        /// Name of the SCF namespace to be queried.
        /// </summary>
        public readonly string Namespace;
        /// <summary>
        /// Type of the SCF namespace.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GetNamespacesNamespaceResult(
            string createTime,

            string description,

            string modifyTime,

            string @namespace,

            string type)
        {
            CreateTime = createTime;
            Description = description;
            ModifyTime = modifyTime;
            Namespace = @namespace;
            Type = type;
        }
    }
}