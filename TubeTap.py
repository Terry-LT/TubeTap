import instaloader
from pytubefix import YouTube
from pytubefix.cli import on_progress
from RedDownloader import RedDownloader

def remove_white_space(text):
    return "".join(text.split())
def youtube_download(mp3_or_mp4,url_input):
    try:
        yt = YouTube(url_input, on_progress_callback=on_progress)
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

def instagram_download(post_url):
    # Create an Instaloader instance
    loader = instaloader.Instaloader()
    # Extract the shortcode from the URL (if it's a full URL)
    shortcode = post_url.split("/")[-2]
    # Download the post
    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=f"{post.owner_username}_{post.shortcode}")
        print("Download successful!")
    except Exception as e:
        print(f"An error occurred: {e}")

def tik_tok_download(post_url):
    pass

def reddit_download(post_url):
    try:
        RedDownloader.Download(post_url)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    commands = {
        "y":"Youtube",
        "i": "Instagram",
        "r":"Reddit"
    }
    print(commands)
    social_media = input("Write the name of a social media. If you want to see the available list of themes, type help:")
    social_media = remove_white_space(social_media)
    url_input = input("Url:")
    if social_media == "y":
        mp3_or_mp4 = input("Select format (Type + for MP4 or - for MP3):")
        youtube_download(mp3_or_mp4, url_input)
    elif social_media == "i":
        instagram_download(url_input)
    elif social_media == "r":
        reddit_download(url_input)

    input("Press to quit...")
if __name__ == "__main__":
    main()