import os
import PyInstaller
import shutil

WORKING_DIR = os.path.abspath(os.getcwd())
DISTPATH = f"{WORKING_DIR+os.sep}dist{os.sep}windows-dist"


def build():
    args = ['--onefile',
            # '--windowed',
            f'--distpath={DISTPATH}',
            f'--workpath={WORKING_DIR+os.sep}dist{os.sep}windows-build',
            '--name=yt-dlp-InteractiveExecutable',
            # '--icon=icon.ico',
            ]
    c = "pyinstaller executable.py"
    for arg in args:
        c += " {}".format(arg)
    os.system(c)


def build_updater():
    args = ['--onefile',
            # '--windowed',
            f'--distpath={DISTPATH}',
            f'--workpath={WORKING_DIR+os.sep}dist{os.sep}windows-build-updater',
            '--name=yt-dlp-InteractiveExecutable_Updater',
            # '--icon=icon.ico',
            ]
    c = "pyinstaller Update_yt-dlp.py"
    for arg in args:
        c += " {}".format(arg)
    os.system(c)


if __name__ == '__main__':
    shutil.copyfile(f"{WORKING_DIR+os.sep}yt-dlp", f"{DISTPATH+os.sep}yt-dlp")
    shutil.copyfile(f"{WORKING_DIR+os.sep}config{os.sep}config.json", f"{DISTPATH+os.sep}config{os.sep}config.json")
    build()
    build_updater()
