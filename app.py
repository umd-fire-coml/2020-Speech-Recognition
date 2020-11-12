from flask import Flask, render_template, request, redirect, url_for
from io import BufferedReader
import visualization

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    #uploaded_file = BufferedReader(uploaded_file.stream)
    #print(type(uploaded_file.filename))
    res = visualization.visualizer(uploaded_file.filename)
    #return str(res)
    return render_template('index.html', data=res)
  

if __name__ == "__main__":
  app.run(debug=True)