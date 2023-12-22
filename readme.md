# Text-to-Speech Application

## Overview
This Text-to-Speech application allows users to convert written text into speech. It provides two modes of operation:

1. **GUI Mode**: A simple graphical user interface where users can type text into a box and have it read aloud by clicking a "Talk" button.
2. **Command Line Mode**: Allows users to input text directly through the command line for the application to speak.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Setup Virtual Environment

It's recommended to run this application within a Python virtual environment. This helps in managing dependencies and keeping your system tidy. Here's how you can set it up:

1. **Create a Virtual Environment**
   
   Navigate to the project directory in your terminal and run the following command to create a virtual environment named `venv` (you can name it anything you prefer):

`python3 -m venv venv`

Activate the Virtual Environment

`source /venv/bin/activate`

Install Dependencies

With the virtual environment activated, install the required dependencies using pip:

`pip install pyttsx3`

### Usage

After installing the dependencies, you can run the application in either mode.


#### GUI Mode:

To launch the GUI, run the following command:

```python main.py -gui```

python main.py -gui

#### Command Line Mode:

To use the application from the command line, provide the text you want to be spoken using the -say flag:

`python main.py -say "Hello, world!"`




Make sure to replace `script_name.py` with the actual name of your Python script file. This formatted README can be placed directly into your Python script for easy reference and documentation. Let me know if you need any more assistance!
