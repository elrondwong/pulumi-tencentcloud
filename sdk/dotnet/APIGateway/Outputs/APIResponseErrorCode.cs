// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Tencentcloud.APIGateway.Outputs
{

    [OutputType]
    public sealed class APIResponseErrorCode
    {
        public readonly int Code;
        public readonly int? ConvertedCode;
        public readonly string? Desc;
        public readonly string Msg;
        public readonly bool? NeedConvert;

        [OutputConstructor]
        private APIResponseErrorCode(
            int code,

            int? convertedCode,

            string? desc,

            string msg,

            bool? needConvert)
        {
            Code = code;
            ConvertedCode = convertedCode;
            Desc = desc;
            Msg = msg;
            NeedConvert = needConvert;
        }
    }
}