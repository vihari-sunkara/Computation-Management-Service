from flask import Flask, render_template, jsonify, request
import random
import json
from pymongo import MongoClient
import urllib.parse
from datetime import datetime

app = Flask(__name__)

def revStr(s1,s2):
	return ''.join(reversed(s1))

def toUpper(s1,s2):
	return s1.upper()

def toLower(s1,s2):
	return s1.lower()

def concat(s1,s2):
	return s1+s2

def getResult(str1,str2,op):
	switcher = {
	"reverse":revStr,
	"toUpper":toUpper,
	"toLower":toLower,
	"concatenate":concat
	}
	func = switcher.get(op,lambda:"invalid operation")
	return func(str1,str2)


@app.route('/',methods=['GET','POST'])
def index():
	num1 = 10
	num2 = 20
	sum = num1+num2
	randNum = random.randint(70,100)
	data = {"sum":sum, "randNum":randNum}
	response = jsonify(data)
	response.status_code = 200
	response.headers['Access-Control-Access-Origin'] = "*"
	return response

@app.route('/add',methods=['GET','POST'])
def add():
	print("request args num1: ",request.args.get("num1"))
	num1 = request.args.get("num1")
	num2 = request.args.get("num2")
	sum = int(num1)+int(num2)
	randNum = random.randint(70,100)
	data = {"sum":sum, "randNum":randNum}
	response = app.response_class(
	response = json.dumps(data))
	response.headers['Access-Control-Access-Origin'] = "*"
	response.status_code = 200
	print("response here: ",response)
	return response

@app.route('/computeString',methods=['GET','POST'])
def math():
	client = MongoClient(host='192.168.56.1', port=27017)
	print(client)
	db = client['assn-database']
	ops = db.operations
	print(ops)
	print("req expression exp1: ",request.args.get('exp1'))
	print("req expression exp2: ",request.args.get('exp2'))
	exp1 = request.args.get('exp1')
	exp2= request.args.get('exp2')
	operation = request.args.get('operation')
	result = getResult(exp1,exp2,operation)
	query = operation+" on--> "+exp1+" "+exp2
	now = datetime.now()
	dt_string = now.strftime("%d/%M/%Y %H:%M:%S")
	op = {
	'query': query,
	'result':result,
	'created_on':dt_string
}
	print("op inserted: ",op)
	res = ops.insert_one(op)
	print("insert obj id: ",res)
	print("result here:", result)
	data = {"result":result}
	response = app.response_class(
	response = json.dumps(data))
	response.headers['Access-Control-Access-Origin'] = "*"
	response.status_code = 200
	print("response here: ",response)
	return response

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8081,debug=True)
	
	
	
	