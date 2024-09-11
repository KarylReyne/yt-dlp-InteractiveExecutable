import os
import subprocess
import pyuac
from pyuac import main_requires_admin
import config_util
from build_command import create_command

@main_requires_admin
def main():
    config_folder = config_util.get_config("config_folder", file="program_config.json")
    prefix = config_util.get_config("autoconfig_prefix", file="program_config.json")
    default = config_util.get_config("default_config", file="program_config.json")

    print(f"Would you like to evaluate all autoconfig files?\n y: yes\n n: no, evaluate only {default}\n *: halts execution\n> ", end="")
    usr_input = input()

    commands = []
    if usr_input == "y":
        print("evaluating all autoconfig files...")

        for _, _, files in os.walk(config_folder):
            for file in files:
                if file.startswith(prefix):
                    commands.append(create_command(config_folder, file))

    elif usr_input == "n":
        print("evaluating the default config file...")
        commands.append(create_command(config_folder, default))

    else:
        print("Execution terminated.")


    for c in commands:
        try:
            subprocess.check_call(c)
        except subprocess.CalledProcessError as e:
            print(e)

    print("press enter to exit\n> ", end="")
    if input():
        exit

if __name__ == '__main__':
    main()    
