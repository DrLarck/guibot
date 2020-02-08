"""
Main class

--

Birth date : 08/02/20 

Author : DrLarck

Last update : 08/02/20 (DrLarck)
"""

# dependancies
import asyncio
import discord
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

        # init
        activity = discord.Game(name = f"--help | v{Config_bot.version} - {Config_bot.phase}")

        client = commands.Bot(
            command_prefix = Config_bot.prefix, help_command = None,
            activity = activity
        )

        # run
        client.run(Config_bot.token)

        return

if(__name__ == "__main__"):
    Main().run()