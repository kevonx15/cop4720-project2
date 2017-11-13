using System.Collections.Generic;
using System.Data;

namespace FCL.Helpers
{
    public class RateHelper
    {
        private class Sql
        {
            public const string SelectStandardRate = "SELECT RT_AMT FROM FCL2.RATE WHERE RT_CODE = @rt_code";
        }

        private class Readers
        {
            public static decimal GetStandardRate(IDataReader reader)
            {
                reader.Read();
                return reader.GetDecimal(0);
            }
        }

        public static decimal GetStandardLaborRate()
        {
            return DbHelper.ExecuteQuery(Readers.GetStandardRate, Sql.SelectStandardRate, new Dictionary<string, object> {
                { "@rt_code", "std_labor_rate"}
            });
        }
    }
}
