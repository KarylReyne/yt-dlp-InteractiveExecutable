import subprocess
import sys

if __name__ == '__main__':
    try:
        sys.path.insert(0, "yt-dlp")
        import yt_dlp
        yt_dlp.main(["--update"])
        
    except subprocess.CalledProcessError as e:
        print(e)
        print("update process aborted.")

    print("press enter to exit\n> ", end="")
    if input():
        exit
