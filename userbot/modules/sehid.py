# BozQurd - aykhan_s
# Modulu və yaxud txt faylını
# kopyalama oğul

import secrets
import string
import aiohttp
from pyrogram import filters
from cryptography.fernet import Fernet
from userbot.events import register as aykhan
from userbot.cmdhelp import CmdHelp
from AykhanPro.komekci import random_line
# Əmr
@aykhan(outgoing=True, pattern="^.sehid ?(.*)")
async def sehid(event):
    await event.edit((await random_line('AykhanPro/txt/sehid.txt')))
# Köməy
CmdHelp('sehid').add_command(
    'sehid', 'Bu əmr vaistəsiylə sizə Şəhid adları göndərəcəm', 'Allah bütün Şəhidlərimizə rəhmət eləsin\nQazilərimizə şəfa versin\nBaşın sağolsun Azərbaycan 🇦🇿\nBazada 2881 Şəhid adı mövcuddur\n👨🏻‍💻 Sahib - @aykhan_s'
).add()
# Support
# RoBotlarimTg - meslehet.py
