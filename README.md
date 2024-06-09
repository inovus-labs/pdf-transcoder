# Document Converter Web App

This Flask web application converts XLSX and DOCX files to PDF using LibreOffice.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/inovus-labs/file-conversion
   cd file-conversion
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Unix/Linux
    venv\Scripts\activate      # For Windows

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4.Run the application:
    ```bash
    python server.py