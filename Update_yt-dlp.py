import subprocess


if __name__ == '__main__':
    try:
        subprocess.check_call("")
    except subprocess.CalledProcessError as e:
        print(e)
    print("press enter to exit\n> ", end="")
    if input():
        exit
