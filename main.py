import wave
import struct


audio_file = wave.open("input.wav")
result_file = wave.open("res.wav", "wb")


CHANNELS = audio_file.getnchannels()
FORMAT = audio_file.getsampwidth()
RATE = audio_file.getframerate()
frames_count = audio_file.getnframes()
frames = audio_file.readframes(frames_count)

result_file.setnchannels(CHANNELS)
result_file.setsampwidth(FORMAT)
result_file.setframerate(RATE)


def slow_sound(values, channels):
    distorted = []
    for i in range(1, len(values)):
        distorted.append(values[i-1])
        if channels == 2:
            distorted.append([(values[i-1][0] + values[i][0]) // 2, (values[i-1][1] + values[i][1]) // 2])
        else:
            distorted.append([(values[i-1][0] + values[i][0]) // 2])
    distorted.append(values[len(values)-1])
    return distorted


def speedup_sound(values):
    distorted = []
    for i in range(len(values)):
        if i % 2 == 0:
            distorted.append(values[i])
    return distorted


def reverse_sound(values):
    return list(values.__reversed__())


def pairs_unpack(in_list):
    out_list = []
    for x in in_list:
        out_list += x
    return out_list


def pairs_pack(values, channels):
    out_list = []
    if channels == 2:
        for i in range(0, len(values), 2):
            out_list.append([values[i], values[i+1]])
    else:
        for i in range(len(values)):
            out_list.append([values[i]])
    return out_list


values = list(struct.unpack(f"<{frames_count*CHANNELS}h", frames))


paired_values = pairs_pack(values, CHANNELS)


out_values = pairs_unpack(speedup_sound(slow_sound(paired_values, CHANNELS)))


frames = struct.pack(f"<{len(out_values)}h", *out_values)
result_file.writeframes(frames)
