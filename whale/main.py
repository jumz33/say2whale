import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from whale.speech import SpeechRecognizer, UnableToRecognizeError
from whale.utils import telegram_bytes_to_wav
from whale.settings import (
    ERROR_TEXT,
    BOT_STICKER,
    BOT_TEXT_MARKUP,
    AUTHOR_GITHUB_TEXT,
    AUTHOR_GITHUB_URL,
    SPEECH_RECOGNIZER_LANGUAGE
)

bot = AsyncTeleBot(
    token=os.environ.get("TOKEN"),
    parse_mode="html",
    disable_notification=True
)
recognizer = SpeechRecognizer()


@bot.message_handler(commands="start", chat_types="private")
async def on_help_command_received(message: Message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(AUTHOR_GITHUB_TEXT, AUTHOR_GITHUB_URL))

    await bot.send_sticker(message.chat.id, BOT_STICKER)
    await bot.send_message(message.chat.id, BOT_TEXT_MARKUP, reply_markup=markup)


@bot.message_handler(content_types="voice", chat_types="private")
async def on_voice_message_received(message: Message):
    try:
        file = await bot.get_file(message.voice.file_id)
        file_bytes = await bot.download_file(file.file_path)
        text = recognizer.recognize_from_wav(
            telegram_bytes_to_wav(file_bytes),
            SPEECH_RECOGNIZER_LANGUAGE
        )
    except UnableToRecognizeError:
        text = ERROR_TEXT

    await bot.reply_to(message, text)


if __name__ == "__main__":
    asyncio.run(bot.infinity_polling())
