import os
from re import U
import sys
sys.path.append(os.getcwd())

import time

import asyncio

from Academy.tan.src import Connection
from Academy.tan.query.SqlCommand import QueryServices
from TransactionData import DataOperationBase


start_time = time.time()

loop = asyncio.new_event_loop()



if __name__ == '__main__':
    
    r = loop.run_until_complete(
                Connection.DBClient.ConnectionDB()
                )
    s = loop.run_until_complete(
                Connection.DBClient.ConnectionDB_test()
                )
    # s = loop.run_until_complete(
    #     DataOperationBase.Extract(
    #         connection= r, 
    #         query= QueryServices.select.format(
    #             Column = 'actor_id, first_name, last_name',
    #             Table = 'actor',
    #             FilterColumn = 'actor_id >= 1 and actor_id < 4'

    # create_DB = loop.run_until_complete(
    #     DataOperationBase.CreateDB(
    #         connection = r, 
    #         query = QueryServices.createDB.format(
    #             DB_name = 'test_tan'
    #         )
    #     )
    # )
    # print(create_DB)

    # create_table = loop.run_until_complete(
    #     DataOperationBase.CreateTable(
    #         connection = s, 
    #         query = QueryServices.create_table.format(
    #             Table = 'user_tan',
    #             Columns = ''' user_id serial4 not null,
    #                         first_name VARCHAR(50) not null,
    #                         last_name VARCHAR(50) not null,
    #                         last_update TIMESTAMP not null default now()''',
    #             PrimaryKey = 'user_id',
    #             ColumnIndex = 'first_name',
    #             ColumnTrigger = 'last_update'
    #         )
    #     )
    # )
    # print(create_table)

    insert = loop.run_until_complete(
        DataOperationBase.Insert(
            connection = s, 
            query = QueryServices.insert.format(
                Column = 'first_name,last_name',
                Value = "'tes','tes'",
                Table = 'user_tan'
            )
        )
    )
    print(insert)

    # update = loop.run_until_complete(
    #     DataOperationBase.Update(
    #         connection = r, 
    #         query = QueryServices.update.format(
    #             Table = 'user_tan',
    #             SetColumn = "first_name = 'tani'",
    #             FilterColumn = "first_name = 'tan'"
    #         )
    #     )
    # )
    # print(update)

    # delete = loop.run_until_complete(
    #     DataOperationBase.Delete(
    #         connection = r, 
    #         query = QueryServices.delete.format(
    #             Table ='user_tan',
    #             FilterColumn = "first_name = 'abc'"
    #         )
    #     )
    # )
    # print(delete)

    # truncate = loop.run_until_complete(
    #     DataOperationBase.Truncate(
    #         connection = r, 
    #         query = QueryServices.truncate.format(
    #             Table ='user_tan'
    #         )
    #     )
    # )
    # print(truncate)

    # upsert = loop.run_until_complete(
    #     DataOperationBase.Upsert(
    #         connection= r, 
    #         query= QueryServices.upsert.format(
    #             Column= 'user_id, first_name, last_name',
    #             Table= 'user_tan',
    #             Value= "1, 't', 'anugrah'",
    #             PrimaryColumn = 'user_id',
    #             ColumnMarkUpdate = """
    #                                first_name = excluded.first_name,
    #                                last_name = excluded.last_name
    #                                """,
    #         )
    #     )
    # )
    # print(upsert)

    print("--- %s seconds ---" % (time.time() - start_time))