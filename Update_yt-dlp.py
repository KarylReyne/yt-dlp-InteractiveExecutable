import subprocess
from build_command import create_update_command

if __name__ == '__main__':
    c = create_update_command()
    try:
        subprocess.check_call(c)
    except subprocess.CalledProcessError as e:
        print(e)
        print("update process aborted.")
    print("press enter to exit\n> ", end="")
    if input():
        exit
