import subprocess
from flask import Flask, request, render_template, redirect, url_for
from wtforms import Form, validators
from wtforms.fields import StringField, SelectField
from wtforms.fields.html5 import IntegerField, TimeField
from AlarmManager import *
from os import listdir,getcwd
from os.path import isfile, join

app = Flask(__name__)
alarms = AlarmManager()

class ChangeVolumeForm(Form):
    volume = IntegerField(validators=[validators.InputRequired(), validators.NumberRange(min=0, max=100)])

class AlarmForm(Form):
    name=StringField(label="Alarm name", validators=[validators.InputRequired()])
    ringtone=SelectField(label="Ringtone", validators=[validators.InputRequired()])
    time = TimeField(label="Time", validators=[validators.InputRequired()])

class TestSoundForm(Form):
    ringtone=SelectField(label="Ringtone", validators=[validators.InputRequired()])


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form = ChangeVolumeForm(request.form)
        if form.validate():
            subprocess.call(["bash", "/root/web/volume.sh", "setvolume", request.form['volume']])
            return redirect(url_for('index'))
    else:
        form = ChangeVolumeForm()
    alarms_list = alarms.get_all_alarm()
    return render_template("index.html", volume_form=form, alarms_list=alarms_list)

@app.route('/add_alarm', methods=["GET", "POST"])
def add_alarm():
    files = [(f,f) for f in listdir(join(getcwd(),"ringtones")) if isfile(join(getcwd(),"ringtones", f))]
    if request.method == "POST":
        form = AlarmForm(request.form)
        form.ringtone.choices = files
        if form.validate():
            alarms.add_alarm(Alarm(request.form["name"],request.form["ringtone"],request.form["time"]))
            return redirect(url_for('index'))
    else:
        form = AlarmForm()
    
    form.ringtone.choices = files
    return render_template("add_alarm.html", alarm_form=form)

@app.route('/enable')
def enable():
    subprocess.call(["bash", "/root/web/audio.sh", "enable"])
    return redirect(url_for('index'))

@app.route('/disable')
def disable():
    subprocess.call(["bash", "/root/web/audio.sh", "disable"])
    return redirect(url_for('index'))

@app.route('/test_sound', methods=["GET", "POST"])
def test_sound():
    files = [(f,f) for f in listdir(join(getcwd(),"ringtones")) if isfile(join(getcwd(),"ringtones", f))]
    if request.method == "POST":
        form = TestSoundForm(request.form)
        form.ringtone.choices = files
        if form.validate():
            a = str(request.form['ringtone'])
            print(a)
            subprocess.call(["aplay", f"/root/web/ringtones/{a}"])
            return redirect(url_for('test_sound'))
    else:
        form = TestSoundForm()
    
    form.ringtone.choices = files
    return render_template("test_sound.html", test_form=form)



