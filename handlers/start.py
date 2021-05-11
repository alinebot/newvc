from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
I am 𝗠𝘂𝘀𝗶𝗰𝗕𝗼𝘁 VC Music Player, an open-source bot that lets you play music in your Telegram groups.
For source code Join our support group @MusicBotEnjoy_group.
/help to know my commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support⚡️", url="https://t.me/MusicBotEnjoy_group"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Creater⚡️", url="https://t.me/XDENVIL"
                    ),
                    InlineKeyboardButton(
                        "Friend chatting here⚡️", url="https://t.me/chatting_friendship"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Add To Your Group⚡️", url="https://t.me/Denvilmusicbot?startgroup=true"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
