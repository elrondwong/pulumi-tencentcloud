// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace TencentCloudIAC.PulumiPackage.Tencentcloud.Monitor
{
    public static class GetPolicyConditions
    {
        /// <summary>
        /// Use this data source to query monitor policy conditions(There is a lot of data and it is recommended to output to a file)
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
        ///         var monitorPolicyConditions = Output.Create(Tencentcloud.Monitor.GetPolicyConditions.InvokeAsync(new Tencentcloud.Monitor.GetPolicyConditionsArgs
        ///         {
        ///             Name = "Cloud Virtual Machine",
        ///             ResultOutputFile = "./tencentcloud_monitor_policy_conditions.txt",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetPolicyConditionsResult> InvokeAsync(GetPolicyConditionsArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPolicyConditionsResult>("tencentcloud:Monitor/getPolicyConditions:getPolicyConditions", args ?? new GetPolicyConditionsArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query monitor policy conditions(There is a lot of data and it is recommended to output to a file)
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
        ///         var monitorPolicyConditions = Output.Create(Tencentcloud.Monitor.GetPolicyConditions.InvokeAsync(new Tencentcloud.Monitor.GetPolicyConditionsArgs
        ///         {
        ///             Name = "Cloud Virtual Machine",
        ///             ResultOutputFile = "./tencentcloud_monitor_policy_conditions.txt",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetPolicyConditionsResult> Invoke(GetPolicyConditionsInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPolicyConditionsResult>("tencentcloud:Monitor/getPolicyConditions:getPolicyConditions", args ?? new GetPolicyConditionsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPolicyConditionsArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the policy name, support partial matching, eg:`Cloud Virtual Machine`,`Virtual`,`Cloud Load Banlancer-Private CLB Listener`.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// Used to store results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetPolicyConditionsArgs()
        {
        }
    }

    public sealed class GetPolicyConditionsInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the policy name, support partial matching, eg:`Cloud Virtual Machine`,`Virtual`,`Cloud Load Banlancer-Private CLB Listener`.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Used to store results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetPolicyConditionsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetPolicyConditionsResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// A list policy condition. Each element contains the following attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPolicyConditionsListResult> Lists;
        /// <summary>
        /// Name of this policy name.
        /// </summary>
        public readonly string? Name;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private GetPolicyConditionsResult(
            string id,

            ImmutableArray<Outputs.GetPolicyConditionsListResult> lists,

            string? name,

            string? resultOutputFile)
        {
            Id = id;
            Lists = lists;
            Name = name;
            ResultOutputFile = resultOutputFile;
        }
    }
}