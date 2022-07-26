// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.Sqlserver
{
    public static class Accounts
    {
        public static Task<AccountsResult> InvokeAsync(AccountsArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<AccountsResult>("tencentcloud:Sqlserver/accounts:Accounts", args ?? new AccountsArgs(), options.WithDefaults());

        public static Output<AccountsResult> Invoke(AccountsInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<AccountsResult>("tencentcloud:Sqlserver/accounts:Accounts", args ?? new AccountsInvokeArgs(), options.WithDefaults());
    }


    public sealed class AccountsArgs : Pulumi.InvokeArgs
    {
        [Input("instanceId", required: true)]
        public string InstanceId { get; set; } = null!;

        [Input("name")]
        public string? Name { get; set; }

        [Input("resultOutputFile")]
        public string? ResultOutputFile { get; set; }

        public AccountsArgs()
        {
        }
    }

    public sealed class AccountsInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("instanceId", required: true)]
        public Input<string> InstanceId { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("resultOutputFile")]
        public Input<string>? ResultOutputFile { get; set; }

        public AccountsInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class AccountsResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string InstanceId;
        public readonly ImmutableArray<Outputs.AccountsListResult> Lists;
        public readonly string? Name;
        public readonly string? ResultOutputFile;

        [OutputConstructor]
        private AccountsResult(
            string id,

            string instanceId,

            ImmutableArray<Outputs.AccountsListResult> lists,

            string? name,

            string? resultOutputFile)
        {
            Id = id;
            InstanceId = instanceId;
            Lists = lists;
            Name = name;
            ResultOutputFile = resultOutputFile;
        }
    }
}