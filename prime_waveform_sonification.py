# -*- coding: utf-8 -*-
"""Prime Waveform Sonification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IS-fCjUA8S9oV5Nj1Ej7ouCCCqQpJsPO
"""

# 📦 Install dependencies (run this cell once)
!pip install numpy pandas scipy matplotlib pydub --quiet

# 🔧 Import libraries
import numpy as np
import pandas as pd
from scipy.io.wavfile import write as wav_write
from IPython.display import Audio
import os

# 🧠 Load your CSV file (Upload manually in Colab files section)
# Make sure it has headers like: "log_midpoint", "alt_gap"
filename = "/content/prime_waveform_coords_100000.csv"  # <-- change if different

df = pd.read_csv(filename)

# 🧹 Drop NA or bad rows if any
df = df.dropna()

# 🎯 Settings
sample_rate = 44100  # CD-quality
tone_duration = 0.1  # base duration in seconds
volume = 0.5
base_freq = 220.0  # base frequency for scaling
duration_scaling = 0.06  # how quickly to progress through timeline

# 🎼 Convert a single note to stereo waveform
def generate_stereo_tone(freq, duration, left=1.0, right=1.0):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * freq * t)
    left_channel = wave * left * volume
    right_channel = wave * right * volume
    stereo = np.vstack([left_channel, right_channel]).T
    return stereo.astype(np.float32)

# 🔊 Prepare stereo audio track
track = []

for i in range(len(df)):
    x = df.iloc[i]["log_midpoint"]
    y = df.iloc[i]["alt_gap"]

    freq = base_freq + abs(y) * 10  # map gap to frequency
    dur = duration_scaling  # can use x for timing if you want variable pacing

    if y > 0:
        tone = generate_stereo_tone(freq, dur, left=0.0, right=1.0)
    else:
        tone = generate_stereo_tone(freq, dur, left=1.0, right=0.0)

    track.append(tone)

# 🧩 Combine all audio
final_audio = np.concatenate(track)

# 💾 Save to WAV
output_file = "prime_waveform_stereo.wav"
wav_write(output_file, sample_rate, (final_audio * 32767).astype(np.int16))

# ▶️ Playback in notebook
Audio(output_file)