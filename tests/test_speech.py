from whale.speech import SpeechRecognizer
from whale.utils import telegram_bytes_to_wav

SOURCE_WAV_1_EN = "./data/enUS_speech1.wav"
SOURCE_WAV_2_EN = "./data/enUS_speech2.wav"
SOURCE_OGG_1_RU = "./data/ruRU_speech1.ogg"

recognizer = SpeechRecognizer()

print(recognizer.recognize_from_wav(SOURCE_WAV_1_EN, "en-US"))
print(recognizer.recognize_from_wav(SOURCE_WAV_2_EN, "en-US"))
print(recognizer.recognize_from_wav(telegram_bytes_to_wav(SOURCE_OGG_1_RU), "ru-RU"))
