from io import BytesIO
from speech_recognition import (
    Recognizer,
    AudioFile,
    UnknownValueError,
    AudioData,
    RequestError
)


class SpeechRecognizer:
    """
    Class that used for recognize speech in audio files via Google Recognition API.
    """

    def __init__(self):
        self._recognizer = Recognizer()

    def recognize_from_source(self, source: BytesIO | str, language: str) -> str:
        """
        Recognizes speech from given source.

        :param source: WAV/AIFF/AIFF-C/FLAC file path, also can be :class:`io.BytesIO`
        :param language: RFC5646 string language tag (like 'en-US' or 'fr-FR')
        :return: recognized string speech from source
        :raises UnknownSpeechError: if source is unrecognizable
        :raises ConnectionLostError: if API or Internet connection lost

        .. note::
            WAV files must be in PCM/LPCM format.
            WAVE_FORMAT_EXTENSIBLE and compressed WAV are not supported
            and may result in undefined behaviour.

            FLAC files must be in native FLAC format.
            OGG-FLAC is not supported and may result in undefined behaviour.
        """

        audio_data = self._record_audio_data_from_source(source)
        return self._try_to_recognize_from_audio_data(audio_data, language)

    def _record_audio_data_from_source(self, source: BytesIO | str) -> AudioData:
        with AudioFile(source) as audio:
            self._recognizer.adjust_for_ambient_noise(audio)
            return self._recognizer.record(audio)

    def _try_to_recognize_from_audio_data(self, audio_data: AudioData, language: str) -> str:
        try:
            return self._recognizer.recognize_google(
                audio_data=audio_data,
                language=language
            )
        except UnknownValueError as exc:
            raise UnknownSpeechError from exc
        except RequestError as exc:
            raise ConnectionLostError from exc


class SpeechRecognizerException(Exception):
    pass


class UnknownSpeechError(SpeechRecognizerException):
    pass


class ConnectionLostError(SpeechRecognizerException):
    pass
