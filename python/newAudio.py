import numpy as np
import librosa 
from pydub import AudioSegment

pcm_data = np.fromfile("/home/plutoSDR/dev/txdata.pcm", dtype=np.int16)

audio = AudioSegment(
    data=pcm_data.tobytes(),
    sample_width=4,      # 2 байта = 16 бит
    frame_rate=44100,    # частота дискретизации
    channels=1           # моно
)
audio.export("../audio/new_ugar.mp3", format="mp3", bitrate="192k")
