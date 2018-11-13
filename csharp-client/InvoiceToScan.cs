using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Text;

namespace csharp_client
{
    public class InvoiceToScan
    {
        [JsonProperty("image")]
        public byte[] Image { get; set; }

        [JsonProperty("language")]
        public string Language { get; set; }

        [JsonProperty("date")]
        public DateTime Date { get; set; }
    }
}
