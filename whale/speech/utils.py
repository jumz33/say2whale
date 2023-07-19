from io import BytesIO
from pydub import AudioSegment


def ogg_to_wav(source: str | BytesIO, out: str | BytesIO) -> BytesIO | str:
    """
    Converts OGG to WAV.

    :param source: OGG file path or :class:`io.BytesIO` object
    :param out: WAV file path or :class:`io.BytesIO` object
    :return: out WAV file path or :class:`io.BytesIO` object
    """

    segment = AudioSegment.from_ogg(source)
    return segment.export(out, format="wav")
