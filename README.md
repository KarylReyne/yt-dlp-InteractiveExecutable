# Readme
_yt-dlp-InteractiveExecutable_ is basically just a simple wrapper for [yt-dlp](https://github.com/yt-dlp/yt-dlp) that reads informations from a json file and constructs the corresponding command for executing yt-dlp.

## config.json
- **url** the URL to a video or playlist
- **only_audio** if true, converts all videos to audio-only files
- **write_desc** if true, saves the video descriptions to text files 
- **video_format** supported formats are mp4 and mkv
- **audio_format** supported formats are mp3 and wav
- **download_path** the directory to which to save the video/audio/text files
- **ffmpeg_path** path/to/ffmpeg/bin
(all directory paths default to the directory of yt-dlp.exe)

## Dependencies
- [yt-dlp](https://github.com/yt-dlp/yt-dlp): The executable comes bundled with the windows 64 binary. If you use a different OS, download the [release](https://github.com/yt-dlp/yt-dlp#release-files) you need and replace `yt-dlp.exe`.
- [ffmpeg and ffprobe](https://github.com/yt-dlp/FFmpeg-Builds/releases/tag/latest) (**don't forget to provide the path to the binaries in `config/config.json` under `ffmpeg_path`**)

## License
This release of _yt-dlp-InteractiveExecutable_ is licensed under the BSD 3-Clause license. It is bundled with a windows 64 version of [yt-dlp](https://github.com/yt-dlp/yt-dlp) which is licensed under the Unlicense. Please refer to the `LICENSES` directory for the individual licenses.
