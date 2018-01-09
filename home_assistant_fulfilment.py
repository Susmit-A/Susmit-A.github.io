import json
import os
import urllib
from flask import Flask
from flask import request
from flask import make_response
app=Flask(__name__)
@app.route('/webhook',methods=['POST','GET'])
def webhook():
	req = request.get_json(silent=True,force=True)
	print("Request:")
	print(json.dumps(req,indent=4))
	res={
		"speech": "Complete",
		"displayText": "Complete",
		"source": "Myself"
	}
	res=json.dumps(res,indent=4)
	r=make_response(res)
	r.headers['Content-Type']='application/json'
	return r

def makeWebHookResult(req):
	return {
		"speech": "Complete",
		"source": "Myself"
	}

if __name__ == '__main__':
	port=int(os.getenv('PORT',8080))
	app.run(port=port,host='localhost',ssl_context='adhoc',debug=False)

