# RoBotlarimTg - tyeni.py
# Yazılanları silmədən istədiyiniz
# UserBot da istifadə edə bilərsiniz
# Sahib - @aykhan_s

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
from userbot.cmdhelp import CmdHelp
class FlagContainer:
    is_active = False
# Əkmə Oğlum...!!!
reng = (
 "🔴",
 "🟠",
 "🟡",
 "🟢",
 "🔵",
 "🟣",
 "🟤",
 "⚫",
 "⚪",
)
# Əkmə Oğlum...!!!
reqem = (
 "0️⃣",
 "1️⃣",
 "2️⃣",
 "3️⃣",
 "4️⃣",
 "5️⃣",
 "6️⃣",
 "7️⃣",
 "8️⃣",
 "9️⃣",
)
# Əkmə Oğlum...!!!
ad = (
 "Şirin💞",
 "Dəcəl👀",
 "Əsəbi🤨",
 "Qorxulu😠",
 "Vəhşi😡",
 "Pişiy😺",
 "Ceyran🦌",
 "Nəfəs🌬️",
 "Ömür😍",
 "Bal🍯",
 "Ürəy❤️",
 "Evli💍",
 "Dəli😉",
 "Subay😜",
 "Sərxoş🥴",
 "Kəpənəy🦋",
 "Arı🐝",
 "Balıq🐠",
 "Sevimli😌",
 "Sehirbaz🎩",
 "Alim🎓",
 "Kral👑",
 "Gözəl💄",
 "Çirkin😒",
 "Meymun🙈",
 "Mələy😇",
 "Dovşan🐰",
 "Maral🦌",
 "Ulduz⭐",
 "Günəş🌅",
 "Vor📿",
 "Qıcıq😈",
 "Varlı💵",
 "Almaz💎",
 "Gül🌺",
 "Qızılgül🌹",
 "Bikef🙄",
 "Xəstə🤒",
 "Ufo🛸",
 "Şanslı🔮",
 "Avara🚬",
 "Futbolçu⚽",
 "Müğənni🎤",
 "A.Y.E🤘",
 "Qız♀️",
 "Oğlan♂️",
 "Gecə🌃",
 "Cücə🐥",
 "DON🕴️",
 "Məşuqə💃",
 "Gəlin👰",
 "Bəy🤵",
 "Covid19😷",
 "Joker🤡",
 "Ağıllı🧠",
 "Qardaş✊",
 "Saturn🪐",
 "Pullu🤑",
 "Susqun🤐",
 "Nevroz😤",
 "Güclü💪",
 "Virus🦠",
 "Usta👷",
 "Əsgər💂",
 "Üzgüçü🏊",
 "İdmançı🏋️",
 "Tülkü🦊",
 "Supermen🦸",
 "Zombi🧟",
 "Cin🧞",
 "Bəstəkar🎼",
 "Çiyələk🍓",
 "Nərgiz🌼",
 "Robot🤖",
 "İlan🐍",
 "Bahar💮",
 "Yazar✍️",
 "Payız🍂",
 "Qar❄️",
 "Qasırğa🌀",
 "Mesaj💌",
 "Vulkan🌋",
 "Pizza🍕",
 "Nənə🧓",
 "Soyuq🥶",
 "Dino🦕",
 "Ay🌙",
 "Meteor☄️",
 "Hicablı🧕",
 "Gözəl💅",
 "Alpen🍫",
 "Kofe☕",
 "Mişka🧸",
 "Alp🏔️",
 "Pubg🎮",
 "Popcorn🍿",
 "Qartal🦅",
 "Bozqurd🐺",
 "Rəssam🎨",
 "Panda🐼",
 "Aslan🦁",
)
# Əkmə Oğlum...!!!
emj = ['😇','🥰','😎','🤩','😍','👾','🤡','🥳','😻','😼','😽','💋','👸','🤴','🎅🏻','🤶','🧞‍♀️','🧞','🧞‍♂️','🧜‍♀️','🧜','🧚‍♀️','🧚','👑','💍','🕶','🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼','🐨','🐯','🦁','🐮','🐷','🐽','🐸','🐵','🙈','🙉','🙊','🐒','🐣','🐥','🦅','🐝','🦋','🐞','💐','🌹','🥀','🌺','🌸','🌼','🌻','⭐️','🌟','✨','⚡️','🔥','🌈','☃️','🍫','💅','🐺','🍫','🍕','☕','🧸','🦅','👩‍🦰','🎮','☄️','🌙','🦕','👨🏻‍✈️','🥶','🍿','👀','💀','💟','♥️','💘','💝','💗','💙','💛','🖤','🤑','⚡','😈','🤡','🎊','🔥','😼','💤','✊','👩‍🎨','🧕','🌼','💐','🌹','🥀','🌷','🌺','🌸','🏵️','🌻','🍂','🍁','🌾','🌱','🌿','🍃','☘️','🍀','🌵','🌴','🌳','🌲','🏞️','🌪️','☃️','⛄','❄️','🏔️','🌋','🙋','🤶','👩‍💼','🧓','🧔','💃','🕺','👩‍🦰','🪐','🦄','🐢','🐁','🐤','🐣','🐥','🦉','🐓','🕊️','🦢','🦩','🦈','🐬','🐋','🐳','🐟','🐠','🦚','🐡','🦐','🦞','🦀','🦑','🐙','🦂','🕷️','🕸️','🐜','🦗','🦟','🐝','🐞','🐾','🍓','🍒','🍎','🍉','🍊','🥭','🍍','🍋','🍇','🥝','🍐','🥥','🌶️','🍄','🍔','🧆','🥙','🦞','🍧','🍨','🍦','🥧','🍰','🍮','🎂','🧁','🍭','🍬','🍩','🍺','🍻','🥂','🍾','🍷']
# Əkmə Oğlum...!!!
cumle = (
 "Hayat yalansa gerçek sen ol!",
 "Biz insanların insan olanlarını severiz!",
 "İlahi Azrail, sen adamı öldürürsün.",
 "Dışarıda mucize arama, mucize sensin.",
 "Keşke seni kopyalayıp yanıma yapıştırabilsem…",
 "Son gülen sen olacaksın, çünkü geç anlıyorsun.",
 "Oğlumun adını mafya koydum, artık bir mafya babasıyım.",
 "Bir qızın ən şirin halı, ağlarkən gülməyə çalışanda ortaya çıxan üz ifadəsidir",
"Ya tutulacaq qədər yaxın ol, yada unudulacaq qədər uzaq...",
"Sənə Çox insan, 'Səni Sevirem' deyər... Ama Sadəcə biri Səni Gəlinliklə görmək isdər ...!",
"Gecə mesajlaşarkən sms-in ən şirin yerində,sizi qoyub öküz kimi yatan insana sevgili deyilir :D",
"Bir cümlə ilə xoşbəxtliyimi məhv edən xoşbəxt ol dedi ",
"Göy qurşağinin bitdiyi yerdə bir xəzinə var deyirler. Bir gün təqib etdim, bitdiyi yerdə sən vardın.!",
"Sevgi vaxtsiz gələn qonağın uşağı kimidir... Gələr dağıdar və gedər, səsini belə çıxara bilməzsən..."
"İnsan odun deyil ki, qırıldığı zaman səs çıxartsın... Səssiz-səmirsiz də qırılır bəzən...",
"🤖UserBot: Mesajlar uzun olduğu üçün hər istifadəçini 3 saniyə intervalı ilə tağ edirəm",
"Bir mənə bax görüm",
"Bir mənə bax görüm",
"Bir mənə bax görüm",
"Bir mənə bax görüm",
"Kiməm mən ?",
"Bayaqdan səni gözləyirəme mən 🙄",
"Bayaqdan səni gözləyirəme mən 🙄",
"Bayaqdan səni gözləyirəme mən 🙄",
"Bayaqdan səni gözləyirəme mən 🙄",
"Bayaqdan səni gözləyirəme mən 🙄",
"Bayaqdan səni gözləyirəme mən 🙄",
"Hardasanki sən ?",
"Mənə lazımdı bircədəfə görüm onu fsoo getdi ömrümün axrınacan",
"Bağlanmıyın a kişi kiməsə bax adamın burası ağrıyır",
"Bağlanmıyın a kişi kiməsə bax adamın burası ağrıyır",
"Salam",
"Necəsən",
"Salam necəsən ?",
"Gəl gəl görəy 😐",
"Təzə maşın almışam",
"Gəl desəm gələrsən ?",
"Gəl desəm gələrsən ?",
"Gəl desəm gələrsən ?",
"Gəl desəm gələrsən ?",
"Gəl desəm gələrsən ?",
"Gəl desəm gələrsən ?",
"bir iki adam var danisim gedirem",
"Xoş gəldin 🍾",
"Səhvlərdən yalnızca heç bir şey etməyən kəslər yayına bilər. Səhv etməkdən qorxmayın, səhvi təkrarlamaqdan qorxun.- Teodor Ruzvelt.",   
 "Böyük işi görə bilmənin yalnızca bir üsulu var- o işi sevməniz. - Stiv Cobs.   ",
  "Tırtılın həyatın sonu adlandırdığını ustad kəpənək adlandırır. - Riçard Bax.   ",
 "Xəyallarınızın arxasınca yürüməyin, onları təqib edin. - Riçard Damb.   ",
 "Uğurun asılı olduğu yeganə şərt səbrdir. - Lev Tolstoy.   ",
 "İnsanlarla düzgün rəftar, uğurun ən başlıca üsuludur. - Teodor Ruzvelt.   ",
  "Bəxtəvər insan o insandır ki, başqalarının hələ etməyə hazırlaşdığı işi o artıq həyata keçirmişdir.  ",
 "Hərəkətlər hər zaman xoşbəxtlik gətirmir, lakin onlar olmasa xoşbəxtlik heç olmaz. - Benjamin Dizraeli.   ",
 "Ən yaxşı motivasiya daxildən gəlir. - Maykl Jonson.   ",
 "Hər bir arzu sizlərə onu həyata keçirməkdə yardımcı olacaq qüvvələrlə verilir. - Riçard Bax.","Min mil ölçüsündə olan yol sadəcə bir addımla başlayır. - Lao Szı.   ",
 "Xoşbəxt olmaq qabiliyyəti elə özümüzdən asılıdır. - Şarlotta Bronte.",
   " Mən şəxsən çiyələklə qaymaq yeməyi sevirəm. Amma balıqlar qurd sevir. Ona görə də balıq tutmağa gedəndə mən öz sevdiyim yemək haqda deyil, balığın sevdiyi yemək haqda düşünürəm. Deyl Karnegi",
" Mənim çıxartdığım və hər zaman əməl etdiyim bir dərs var, cəhd etmək, cəhd etmək, yenə də cəhd etmək! Və heç vaxt təslim olmamaq! Riçard Brenson",
" Mən məğlubiyyətlərə dözmürdüm. Mən sadəcə 10 min yol tapırdım, hansılar ki, heç vaxt işləmirdi. Tomas Edison",
 "Mən bunu istəyirəmsə, deməli bu olacaq. Henri Ford",
"Bədbəxt, uğursuz, xoşbəxt və sağlam olmayan o adamdır ki, o tez-tez sabah sözünü işlədir. Robert Kiyosaki",
"Bizim ən böyük çatışmazlığımız ondadır ki, biz çox tez vaz keçirik. Uğura gedən yol yenidən cəhd etməkdən keçir. Tomas Edison",
" Həyatda bir dəfə bəxt insanın qapısını döyür, amma insan həmin vaxtı yaxınlıqdakı pivəxanada oturur və heç bir qapı səsi eşitmir. Mark Tven",
"Optimist bir insan ayaqqabıları oğurlanınca ayaqlarım var dəyə bilən insandır. Sokrat",
 "Kişilər qadınların ilk eşqi, qadınlar kişilərin son eşqi olmaq istər. Oskar Vayld",
 "Mal itirən bir şey itirmişdir, qürurunu itirən bir çox şey itirmişdir, lakin cəsarətini itirən hər şeyini itirmişdir. Höte",
"Çətinlikləri qarşılamanın iki yolu vardır; ya çətinlikləri dəyişdirərsiniz, ya da çətinlikləri həll etmək üçün özünüzü. Filis Botom.",
"Heç bir şey insan qədər yüksələ bilməz və onun qədər də alçala bilməz. Fridrix Holderlin",
"Müvəffəqiyyətin dörd şərti; bilmək, istəmək, cəsarət etmək və susmaq. Aksel Munte",
"Kiçik xərcləmələri gözdən qaçırmayın. Bəzən kiçik bir dəlik böyük bir gəmini batırar. Benjamin Franklin",
 "Düşmənlərinizi sevin, çünki qüsurlarınızı tək onlar açıqca söyləyə bilər. Benjamin Franklin",
 "Həyat o qədər qısadır ki, kiməsə nifrət edərək vaxt itirmə. Anonim",
"Keçmişinlə barış ki, gələcəyini zəhərə döndərməsin. Anonim",
"Həyatını başqalarının həyatı ilə müqayisə etmə. Hansı şərtlər altında bura gəlib çıxdıqlarını bilmirsən. Anonim",
"Həyatda nəyə marağın varsa, arxasınca getməli və bu yolda “yox” sözünü bir cavab olaraq qəbul etməməlisən. Anonim",
 "Xəstə olanda işin sənə baxmayacaq, dostların baxacaq. Əlaqələri kəsmə, dostlarına vaxt ayır. Anonim",
 "Unutma, səni öldürməyən şey, səni daha da güclü edir. Anonim",
 "Həyatı çox sorğu-sual etmə, hərəkətə keç və lazım olanı indi et. Anonim",
" Həyatda nəyə marağın varsa, arxasınca getməli və bu yolda “yox” sözünü bir cavab olaraq qəbul etməməlisən. Anonim",
 "Gözəl bağlanmış qutuda olmasa da, həyat yenə də bir hədiyyədir. Anonim",
 "Nəyəsə nail olacaqsan, yalnız taleyə müqavimət göstərərək…",
"Ola bilər ki, axın səni düşündüyün yerə aparmayacaq.",
"Əgər atdığın addım sənə çətindirsə, o zaman düşün və cavabla. Bu addımı atmağa ehtiyac duyursanmı?",
"Növbəti dəfə ya yaxşısını et, ya da başqa cür.",
"Əgər zaman, məkan, insanlar və hərəkət istiqaməti düzgün seçilməyibsə və nəticədə heç nə alınmırsa, təəccüblənmə.",
"Əgər sən öz səhvinin nəticələrini düzəldə bilirsənsə, demək ki, hələ səhv etməmisən.",
"Əgər sən büdrədinsə və yıxıldınsa, bu o demək deyil ki, sən ora getmirsən.",
"Yol yalnız hamar yerlərdən keçə bilməz.",
"Yolun eyni olan insanın arxasıyca get.",
"Sənin səhvlərin dünyanı dağıtmayacaq.",
"Özün üçün qorxma. Nahaqdan itməyə görə dünya üçün çox dəyərlisən.",
"Nə baş verirsə, vaxtında baş verir.",
"Nə baş verəcəksə, sənin həyatının yaxınlığında baş verəcək.",
"Ümidin sevincli hissləri üçün qaçırdılmış imkanlara təşəkkür et.",
"Dünyaya sənin xeyrin deyil, iştirakın lazımdır.",
"Əgər lazımdırsa əziyyət çək, amma öz əzablarını bu ehtiyaca görə doğrultma.",
"Asanmış kimi davran, bu zaman sənə daha asan görünəcək.",
"Sevinc az oldu deyə kədərlənmə: bununla sən sevincini kədərə çevirəcəksən.",
"Dadmağın və doymağın öz sevinci var. Bunları qarışdırma.",
"Arzu etmək olar ki, külək yox olsun. Arzu etmək olmaz ki, külək həmişəlik yox olsun.",
"Vaxtaşırı kimisə sevindir, heç olmasa özünü…",
"Harmoniya məqsəd deyil, vasitədir. Əgər sən onunla nə etməli olduğunu bilsən, onu tapacaqsan.",
"Pis heçnə yoxdur. Sənin xoşuna gəlməyən var.",
"Bəzən düzgün qərarın axtarışı səhvlərdən daha çətin keçir.",
"Çox deməkdən qorxma. Məgər sən nə dərəcədə demək lazım olduğunu bilmirsən?",
"Məqsədimiz mümkünsüzü mümkün etmək, mümkünü asan etmək, asanı da zərif və zövqlü etmənin yollarını tapmaqdır. Dr.Feldenkrais",
"Kifayət qədər səbəbiniz varsa, hər şeyi edə bilərsiniz. Jim Rohn",
"Həyatdan qorxmayın uşaqlar; yaxşı və doğru bir şeylər etdiyiniz zaman həyat elə gözəl ki! Dostoyevski",
"İnsanoğlunun içində yatan güclər vardır; özü bilsə çaşar. Çünki bu güclərə sahib olduğu ağılından belə keçməz. Bu gücləri oyandırıb hərəkətə keçirə bilən adamın həyatında böyük bir inqilab olar. Swett Marden",
"Möhtəşəm şeylər, ancaq içlərindəki bir şeyin, şərtlərin üzərində olduğuna inanma cəsarətini göstərənlər tərəfindən edilmişdir. Bruce Barton",
"Həyat bir velosipedə minmək kimidir. Pedalı fırlatmağa davam etdiyiniz müddətcə yıxılmazsınız.  Claude Pepper",
"Ümidlə yol getmək gediləcək yerə çatmaqdan daha gözəldir. Louis Stevenson",
"Bir işi doğru etmək, nə üçün yalnış etdiyini izah etməkdən daha az zaman aparır.  Henry Wodsworth",
"Dualarınıza diqqət edin. Həyata keçə bilər. Emerson",
"Məşğul ol, didin, düşün, axtar, tap, qaç. Dayanmaq zamanı keçdi çalışmaq zamanıdır. Tofiq Fikrət",
"Statistika nə deyir desin, hər vəziyyətdə müvəffəqiyyətə gedən bir yol vardır. Bemard Segeln",
"İnsana olanlar deyil, insanın içində olanlar əhəmiyyətlidir. Louis Mann",
"Mənfi düşünən adam, çiy bir yumurtanı bütün halda qabığıyla udmuş ​​bir adama bənzəyir. Yumurtanın qırılacağı qorxusuyla hərəkət edə bilməz, cücə çıxacağı qorxusuyla da hərəkətsiz dayana bilməz. Rus Atalar sözü",
"Yalnız işsiz olanların deyil, daha yaxşısını edə biləcək, amma etməyənlərin də başı boşdur. Sokrates",
"Batan günəş üçün ağlamayın; yenidən doğulduğunda nə edəcəyinizə qərar verin. Dale Camegie",
)
# Adlarla Tağ
@aykhan(outgoing=True, pattern="^.adtag.*")
async def t22(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozad = None
          aykhan1 = event.message.text.split(" ", 1)
          if len(aykhan1) > 1:
              sozad = aykhan1[1]
  
          chat = await event.get_input_chat()
          await event.delete()
  
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
          await event.delete()
  
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
          await event.delete()
  
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
          await event.delete()
  
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
          await event.delete()
  
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
  
@aykhan(outgoing=True, pattern="^.stoptag$")
async def restart(event):
    await event.edit("⛔ **Tağ prosesi dayandırıldı**")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#AYKHAN \n"
                                        "Tağ prosesi dayandırıldı")

    try:
        await bot.disconnect()
    except:
        pass

    execl(sys.executable, sys.executable, *sys.argv)
# Əkmə oğul...!!!
CmdHelp('tyeni').add_command(
    'adtag', None, '<Mesajınız> Dəyişiy adlarla tağ edir'
).add_command(
    'rgtag', None, '<Mesajınız> Rəngli tağ edir'
).add_command(
    'rqtag', None, '<Mesajınız> Rəqəmlərlə tağ edir'
).add_command(
    'emtag', None, '<Mesajınız> Emojilərlə tağ edir'
).add_command(
    'ctag', None, '<Mesajınız> Cümlələrlə və maraqlı sözlərlə tək tək tağ edir'
).add_command(
    'stoptag', None, '⛔Aktiv tağ prosesini dayandırır\n\n ✅Sahib - @aykhan_s'
).add()
