# Port-Scanner---Cybersecurity


A simple Python-based port scanner that allows you to scan a range of ports on one or more target IP addresses to check their status. This project provides color-coded output to easily identify open and closed ports.

## Features

- **Single and Multiple Target Scanning**: Scan one or multiple IP addresses.
- **Port Range Scanning**: Specify the number of ports to scan.
- **Color-Coded Output**: Provides visual clarity for open and closed ports using colors.

## Installation

To run this project, you need Python 3.x installed on your machine. You also need to install the required dependencies.

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/EihabKK/Port-Scanner---Cybersecurity.git
    cd Port-Scanner---Cybersecurity
    ```

2. **Install Dependencies**:
    Ensure you have a virtual environment set up (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Script**:
    ```bash
    python Portscanner-Context.py
    ```

2. **Input Prompts**:
    - **Targets**: Enter the IP addresses you want to scan. Separate multiple IPs with commas.
    - **Ports**: Specify the number of ports you want to scan.

    Example:
    ```text
    Enter targets to scan (separate multiple targets with commas): 192.168.1.1, 192.168.1.2
    How many ports do you want to scan?: 100
    ```

3. **Output**:
    - The script will print a list of ports for each IP address.
    - Open ports will be displayed in green, and closed or error ports will be in red.

## Requirements

- Python 3.x
- `termcolor` (for color-coded output)

Install dependencies using:
```bash
pip install termcolor
