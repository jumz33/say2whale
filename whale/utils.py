from io import BytesIO
from pydub import AudioSegment


def telegram_bytes_to_wav(source: str | bytes | BytesIO) -> BytesIO:
    segment = AudioSegment.from_ogg(source)
    return segment.export(
        BytesIO(),
        format="wav"
    )
