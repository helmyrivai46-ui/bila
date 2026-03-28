from flask import Flask, Response
import os

app = Flask(__name__)

@app.route('/stream/<filename>')
def stream_audio(filename):
    def generate():
        with open(f'{filename}', 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    f.seek(0)  # Loop infinite
                    data = f.read(4096)
                yield data
    return Response(generate(), mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)