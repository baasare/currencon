from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)      


api_key = "4VjfD5UhQcCADQTeswWdXYEmSLVmuq"


def cedi_to_oth(amount, curr):
	currency1 = "USD"
	currency2 = "GBP"
	currency3 = "EUR"


	if curr == currency1:
		cur = currency1 
		url = "https://www.amdoren.com/api/currency.php?api_key=" + api_key + "&from=GHS&to=" + cur + "&amount=" + amount
	elif curr == currency2:
		cur = currency2 
		url = "https://www.amdoren.com/api/currency.php?api_key=" + api_key + "&from=GHS&to=" + cur + "&amount=" + amount
	elif curr == currency3:
		cur = currency1 
		url = "https://www.amdoren.com/api/currency.php?api_key=" + api_key + "&from=GHS&to=" + cur + "&amount=" + amount
	else:
		print "Sorry please enter a valid option"

	q = requests.get(url)
	json_d = q.json()

	return str(json_d[u'amount'])
	
	 
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def res():
	if request.method == 'POST':
		value = request.form['value']
		currency = request.form['currency']
		
		if currency == "USD":
			denom = " Dollars"
		elif currency == "GBP":
			denom = " Pounds"
		elif currency == "EUR":
			denom = " Euros"
		else:
			denom = "Error"
		fresult = cedi_to_oth(value, currency)
		return render_template('result.html', fresult = fresult, denom = denom)
	
 
if __name__ == '__main__':
  app.run(debug=True)
