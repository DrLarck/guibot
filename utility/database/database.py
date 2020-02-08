"""
Database object

--

Author : DrLarck

Last update : 08/02/20 (DrLarck)
"""

# dependancies
import asyncio
import asyncpg
import os

class Database():
    """
    Manages the database operations

    - Attribute :

    `connection` : `None` - Represent a database connection from the pool

    `connection_pool` : `None` - Represents the connection pool

    - Method :

    :coro:`get_pool()` : `connection pool` - Create a connection pool
    """

    # attribute
    def __init__(self):
        # connection
        self.connection = None  # represents the connection
        self.connection_pool = None  # represents the connection pool

        # configuration
        self.name = os.environ["guibot_db_name"]
        self.host = os.environ["guibot_db_host"]
        self.user = os.environ["guibot_db_user"]
        self.password = os.environ["guibot_db_password"]
        self.port = "5432"
    
    # method
    async def get_pool(self):
        """
        `coroutine`

        Creates a connection pool to the database

        --

        Return : `connection pool`
        """

        self.connection_pool = await asyncpg.create_pool(
            name = self.name,
            host = self.host,
            user = self.user,
            password = self.password,
            port = self.port
        )

        return(self.connection_pool)
    
    async def connect(self):
        """
        `coroutine`

        Get a connection from the pool

        --

        Return : `connection`
        """

        self.connection = await self.connection_pool.acquire()

        return(self.connection)
    
    async def release(self):
        """
        `coroutine`

        Release the connection to the pool

        --

        Return : `None`
        """

        await self.connection_pool.release(self.connection)

        return
    
    async def stop(self):
        """
        `coroutine`

        Close the connection to the database

        --

        Return : `None`
        """

        await self.connection_pool.close()

        return
    
    