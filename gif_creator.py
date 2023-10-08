from pytube import YouTube
from PIL import Image
import cv2, glob

def download_video(video_url: str, videos_path: str) -> str:
    """Downloads the video"""
    yt = YouTube(video_url) 
    yt = yt.streams.get_highest_resolution()
    return yt.download(videos_path)


def frame_creator(video: str, directory: str, name: str = "frame") -> None:
    """Convert the video to a set of frames"""
    vidcap = cv2.VideoCapture(video)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(f'{directory}/{name}{count:04d}.jpg', image) # Convert frames to JPG
        success, image = vidcap.read()
        print('Reading next frame:', success)
        count += 1


def create_gif(name: str, frame_dir: str, gif_dir: str) -> Image:
    """Generates the gif"""
    frames = [Image.open(images) for images in sorted(glob.glob(f"{frame_dir}/*.jpg"))]
    my_gif = frames[0]
    my_gif.save(f"{gif_dir}/{name}", format='GIF', save_all=True, append_images=frames[1:], optimize=True, duration=100)
    
    return my_gif


if __name__ == '__main__':
    url = input("Insert video's URL: ")
    video_dir = input("Insert the path to the video directory: ")
    video = download_video(url, video_dir)

    gif_name = input("Insert gif's name: ") + '.gif'
    frame_dir = input("Insert the path to the frame directory: ")
    frame_creator(video, frame_dir, gif_name)

    gif_dir = input("Insert the path to the gif directory: ")
    create_gif(gif_name, frame_dir, gif_dir)
