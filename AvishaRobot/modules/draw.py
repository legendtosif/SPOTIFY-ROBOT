from pyrogram import filters
from pyrogram.types import  Message
from pyrogram.types import InputMediaPhoto
from AvishaRobot import pbot as  Avisha, BOT_USERNAME
from MukeshAPI import api
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatAction,ParseMode

####
EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/Avishaxbot?startgroup=true"),
    ],
]

####

@Avisha.on_message(filters.command("draw"))
async def imagine_(b, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:

        text =message.text.split(None, 1)[1]
    avisha=await message.reply_text( "🎨")
    try:
        await b.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        x=api.ai_image(text)
        with open("avisha.jpg", 'wb') as f:
            f.write(x)
        caption = f"""⬤ ᴅʀᴀᴡɪɴɢ ɪᴍɢ ʙʏ ➥ ˹ ᴀᴠɪsʜᴀ ꭙ ʀᴏʙᴏᴛ™ ♡゙ """
        await avisha.delete()
        await message.reply_photo("avisha.jpg",caption=caption, reply_markup=InlineKeyboardMarkup(EVAA), quote=True)
    except Exception as e:
        await avisha.edit_text(f"error {e}")

