import os
import random
from moviepy import *
from moviepy.audio.fx import AudioFadeOut

if not os.path.exists("./output"):
    os.makedirs("./output")


def mix_sounds(path_music, path_recite, o):
    music_clips = [AudioFileClip(m) for m in path_music]
    recite_clip = AudioFileClip(path_recite)

    connected_music = concatenate_audioclips(music_clips).with_volume_scaled(0.35)

    mixed_audio = CompositeAudioClip([connected_music, recite_clip])
    mixed_audio = mixed_audio.subclipped(0, end_time=recite_clip.end)
    mixed_audio = mixed_audio.with_effects([AudioFadeOut(6)])

    mixed_audio.write_audiofile(o)

error = 0

for part in os.listdir("./recite"):
    print(f"Start to mix sound in {part}")
    if not os.path.exists(f"./output/{part}"):
        os.makedirs(f"./output/{part}")
    for file in os.listdir(f"./recite/{part}"):
        try:
            musics = ['./music/' + f for f in random.choices(os.listdir("./music"), k=3)]
            recite = f"./recite/{part}/" + file
            output = f"./output/{part}/" + os.path.splitext(file)[0] + ".mp3"

            print(f"-=||=- Mixing sound : {musics} with recite : {recite}. Output to : {output}")
            mix_sounds(musics, recite, output)
        except Exception as e:
            error += 1
            print("Error:", e)

print(f"\n\nFinished with {error} errors.")