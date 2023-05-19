import os
import PyInstaller


def build():
    args = ['--onefile',
            # '--windowed',
            '--distpath=./dist/windows-dist',
            '--workpath=./dist/windows-build',
            '--name=yt-dlp-InteractiveExecutable',
            # '--icon=icon.ico',
            ]
    c = "pyinstaller executable.py"
    for arg in args:
        c += " {}".format(arg)
    os.system(c)


if __name__ == '__main__':
    build()
