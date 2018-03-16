from flask import Flask, render_template
import tgchanbot
app = Flask(__name__)
"""
example:
check_group('@channelname')
check_group_admin('@channelname')
"""

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/checkgroup')
def check_group(channe_name):
    check=tgchanbot.check_group(tgchanbot.bot, channe_name)
    if check==None:
        #print('No group')
        pass
    else:
        return check #returns group\channel id
@app.route('/checkgroupadmin')
def check_group_admin(channe_name):
    check_admin=tgchanbot.check_group_admin(tgchanbot.bot, channe_name)
    if check_admin==None:
        #print('no admins')
        pass
    else:
        return check_admin #returns admin list

if __name__ == '__main__':
    tgchanbot.start_bot()
    app.run(host="localhost", port=8001, debug=True)