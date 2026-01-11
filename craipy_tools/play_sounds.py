import sys
import time
import math
import struct
import io
import wave


PLATFORM = sys.platform

if PLATFORM == "win32":
	import winsound


	def generate_silence(duration_ms):
		sample_rate = 44100
		num_samples = int(sample_rate * (duration_ms / 1000.0))
		return struct.pack('<' + ('h' * num_samples), *[0] * num_samples)


	def generate_tone(frequency, duration_ms):
		sample_rate = 44100
		num_samples = int(sample_rate * (duration_ms / 1000.0))
		amplitude = 16000

		audio = []
		for x in range(num_samples):
			sample = int(amplitude * math.sin(2 * math.pi * frequency * (x / sample_rate)))
			audio.append(sample)
		return struct.pack('<' + ('h' * len(audio)), *audio)


	def play_sound(sound: str, n_times: int = 1, sleep_time: float = 0.5) -> None:
		sound = sound.lower()

		if sound == "test":
			melody = [(1000, 100)]
		elif sound == "mozart":
			G4, D4, B4, D5 = 392, 294, 494, 587
			C5, A4, Fs4 = 523, 440, 370
			melody = [ (G4, 500), (D4, 500), (G4, 500), (D4, 500), (G4, 250), (D4, 250), (G4, 250), (B4, 250), (D5, 1000), (0, 250), (C5, 500), (A4, 500), (C5, 500), (A4, 500), (C5, 250), (A4, 250), (Fs4, 250), (A4, 250), (D5, 1000), (0, 250), (G4, 500), (D4, 500), (G4, 500), (D4, 500), (G4, 250), (D4, 250), (G4, 250), (B4, 250), (D5, 1000), (0, 250)]
		elif sound == "ok":
			melody = [(523, 100), (880, 200)]
		elif sound == "error":
			melody = [(440, 250), (311, 400)]
		else:
			raise Exception(f"Sound '{sound}' not found.")

		wav_buffer = io.BytesIO()

		with wave.open(wav_buffer, 'wb') as wav_file:
			wav_file.setnchannels(1)
			wav_file.setsampwidth(2)
			wav_file.setframerate(44100)

			for i in range(n_times):
				for freq, duration in melody:
					wav_file.writeframes(generate_tone(freq, duration))
				if i < n_times - 1:
					wav_file.writeframes(generate_silence(sleep_time * 1000))

		wav_data = wav_buffer.getvalue()
		winsound.PlaySound(wav_data, winsound.SND_MEMORY)

else:
	def play_sound(sound: str, n_times: int, sleep_time: float) -> None:
		print(f"Audio not implemented for {PLATFORM}")