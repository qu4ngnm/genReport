from flask import *
from werkzeug.utils import secure_filename
from modules.checkUpload import allowed_file

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__,template_folder='template') 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"



@app.route('/') 
def main(): 
    return render_template("index.html") 


@app.route('/uploads', methods=['POST'])
def upload(): 
    if 'file' not in request.files:
        flash('No file part')
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect('/')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('download_file', name=filename))

if __name__ == '__main__': 
    app.run(debug=True) 