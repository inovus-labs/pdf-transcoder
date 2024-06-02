import sys
import os

# Add the path to your virtual environment and Flask project directory
virtualenv_path = '/home/nithindaniel/file-conversion/myenv'
project_path = '/home/nithindaniel/file-conversion'

# Activate the virtual environment
activate_this = os.path.join(virtualenv_path, 'bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Add the Flask project directory to sys.path
if project_path not in sys.path:
    sys.path.append(project_path)

# Import the Flask application
from your_flask_app import app as application
