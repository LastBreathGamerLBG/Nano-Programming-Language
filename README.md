# Nano Programming Language 🚀

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-brightgreen.svg)](https://github.com/yourusername/nano-lang)  
[![Package Manager](https://img.shields.io/badge/Package%20Manager-yoyo-yellow.svg)](https://github.com/yourusername/nano-lang)

**Nano: Less Code, More Output.**

Nano is a minimalist programming language designed for developers who value conciseness and efficiency. Built on a robust Python backend, Nano leverages the power of Python's extensive module ecosystem while offering a simplified, more intuitive syntax. With its unique AI-powered features, Nano aims to streamline the development process by providing runtime code generation and automatic error correction.

## Key Features ✨

*   **Concise Syntax:** Nano prioritizes readability and reduces boilerplate code, allowing you to express complex logic with fewer lines.
*   **Python Integration:** Seamlessly access and utilize the vast library of Python modules and packages.
*   **AI-Powered Development:**
    *   **Runtime Code Generation:** Nano can generate code snippets dynamically based on context, accelerating development.
    *   **Automatic Error Correction:** The built-in AI engine attempts to identify and fix syntax errors at runtime, reducing debugging time.
*   **Cross-Platform Compatibility:** Currently supports both Windows and Linux operating systems.
*   **Dedicated Package Manager:** Nano comes with its own package manager, `yoyo`, for easy installation and management of dependencies.

## Getting Started 🛠️

### Prerequisites 📋

*   Python 3.7+ installed on your system.
*   A terminal or command prompt.

### Installation 🔧

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/LastBreathGamerLBG/NanoLanguage.git
    cd NanoLanguage/Core
    ```

2.  **Setup Nano using `yoyo`:**
    *   **Windows:**
        ```bash
        .\yoyo setup nano
        ```
    *   **Linux:**
        ```bash
        ./yoyo.sh setup nano 
        ```
        or
        ```bash
        bash yoyo setup nano
        ```

    This command initializes the Nano environment and prepares it for use.

### Running Nano Code ▶️

1.  Create a file with the `.nano` extension (e.g., `test.nano`).
2.  Write your Nano code in the file.
3.  Execute the file using the Nano interpreter (specific command will depend on your implementation). For example:
    ```bash
    nano test.nano 
    ```

## Nano Syntax Example 📝

```nano
// When creating variables, define the type using variable_name:type
a:int = 7
b:int = 1  

// The print function is the same as Python's
print(a + b)
```

## Package Management with `yoyo` 📦

`yoyo` is Nano's package manager. Use it to install, update, and manage Nano packages.

### Common `yoyo` Commands 📜

*   `yoyo setup nano`: Initializes the Nano environment.
*   `yoyo install <package_name>`: Installs a specific package.
*   `yoyo update <package_name>`: Updates a specific package.
*   `yoyo list`: Lists installed packages.

## Contributing 🤝

We welcome contributions! If you have ideas for new features, bug fixes, or improvements, please feel free to:

1.  Fork the repository.
2.  Create a branch for your changes.
3.  Submit a pull request.

## License 📜

This project is licensed under the MIT License - see the **LICENSE** file for details.

## Example Code 💻

The Nano template includes two example code files to help you get started. Explore them to learn more about Nano's syntax and capabilities.

## Disclaimer ⚠️

Nano is under active development, and some features may be experimental. We appreciate your feedback and contributions as we continue to improve the language.
