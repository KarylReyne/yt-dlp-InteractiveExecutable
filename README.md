# Readme
yt-dlp-InteractiveExecutable is basically just a simple wrapper for [yt-dlp](https://github.com/yt-dlp/yt-dlp) that reads informations from a json file and constructs the corresponding command for executing yt-dlp.

## Dependencies
- [yt-dlp](https://github.com/yt-dlp/yt-dlp): The executable comes bundled with the windows 64 binary. If you use a different OS, download the [release](https://github.com/yt-dlp/yt-dlp#release-files) you need and replace `yt-dlp.exe`.
- [ffmpeg and ffprobe](https://github.com/yt-dlp/FFmpeg-Builds/releases/tag/latest) (**don't forget to provide the path to the binaries in `config/config.json` under `ffmpeg_path`**)
