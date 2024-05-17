from os import getenv
from sys import argv, orig_argv
from dotenv import load_dotenv

from src.app import App
from src.types.app_types import AppConfig

from interactions import (
    listen, slash_command, slash_option, SlashContext, OptionType)
from interactions.api.events import (
    Ready, MessageCreate, InteractionCreate, Error, Startup)

###############################################################################
# Initialize
# region: initialize
# region: initialize environment


load_dotenv(".env", override=False)


def is_debug() -> bool:
    return any([
        getenv("DEBUG") is not None,
        "--debug" in argv,
        "--debug" in orig_argv
    ])


def validate_environment():
    if getenv("DEBUG") and getenv("PRODUCTION"):
        raise ValueError(
            "Both DEBUG and PRODUCTION environment variables are set. Only "
            "one must be set.")


validate_environment()

# endregion: initialize environment

# region: initialize app
APP_NAME = "ConiBotti"
APP_VERSION = "0.1.0"

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

# endregion: initialize app
# endregion: initialize

###############################################################################
# Setup
# region: setup
# region: setup event listeners


@listen(Startup)
async def on_startup():
    print(f"{app} startup complete")


@listen(Ready)
async def on_ready() -> None:
    print("Bot is ready")


@listen()
async def on_message_create(event: MessageCreate):
    print(f"message received: {event.message.content}")


@listen()
async def on_error(event: Error):
    print(f"An error occured: {event.error}")


@listen()
async def on_interaction_create(event: InteractionCreate):
    print(f"New interaction: {event.interaction}")

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
    bot = app.bot
    bot.start(app.config["TOKEN"])
# endregion: main


if __name__ == "__main__":
    main()
