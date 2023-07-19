import os
import asyncio
from io import BytesIO
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from whale.speech.recognizer import SpeechRecognizer, UnknownSpeechError, ConnectionLostError
from whale.speech.utils import ogg_to_wav
from whale import settings
from whale.resources import Bot, Author, ErrorText


bot = AsyncTeleBot(
    token=os.getenv("TOKEN"),
    parse_mode=settings.BOT_PARSE_MODE,
    disable_notification=settings.BOT_DISABLE_NOTIFICATION
)
recognizer = SpeechRecognizer()


@bot.message_handler(commands="start", chat_types="private")
async def on_start_command_received(message: Message):
    """
    Triggers when /start message received in private chat.
    Bot sends description of itself

    :param message: Telegram's chat message
    """

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(Author.GITHUB_TEXT, Author.GITHUB_URL))

    await bot.send_message(message.chat.id, Bot.DESCRIPTION, reply_markup=markup)


@bot.message_handler(content_types="voice", chat_types="private")
async def on_voice_message_received(message: Message):
    """
    Triggers when voice message received in private chat.
    Bot replies with recognized text in this message,
    if it cannot recognize, replies with error text.

    :param message: Telegram's chat message
    """

    try:
        voice_file = await bot.get_file(message.voice.file_id)
        voice_ogg_bytes = await bot.download_file(voice_file.file_path)
        text = recognizer.recognize_from_source(
            ogg_to_wav(BytesIO(voice_ogg_bytes), BytesIO()),
            settings.VOICE_MESSAGE_LANGUAGE
        )
        await bot.reply_to(message, text)
    except UnknownSpeechError:
        await bot.reply_to(message, ErrorText.RECOGNIZER_UNKNOWN_SPEECH)


if __name__ == "__main__":
    asyncio.run(bot.infinity_polling())
