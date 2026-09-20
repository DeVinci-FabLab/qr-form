from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/')
def qr():
    form_url = os.getenv('FORM_URL', 'https://example.com')
    return redirect(form_url, code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
