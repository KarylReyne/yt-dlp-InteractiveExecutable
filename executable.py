import subprocess
import os
from build_dist import build
from build_command import create_command


CREATE_BUILD = False


if __name__ == '__main__':
    if CREATE_BUILD:
        build()
    else:
        print("starting execution...\n")

        c = create_command()
        subprocess.check_call(c)
