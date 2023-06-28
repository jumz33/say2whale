from io import BytesIO
from speech_recognition import (
    Recognizer,
    AudioFile,
    UnknownValueError
)


class SpeechRecognizer:
    def __init__(self):
        self._recognizer = Recognizer()

    def recognize_from_wav(self, source: BytesIO | str, language: str):
        audio_data = self._record_audio_data_from_source(source)
        return self._try_to_recognize_from_audio_data(audio_data, language)

    def _record_audio_data_from_source(self, source):
        with AudioFile(source) as audio:
            self._recognizer.adjust_for_ambient_noise(audio)
            return self._recognizer.record(audio)

    def _try_to_recognize_from_audio_data(self, audio_data, language):
        try:
            return self._recognizer.recognize_google(
                audio_data=audio_data,
                language=language
            )
        except UnknownValueError:
            raise UnableToRecognizeError("unable to recognize speech")


class SpeechRecognizerException(Exception):
    pass


class UnableToRecognizeError(SpeechRecognizerException):
    pass
