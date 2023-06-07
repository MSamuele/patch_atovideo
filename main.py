import os
import subprocess
#from pocketsphinx import LiveSpeech, AudioFile
import pysrt
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
from sympy.physics.units import *

import whisper
from whisper.utils import get_writer





pwd = os.getcwd()
path = "C:\\Users\\samum\\Desktop\\posts"
audio_path = "C:\\Users\\samum\\Desktop\\posts\\audio"
video_path = "C:\\Users\\samum\\Desktop\\posts\\video"
t_path = "C:\\Users\\samum\\Desktop\\posts\\text"

def capts():

    model = whisper.load_model("base")
    audio = audio_path+"//"+"crypticsage.wav"
    result = model.transcribe(audio)
    output_directory = "./"

    # Save as an SRT file
    srt_writer = get_writer("srt", output_directory)
    srt_writer(result, audio)

    # Save as a VTT file
    vtt_writer = get_writer("vtt", output_directory)
    vtt_writer(result, audio)

def read_names(p):
    list = []

    files = os.listdir(p)
    for file in files:
            list.append(file)  # [0] necessario, altrimenti gli elementi della lista sarebbero stati liste loro stessi, in quanto
            # re.findall restituisce una lista
    # print(list)
    return list



def start():
    #capts()

    #ac = AudioFileClip("C:\\Users\\samum\\Desktop\\posts\\audio\\crypticsage.wav")
    #vc = VideoFileClip("C:\\Users\\samum\\Desktop\\posts\\video\\v1.mp4").subclip(0, ac.duration)
    #vc = vc.without_audio()
    #os.chdir(path)
    #final_clip = vc.set_audio(ac)
    #os.chdir(pwd)
    #final_clip.write_videofile("tiprego.mp4")

    os.chdir(pwd)
    command = "ffmpeg  -i \"tiprego.mp4\" -vf subtitles=crypticsage.srt:force_style=\'Fontname=Simplicity.ttf,FontSize=24\' \"ti_imploro.mp4\""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.returncode)

    #list = read_names(path+"\\audio")
    #print(list)
    #for a in list:
    #    video_clip = VideoFileClip(video_path+"\\"+"v1.mp4")
    #    audio_clip = AudioFileClip(audio_path+"\\"+a)
    #    final_clip = video_clip.set_audio(audio_clip)

    #    os.chdir(path)
    #    final_clip.write_videofile(a+".mp4")

    #    os.chdir(pwd)

start()


