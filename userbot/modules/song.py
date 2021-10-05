import os
from telethon.errors import ChatAdminRequiredError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register as aykhan
from userbot.cmdhelp import CmdHelp

chat = "@MusicSOBot"

@aykhan(outgoing=True, pattern="^.so ?(.*)")
async def so(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        sobot = event.pattern_match.group(1)
    else:
        sobot = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        istifadeci = str(replied_user.user.id)
        
        await e.edit(f"♻️**Musiqini Göndərirəm**")
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/botmusic " + sobot)
                so = await conv.get_response()
                if "file" in so.text:
                    await so.click(1)
                    cavab = await conv.get_response()
                    await event.client.send_message(event.chat_id, cavab)
                else:
                    await event.client.send_message(event.chat_id, so)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MusicSOBot -u Bloklamısınız. Plugin işləməsi üçün blokdan çıxarın.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/botmusic " + sobot)
                so = await conv.get_response()
                if "file" in so.text:
                    await so.click(1)
                    cavab = await conv.get_response()
                    await event.client.send_message(event.chat_id, cavab)
                else:
                    await event.client.send_message(event.chat_id, so)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MusicSOBot -u Bloklamısınız. Plugin işləməsi üçün blokdan çıxarın.")
                

@aykhan(outgoing=True, pattern="^.topmusic ?(.*)")
async def top(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        topmsc = event.pattern_match.group(1)
    else:
        topmsc = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        istifadec = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/topmusic ")
                so = await conv.get_response()
                if "file" in so.text:
                    await so.click(1)
                    cavab = await conv.get_response()
                    await event.client.send_message(event.chat_id, cavab)
                else:
                    await event.client.send_message(event.chat_id, so)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MusicSOBot -u Bloklamısınız. Plugin işləməsi üçün blokdan çıxarın.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/topmusic ")
                so = await conv.get_response()
                if "file" in so.text:
                    await so.click(1)
                    cavab = await conv.get_response()
                    await event.client.send_message(event.chat_id, cavab)
                else:
                    await event.client.send_message(event.chat_id, so)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MusicSOBot -u Bloklamısınız. Plugin işləməsi üçün blokdan çıxarın.")
                

@aykhan(outgoing=True, pattern="^.topuser ?(.*)")
async def topuser(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        topusr = event.pattern_match.group(1)
    else:
        topusr = ""
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(
            GetFullUserRequest(previous_message.sender_id)
        )
        istifade = str(replied_user.user.id)
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/topusers ")
                so = await conv.get_response()
                if "file" in so.text:
                    await so.click(1)
                    cavab = await conv.get_response()
                    await event.client.send_message(event.chat_id, cavab)
                else:
                    await event.client.send_message(event.chat_id, so)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MusicSOBot -u Bloklamısınız. Plugin işləməsi üçün blokdan çıxarın.")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                await conv.send_message("/topusers ")
                so = await conv.get_response()
                if "file" in so.text:
                    await so.click(1)
                    cavab = await conv.get_response()
                    await event.client.send_message(event.chat_id, cavab)
                else:
                    await event.client.send_message(event.chat_id, so)
                await event.delete()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("@MusicSOBot -u Bloklamısınız. Plugin işləməsi üçün blokdan çıxarın.")
                
CmdHelp('song').add_command(
'so', None, 'so <Musiqi Adı> Musiqini yükləyər'
    ).add_command(
        'topmusic', None, 'Ən çox yüklənən musiqilər'
    ).add_command(
        'topuser', None, 'Ən çox musiqi yükləyənlər reytingi\n\n👨🏻‍💻Sahib - @aykhan_s\n👨🏻‍💻Bot Sahibi - @SenanOguz'
    ).add()
