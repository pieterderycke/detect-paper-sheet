using Newtonsoft.Json;
using System;
using System.IO;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace csharp_client
{
    class Program
    {
        static void Main(string[] args)
        {
            string imagePath = (args.Length > 0) ? args[0] : null;

            if (!File.Exists(imagePath))
            {
                Console.WriteLine("Error: The file \"{0}\" does not exist.", imagePath);
                return;
            }

            CallRestApi(imagePath).Wait();
        }

        private static async Task CallRestApi(string imagePath)
        {
            try
            {
                using (HttpClient client = new HttpClient())
                {
                    client.BaseAddress = new Uri("http://localhost:8080/api/");
                    client.DefaultRequestHeaders.Accept.ParseAdd("application/json");

                    InvoiceToScan invoiceToScan = new InvoiceToScan();
                    invoiceToScan.Image = File.ReadAllBytes(imagePath);
                    invoiceToScan.Language = "nl";
                    invoiceToScan.Date = DateTime.Today;

                    string json = JsonConvert.SerializeObject(invoiceToScan);
                    HttpResponseMessage response = await client.PostAsync("invoices", new StringContent(json, Encoding.UTF8, "application/json"));

                    string responseContent = await response.Content.ReadAsStringAsync();
                    Console.WriteLine(responseContent);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("An error occured when calling the REST API: {0}", ex.Message);
            }
        }
    }
}
