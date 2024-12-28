# Reading Time Calculator

This application provides an easy-to-use interface for calculating reading times from PDF files. With a few clicks, users can determine how long it will take to read a document at different speeds.

## Features

- Extracts text from any PDF file.
- Calculates reading time for three reading speeds:
  - Slow: 100 words per minute
  - Average: 200 words per minute
  - Fast: 300 words per minute
- Allows live reading of the extracted text at the selected speed.

## Prerequisites

Ensure your system has the following installed:

- Python 3.6 or newer
- Required Python packages:
  - `tkinter` (included with Python by default)
  - `PyPDF2` (installable via pip)

## Installation

1. Clone the repository or download the script to your local machine.

```bash
git clone <repository_url>
cd <repository_directory>
```

2. Install the required Python package:

```bash
pip install PyPDF2
```

## How to Run the Application

1. Save the script with a filename like `reading_time_calculator.py`.
2. Open your terminal or command prompt and navigate to the script's directory.
3. Run the script using the command:

```bash
python reading_time_calculator.py
```

4. Use the graphical interface to select a PDF file and calculate the reading time.

## Usage Instructions

1. Launch the application by running the script.
2. Click the **Select PDF File** button to choose a PDF from your computer.
3. The application will display the word count and the estimated reading times for different speeds.
4. You can also choose to view the text at your preferred reading speed by clicking the relevant button.

## Example Screenshot

![Reading Time Calculator Screenshot](./screenshot.png)

## Contribution

Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. Refer to the [LICENSE](./LICENSE) file for details.
