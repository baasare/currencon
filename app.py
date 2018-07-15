import os
from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)      



api_key = "SDX6VUX5ZH5RBERM"

#"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=GHS&to_currency=USD&apikey=SDX6VUX5ZH5RBERM"






def cedi_to_oth(amount, curr):
	currency1 = "USD"
	currency2 = "GBP"
	currency3 = "EUR"


	if curr == currency1:
		cur = currency1 
		url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=GHS&to_currency=" + cur + "&apikey=" + api_key
	elif curr == currency2:
		cur = currency2 
		url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=GHS&to_currency=" + cur + "&apikey=" + api_key
	elif curr == currency3:
		cur = currency1 
		url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=GHS&to_currency=" + cur + "&apikey=" + api_key
	else:
		print "Sorry please enter a valid option"

	q = requests.get(url)
	json_d = q.json()
	json_d = json_d.values()
	json_d = json_d[0]
	json_d = json_d.values()
	rate = json_d[4]
	rate = rate.encode("ascii", "replace")
	rate = float(rate)

	converted_amount = rate * float(amount)
	converted_amount = round(converted_amount, 2)


	return str(converted_amount)
	
	 
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




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
#    app.run(debug=True, port=33507)
