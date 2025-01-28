import os
import sys
import hashlib
from sys import platform
import google.generativeai as genai

if platform == "linux" or platform == "linux2":
    python_ref = "python3"
else:
    python_ref = "python"

CACHE_DIR = "cache"

os.makedirs(CACHE_DIR, exist_ok=True)

def get_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        hasher.update(file.read())
    return hasher.hexdigest()

def readDocs():
    docs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs', 'Readme.txt')
    try:
        with open(docs_path, 'r', encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Readme.txt not found at {docs_path}")
        sys.exit(1)

def runner(nano_code: str, docs: str, req: str, old_python_code: str = None) -> str:
    gemini_api_key = "AIzaSyC0JYPMrXz3uyilRkkuVKaIkC3HBQ9xmLg"
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    try:
        if req == "run":
            print("Running Nano Code...")
        
        prompt = f"{docs}\n\n{nano_code}"
        if old_python_code:
            prompt += f"\n\nPreviously Generated Python Code:\n{old_python_code}"
        
        response = model.generate_content(prompt)
        responseData = response.text.replace("```", "").strip()
        
        if responseData.lower().startswith("python"):
            responseData = responseData[6:].lstrip()
        
        return responseData

    except Exception as e:
        print(f"Error during AI call: {e}")
        sys.exit(1)

def execute_python_file(py_file: str):
    exit_code = os.system(f"{python_ref} {py_file}")
    if exit_code != 0:
        print(f"Execution failed with exit code {exit_code}")

def cache_all_nano_files():
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    for file in os.listdir(os.path.join(parent_dir, "..")):
        if file.endswith(".nano"):
            nano_path = os.path.join(parent_dir, "..", file)
            py_file = os.path.join(CACHE_DIR, file.replace(".nano", ".py"))
            hash_file = os.path.join(CACHE_DIR, file.replace(".nano", ".hash"))
            
            nano_hash = get_file_hash(nano_path)
            old_hash = ""
            if os.path.exists(hash_file):
                with open(hash_file, 'r') as f:
                    old_hash = f.read().strip()
            
            old_python_code = ""
            if os.path.exists(py_file):
                with open(py_file, 'r', encoding="utf-8") as f:
                    old_python_code = f.read()
            
            if not os.path.exists(py_file) or nano_hash != old_hash:
                print(f"Caching: {file}")
                with open(nano_path, 'r', encoding="utf-8") as file:
                    nano_code = file.read()
                docs = readDocs()
                
                python_code = runner(nano_code, docs, "cache", old_python_code)
                
                with open(py_file, "w", encoding="utf-8") as f:
                    f.write(python_code)
                
                with open(hash_file, "w") as f:
                    f.write(nano_hash)
            else:
                print(f"Already Cached: {file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: nano <filename.nano> or nano cache")
        sys.exit(1)
    
    if sys.argv[1] == "cache":
        print("Caching .nano files...")
        cache_all_nano_files()
        sys.exit(0)
    
    nano_file = sys.argv[1]
    if not nano_file.endswith(".nano"):
        print("Error: Only .nano files are supported.")
        sys.exit(1)
    
    nano_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", nano_file)
    py_file = os.path.join(CACHE_DIR, nano_file.replace(".nano", ".py"))
    hash_file = os.path.join(CACHE_DIR, nano_file.replace(".nano", ".hash"))
    
    if not os.path.exists(nano_path):
        print(f"Error: Nano file '{nano_path}' not found!")
        sys.exit(1)
    
    nano_hash = get_file_hash(nano_path)
    old_hash = ""
    if os.path.exists(hash_file):
        with open(hash_file, 'r') as f:
            old_hash = f.read().strip()
    
    old_python_code = ""
    if os.path.exists(py_file):
        with open(py_file, 'r', encoding="utf-8") as f:
            old_python_code = f.read()
    
    if not os.path.exists(py_file) or nano_hash != old_hash:
        print("Updating Cache...")
        with open(nano_path, 'r', encoding="utf-8") as file:
            nano_code = file.read()
        docs = readDocs()
        python_code = runner(nano_code, docs, "run", old_python_code)
        
        with open(py_file, "w", encoding="utf-8") as f:
            f.write(python_code)
        
        with open(hash_file, "w") as f:
            f.write(nano_hash)
    else:
        print("Using Cache...")
    
    execute_python_file(py_file)

if __name__ == "__main__":
    main()
