from io import BytesIO
from pydub import AudioSegment


def ogg_to_wav(source: BytesIO) -> BytesIO:
    """
    Converts OGG to WAV.

    :param source: OGG bytes
    :return: WAV bytes
    """

    segment = AudioSegment.from_ogg(source)
    return segment.export(BytesIO(), format="wav")
