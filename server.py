from flask import Flask, request, jsonify, send_file
import subprocess
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
ALLOWED_EXTENSIONS = {'xlsx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Ensure the upload and output directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_xlsx_to_pdf(xlsx_path, output_dir):
    try:
        command = ['libreoffice', '--headless', '--convert-to', 'pdf', xlsx_path, '--outdir', output_dir]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            return False, result.stderr.decode()
        return True, None
    except Exception as e:
        return False, str(e)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(error="No file part"), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify(error="No selected file"), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Convert XLSX to PDF
        success, error = convert_xlsx_to_pdf(file_path, app.config['OUTPUT_FOLDER'])
        if not success:
            return jsonify(error=error), 500

        pdf_filename = filename.rsplit('.', 1)[0] + '.pdf'
        pdf_path = os.path.join(app.config['OUTPUT_FOLDER'], pdf_filename)

        return send_file(pdf_path, as_attachment=True, download_name=pdf_filename)

    return jsonify(error="Invalid file type"), 400

if __name__ == '__main__':
    app.run(debug=True)
