using System;

namespace FCL.DataLoader
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length == 1 && args[0] == "0") 
            {
                SeedBatch0.Run();
            } 
            else if (args.Length == 1 && args[0] == "1")
            {
                SeedBatch1.Run();
            } 
            else 
            {
                Console.WriteLine("Usage: `dotnet run <seedbatch>`");
                Console.WriteLine("\t<seedbatch> must be either 0 or 1...");
            }

            Console.WriteLine("Processing complete. Press any key to exit.");
            Console.ReadKey();
        }
    }
}
