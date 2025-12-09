from flask import request, send_from_directory, render_template, redirect, url_for
import os
import uuid
from functions.deleter import deletefile

folder = 'uploads'

def register_routes(app):
    @app.route('/', methods=['GET'])
    def index():
        base_url = request.url_root.rstrip('/')
        return render_template('index.html', base_url=base_url)

    @app.route('/upload', methods=['POST'])
    def upload():
        if 'file' not in request.files:
            return 'no file', 400
        f = request.files['file']
        ext = os.path.splitext(f.filename)[1]
        name = f"{uuid.uuid4().hex}{ext}"
        path = os.path.join(folder, name)
        f.save(path)
        deletefile(path)
        base_url = request.url_root.rstrip('/')
        return f"{base_url}/{name}"

    @app.route('/<filename>', methods=['GET'])
    def serve_image(filename):
        return send_from_directory(folder, filename)

    @app.errorhandler(404)
    def page_not_found(e):
        return redirect(url_for('index'))
