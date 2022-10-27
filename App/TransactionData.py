import asyncpg
import asyncio
import os
import sys
sys.path.append(os.getcwd())


class DataOperationBase ():
  
    ####### running extract data #######
    async def Extract (connection, query):
        try:
            record = await connection.fetch(query)

        except asyncpg.PostgresError as exc:
                return ("Failed to extract data. ", exc)
        else:
            return connection
            await connection.close()

    async def CreateDB (connection, query):
        try:
            await connection.execute(query)
        except asyncpg.PostgresError as exc:
            return ("Failed to Create Table. ", exc)
        else:
            return connection
            await connection.close()
    
        ####### running extract data #######
    async def CreateTable (connection, query):
        tr = connection.transaction()
        await tr.start() #Masukkan blok transaksi atau savepoint
        try:
            await connection.execute(query)
        except asyncpg.PostgresError as exc:
            return ("Failed to Create Table. ", exc)
        else:
            await tr.commit()
            return connection
            await connection.close()


    ####### running insert data #######
    async def Insert (connection, query):
        tr = connection.transaction()
        await tr.start() #Masukkan blok transaksi atau savepoint
        try:
             # Execute a statement
            await connection.execute(query)    
        except asyncpg.PostgresError as exc:
            await tr.rollback() #Keluar dari transaksi atau blok savepoint dan kembalikan perubahan.
            return ("Failed to insert data. ", exc)
        else:
            await tr.commit() #Keluar dari blok transaksi atau savepoint dan lakukan perubahan.
            return connection
            await connection.close()


    ####### running update data #######
    async def Update (connection, query):
        tr = connection.transaction()
        await tr.start()
        try:
            await connection.execute(query)
        except asyncpg.PostgresError as exc:
            await tr.rollback()
            return ("Failed to update data. ", exc)
        else:
            await tr.commit()
            return connection
            await connection.close()


    ####### running delete data #######
    async def Delete (connection, query):
        tr = connection.transaction()
        await tr.start()
        try:
            # -- replace True with logical code for delete data --
            await connection.execute(query)
        except asyncpg.PostgresError as exc:
            await tr.rollback()
            return ("Failed to delete data. ", exc)
        else:
            await tr.commit()
            return connection
            await connection.close()
    
    ####### running truncate data #######
    async def Truncate (connection, query):
        tr = connection.transaction()
        await tr.start()
        try:
            # -- replace True with logical code for delete data --
            await connection.execute(query)
        except asyncpg.PostgresError as exc:
            await tr.rollback()
            return ("Failed to Truncate data. ", exc)
        else:
            await tr.commit()
            return connection
            await connection.close()


    ####### running upsert data #######
    async def Upsert (connection, query):
        # define connection to running query transaction
        tr = connection.transaction()
        await tr.start()
        try:
            # -- replace True with logical code for upsert data --
            await connection.execute(query)
        except asyncpg.PostgresError as exc:
            await tr.rollback()
            return ("Failed to upsert data. ", exc)
        else:
            await tr.commit()
            return connection
            await connection.close()