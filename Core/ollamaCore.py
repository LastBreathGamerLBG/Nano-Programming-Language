#!/usr/bin/env python3
import os
import sys
import requests
import subprocess
from sys import platform

# Checking Operating System
if  platform == "linux" or platform == "linux2":
    python_ref = "python3"
else:
    python_ref = "python"


def readDocs():
    docs_path = os.path.join(os.getcwd(), 'docs', 'Readme.txt')
    try:
        with open(docs_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Readme.txt not found at {docs_path}")
        sys.exit(1)

def readNano(file_path: str) -> str:
    if file_path == "cache":
        temp_file = "temp.py"
        exit_code = os.system(f"{python_ref} {temp_file}")
        return exit_code
    
    abs_path = os.path.abspath(file_path)
    if not os.path.exists(abs_path):
         raise FileNotFoundError(f"File {abs_path} not found! at {abs_path}")
    
    with open(abs_path, 'r') as file:
        return file.read()

def runner(nano_code: str, docs: str) -> str:
    url = "http://127.0.0.1:11434/api/generate"

    payload = {
        "model": "qwen2.5-coder:7b",
        "prompt": nano_code,
        "system": docs,
        "stream": False
    }

    try:
        print("Executing Nano Code...")
        response = requests.post(url, json=payload)
        response.raise_for_status()
        jsonData = response.json()

        rawData = jsonData.get('response', 'No response found')

        if rawData.startswith('```python'):
            responseData = rawData[9:].strip('```').strip()
        else:
            responseData = rawData.strip('```').strip()

        return responseData

    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
        sys.exit(1)

def execute_python_code(python_code: str):
    temp_file = "temp.py"
    
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    with open(temp_file, "w") as file:
        file.write(python_code)

    exit_code = os.system(f"{python_ref} {temp_file}")
    if exit_code != 0:
        print(f"Execution failed with exit code {exit_code}")

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    nano_file = sys.argv[1]
    
    try:
        nano_code = readNano(nano_file)
        
        if nano_code != 0:
            docs = readDocs()
            python_code = runner(nano_code, docs)
            execute_python_code(python_code)

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()