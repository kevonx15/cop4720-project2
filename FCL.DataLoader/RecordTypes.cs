using System;
using System.Collections.Generic;
using System.Text;

namespace FCL.DataLoader
{
    public class Rate
    {
        public string RT_CODE { get; set; }
        public string RT_NAME { get; set; }
        public decimal RT_AMT { get; set; }
    }

    public class Mechanic
    {
        public Guid MECH_ID { get; set; }
        public string MECH_FNAME { get; set; }
        public string MECH_LNAME { get; set; }
    }
}
