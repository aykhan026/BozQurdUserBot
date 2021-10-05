import codecs
import heroku3
import asyncio
import aiohttp
import math
import os
import ssl
import requests

from userbot import (
    HEROKU_APPNAME,
    HEROKU_APIKEY,
    BOTLOG,
    BOTLOG_CHATID
)

from userbot.events import register
from userbot.cmdhelp import CmdHelp

heroku_api = "https://api.heroku.com"
if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None:
    Heroku = heroku3.from_key(HEROKU_APIKEY)
    app = Heroku.app(HEROKU_APPNAME)
    heroku_var = app.config()
else:
    app = None

@register(outgoing=True,
          pattern=r"^.(get|del) var(?: |$)(\w*)")
async def variable(var):
    exe = var.pattern_match.group(1)
    if app is None:
        await var.edit("`[HEROKU]"
                       "\n**HEROKU_APPNAME** Yükləyin.")
        return False
    if exe == "get":
        await var.edit("`Herokudan Məlumat Götürürəm.`")
        variable = var.pattern_match.group(2)
        if variable != '':
            if variable in heroku_var:
                if BOTLOG:
                    await var.client.send_message(
                        BOTLOG_CHATID, "#CONFIGVARS\n\n"
                        "**ConfigVars**:\n"
                        f"`{variable}` = `{heroku_var[variable]}`\n"
                    )
                    await var.edit("`BOTLOG qrupuna göndərirəm!`")
                    return True
                else:
                    await var.edit("`Zəhmət olmasa BOTLOG qrupu ayarlayın.`")
                    return False
            else:
                await var.edit("`Xəta:` **NoInfo.**")
                return True
        else:
            configvars = heroku_var.to_dict()
            if BOTLOG:
                msg = ''
                for item in configvars:
                    msg += f"`{item}` = `{configvars[item]}`\n"
                await var.client.send_message(
                    BOTLOG_CHATID, "#CONFIGVARS\n\n"
                    "**ConfigVars**:\n"
                    f"{msg}"
                )
                await var.edit("`BOTLOG_CHATID alındı.`")
                return True
            else:
                await var.edit("`Zəhmət olmasa BOTLOG qrupu ayarlayın!`")
                return False
    elif exe == "del":
        await var.edit("`ConfigVars'ı silirəm.`")
        variable = var.pattern_match.group(2)
        if variable == '':
            await var.edit("`Silməy istədiyiniz ConfigVars'ı yazın.`")
            return False
        if variable in heroku_var:
            if BOTLOG:
                await var.client.send_message(
                    BOTLOG_CHATID, "#DELCONFIGVARS\n\n"
                    "**ConfigVars Silindi**:\n"
                    f"`{variable}`"
                )
            await var.edit("`ConfigVars silindi!`")
            del heroku_var[variable]
        else:
            await var.edit("ConfigVars Tapılmadı!`")
            return True


@register(outgoing=True, pattern=r'^.set var (\w*) ([\s\S]*)')
async def set_var(var):
    await var.edit("`Verdiyiniz məlumatlar herokuya yazılır...`")
    variable = var.pattern_match.group(1)
    value = var.pattern_match.group(2)
    if variable in heroku_var:
        if BOTLOG:
            await var.client.send_message(
                BOTLOG_CHATID, "#SETCONFIGVARS\n\n"
                "**ConfigVars Düzenlemesi**:\n"
                f"`{variable}` = `{value}`"
            )
        await var.edit("`Verdiyiniz məlumatlar herokuya yazılır....`")
    else:
        if BOTLOG:
            await var.client.send_message(
                BOTLOG_CHATID, "#ADDCONFIGVARS\n\n"
                "**ConfigVars Eklendi**:\n"
                f"`{variable}` = `{value}`"
            )
        await var.edit("`ConfigVars Əlavə olundu!`")
    heroku_var[variable] = value

@register(outgoing=True, pattern=r"^.dyno(?: |$)")
async def dyno_usage(dyno):

    await dyno.edit("`Zəhmət olmasa gözləyin...`")
    useragent = ('Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/80.0.3987.149 Mobile Safari/537.36'
                 )
    u_id = Heroku.account().id
    headers = {
     'User-Agent': useragent,
     'Authorization': f'Bearer {HEROKU_APIKEY}',
     'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
    }
    path = "/accounts/" + u_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("`Xəta: Pis bir şey oldu.`\n\n"
                               f">.`{r.reason}`\n")
    result = r.json()
    quota = result['account_quota']
    quota_used = result['quota_used']

    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)

    App = result['apps']
    try:
        App[0]['quota_used']
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]['quota_used'] / 60
        AppPercentage = math.floor(App[0]['quota_used'] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await dyno.edit("✅**Heroku ilə əlaqə qurulub** \n\n🐺**BozQurd Dyno İstifadəsi**:\n"
                           f" 👉 **UserBotun adı**  **({HEROKU_APPNAME})**:\n\n🔴 **İstifadə olunmuş saatlar:**"
                           f"\n🔆 `{AppHours}` **saat**  `{AppMinutes}` **dəqiqə**  "
                           f"\n 👉**Faizlə**  [`{AppPercentage}` **%**]"
                           "\n\n"
                           " 🟢 Qalan dyno saatı:**\n"
                           f"🔆  `{hours}` **saat**  `{minutes}` **dəqiqə**  "
                           f"\n 👉**Faizlə**  [`{percentage}` **%**]"
                           )

@register(outgoing=True, pattern=r"^.hlog")
async def _(dyno):
    try:
        Heroku = heroku3.from_key(HEROKU_APIKEY)
        app = Heroku.app(HEROKU_APPNAME)
    except BaseException:
        return await dyno.reply(
            "`Zəhmət olmasa gözləyin`"
        )
    await dyno.edit("`Log göndərirəm....`")
    with open("BozQurdLogs.txt", "w") as log:
        log.write(app.get_log())
    fd = codecs.open("BozQurdLogs.txt", "r", encoding="utf-8")
    data = fd.read()
    key = (requests.post("https://nekobin.com/api/documents",
                         json={"content": data}) .json() .get("result") .get("key"))
    url = f"https://nekobin.com/raw/{key}"
    await dyno.edit(f"`Heroku log'u :`\n\n [Burda]({url})")
    return os.remove("BozQurdLogs.txt")


CmdHelp('heroku').add_command(
'dyno', None, 'Qalan və işlədilən dyno saatınız haqqında məlumat verir.'
    ).add_command(
        'set var', '<Vars adı> <Key>', 'Botunuza yeni ConfigVars əlavə edər vəya var olan ConfigVars dəyərini dəyişdirər.'
    ).add_command(
        'get var', '<Vars Adı>', 'Mövcud olan ConfigVars dəyərini gətirəbilərsiniz. Botlog qrupunuzdan tapa bilərsiniz.'
    ).add_command(
        'del var', '<Vars Adı>', 'Seçdiyiniz ConfigVars ı silər. Sildiydən sonra .restart yazın.'
    ).add_command(
        'hlog', None, 'Heroku logunuzu göndərin'
    ).add()
