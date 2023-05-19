import subprocess
from build_command import create_command


if __name__ == '__main__':
    c = create_command()
    subprocess.check_call(c)
