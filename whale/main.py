import os
import asyncio
from io import BytesIO
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
from whale.speech.recognizer import SpeechRecognizer
from whale.speech.recognizer import UndefinedSpeechError
from whale.speech.utils import ogg_to_wav
from whale.res import String

VOICE_MESSAGE_LANGUAGE = "en-US"

bot = AsyncTeleBot(token=os.getenv("TOKEN"), parse_mode="html")
recognizer = SpeechRecognizer()


@bot.message_handler(commands="start", chat_types="private")
async def on_start_command_received(message: Message):
    """
    Triggers when /start message received in private chat.
    Bot sends description of itself
    :param message: Telegram's chat message
    """
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(String.AUTHOR_GITHUB_TEXT, String.AUTHOR_GITHUB_URL))
    await bot.send_message(message.chat.id, String.BOT_DESCRIPTION, reply_markup=markup)


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
        voice_ogg_bytes = BytesIO(await bot.download_file(voice_file.file_path))
        text = recognizer.recognize_from_source(
            ogg_to_wav(voice_ogg_bytes),
            VOICE_MESSAGE_LANGUAGE
        )
        await bot.reply_to(message, text)
    except UndefinedSpeechError:
        await bot.reply_to(message, String.RECOGNIZER_ERROR)


if __name__ == "__main__":
    asyncio.run(bot.infinity_polling())
