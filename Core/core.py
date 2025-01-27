#!/usr/bin/env python3
import os
import sys
from sys import platform
import google.generativeai as genai

# Checking Operating System
if  platform == "linux" or platform == "linux2":
    python_ref = "python3"
else:
    python_ref = "python"

def readDocs():
    docs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs', 'Readme.txt')
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
    
    core_dir = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(core_dir, "..", file_path)

    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"File {abs_path} not found! at {abs_path}")
    
    with open(abs_path, 'r') as file:
        return file.read()

def runner(nano_code: str, docs: str) -> str:
    gemini_api_key = "AIzaSyC0JYPMrXz3uyilRkkuVKaIkC3HBQ9xmLg"
    if not gemini_api_key:
        print("API key not found.")
        sys.exit(1)
    
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        print("Executing Nano Code...")
        response = model.generate_content(f"{docs}\n\n{nano_code}")
        
        responseData = response.text.replace("```", "").strip()

        if responseData.lower().startswith("python"):
           responseData = responseData[6:].lstrip()
        
        return responseData

    except Exception as e:
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