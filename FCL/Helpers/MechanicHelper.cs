using FCL.Models;
using System.Collections.Generic;
using System.Data;

namespace FCL.Helpers
{
    public class MechanicHelper
    {
        private class Sql
        {
            public const string SelectByLastName = @"
SELECT MECH_ID, MECH_FNAME, MECH_LNAME
FROM FCL2.MECHANIC
WHERE MECH_LNAME LIKE @mech_lname
";

            public const string InsertMechanic = @"
INSERT INTO FCL2.MECHANIC (MECH_FNAME, MECH_LNAME)
VALUES(@mech_fname, @mech_lname)
";
        }

        private class Readers
        {
            public static List<Mechanic> ReadMechanics(IDataReader reader)
            {
                var list = new List<Mechanic>();

                while (reader.Read())
                {
                    var mechanic = new Mechanic
                    {
                        Id = reader.GetInt32(0),
                        FirstName = reader.GetString(1),
                        LastName = reader.GetString(2)
                    };

                    list.Add(mechanic);
                }

                return list;
            }
        }

        public static List<Mechanic> GetMechanicsByLastName(string lastName)
        {
            return DbHelper.ExecuteQuery(Readers.ReadMechanics, Sql.SelectByLastName, new Dictionary<string, object>
            {
                { "@mech_lname", lastName + "%" }
            });
        }

        public static int InsertNewMechanic(string firstName, string lastName)
        {
            return DbHelper.ExecuteCommand(Sql.InsertMechanic, new Dictionary<string, object>
            {
                { "@mech_fname", firstName },
                { "@mech_lname", lastName }
            });
        }
    }
}
