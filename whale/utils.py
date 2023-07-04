from io import BytesIO
from pydub import AudioSegment


def ogg_to_wav(source: str | BytesIO, out: str | BytesIO) -> BytesIO | str:
    segment = AudioSegment.from_ogg(source)
    return segment.export(out, format="wav")
