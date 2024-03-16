from scipy.io import wavfile
import numpy as np

class AudioDemodulator:
    def __init__(self, filename):
        self.filename = filename
        self.sample_rate = None
        self.audio_data = None
        self.frequency_mapping_reverse = {200: '0', 500: '1'}

    def load_audio(self):
        self.sample_rate, self.audio_data = wavfile.read(self.filename)

    def demodulate_audio(self):
        if self.sample_rate is None or self.audio_data is None:
            raise ValueError("Audio data not loaded. Call load_audio() first.")

        bit_duration = int(self.sample_rate * 0.1)  # Duration of each bit
        bits = []

        for i in range(0, len(self.audio_data), bit_duration):
            chunk = self.audio_data[i:i + bit_duration]
            fft_result = np.fft.fft(chunk)

            # Find the dominant frequency in the chunk
            freqs = np.fft.fftfreq(len(chunk), 1 / self.sample_rate)
            dominant_freq = np.abs(freqs[np.argmax(np.abs(fft_result))])

            # Determine the corresponding bit
            nearest_frequency = min(self.frequency_mapping_reverse.keys(), key=lambda x: abs(x - dominant_freq))
            bit = self.frequency_mapping_reverse[nearest_frequency]
            bits.append(bit)

        return ''.join(bits)

    @staticmethod
    def binary_to_text(binary_code):
        return ''.join(chr(int(binary_code[i:i + 8], 2)) for i in range(0, len(binary_code), 8))

    def process_audio(self):
        binary_code = self.demodulate_audio()
        return self.binary_to_text(binary_code)