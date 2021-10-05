# RoBotlarimTg
# aykhan_s | aykhan026
# //////////\\\\\\\\
# Yazıları silib istifadə eləmə oğlum
# \\\\\\\\///////////
from userbot.events import register as aykhan
from userbot.cmdhelp import CmdHelp
import asyncio
# RoBotlarimTg
@aykhan(outgoing=True, pattern="^.fyaz(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Səhv format`")
    await event.edit(f"♻️ `Mesaj Modu Aktiv Olunur`")
    await event.edit(f"✅ `Mesaj Modu Aktiv Olundu`")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)
# RoBotlarimTg
@aykhan(outgoing=True, pattern="^.fses(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Səhv format`")
    await event.edit(f"✅ `Səs Modu Aktiv Olundu`")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)
# RoBotlarimTg
@aykhan(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Səhv format`")
    await event.edit(f"✅ `Video Modu Aktiv Olundu`")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)
# RoBotlarimTg
@aykhan(outgoing=True, pattern="^.foyun(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Səhv Format`")
    await event.edit(f"✅ `Oyun Modu Aktiv Olundu`")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)
# aykhan_s | aykhan026
CmdHelp('fakeyaz').add_command(
'fyaz', None, 'Mesaj yazırsınızmış kimi göstərəcək'
    ).add_command(
        'fses', None, 'Səs atırsınızmış kimi göstərəcək'
    ).add_command(
        'fvideo', None, 'Video atırsınızmış kimi göstərəcək'
    ).add_command(
        'foyun', None, 'Oyun oynadığınızı göstərəcək'
    ).add()
