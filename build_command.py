import config_util
import os


def create_command(config_folder: str="config", config_file: str="config.json", program_config: str="program_config.json"):
    get_config = lambda k: config_util.get_config(k, path=config_folder, file=config_file)
    ffmpeg_path = config_util.get_config("ffmpeg_path", file=program_config)
    command = "yt-dlp --abort-on-error --check-formats"

    # raise EXCEPTIONS
    if get_config("audio_format") not in ["mp3", "wav"]:
        raise config_util.InvalidConfig("currently only mp3 and wav are supported audio formats")
    if get_config("video_format") not in ["mp4", "mkv"]:
        raise config_util.InvalidConfig("currently only mp4 and mkv are supported video formats")

    # OPTIONS - paths
    download_path = get_config("download_path")
    download_path += "/" if not download_path.endswith("/") else ""

    if get_config("prepend_creator"):
        command += " -o {}%(uploader)s_-_%(title)s.%(ext)s".format(download_path)
    else:
        command += " -o {}%(title)s.%(ext)s".format(download_path)
    command += " --ffmpeg-location "+ffmpeg_path

    # OPTIONS - audio
    if get_config("only_audio"):
        command += " --extract-audio"
        command += " --audio-format "+get_config("audio_format")
        command += " --audio-quality 8"
    # OPTIONS - video
    else:
        command += " --remux-video "+get_config("video_format")
    
    # OPTIONS - description
    if get_config("write_desc"):
        command += " --write-description"

    # URL
    command += " -- "+get_config("url")

    return command


def create_update_command():
    command = "yt-dlp --update"
    return command