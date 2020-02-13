# this will play sounds with python

# mixer.init()
# mixer.music.load('C:/Users/Brian Culberson/Downloads/Post Malone - Circles (Lyrics).mp3')
# # mixer.music.load('e:/LOCAL/Betrayer/Metalik Klinik1-Anak Sekolah.mp3')
# mixer.music.play()
# while True:
#     stop = input("quit to stop")
#     if stop == "quit":
#         mixer.music.stop()
#         break

# import pyttsx
# engine = pyttsx.init()
# engine.say("I will speak this text")
# engine.runAndWait()

defaultstring = 'Hello, This is the W,8,Y,X repeater'
from gtts import gTTS
from pygame import mixer
from time import sleep
import sys
import youtube_dl
from io import BytesIO


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'file.mp3',
    'extractaudio': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


# mystring = str(sys.argv[1])

def speak(input):
    mystring = input
    if mystring == '::youtube':
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            filenames = sys.argv[2:]
            ydl.download(filenames)
    elif mystring == '':
        mystring = defaultstring
    # else:
        # mystring = str(sys.argv[1:])

    print(mystring)
    if mystring != '::youtube':
        tts = gTTS(text=mystring)
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        # print(mp3_fp.seek(0))
        # tts.save('file.mp3')
        mixer.init()
        mp3_fp.seek(0)
        mixer.music.load(mp3_fp)
        mixer.music.play()


        # this is for the playing of files in python
        # mixer.init()
        # mixere.music.load(filename)
        # mixer.music.play()
        # song = MP3(filename)
        # songLength = song.info.length
        # sleep(songLength)
        # mixer.music.stop()

    else:
        # mystring is ::youtube
        mixer.init()
        mixer.music.load('file.mp3')
        song = MP3('file.mp3')
        songLength = song.info.length
        mixer.music.play()
        sleep(songLength)
        mixer.music.stop()

