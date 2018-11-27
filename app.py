from flask import Flask,render_template,request
import genlist
import numpy as np
import math
app = Flask(__name__)

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.debug = True

@app.route("/set",methods=['GET'])
def sett():
     if request.method == 'GET':
         mode = request.args.get('mode')
         if mode=='host':
             return render_template('app.pug' , IP='160.10.0.0' , hostNum=10 , samNum=3 , host='on')
         else:
             return render_template('app.pug' , IP='160.10.0.0' , netNum=10 , samNum=3)

@app.route("/")
def run():
    
    return render_template('app.pug' , IP='160.10.0.0' , netNum=10 , samNum=3)

@app.route("/cal" , methods=['GET', 'POST'] )
def cal():

    if request.method == 'GET':
        # print("med="+request.method)
        # print(request)
        netNum = request.args.get('netNumber')
        hostNum = request.args.get('hostNumber')
        samNum = request.args.get('sampleNumber')
        IP = request.args.get('IP')

         

        if IP == '':
            return render_template('app.pug', resultarray=[])

        c , fix = genlist.defClass(IP)

        if hostNum:
            netNum = 2**(32 - fix - math.ceil( math.log2(int(hostNum) ) ))
    
        s , a , info = genlist.run(str(IP),int(netNum),int(samNum))
        if hostNum:
            return render_template('app.pug', resultarray=a , IP=IP , samNum=samNum , info=info , hostNum=hostNum , host='on')
        else:
            return render_template('app.pug', resultarray=a , IP=IP , netNum=netNum , samNum=samNum , info=info )
 
if __name__ == "__main__":
    app.run()