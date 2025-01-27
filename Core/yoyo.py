#!/usr/bin/env python3
import os
import sys
import subprocess
import platform

def install_module(module_name: str):
    try:
        print(f"Installing {module_name}...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", module_name],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error installing {module_name}: {e.stderr}")
        sys.exit(1)

def setup_nano():

    try:
        print("Setting up Nano programming language...")
        with open("needed.txt", "r") as file:
            dependencies = [line.strip() for line in file.readlines() if line.strip()]
        for dep in dependencies:
            install_module(dep)
    except FileNotFoundError:
        print("Error: 'needed.txt' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: yoyo <command> <target>")
        print("Commands:")
        print("  get <module_name>   - Install a Module")
        print("  setup nano   - Set up the Nano programming language")
        sys.exit(1)

    command = sys.argv[1]
    target = sys.argv[2]

    if command == "get":
        install_module(target)
    elif command == "setup":
        setup_nano()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
