import pyaudio
import numpy as np
import math

# Constants
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def calculate_volume(data):
    # Convert raw data to numpy array
    audio_data = np.frombuffer(data, dtype=np.int16)
    # Calculate RMS (Root Mean Square) of the audio signal
    rms = np.sqrt(np.mean(np.square(audio_data)))
    # Convert RMS to dB
    if rms > 0:
        volume = 20 * math.log10(rms)
    else:
        volume = 0
    # Normalize volume to a range of 1-255
    normalized_volume = int((volume + 60) * (255 / 60))
    # Clip the value to make sure it stays within the valid range
    return max(0, min(normalized_volume, 255))

def detect():
    p = pyaudio.PyAudio()

    # Open stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    try:
        # Read audio data from stream
        data = stream.read(CHUNK)
        # Calculate volume
        volume = calculate_volume(data)
        print("Volume:", volume)
    except KeyboardInterrupt:
        print("Stopped by user")

    # Stop stream
    stream.stop_stream()
    stream.close()

    # Close PyAudio
    p.terminate()
