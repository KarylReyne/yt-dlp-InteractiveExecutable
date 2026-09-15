# Readme
_yt-dlp-InteractiveExecutable_ is basically just a simple wrapper for [yt-dlp](https://github.com/yt-dlp/yt-dlp) that reads informations from a json file and constructs the corresponding command for executing yt-dlp. It also includes an executable for updating the yt-dlp binary.

## config.json
- **url** the URL to a video or playlist
- **only_audio** if true, converts all videos to audio-only files
- **write_desc** if true, saves the video descriptions to text files 
- **prepend_creator**: if true, adds the creator name in front of the output file name
- **video_format** supported formats are mp4 and mkv
- **audio_format** supported formats are mp3 and wav
- **download_path** the directory to which to save the video/audio/text files
- **custom_options** here you can provide additional yt-dlp options
(all directory paths default to the directory of yt-dlp.exe)

## program_config.json
- **ffmpeg_path**: the path to the ffmpeg/ffprobe binaries (you have to download these yourself, see _Dependencies_)
- **po_token_provider**: either `"bgutil-ytdlp-pot-provider.zip"` (run the Updater or download it yourself and put it in the `yt-dlp-plugins` folder) or `""`, the latter disables PO token generation
- **config_folder**: the folder where you store the config files (note that the `program_config.json` file itself has to remain in the `config` folder)
- **autoconfig_prefix**: filename prefix of your autoconfig files (see _autoconfig*.json_)
- **default_config**: the name of the default config file (that is evaluated if you choose not to evaluate the autoconfig files, see _autoconfig*.json_)
(all directory paths default to the directory of yt-dlp.exe)

## autoconfig*.json
If you choose to evaluate the autoconfig files instead of the default config file, all files in the `config_folder` that start with `autoconfig_prefix` are evaluated consecutively.

## PO Tokens
_yt-dlp-InteractiveExecutable_ can integrate the Proof of Origin (PO) Token provider [bgutil-ytdlp-pot-provider](https://github.com/Brainicism/bgutil-ytdlp-pot-provider). For [reference](https://github.com/Brainicism/bgutil-ytdlp-pot-provider#bgutils-pot-provider), _yt-dlp-InteractiveExecutable_ uses bgutil-ytdlp-pot-provider's provider option (b) using Node.js and integrates the provider in yt-dlp via the provider plugin. All necessary components can be installed/updated with _yt-dlp-InteractiveExecutable_'s Updater. Note that the Updater always installs version 2.0.0 of bgutil-ytdlp-pot-provider, but updates always to the latest commit of the repository (i.e. run the Updater twice if you use it to install bgutil-ytdlp-pot-provider for the first time).

## Dependencies
- [yt-dlp](https://github.com/yt-dlp/yt-dlp): _yt-dlp-InteractiveExecutable_ comes bundled with the Windows 64 binary and is tested on this operating system. If you use a different OS, you can try to download the [release](https://github.com/yt-dlp/yt-dlp#release-files) you need and replace `yt-dlp.exe`.
- [ffmpeg and ffprobe](https://github.com/yt-dlp/FFmpeg-Builds/releases/tag/latest) (**don't forget to provide the path to the binaries in `config/program_config.json` under `ffmpeg_path`**)
- if using the PO token provider, make sure your system satisfies [bgutil-ytdlp-pot-provider's dependencies](https://github.com/Brainicism/bgutil-ytdlp-pot-provider#base-requirements)

## License
This release of _yt-dlp-InteractiveExecutable_ is licensed under the BSD 3-Clause license. It is bundled with a Windows 64 version of [yt-dlp](https://github.com/yt-dlp/yt-dlp) which is licensed under the Unlicense. Please refer to the `LICENSES` directory for the individual licenses.

## FAQ
**_yt-dlp-InteractiveExecutable_ fails due to a `subprocess.TimeoutExpired` exception after using the Updater.**
This sometimes happens. Run the _yt-dlp-InteractiveExecutable_ executable a second time and it should work again.