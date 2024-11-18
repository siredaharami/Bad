from pyrogram import filters

import config
from ANWIVIBES import app
from ANWIVIBES.misc import SUDOERS
from ANWIVIBES.utils.database import add_off, add_on
from ANWIVIBES.utils.decorators.language import language



@app.on_message(filters.command(["log"]) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await add_on(config.LOG)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(config.LOG)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
