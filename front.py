from flask import Flask, render_template, request
from embed import embed
from classify import classificador_textos

import os
import joblib

# Create an instance of the embed class
e = embed("API_KEY", "dataset/dados_tratados1.csv")

app = Flask(__name__)

@app.route('/music', methods=['GET', 'POST'])
def home():
    user_input = ""
    if request.method == 'POST':
        action = request.form.get("action")

        if action == "submit":
            user_input = request.form.get('video_description')
            hashtags = request.form.get('hashtags')

            if user_input != "":
                result = e.recomend_music(user_input + hashtags)
            else:
                result = None
            
            return render_template('music.html', result=result, user_input=user_input, hashtags=hashtags)
        else:
            return render_template('music.html', result=None, user_input="", hashtags="")
    else:
        return render_template('music.html', result=None, user_input="", hashtags="")
    
@app.route('/', methods=['GET', 'POST'])
def index():
    action = request.form.get("action")

    if action == "music":
        return render_template('music.html', result=None, user_input="", hashtags="")
    
    if action == "evaluate":
        return render_template('/viral.html', result=None, user_input="", hashtags="")
    
    return render_template("index.html")
    

@app.route('/viral', methods=['GET', 'POST'])
def viral():
    result = None
    user_input = ""
    if request.method == 'POST':
        action = request.form.get("action")

        if action == "submit":
            user_input = request.form.get('video_description')
            hashtags = request.form.get('hashtags')

            if user_input != "":
                result = classificador_textos(user_input + hashtags)
            else:
                result = None
            

            return render_template('/viral.html', result=result, user_input=user_input, hashtags=hashtags)
        else:
            return render_template('/viral.html', result=None, user_input="", hashtags="")
    else:
        return render_template('/viral.html', result=None, user_input="", hashtags="")
    
@app.route('/show-modal', methods=['GET'])
def show_modal():
    # Here, you can return a response that includes JavaScript to open the modal
    response = '''
        <script>
        document.getElementById("myModal").style.display = "block";
        </script>
    '''
    return response

if __name__ == '__main__':
    app.run(debug=True)
