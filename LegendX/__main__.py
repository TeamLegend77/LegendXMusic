import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from LegendX import LOGGER, app, userbot
from LegendX.core.call import Legend
from LegendX.plugins import ALL_MODULES
from LegendX.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("LegendX").error(
            "No Assistant Clients Vars Defined!.. Exiting Process.."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("LegendX").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("LegendX.plugins" + all_module)
    LOGGER("LegendX.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Legend.start()
    try:
        await Legend.stream_call(
            "https://telegra.ph/file/8d5db123638c2f6bb6ce4.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("LegendX").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group."
        )
        sys.exit()
    except:
        pass
    await Legend.decorators()
    LOGGER("LegendX").info("Music Bot Started Successfully,")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("LegendX").info("Stopping Music Bot, (Good Bye Lala)")
