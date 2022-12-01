from pytube import YouTube

print("Füge den Link ein!")
link = input("")
yt = YouTube(link)

print("Möchtest du Audio(1) oder Audio und Video(2)?")
audio_video = int(input(""))

print("")
print(f"Titel: {yt.title}\n") # Number of views of video
print(f"Gesehen: {yt.views} mal\n") # Length of the video
print(f"Länge: {yt.length} sek.") # Description of video

if audio_video == 1:
    ys = yt.streams.get_audio_only()
    ys.download()
    print("Fertig!")
if audio_video == 2:
    ys = yt.streams.get_highest_resolution()
    ys.download()
    print()
    print("Fertig!")

_ = input("Drücken Sie ENTER zum Beenden.")