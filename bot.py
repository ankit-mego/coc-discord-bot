# Import other libraries to be used in your code
import coc
import creds
import traceback

from database.database import BotDatabase
from discord.ext import commands

description = "This is where you provide a concise description of your bot. Not sure if this is ever visible anywhere."

# This is where you can select the prefix you'd like used for your bot commands
prefix = "/"

# Here you make the connection to the COC API using the coc.py library
coc_client = coc.login(creds.coc_dev_email, creds.coc_dev_password, client=coc.EventsClient, key_names="war_home")

# These are the cogs that you are using in your bot
initial_extensions = (
    "cogs.general",
    "cogs.special",
    "cogs.database_bg",
    "cogs.war-reporter",
)

# File path to your sqlite3 db file
SQLITE_FILE = 'database/bot_database.db'


class MyBot(commands.Bot):
    # The __init__ method is a standard method seen at the beginning of most classes
    # it declares the variables that will be used throughout the class
    def __init__(self):
        super().__init__(command_prefix=prefix,
                         description=description,
                         case_insensitive=True)
        self.coc = coc_client
        # This instantiates the database class
        self.dbconn = BotDatabase(SQLITE_FILE)

        # Load all extensions (see the cogs folder)
        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except Exception as extension:
                traceback.print_exc()

    async def on_ready(self):
        print(f"Bot is logged in as {self.user} ID: {self.user.id}")


# the following if statement ensures that bot.py is the actual file being executed
# the alternative is that this file might be imported into another file (in which case, we don't run the following)
if __name__ == "__main__":
    try:
        bot = MyBot()
        bot.run(creds.discord_bot_token)
    except:
        traceback.print_exc()

def search_clans(ctag):
   clan = client.get_clan(ctag)
  return clan.name + ' | LVL: ' + str(clan.level) + ' | LOG:W/L/D: ' + str(clan.war_wins) + '/' + str(war_losses) + '/' + str(clan.war_ties) + ' | CWL: ' + str(clan.war_league) + ' | Tag: ' + clan.tag 

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # Example - !clan #2PP
  if message.content.startswith(prefix + "title"):
    
    clan_tag = message.content.split(" ")[1] or None
    if(not clan_tag):
        return message.channel.send("Provide a clan tag.")

    title = search_clans(clan_tag)
    await message.channel.send(title)
