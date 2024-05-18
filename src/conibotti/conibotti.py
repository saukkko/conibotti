from os import getenv
from sys import stderr
from logging import getLogger

from __version__ import __version__
from dotenv import load_dotenv
from util import is_debug, validate_env
from app.app import App
from app.logger import LogLevel, setup_logger
from app.app_types import AppConfig

from interactions import (
    listen, slash_command, slash_option, SlashContext, OptionType)
from interactions.api.events import (
    Ready, InteractionCreate, Error, Startup)


###############################################################################
# Initialize
# region: initialize

# region: initialize logger

setup_logger()
logger = getLogger("conibotti")
logger.info("Hello")
# endregion: initialize logger

# region: initialize environment


load_dotenv(".env", override=False)
validate_env()

# endregion: initialize environment

# region: initialize app
APP_NAME = "ConiBotti"
APP_VERSION = __version__

CONFIG: AppConfig = {
    "APP_NAME": APP_NAME,
    "APP_VERSION": APP_VERSION,
    "ENDPOINT_URL": "https://kompassi.eu/api/v1/listings/conit.fi",
    "APPLICATION_ID": None,
    "PUBLIC_KEY": None,
    "TOKEN": getenv("TOKEN", None),
    "DEBUG": is_debug(),
}

app = App(config=CONFIG)
bot = app.bot

pass

# endregion: initialize app
# endregion: initialize

###############################################################################
# Setup
# region: setup
# region: setup event listeners


@listen(Startup)
async def on_startup():
    bot.logger.info(f"{app} startup complete")


@listen(Ready)
async def on_ready() -> None:
    bot.logger.info("Bot is ready")


@listen()
async def on_error(event: Error):
    bot.logger.error(f"An error occured: {event.error}")


@listen()
async def on_interaction_create(event: InteractionCreate):
    bot.logger.info(f"New interaction: {event.interaction}")

# endregion: setup event listeners


# region: setup commands
# region: setup command: say-hello


@slash_command(name="say-hello", description="Say \"Hello!\"")
async def say_hello(ctx: SlashContext):
    await ctx.send("Hello!")
# endregion


# region: setup command: list-events
@slash_command(name="list-events", description="List events")
async def list_events(ctx: SlashContext):
    await ctx.send(app.list_events())
# endregion


# region: setup command: get-event
@slash_command(name="get-event", description="Get single event")
@slash_option(name="hakusana", description="Hakusana",
              required=True, opt_type=OptionType.STRING,
              argument_name="slug")
async def get_event(ctx: SlashContext, slug: str):
    await ctx.send(app.get_event(slug))
# endregion


# endregion: setup commands
# endregion: setup

###############################################################################
# Main entry point
# region: main
def main():
    try:
        logger.log(level=LogLevel.ALL,
                   msg="App initialized, starting the bot...")
        bot.start(app.config["TOKEN"])
    except Exception as e:
        print(e, file=stderr)
        bot.stop()
# endregion: main


if __name__ == "__main__":
    main()
