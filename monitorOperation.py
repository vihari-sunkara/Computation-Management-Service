from flask import Flask, render_template,jsonify,Response,request
import json
import random
import requests
import os

app = Flask(__name__)

@app.route('/compute',methods=['POST','GET'])
def postData():
	print("in 8085: ")
	print("req data: ",request)
	# num1 = request.json["num1"]
	# num2 = request.json["num2"]
	# data={"num1":4,"num2":5}
	exp = request.args.get('exp')
	
	operationType = request.args.get('operationType')
	operation =  request.args.get('operation')
	if(operationType=="math"):
		url1 = "http://192.168.56.108:8000/computeMath"
		params = {"exp":exp}
		try:
			response = requests.get(url1, headers={'User-Agent': 'Chrome'}, params=params)
			print("response from one: ",response.status_code)
			res1 = response.status_code
			if(res1==200):
				jsonData = response.json()
				result = jsonData["result"]
				print("sum in 8085: ",result)
				dataNew = {"resCode":response.status_code,"result":result}
				response = app.response_class(response=json.dumps(dataNew),mimetype='application/json')
				response.headers['Access-Control-Allow-Origin'] = "*"
				response.status_code = 200
				return response

		except:
			print("service1 down")
	# url1 = "http://192.168.56.102:8000/computeMath"
	elif operationType=="string":
		print("in string op")
		url2 = "http://192.168.56.107:8081/computeString"
		exp1 = request.args.get('exp1')
		exp2 = request.args.get('exp2')
		params = {"exp1":exp1,"exp2":exp2,"operation":operation}
		try:
			response = requests.get(url2, headers={'User-Agent': 'Chrome'}, params=params)
			print("response from one: ",response.status_code)
			res1 = response.status_code
			if(res1==200):
				jsonData = response.json()
				result = jsonData["result"]
				print("sum in 8085: ",result)
				dataNew = {"resCode":response.status_code,"result":result}
				response = app.response_class(response=json.dumps(dataNew),mimetype='application/json')
				response.headers['Access-Control-Allow-Origin'] = "*"
				response.status_code = 200
				return response

		except:
			print("service1 down")

# @app.route('/computeString',methods=['POST','GET'])
# def postData():
# 	print("in 8085: ")
# 	print("req data: ",request)
# 	# num1 = request.json["num1"]
# 	# num2 = request.json["num2"]
# 	# data={"num1":4,"num2":5}
# 	exp = request.args.get('exp')

# 	operation = request.args.get('operation')
# 	if(operation=="math"):
# 		url1 = "http://192.168.56.103:8001/computeString"
# 		params = {"exp":exp}
# 		try:
# 			response = requests.get(url1, headers={'User-Agent': 'Chrome'}, params=params)
# 			print("response from one: ",response.status_code)
# 			res1 = response.status_code
# 			if(res1==200):
# 				jsonData = response.json()
# 				result = jsonData["result"]
# 				print("sum in 8085: ",result)
# 				dataNew = {"resCode":response.status_code,"result":result}
# 				response = app.response_class(response=json.dumps(dataNew),mimetype='application/json')
# 				response.headers['Access-Control-Allow-Origin'] = "*"
# 				response.status_code = 200
# 				return response

# 		except:
# 			print("service1 down")
# 	# url1 = "http://192.168.56.102:8000/computeMath"
# 	elif operation=="string":
# 		url2 = "http://192.168.56.103:8001/computeString"
# 	# print("req args num1: ",request.args.get('num1'))
# 	# print("req args num2: ",request.args.get('num2'))
# 	# num1 = request.args.get('num1')
# 	# num2 = request.args.get('num2')
# 	# params = {"num1":num1,"num2":num2}
# 	# res1=200
# 	# res2=200

# 	# response=Response()
# 	# response.status_code = 200
# 	# response._content = b'{ "key" : "a" }'
	
			
# 		# print("status code: ",response.status_code)
	
	
	
    	
# 	# print("RESPONSE HERE:",response)
# 	# response.headers['Access-Control-Allow-Origin'] = "*"
# 	# response.status_code = 200
# 	# print("response here:",response)
# 	# return response





if __name__ == '__main__':
    app.run(port=8085,debug=True)