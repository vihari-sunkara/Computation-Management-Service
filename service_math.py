from flask import Flask, render_template,jsonify,request
import random
import json
from pymongo import MongoClient
import urllib.parse
from datetime import datetime
from math import sqrt, log, sin, cos, tan
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	data = {"sum":1,"randNum":1}
	response = app.response_class(
	response = json.dumps(data))
	response.headers['Access-Control-Allow-Origin']="*"
	#response = jsonify(data)
	response.status_code=200
	#response.headers['Access-Control-Allow-Origin']="*"
	print("response here:",response)
	return response

@app.route('/add', methods=['GET','POST'])
def add():
	print("req num1:  ",request.args.get('num1'))
	num1=request.args.get('num1')
	num2=request.args.get('num2')
	sum=int(num1) + int(num2)
	randNum = random.randint(1,40)
	print("sum here: ",sum)
	print("randNum here: ",randNum)
	data = {"sum":sum,"randNum":randNum}
	response = app.response_class(
	response = json.dumps(data))
	response.headers['Access-Control-Allow-Origin']="*"
	#response = jsonify(data)
	response.status_code=200
	#response.headers['Access-Control-Allow-Origin']="*"
	print("response here:",response)
	return response

@app.route('/computeMath', methods=['GET','POST'])
def math():
	client = MongoClient(host='192.168.56.1',port=27017)
	print(client)
	db = client['assn-database']
	ops = db.operations
	print("ops: ",ops)


	print("req expression:  ",request.args.get('exp'))
	encodedExp=request.args.get('exp')
	exp = urllib.parse.unquote(encodedExp)
	print("decoded string: ",exp)
	if("math.sqrt" in exp):
		val = exp[9:]
		result = eval(val)
		print("result before sqrt: ",result)
		result = sqrt(result)
	elif("log" in exp):
		val = exp[3:]
		result = eval(val)
		print("result before log: ",result)
		result = log(result)
	elif("sin" in exp):
		val = exp[3:]
		result = eval(val)
		print("result before sin: ",result)
		result = sin(result)
	elif("cos" in exp):
		val = exp[3:]
		result = eval(val)
		print("result before cos: ",result)
		result = cos(result)
	elif("tan" in exp):
		val = exp[3:]
		result = eval(val)
		print("result before tan: ",result)
		result = tan(result)
	else:
		result=eval(exp)
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	operation = {
	'query':exp,
	'result':result,
	'created_on': dt_string
	}
	print("inserted record: ",operation)
	res = ops.insert_one(operation)
	print("insert result objId: ",res)
	print("sum here: ",result)
	data = {"result":result}
	response = app.response_class(
	response = json.dumps(data))
	response.headers['Access-Control-Allow-Origin']="*"
	response.status_code=200
	print("response here:",response)
	return response
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)