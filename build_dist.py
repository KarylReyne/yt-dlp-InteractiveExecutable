import os
import PyInstaller
import shutil
import pyuac
from pyuac import main_requires_admin
import subprocess
from pathlib import Path

WORKING_DIR = os.path.abspath(os.getcwd())
DISTPATH = f"{WORKING_DIR+os.sep}dist{os.sep}windows-dist{os.sep}yt-dlp-InteractiveExecutable"


def build_command():
    args = ['--onefile',
            # '--windowed',
            f'--distpath={DISTPATH}',
            f'--workpath={WORKING_DIR+os.sep}dist{os.sep}windows-build',
            '--name=yt-dlp-InteractiveExecutable',
            '--icon=logo.ico',
            '-c',
            ]
    c = "pyinstaller executable.py"
    for arg in args:
        c += " {}".format(arg)
    return c


def build_updater_command():
    args = ['--onefile',
            # '--windowed',
            f'--distpath={DISTPATH}',
            f'--workpath={WORKING_DIR+os.sep}dist{os.sep}windows-build-updater',
            '--name=yt-dlp-InteractiveExecutable_Updater',
            '--icon=updater_logo.ico',
            '-c',
            ]
    c = "pyinstaller Update_yt-dlp.py"
    for arg in args:
        c += " {}".format(arg)
    return c


@main_requires_admin
def main():
    # update requirements.txt
    subprocess.check_call("pipreqs . --force")
    # create directories
    Path(f"{WORKING_DIR+os.sep}dist{os.sep}windows-build").mkdir(parents=True, exist_ok=True)
    Path(f"{WORKING_DIR+os.sep}dist{os.sep}windows-build-updater").mkdir(parents=True, exist_ok=True)
    Path(f"{DISTPATH+os.sep}config").mkdir(parents=True, exist_ok=True)
    Path(f"{DISTPATH+os.sep}LICENSES").mkdir(parents=True, exist_ok=True)
    Path(f"{DISTPATH+os.sep}download").mkdir(parents=True, exist_ok=True)
    # copy files
    shutil.copyfile(f"{WORKING_DIR+os.sep}yt-dlp.exe", f"{DISTPATH+os.sep}yt-dlp.exe")
    shutil.copyfile(f"{WORKING_DIR+os.sep}config{os.sep}config.json", f"{DISTPATH+os.sep}config{os.sep}config.json")
    shutil.copyfile(f"{WORKING_DIR+os.sep}config{os.sep}program_config.json", f"{DISTPATH+os.sep}config{os.sep}program_config.json")
    shutil.copyfile(f"{WORKING_DIR+os.sep}config{os.sep}autoconfig_onlyaudio.json", f"{DISTPATH+os.sep}config{os.sep}autoconfig_onlyaudio.json")
    shutil.copyfile(f"{WORKING_DIR+os.sep}LICENSES{os.sep}yt-dlp-InteractiveExecutable.LICENSE", f"{DISTPATH+os.sep}LICENSES{os.sep}yt-dlp-InteractiveExecutable.LICENSE")
    shutil.copyfile(f"{WORKING_DIR+os.sep}LICENSES{os.sep}yt-dlp.LICENSE", f"{DISTPATH+os.sep}LICENSES{os.sep}yt-dlp.LICENSE")
    shutil.copyfile(f"{WORKING_DIR+os.sep}README.md", f"{DISTPATH+os.sep}README.md")
    # build applications
    for c in [build_command(), build_updater_command()]:
        try:
            subprocess.check_call(c.split(" "))
            print(f"{c} executed successfully")
        except subprocess.CalledProcessError as e:
            print(e)
    print("press enter to exit\n> ", end="")
    if input():
        exit
    

if __name__ == '__main__':
    main()
