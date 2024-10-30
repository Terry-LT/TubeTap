from download import Video

def main():
    video_url = input("Url:")
    video = Video(video_url)
    video.download()
    input("Press to quit...")

if __name__ == "__main__":
    main()