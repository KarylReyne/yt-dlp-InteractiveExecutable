import subprocess
import pyuac
from pyuac import main_requires_admin
from build_command import create_command

@main_requires_admin
def main():
    c = create_command()
    try:
        subprocess.check_call(c)
    except subprocess.CalledProcessError as e:
        print(e)
    print("press enter to exit\n> ", end="")
    if input():
        exit

if __name__ == '__main__':
    main()    
