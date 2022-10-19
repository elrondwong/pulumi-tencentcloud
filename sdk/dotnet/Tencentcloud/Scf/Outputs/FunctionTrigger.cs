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
    public sealed class FunctionTrigger
    {
        /// <summary>
        /// Region of cos bucket. if `type` is `cos`, `cos_region` is required.
        /// </summary>
        public readonly string? CosRegion;
        /// <summary>
        /// Name of the SCF function trigger, if `type` is `ckafka`, the format of name must be `&lt;ckafkaInstanceId&gt;-&lt;topicId&gt;`; if `type` is `cos`, the name is cos bucket id, other In any case, it can be combined arbitrarily. It can only contain English letters, numbers, connectors and underscores. The maximum length is 100.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// TriggerDesc of the SCF function trigger, parameter format of `timer` is linux cron expression; parameter of `cos` type is json string `{"bucketUrl":"&lt;name-appid&gt;.cos.&lt;region&gt;.myqcloud.com","event":"cos:ObjectCreated:*","filter":{"Prefix":"","Suffix":""}}`, where `bucketUrl` is cos bucket (optional), `event` is the cos event trigger, `Prefix` is the corresponding file prefix filter condition, `Suffix` is the suffix filter condition, if not need filter condition can not pass; `cmq` type does not pass this parameter; `ckafka` type parameter format is json string `{"maxMsgNum":"1","offset":"latest"}`; `apigw` type parameter format is json string `{"api":{"authRequired":"FALSE","requestConfig":{"method":"ANY"},"isIntegratedResponse":"FALSE"},"service":{"serviceId":"service-dqzh68sg"},"release":{"environmentName":"test"}}`.
        /// </summary>
        public readonly string TriggerDesc;
        /// <summary>
        /// Type of the SCF function trigger, support `cos`, `cmq`, `timer`, `ckafka`, `apigw`.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private FunctionTrigger(
            string? cosRegion,

            string name,

            string triggerDesc,

            string type)
        {
            CosRegion = cosRegion;
            Name = name;
            TriggerDesc = triggerDesc;
            Type = type;
        }
    }
}