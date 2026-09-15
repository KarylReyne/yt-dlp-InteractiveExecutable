import subprocess
import os
import urllib.request
from build_command import create_update_command

if __name__ == '__main__':
    # update yt-dlp
    c = create_update_command()
    try:
        subprocess.check_call(c)
    except subprocess.CalledProcessError as e:
        print(e)
        print("update process aborted.")
    
    # clone/fetch bgutil-ytdlp-pot-provider
    print(f"Would you like to also update Brainicism/bgutil-ytdlp-pot-provider?\n y: yes\n n: no\n>", end="")
    usr_input = input()
    if usr_input == "y":
        try:
            if not os.listdir('bgutil-ytdlp-pot-provider'):
                print("cloning https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git...")
                c = "git clone --single-branch --branch 2.0.0 https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git"
                subprocess.check_call(c)
                c = "npm ci"
                subprocess.check_call(c, cwd=f"{os.getcwd()}{os.sep}bgutil-ytdlp-pot-provider{os.sep}server", shell=True)
                c = "npx tsc"
                subprocess.check_call(c, cwd=f"{os.getcwd()}{os.sep}bgutil-ytdlp-pot-provider{os.sep}server", shell=True)
            else:
                print("fetching https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git...")
                c = "git fetch https://github.com/Brainicism/bgutil-ytdlp-pot-provider.git"
                subprocess.check_call(c, cwd=f"{os.getcwd()}{os.sep}bgutil-ytdlp-pot-provider")
                c = "npm ci"
                subprocess.check_call(c, cwd=f"{os.getcwd()}{os.sep}bgutil-ytdlp-pot-provider{os.sep}server", shell=True)
                c = "npx tsc"
                subprocess.check_call(c, cwd=f"{os.getcwd()}{os.sep}bgutil-ytdlp-pot-provider{os.sep}server", shell=True)

            print("downloading bgutil-ytdlp-pot-provider.zip...")
            urllib.request.urlretrieve("https://github.com/Brainicism/bgutil-ytdlp-pot-provider/releases/latest/download/bgutil-ytdlp-pot-provider.zip", "yt-dlp-plugins/bgutil-ytdlp-pot-provider.zip")
        except subprocess.CalledProcessError as e:
            print(e)
            print("update process aborted.")
    else:
        print("update process aborted.")
    
    print("all updates successful.")
    print("press enter to exit\n> ", end="")
    if input():
        exit
