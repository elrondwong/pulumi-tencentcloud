// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Eks
{
    public static class GetClusters
    {
        /// <summary>
        /// Use this data source to query elastic kubernetes cluster resource.
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
        ///         var foo = Output.Create(Tencentcloud.Eks.GetClusters.InvokeAsync(new Tencentcloud.Eks.GetClustersArgs
        ///         {
        ///             ClusterId = "cls-xxxxxxxx",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetClustersResult> InvokeAsync(GetClustersArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetClustersResult>("tencentcloud:Eks/getClusters:getClusters", args ?? new GetClustersArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to query elastic kubernetes cluster resource.
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
        ///         var foo = Output.Create(Tencentcloud.Eks.GetClusters.InvokeAsync(new Tencentcloud.Eks.GetClustersArgs
        ///         {
        ///             ClusterId = "cls-xxxxxxxx",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetClustersResult> Invoke(GetClustersInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetClustersResult>("tencentcloud:Eks/getClusters:getClusters", args ?? new GetClustersInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetClustersArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the cluster. Conflict with cluster_name, can not be set at the same time.
        /// </summary>
        [Input("clusterId")]
        public string? ClusterId { get; set; }

        /// <summary>
        /// Name of the cluster. Conflict with cluster_id, can not be set at the same time.
        /// </summary>
        [Input("clusterName")]
        public string? ClusterName { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public GetClustersArgs()
        {
        }
    }

    public sealed class GetClustersInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the cluster. Conflict with cluster_name, can not be set at the same time.
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        /// <summary>
        /// Name of the cluster. Conflict with cluster_id, can not be set at the same time.
        /// </summary>
        [Input("clusterName")]
        public Input<string>? ClusterName { get; set; }

        /// <summary>
        /// Used to save results.
        /// </summary>
        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public GetClustersInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetClustersResult
    {
        /// <summary>
        /// ID of the cluster.
        /// </summary>
        public readonly string? ClusterId;
        /// <summary>
        /// Name of the cluster.
        /// </summary>
        public readonly string? ClusterName;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// EKS cluster list.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetClustersListResult> Lists;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private GetClustersResult(
            string? clusterId,

            string? clusterName,

            string id,

            ImmutableArray<Outputs.GetClustersListResult> lists,

            string? resultOutputFile)
        {
            ClusterId = clusterId;
            ClusterName = clusterName;
            Id = id;
            Lists = lists;
            ResultOutputFile = resultOutputFile;
        }
    }
}