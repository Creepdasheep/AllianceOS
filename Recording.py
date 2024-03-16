import pyaudio
import wave
import keyboard

class AudioRecorder:
    def __init__(self, output_filename="output.wav"):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.output_filename = output_filename

    def record(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.FORMAT, channels=self.CHANNELS,
                            rate=self.RATE, input=True,
                            frames_per_buffer=self.CHUNK)

        print("Recording... Press 'q' to stop recording.")

        frames = []

        while not keyboard.is_pressed('q'):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("Recording stopped.")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        with wave.open(self.output_filename, 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(audio.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))

        print("Audio saved as:", self.output_filename)

if __name__ == "__main__":
    recorder = AudioRecorder()
    recorder.record()
