import wave, struct

audio_file = wave.open("aaa.wav")
result_file = wave.open("res.wav", "wb")


CHANNELS = audio_file.getnchannels() # количество каналов
FORMAT = audio_file.getsampwidth() # глубина звука
RATE = audio_file.getframerate() # частота дискретизации
frames_count = audio_file.getnframes()
frames = audio_file.readframes(frames_count)


result_file.setnchannels(CHANNELS) # количество каналов
result_file.setsampwidth(FORMAT) # глубина звука
result_file.setframerate(RATE) # частота дискретизации


values = list(struct.unpack(f"<{frames_count}h", frames))

distorted = []

for i in range(len(values)):
    if i % 3 in {1, 2}:
        values[i] *= 10
        distorted.append(values[i])



frames = struct.pack(f"<{frames_count // 3 * 2}h", *distorted)
result_file.writeframes(frames)


