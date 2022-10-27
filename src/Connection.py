import os
import sys
sys.path.append(os.getcwd())

import asyncpg
import asyncio

from Academy.tan.src import Config
from google.cloud import bigquery

# Credential
SERVER_DB = Config.DB_URL
DATABASE_DB = Config.DB_NAME
USERNAME_DB = Config.DB_USER
PASSWORD_DB = Config.DB_PASS
PORT_DB = Config.DB_PORT


class DBClient:
    ####### setup connection #######
    async def ConnectionDB():

        conn = None
        if conn == None:
            try:
                conn = await asyncpg.connect(
                        user=USERNAME_DB,
                        password=PASSWORD_DB,
                        database=DATABASE_DB,
                        host=SERVER_DB,
                        port=PORT_DB,
                    )
                print(f"[INFO]success connect to postgresDB...")
                # await conn.close()
            except asyncpg.PostgresError as exc:
                return ("Failed to initialise database.", exc)
            else:
                pass
        return conn
    
    async def ConnectionDB_test():
        conn = None
        if conn == None:
            try:
                conn = await asyncpg.connect(
                        user=USERNAME_DB,
                        password=PASSWORD_DB,
                        database='test_tan',
                        host=SERVER_DB,
                        port=PORT_DB,
                    )
                print(f"[INFO]success connect to postgresDB...")
                # await conn.close()
            except asyncpg.PostgresError as exc:
                return ("Failed to initialise database.", exc)
            else:
                pass
        return conn

    async def ConnectionBQ():
        conn = None
        if conn == None:
            try:
                conn = os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = \
                '/home/academydataengineer/Academy/tan/vibrant-fabric-364101-b92cc447257a.json'
                client = bigquery.Client.from_service_account_json(conn)
            except:
                print("error")
        return conn