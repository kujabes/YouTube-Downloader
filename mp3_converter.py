from pytube import YouTube
from tqdm import tqdm
import sys
import os

def mp3_download(url, path):
    yt = YouTube(url, on_progress_callback=lambda chunk, file_handle, bytes_remaining: 
                progress_bar.update(bytes_remaining - progress_bar.n))
    
    video = yt.streams.filter(only_audio=True).first()
    
    # Get the file size
    file_size = video.filesize

    # Create a progress bar using tqdm
    progress_bar = tqdm(total=file_size, 
                        unit='B', 
                        unit_scale=True, 
                        desc=yt.title,
                        leave=False)

    # Download the file with progress bar
    out_file = video.download(output_path=path, filename=yt.title)

    # Close the progress bar
    progress_bar.close()

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    return new_file, yt.title

def mp3_playlist_download(url):
    ...


if __name__ == '__main__':
    function_map = {
        "solo": mp3_download,
        "playlist": mp3_playlist_download
    }

    if len(sys.argv) > 1:
        url = sys.argv[1]
        mode = sys.argv[2]
        # path = sys.argv[3]
    else:
        url = input('Please enter the URL of the video you want to convert: ')
        mode = input('Is this a single video or a playlist (respond with solo or playlist): ')
        # path = input('Where should I save the file (enter file path): ')

    # Picking out function given a modality
    f = function_map[mode]
    
    # Defaulting file path to the music folder
    path = r'./music'
    
    file_path, title = f(url, path)


    ...