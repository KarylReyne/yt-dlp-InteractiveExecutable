from config_util import get_config, InvalidConfig


def create_command():
    command = "yt-dlp --abort-on-error --check-formats"

    # raise EXCEPTIONS
    if get_config("audio_format") not in ["mp3", "wav"]:
        raise InvalidConfig("currently only mp3 and wav are supported audio formats")
    if get_config("video_format") not in ["mp4", "mkv"]:
        raise InvalidConfig("currently only mp4 and mkv are supported video formats")

    # OPTIONS - paths
    command += " -o {}%(title)s.%(ext)s".format(get_config("download_path"))
    command += " --ffmpeg-location "+get_config("ffmpeg_path")

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