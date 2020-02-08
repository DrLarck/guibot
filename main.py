"""
Main class

--

Birth date : 08/02/20 

Author : DrLarck

Last update : 08/02/20 (DrLarck)
"""

# dependancies
import asyncio
from discord.ext import commands

# conf
from configuration.bot import Config_bot

class Main():
    """
    Represents the main class of the program which runs it.

    - Method :

    `run()` : Connect the bot
    """

    # method
    def run(self):
        """
        Connect the bot

        --

        Return : `None`
        """

        client = commands.Bot(
            command_prefix = Config_bot.prefix, help_command = None
        )

        # run
        client.run(Config_bot.token)

        return

if(__name__ == "__main__"):
    Main().run()