// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace TencentCloudIAC.PulumiPackage.Tencentcloud.Tcr
{
    /// <summary>
    /// Use this resource to create tcr instance.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Tencentcloud = TencentCloudIAC.PulumiPackage.Tencentcloud;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var foo = new Tencentcloud.Tcr.Instance("foo", new Tencentcloud.Tcr.InstanceArgs
    ///         {
    ///             InstanceType = "basic",
    ///             Tags = 
    ///             {
    ///                 { "test", "tf" },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// Using public network access whitelist
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Tencentcloud = TencentCloudIAC.PulumiPackage.Tencentcloud;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var foo = new Tencentcloud.Tcr.Instance("foo", new Tencentcloud.Tcr.InstanceArgs
    ///         {
    ///             InstanceType = "basic",
    ///             OpenPublicOperation = true,
    ///             SecurityPolicies = 
    ///             {
    ///                 new Tencentcloud.Tcr.Inputs.InstanceSecurityPolicyArgs
    ///                 {
    ///                     CidrBlock = "10.0.0.1/24",
    ///                 },
    ///                 new Tencentcloud.Tcr.Inputs.InstanceSecurityPolicyArgs
    ///                 {
    ///                     CidrBlock = "192.168.1.1",
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// tcr instance can be imported using the id, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import tencentcloud:Tcr/instance:Instance foo cls-cda1iex1
    /// ```
    /// </summary>
    [TencentcloudResourceType("tencentcloud:Tcr/instance:Instance")]
    public partial class Instance : Pulumi.CustomResource
    {
        /// <summary>
        /// Indicate to delete the COS bucket which is auto-created with the instance or not.
        /// </summary>
        [Output("deleteBucket")]
        public Output<bool?> DeleteBucket { get; private set; } = null!;

        /// <summary>
        /// TCR types. Valid values are: `standard`, `basic`, `premium`.
        /// </summary>
        [Output("instanceType")]
        public Output<string> InstanceType { get; private set; } = null!;

        /// <summary>
        /// Internal address for access of the TCR instance.
        /// </summary>
        [Output("internalEndPoint")]
        public Output<string> InternalEndPoint { get; private set; } = null!;

        /// <summary>
        /// Name of the TCR instance.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Control public network access.
        /// </summary>
        [Output("openPublicOperation")]
        public Output<bool?> OpenPublicOperation { get; private set; } = null!;

        /// <summary>
        /// Public address for access of the TCR instance.
        /// </summary>
        [Output("publicDomain")]
        public Output<string> PublicDomain { get; private set; } = null!;

        /// <summary>
        /// Status of the TCR instance public network access.
        /// </summary>
        [Output("publicStatus")]
        public Output<string> PublicStatus { get; private set; } = null!;

        /// <summary>
        /// Public network access allowlist policies of the TCR instance. Only available when `open_public_operation` is `true`.
        /// </summary>
        [Output("securityPolicies")]
        public Output<ImmutableArray<Outputs.InstanceSecurityPolicy>> SecurityPolicies { get; private set; } = null!;

        /// <summary>
        /// Status of the TCR instance.
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// The available tags within this TCR instance.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Instance resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Instance(string name, InstanceArgs args, CustomResourceOptions? options = null)
            : base("tencentcloud:Tcr/instance:Instance", name, args ?? new InstanceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Instance(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
            : base("tencentcloud:Tcr/instance:Instance", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Instance resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Instance Get(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
        {
            return new Instance(name, id, state, options);
        }
    }

    public sealed class InstanceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicate to delete the COS bucket which is auto-created with the instance or not.
        /// </summary>
        [Input("deleteBucket")]
        public Input<bool>? DeleteBucket { get; set; }

        /// <summary>
        /// TCR types. Valid values are: `standard`, `basic`, `premium`.
        /// </summary>
        [Input("instanceType", required: true)]
        public Input<string> InstanceType { get; set; } = null!;

        /// <summary>
        /// Name of the TCR instance.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Control public network access.
        /// </summary>
        [Input("openPublicOperation")]
        public Input<bool>? OpenPublicOperation { get; set; }

        [Input("securityPolicies")]
        private InputList<Inputs.InstanceSecurityPolicyArgs>? _securityPolicies;

        /// <summary>
        /// Public network access allowlist policies of the TCR instance. Only available when `open_public_operation` is `true`.
        /// </summary>
        public InputList<Inputs.InstanceSecurityPolicyArgs> SecurityPolicies
        {
            get => _securityPolicies ?? (_securityPolicies = new InputList<Inputs.InstanceSecurityPolicyArgs>());
            set => _securityPolicies = value;
        }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// The available tags within this TCR instance.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public InstanceArgs()
        {
        }
    }

    public sealed class InstanceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicate to delete the COS bucket which is auto-created with the instance or not.
        /// </summary>
        [Input("deleteBucket")]
        public Input<bool>? DeleteBucket { get; set; }

        /// <summary>
        /// TCR types. Valid values are: `standard`, `basic`, `premium`.
        /// </summary>
        [Input("instanceType")]
        public Input<string>? InstanceType { get; set; }

        /// <summary>
        /// Internal address for access of the TCR instance.
        /// </summary>
        [Input("internalEndPoint")]
        public Input<string>? InternalEndPoint { get; set; }

        /// <summary>
        /// Name of the TCR instance.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Control public network access.
        /// </summary>
        [Input("openPublicOperation")]
        public Input<bool>? OpenPublicOperation { get; set; }

        /// <summary>
        /// Public address for access of the TCR instance.
        /// </summary>
        [Input("publicDomain")]
        public Input<string>? PublicDomain { get; set; }

        /// <summary>
        /// Status of the TCR instance public network access.
        /// </summary>
        [Input("publicStatus")]
        public Input<string>? PublicStatus { get; set; }

        [Input("securityPolicies")]
        private InputList<Inputs.InstanceSecurityPolicyGetArgs>? _securityPolicies;

        /// <summary>
        /// Public network access allowlist policies of the TCR instance. Only available when `open_public_operation` is `true`.
        /// </summary>
        public InputList<Inputs.InstanceSecurityPolicyGetArgs> SecurityPolicies
        {
            get => _securityPolicies ?? (_securityPolicies = new InputList<Inputs.InstanceSecurityPolicyGetArgs>());
            set => _securityPolicies = value;
        }

        /// <summary>
        /// Status of the TCR instance.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// The available tags within this TCR instance.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public InstanceState()
        {
        }
    }
}