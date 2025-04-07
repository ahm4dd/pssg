# pssg: A Simple Python Static Site Generator

[![Python Version](https://img.shields.io/badge/Python-3.12.3+-blue.svg)](https://www.python.org/downloads/release/python-3123/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Pages Deploy Status](https://img.shields.io/github/deployments/ahm4dd/pssg/github-pages)](https://github.com/ahm4dd/pssg/deployments/activity_log?environment=github-pages)

`pssg` is a lightweight static site generator (SSG) built with Python. It transforms your Markdown content into static HTML files using a provided template, incorporating static assets like CSS and images.

**Key Features:**

*   Converts Markdown files from `/content` to HTML.
*   Uses `/static` for CSS, images, and other assets.
*   Outputs the generated site to the `/docs` directory.
*   Includes a simple development server with hot-reloading for content changes.

**Note on Markdown Support:** `pssg` currently supports a specific subset of Markdown syntax.

*   **Block Elements** (separated by blank lines):
  ```
       Headings (`# H1` to `###### H6`)
       Paragraphs
       Blockquotes (`> quote`)
       Code Blocks (fenced with `````)
       Ordered Lists (`1. Item`)
       Unordered Lists (`- Item` or `* Item`)
 ```
*   **Inline Elements:**
  ```
       Bold (`**bold**`)
       Italic (`*italic*`)
       Inline Code (``code``)
       Links (`[text](link)`)
       Images (`![alt text](src)`)
  ```
## Table of Contents

*   [Installation](#installation)
*   [Usage](#usage)
*   [Project Structure](#project-structure)
*   [How it Works](#how-it-works)
*   [Testing](#testing)
*   [Contributing](#contributing)
*   [License](#license)

## Installation

1.  **Clone the Repository:**
    ```bash
    # Make sure to use the correct repository name (pssg as per your original clone command)
    git clone https://github.com/ahm4dd/pssg.git
    cd pssg
    ```

2.  **Set up a Virtual Environment (Recommended):**
    This isolates project dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install Dependencies (Required for Testing/Development):**
    If you only plan to *run* `pssg` using the provided scripts and don't need to run tests, you might skip this step (depending on whether `main.sh` relies on external libraries not bundled with Python). However, installing dependencies is generally good practice.
    ```bash
    pip install pytest
    ```
    *Note: `pssg` requires Python 3.12.3 or higher. (Recommended but it may work for some older versions)*

## Usage

> **Platform Note:** The primary execution script (`main.sh`) is designed for Unix-like systems (Linux, macOS). It has not been tested on Windows. You may need to adapt the commands or run the underlying Python scripts directly on Windows.

This script typically performs the following actions:
1. Cleans the output directory (/docs).
2. Builds the HTML site from /content and /static into /docs.
3. Starts a local development server.
   
To build the static site and start the development server with hot-reloading:

```bash
./main.sh
```
Access the generated site via the URL provided by the script (usually http://localhost:8080 or similar).

Press Ctrl+C to stop the server.

## How it Works

1.  **Scanning:** `pssg` scans the `/content` directory for Markdown (`.md`) files and the `/static` directory for assets.
2.  **Parsing & Conversion:** Each Markdown file is parsed according to the [supported syntax](#note-on-markdown-support) and converted into an HTML fragment.
3.  **Templating:** The generated HTML fragment is inserted into the `template.html` file (typically replacing a placeholder like `{{content}}`) to create the final HTML page structure.
4.  **Asset Copying:** Files and directories from `/static` are copied directly into the output `/docs` directory.
5.  **Output:** All generated HTML files and copied static assets are placed in the `/docs` folder, ready for deployment.

**Core Libraries Used:**

*   **File System:** `os`, `shutil`, `glob` (for finding files, copying, managing paths)
*   **Parsing:** `re` (for some Markdown pattern matching)
*   **Testing:** `unittest`, `pytest` (for unit and integration tests, including mocking)
*   **System:** `sys` (for grabbing the repository from the build.sh file or any arguments passed to the python3 src/main.py command)

## Testing

1.  **Ensure Dependencies are Installed:**
    Make sure you have completed the [Installation](#installation) steps, including installing `requirements.txt` (which should include `pytest`).

2.  **Run Tests:**
    Execute the test script:
    ```bash
    ./test.sh
    ```
    This will typically discover and run all tests defined within the project using `pytest`.

## Contributing

Contributions are welcome! If you'd like to help improve `pssg`:

1.  **Fork** the repository on GitHub.
2.  Create a **new branch** for your feature or bug fix.
3.  Make your changes and **add tests** if applicable.
4.  Ensure tests pass (`./test.sh`).
5.  **Commit** your changes and push them to your fork.
6.  Open a **Pull Request** back to the main repository (`ahm4dd/pssg`).

Please open an issue first to discuss significant changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
