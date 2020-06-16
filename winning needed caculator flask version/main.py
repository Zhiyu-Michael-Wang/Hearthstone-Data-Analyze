from flask import Flask,request,redirect,render_template,url_for,send_from_directory
from markupsafe import escape
import os
import caculator as hsc
import uuid

app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('caculation'))


@app.route('/caculation', methods=["POST", "GET"])
def caculation():
    if request.method == "POST":
        winning_needed = request.form["total_winning_needed"] 
        streak_bounce = request.form["winning_streak_bounce"]
        rate = request.form["winning_rate"]

        file_id = uuid.uuid1()

        hsc.main(
            total_winning_needed=winning_needed,
            winning_streak_bounce=streak_bounce,
            winning_rate=rate,
            file_id=file_id
        )
        
        file_url = url_for('download_file', filename=str(file_id) + '.png')
        return render_template('result.html',file_url=file_url)
    else:
        return render_template('caculation.html')


@app.route('/download_file/<filename>')
def download_file(filename):
    return send_from_directory('templates\pic',
                               filename, as_attachment=True)


@app.route('/test/<file_id>')
def test(file_id):
    file_url = url_for('download_file', filename='result' + str(file_id) + '.png')
    return render_template('test.html', file_url=file_url)

