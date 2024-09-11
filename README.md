# Readme
_yt-dlp-InteractiveExecutable_ is basically just a simple wrapper for [yt-dlp](https://github.com/yt-dlp/yt-dlp) that reads informations from a json file and constructs the corresponding command for executing yt-dlp. It also includes an executable for updating the yt-dlp binary.

## config.json
- **url** the URL to a video or playlist
- **only_audio** if true, converts all videos to audio-only files
- **write_desc** if true, saves the video descriptions to text files 
- **video_format** supported formats are mp4 and mkv
- **audio_format** supported formats are mp3 and wav
- **download_path** the directory to which to save the video/audio/text files
(all directory paths default to the directory of yt-dlp.exe)

## program_config.json
- **ffmpeg_path**: the path to the ffmpeg/ffprobe binaries (you have to download these yourself, see _Dependencies_),
- **config_folder**: the folder where you store the config files (note that the `program_config.json` file itself has to remain in the `config` folder),
- **autoconfig_prefix**: filename prefix of your autoconfig files (see _autoconfig*.json_),
- **default_config**: the name of the default config file (that is evaluated if you choose not to evaluate the autoconfig files, see _autoconfig*.json_)
(all directory paths default to the directory of yt-dlp.exe)

## autoconfig*.json
If you choose to evaluate the autoconfig files instead of the default config file, all files in the `config_folder` that start with `autoconfig_prefix` are evaluated consecutively.

## Dependencies
- [yt-dlp](https://github.com/yt-dlp/yt-dlp): _yt-dlp-InteractiveExecutable_ comes bundled with the Windows 64 binary and is tested on this operating system. If you use a different OS, you can try to download the [release](https://github.com/yt-dlp/yt-dlp#release-files) you need and replace `yt-dlp.exe`.
- [ffmpeg and ffprobe](https://github.com/yt-dlp/FFmpeg-Builds/releases/tag/latest) (**don't forget to provide the path to the binaries in `config/program_config.json` under `ffmpeg_path`**)

## License
This release of _yt-dlp-InteractiveExecutable_ is licensed under the BSD 3-Clause license. It is bundled with a Windows 64 version of [yt-dlp](https://github.com/yt-dlp/yt-dlp) which is licensed under the Unlicense. Please refer to the `LICENSES` directory for the individual licenses.
