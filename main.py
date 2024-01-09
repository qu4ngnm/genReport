from flask import *
from werkzeug.utils import secure_filename

app = Flask(__name__,template_folder='template') 



@app.route('/') 
def main(): 
    return render_template("index.html") 

@app.route('/')
def gen_report():
    
    return 0

@app.route('/upload', methods=['POST'])
def upload(): 
    if request.method == 'POST': 
        files = request.files.getlist("file") 
        for file in files: 
            file.save(file.filename)
        return "<h1>Files Uploaded Successfully.!</h1>"

if __name__ == '__main__': 
    app.run(debug=True) 