using System;

namespace FCL.DataLoader
{
    public class SeedBatch0
    {
        public static void Run()
        {
            Console.WriteLine("Running SeedBatch0");

            var rateFilePath = System.IO.Path.GetFullPath(System.IO.Path.Combine(Constants.CSV_ROOT, "fcl.rates.csv"));
            var rateReader = new System.IO.StringReader(System.IO.File.ReadAllText(rateFilePath));

            var csv = new CsvHelper.CsvReader(rateReader);
            
            foreach(var record in csv.GetRecords<Rate>())
            {
                
            }
        }
    }
}
