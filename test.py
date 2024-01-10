folder_path = '/uploads/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


filename = secure_filename(file.filename)
file.save(os.path.join(folder_path, filename))