from pytubefix import YouTube
from pytubefix.cli import on_progress

def youtube_download(mp3_or_mp4,url_input):
    try:
        yt = YouTube(url_input, on_progress_callback=on_progress)
        print(yt.title)
        if "".join(mp3_or_mp4.split()) == "+":
            ys = yt.streams.get_highest_resolution()
            ys.download()
            print("The video mp4 was downloaded!")
        else:
            ys = yt.streams.get_audio_only()
            ys.download(mp3=True)
            print("The audio mp3 was downloaded!")
    except Exception as e:
        print(f"Error message: {e}")
    input("Press to quit...")
def tik_tok_download():
    pass
def instagram_download():
    pass
def reddit_download():
    pass
def main():
    url_input = input("Youtube url:")
    mp3_or_mp4 = input("Select format (Type + for MP4 or - for MP3):")
    youtube_download(mp3_or_mp4,url_input)

if __name__ == "__main__":
    main()