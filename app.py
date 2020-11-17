from flask import Flask, render_template, request, redirect, url_for
from io import BufferedReader
import baseline_model, model2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    res3 = model2.parse_audio(uploaded_file.filename)
    return render_template('index.html', data=res3)
  

if __name__ == "__main__":
  app.run(debug=True)
