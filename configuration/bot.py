"""
Bot config

--

Author : DrLarck

Last update : 08/02/20 (DrLarck)
"""

# dependancies
import os

class Config_bot():
    """
    Manages the bot config

    - Attribute :

    `prefix` (`list`) : List of prefix
    """

    # prefixes
    prefix = ["--", "**"]

    # version
    version = "1.0"
    phase = "ALPHA"

    # bot token
    # hidden
    token = os.environ["guibot_token"]