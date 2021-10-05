# BozQurd - bax.py
# Kopyalama Oğul

import asyncio
import os
from userbot.modules.admin import get_user_from_event
from userbot.events import register as aykhan
from userbot.cmdhelp import CmdHelp

@aykhan(outgoing=True, pattern="^.bax ?(.*)")
@aykhan(outgoing=True, pattern="^.oxu ?(.*)")
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await event.edit("📃**Faylı açıram...**")
    if len(c) > 4095:
        await a.edit(
            "❌**XƏTA** \nTelegram **4095** mesaj limitinə icazə verir. \n❗**Limit aşıldığı üçün proses ləğv olundu**"
        )
    else:
        await event.client.send_message(event.chat_id, f"{c}")
        await a.delete()
    os.remove(b)

@aykhan(outgoing=True, pattern="^.pack ?(.*)")
async def _(event):
    a = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    b = open(input_str, "w")
    b.write(str(a.message))
    b.close()
    a = await event.edit(f" 📝 Mətn `{input_str}` faylına yazılır ")
    await asyncio.sleep(2)
    await a.edit(f"📤 `{input_str}` Faylını göndərirəm")
    await asyncio.sleep(2)
    await event.client.send_file(event.chat_id, input_str)
    await a.delete()
    os.remove(input_str)

# Köməy
CmdHelp('pack').add_command(
'bax', 'Bir fayla reply olaraq yazın', 'Faylın içindəki mətni göstərəcək'
).add_command(
'pack', '<fayl adı>.py', 'Bir mesaja (mətnə) reply olaraq istifadə edin onu paketliyib sizə göndərəcək'
).add()

# Support
# RoBotlarimTg
# BozQurd
