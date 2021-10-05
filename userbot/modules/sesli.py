from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from userbot.cmdhelp import CmdHelp
from userbot.events import register as aykhan

ADMIN_DEYILEM = "⚠️`Bu əmri icra etmək üçün Admin olmalıyam`"

async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@aykhan(outgoing=True, groups_only=True, pattern="^.sesac$")
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await c.edit(ADMIN_DEYILEM)
        return
    try:
        await c.client(startvc(c.chat_id))
        await c.edit("✅`Səsli söhbəti başlatdım...`")
    except Exception as ex:
        await c.edit(f"**XƏTA:** `{ex}`")


@aykhan(outgoing=True, groups_only=True, pattern="^.sbagla$")
@aykhan(outgoing=True, groups_only=True, pattern="^.sbaqla$")
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await c.edit(ADMIN_DEYILEM)
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await c.edit("⛔`Səsli söhbəti sonlandırdım...`")
    except Exception as ex:
        await c.edit(f"**XƏTA:** `{ex}`")


@aykhan(outgoing=True, groups_only=True, pattern="^.sdevet$")
async def _(c):
    await c.edit("`İstifadəçiləri səsli söhbətə dəvət edirəm...`")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    botman = list(user_list(users, 6))
    for p in botman:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await c.edit(f"📲 **Qrupdan** `{z}` **İstifadəçi səsli söhbətə dəvət olundu**")
# Kömək
CmdHelp('sesli').add_command(
'sesac', None, '✅ Qrupda səsli söhbət açın'
    ).add_command(
        'sbagla', None, '⛔ Aktiv səsli söhbəti sonlandırın'
    ).add_command(
        'sdevet', None, '📲 İstifadəçiləri səsli söhbətə dəvət edin'
    ).add()
