# RoBotlarimTg - tyeni.py
# Burdan hər hansı bir şeyi
# Kopyalayan Peysərdi...!!!
# Sahib - @aykhan_s
# _-_-_-_-_-_-_-_-_-_-_-_-_-_ #

import random
import asyncio
from os import execl
import sys
import io
import sys
from userbot.events import register as aykhan
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from telethon.tl.types import ChannelParticipantsAdmins as cp
from time import sleep
from AykhanPro.komekci.tagger import reng, reqem, status, musiqi, ad, emj, cumle
from userbot.cmdhelp import CmdHelp
class FlagContainer:
    is_active = False
    
# Əkmə Oğlum...!!!

# Adlarla Tağ
@aykhan(outgoing=True, pattern="^.adtag.*")
async def adtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozad = None
          aykhan1 = event.message.text.split(" ", 1)
          if len(aykhan1) > 1:
              sozad = aykhan1[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Adlarla Tağ Başladı**\n⏱️ **İnterval** - 1 saniyə\n👤 **User sayı** - 5")
  
          tags = list(map(lambda m: f"[{random.choice(ad)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 5: 
                  tags = list(map(lambda m: f"[{random.choice(ad)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozad:
                      tags.append(sozad)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(1) 
      finally:
          FlagContainer.is_active = False
          
 # Rənglərlə Tağ 
@aykhan(outgoing=True, pattern="^.rgtag.*")
async def rgtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozreng = None
          aykhan2 = event.message.text.split(" ", 1)
          if len(aykhan2) > 1:
              soz = aykhan2[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Rənglərlə Tağ Başladı**\n⏱️ **İnterval** - 0.5 saniyə\n👤 **User sayı** - 4")
  
          tags = list(map(lambda m: f"[{random.choice(reng)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 4: 
                  tags = list(map(lambda m: f"[{random.choice(reng)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozreng:
                      tags.append(sozreng)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(0.5) 
      finally:
          FlagContainer.is_active = False
 # Rəqəmlərlə Tağ 
@aykhan(outgoing=True, pattern="^.rqtag.*")
async def rqtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozreq = None
          aykhan3 = event.message.text.split(" ", 1)
          if len(aykhan3) > 1:
              sozreq = aykhan3[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Rəqəmlərlə Tağ Başladı**\n⏱️ **İnterval** - 0.5 saniyə\n👤 **User sayı** - 3")
  
          tags = list(map(lambda m: f"[{random.choice(reqem)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 3: 
                  tags = list(map(lambda m: f"[{random.choice(reqem)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozreq:
                      tags.append(sozreq)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(0.5) 
      finally:
          FlagContainer.is_active = False
          
 # Emojilərlə Tağ 
@aykhan(outgoing=True, pattern="^.emtag.*")
async def emtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozemj = None
          aykhan4 = event.message.text.split(" ", 1)
          if len(aykhan4) > 1:
              sozemj = aykhan4[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Emoji Tağ Başladı**\n⏱️ **İnterval** - 0.5 saniyə\n👤 **User sayı** - 5")
  
          tags = list(map(lambda m: f"[{random.choice(emj)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 5: 
                  tags = list(map(lambda m: f"[{random.choice(emj)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozemj:
                      tags.append(sozemj)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(0.5) 
      finally:
          FlagContainer.is_active = False
  # Cümlələrlə Tağ 
@aykhan(outgoing=True, pattern="^.ctag.*")
async def ctag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozcm = None
          aykhan5 = event.message.text.split(" ", 1)
          if len(aykhan5) > 1:
              sozcm = aykhan5[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Cümlələrlə Tağ Başladı**\n⏱️ **İnterval** - 3 saniyə\n👤 **User sayı** - 1")
  
          tags = list(map(lambda m: f"[{random.choice(cumle)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 1: 
                  tags = list(map(lambda m: f"[{random.choice(cumle)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozcm:
                      tags.append(sozcm)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(3) 
      finally:
          FlagContainer.is_active = False

# Muisiqi Tağ
@aykhan(outgoing=True, pattern="^.mtag.*")
async def mtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozmus = None
          aykhan6 = event.message.text.split(" ", 1)
          if len(aykhan6) > 1:
              sozmus = aykhan6[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Musiqi Adlarıyla Tağ Başladı**\n⏱️ **İnterval** - 3 saniyə\n👤 **User sayı** - 1")
  
          tags = list(map(lambda m: f"[{random.choice(musiqi)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 1: 
                  tags = list(map(lambda m: f"[{random.choice(musiqi)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozmus:
                      tags.append(sozmus)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(3) 
      finally:
          FlagContainer.is_active = False
          
# Statuslarla Tağ
@aykhan(outgoing=True, pattern="^.stag.*")
async def stag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozsts = None
          aykhan7 = event.message.text.split(" ", 1)
          if len(aykhan7) > 1:
              sozsts = aykhan7[1]
  
          chat = await event.get_input_chat()
          await event.edit("❤️ **Status Mesajlarıyla Tağ Başladı**\n⏱️ **İnterval** - 3 saniyə\n👤 **User sayı** - 1")
  
          tags = list(map(lambda m: f"[{random.choice(status)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 1: 
                  tags = list(map(lambda m: f"[{random.choice(status)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozsts:
                      tags.append(sozsts)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(3) 
      finally:
          FlagContainer.is_active = False

# Stop (Tağ Dayandırmaq)
@aykhan(outgoing=True, pattern="^.stp")
async def restart(event):
    await event.edit("⛔ **Tağ prosesi dayandırıldı**")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "⛔ **Tağ prosesi dayandırıldı**\n"
                                        )

    try:
        await bot.disconnect()
    except:
        pass

    execl(sys.executable, sys.executable, *sys.argv)
# Əkmə oğul...!!!
CmdHelp('tagger').add_command(
    'mtag', '<Mesajınız>', ' Musiqi adlarıyla tağ edir'
).add_command(
    'adtag', '<Mesajınız>', ' Dəyişiy adlarla tağ edir'
).add_command(
    'stag', '<Mesajınız>', ' Status mesajlarıyla tağ edir'
).add_command(
    'rgtag', '<Mesajınız>', ' Rəngli tağ edir'
).add_command(
    'rqtag', '<Mesajınız>', ' Rəqəmlərlə tağ edir'
).add_command(
    'emtag', '<Mesajınız>', ' Emojilərlə tağ edir'
).add_command(
    'ctag', '<Mesajınız>', ' Cümlələrlə və maraqlı sözlərlə tək tək tağ edir'
).add_command(
    'stp', None, '⛔Aktiv tağ prosesini dayandırır\n\n👨🏻‍💻Sahib - @aykhan_s\n📣 Rəsmi Kanal - @RoBotlarimTg'
).add()
