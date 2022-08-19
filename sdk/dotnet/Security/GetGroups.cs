// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Security
{
    public static class GetGroups
    {
        /// <summary>
        /// Use this data source to query detailed information of security groups.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Tencentcloud = Pulumi.Tencentcloud;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var sglab = Output.Create(Tencentcloud.Security.GetGroups.InvokeAsync(new Tencentcloud.Security.GetGroupsArgs
        ///         {
        ///             SecurityGroupId = tencentcloud_security_group.Sglab.Id,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetGroupsResult> InvokeAsync(GetGroupsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetGroupsResult>("tencentcloud:Security/getGroups:getGroups", args ?? new GetGroupsArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query detailed information of security groups.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Tencentcloud = Pulumi.Tencentcloud;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var sglab = Output.Create(Tencentcloud.Security.GetGroups.InvokeAsync(new Tencentcloud.Security.GetGroupsArgs
        ///         {
        ///             SecurityGroupId = tencentcloud_security_group.Sglab.Id,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetGroupsResult> Invoke(GetGroupsInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetGroupsResult>("tencentcloud:Security/getGroups:getGroups", args ?? new GetGroupsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetGroupsArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the security group to be queried. Conflict with `security_group_id`.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// Project ID of the security group to be queried. Conflict with `security_group_id`.
        /// </summary>
        [Input("projectId")]
        public int? ProjectId { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        /// <summary>
        /// ID of the security group to be queried. Conflict with `name` and `project_id`.
        /// </summary>
        [Input("securityGroupId")]
        public string? SecurityGroupId { get; set; }

        [Input("tags")]
        private Dictionary<string, object>? _tags;

        /// <summary>
        /// Tags of the security group to be queried. Conflict with `security_group_id`.
        /// </summary>
        public Dictionary<string, object> Tags
        {
            get => _tags ?? (_tags = new Dictionary<string, object>());
            set => _tags = value;
        }

        public GetGroupsArgs()
        {
        }
    }

    public sealed class GetGroupsInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the security group to be queried. Conflict with `security_group_id`.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Project ID of the security group to be queried. Conflict with `security_group_id`.
        /// </summary>
        [Input("projectId")]
        public Input<int>? ProjectId { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        /// <summary>
        /// ID of the security group to be queried. Conflict with `name` and `project_id`.
        /// </summary>
        [Input("securityGroupId")]
        public Input<string>? SecurityGroupId { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Tags of the security group to be queried. Conflict with `security_group_id`.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public GetGroupsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetGroupsResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Name of the security group.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// Project ID of the security group.
        /// </summary>
        public readonly int? ProjectId;
        public readonly string? ResultOutputFile;
        /// <summary>
        /// ID of the security group.
        /// </summary>
        public readonly string? SecurityGroupId;
        /// <summary>
        /// Information list of security group.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetGroupsSecurityGroupResult> SecurityGroups;
        /// <summary>
        /// Tags of the security group.
        /// </summary>
        public readonly ImmutableDictionary<string, object>? Tags;

        [OutputConstructor]
        private GetGroupsResult(
            string id,

            string? name,

            int? projectId,

            string? resultOutputFile,

            string? securityGroupId,

            ImmutableArray<Outputs.GetGroupsSecurityGroupResult> securityGroups,

            ImmutableDictionary<string, object>? tags)
        {
            Id = id;
            Name = name;
            ProjectId = projectId;
            ResultOutputFile = resultOutputFile;
            SecurityGroupId = securityGroupId;
            SecurityGroups = securityGroups;
            Tags = tags;
        }
    }
}