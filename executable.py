import os
import subprocess
import pyuac
from pyuac import main_requires_admin
import config_util
from build_command import create_command

DEBUG_MODE = True

@main_requires_admin
def main():
    program_config = "debug_" if DEBUG_MODE else ""
    program_config += "program_config.json"

    config_folder = config_util.get_config("config_folder", file=program_config)
    prefix = config_util.get_config("autoconfig_prefix", file=program_config)
    default = config_util.get_config("default_config", file=program_config)

    commands = []

    if DEBUG_MODE:
        print("[DEBUG] evaluating the debug config file...")
        commands.append(create_command(config_folder, "debug_config.json", program_config))
    else:
        print(f"Would you like to evaluate all autoconfig files?\n y: yes\n n: no, evaluate only {default}\n *: halts execution\n> ", end="")
        usr_input = input()

        if usr_input == "y":
            print("evaluating all autoconfig files...")

            for _, _, files in os.walk(config_folder):
                for file in files:
                    if file.startswith(prefix):
                        commands.append(create_command(config_folder, file, program_config))

        elif usr_input == "n":
            print("evaluating the default config file...")
            commands.append(create_command(config_folder, default, program_config))

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
