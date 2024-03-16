import numpy as np
import time
from scipy.io.wavfile import write

# Function to generate audio signal for a given frequency and duration
def generate_audio(frequency, duration, volume=0.5, sample_rate=44100):
    num_samples = int(duration * sample_rate)
    time_axis = np.linspace(0, duration, num_samples)
    audio_data = np.sin(2 * np.pi * frequency * time_axis) * volume
    return audio_data

# Example mapping of binary values to frequencies
frequency_mapping = {'0': 200, '1': 500}

# Example code to communicate
code = ("""

import numpy as np
import time
from scipy.io.wavfile import write

# Function to generate audio signal for a given frequency and duration
def generate_audio(frequency, duration, volume=0.5, sample_rate=44100):
    num_samples = int(duration * sample_rate)
    time_axis = np.linspace(0, duration, num_samples)
    audio_data = np.sin(2 * np.pi * frequency * time_axis) * volume
    return audio_data

# Example mapping of binary values to frequencies
frequency_mapping = {'0': 200, '1': 500}

code = input()

# Convert code to binary
binary_code = ''.join(format(ord(char), '08b') for char in code)

# Generate audio signals and save to file
all_audio_data = []
for bit in binary_code:
    frequency = frequency_mapping[bit]
    audio_data = generate_audio(frequency, 0.1)  # Play each bit for 0.1 seconds
    all_audio_data.append(audio_data)
    time.sleep(0.05)  # Add a slight delay between each bit

# Concatenate all audio data
concatenated_audio = np.concatenate(all_audio_data)

# Normalize audio data to be between -1 and 1
normalized_audio = np.int16(concatenated_audio / np.max(np.abs(concatenated_audio)) * 32767)

# Save audio data to a WAV file
write("output_audio.wav", 44100, normalized_audio)

""")

# Convert code to binary
binary_code = ''.join(format(ord(char), '08b') for char in code)

# Generate audio signals and save to file
all_audio_data = []
for bit in binary_code:
    frequency = frequency_mapping[bit]
    audio_data = generate_audio(frequency, 0.1)  # Play each bit for 0.1 seconds
    all_audio_data.append(audio_data)
    time.sleep(0.05)  # Add a slight delay between each bit

# Concatenate all audio data
concatenated_audio = np.concatenate(all_audio_data)

# Normalize audio data to be between -1 and 1
normalized_audio = np.int16(concatenated_audio / np.max(np.abs(concatenated_audio)) * 32767)

# Save audio data to a WAV file
write("output_audio.wav", 44100, normalized_audio)
