import wave
import struct


audio_file = wave.open("aaa.wav")
result_file = wave.open("res.wav", "wb")


CHANNELS = audio_file.getnchannels()
FORMAT = audio_file.getsampwidth()
RATE = audio_file.getframerate()
frames_count = audio_file.getnframes()
frames = audio_file.readframes(frames_count)

result_file.setnchannels(CHANNELS)
result_file.setsampwidth(FORMAT)
result_file.setframerate(RATE)


values = list(struct.unpack(f"<{frames_count*2}h", frames))

distorted = []

for i in range(len(values)):
    if i % 2 == 0:
        distorted.append(values[i])

frames = struct.pack(f"<{frames_count}h", *distorted)
result_file.writeframes(frames)
