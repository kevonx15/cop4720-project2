using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;

namespace FCL.DataLoader
{
    public class DbHelper
    {
        public static int ExecuteCommand(string sql, IDictionary<string, object> parameters = null)
        {
            using (var connection = new SqlConnection(Constants.CONNECTION_STRING))
            {
                connection.Open();
                var cmd = connection.CreateCommand();
                cmd.CommandText = sql;

                if (parameters != null)
                    foreach (var p in parameters)
                        cmd.Parameters.AddWithValue(p.Key, p.Value);

                return cmd.ExecuteNonQuery();
            }
        }

        public static T ExecuteQuery<T>(Func<IDataReader, T> action, string sql, IDictionary<string, object> parameters = null)
        {
            using (var connection = new SqlConnection(Constants.CONNECTION_STRING))
            {
                connection.Open();
                var cmd = connection.CreateCommand();
                cmd.CommandText = sql;

                if (parameters != null)
                    foreach (var p in parameters)
                        cmd.Parameters.AddWithValue(p.Key, p.Value);

                using (var reader = cmd.ExecuteReader())
                {
                    return action(reader);
                }
            }
        }
    }
}
