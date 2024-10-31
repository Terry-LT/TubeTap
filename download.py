import validators
import instaloader
from urllib.parse import urlparse
from pytubefix import YouTube
from pytubefix.cli import on_progress
from RedDownloader import RedDownloader

def remove_white_space(text):
    return "".join(text.split())

class Video:
    video_url = ""
    supported_social_media_links = [
        "www.youtube.com",
        "youtu.be",
        "www.instagram.com",
        "www.reddit.com"
    ]
    domain = None
    def __init__(self,video_url):
        if validators.url(video_url):
            domain = urlparse(video_url).netloc
            if domain not in self.supported_social_media_links:
                print(f"Currently, we do not support domain {domain}")
            else:
                self.domain = domain
                self.video_url = video_url
        else:
            print("The url is not valid")
    def _youtube_download(self,mp3_or_mp4):
        try:
            yt = YouTube(self.video_url, on_progress_callback=on_progress)
            print(yt.title)
            if remove_white_space(mp3_or_mp4) == "+":
                ys = yt.streams.get_highest_resolution()
                ys.download()
                print("The video mp4 was downloaded!")
            else:
                ys = yt.streams.get_audio_only()
                ys.download(mp3=True)
                print("The audio mp3 was downloaded!")
        except Exception as e:
            print(f"Error message: {e}")

    def _instagram_download(self):
        # Create an Instaloader instance
        loader = instaloader.Instaloader()
        # Extract the shortcode from the URL (if it's a full URL)
        shortcode = self.video_url.split("/")[-2]
        # Download the post
        try:
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            loader.download_post(post, target=f"{post.owner_username}_{post.shortcode}")
            print("Download successful!")
        except Exception as e:
            print(f"An error occurred: {e}")

    def _tik_tok_download(self):
        pass

    def _reddit_download(self):
        try:
            RedDownloader.Download(self.video_url)
        except Exception as e:
            print(f"An error occurred: {e}")
    def download(self):
        if self.domain is not None:
            if (self.domain == self.supported_social_media_links[0]) or (
                    self.domain == self.supported_social_media_links[1]):
                mp3_or_mp4 = input("Select format (Type + for MP4 or - for MP3):")
                self._youtube_download(mp3_or_mp4)
            elif self.domain == self.supported_social_media_links[2]:
                self._instagram_download()
            elif self.domain == self.supported_social_media_links[3]:
                self._reddit_download()
