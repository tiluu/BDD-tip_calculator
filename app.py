from flask import Flask, render_template, request
 
app = Flask(__name__)      
 
@app.route('/')
def home():
 	return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
	error_message={'errors':[]}
	try: 
		assert float(request.form['meal_cost']) > 0
		meal_cost = float(request.form['meal_cost'])
	except ValueError:
		error_message['errors'].append('The meal cost must be a number')
	except AssertionError:
		error_message['errors'].append('The meal cost must be greater than 0')

	try: 
		assert float(request.form['tip_percentage']) > 0
		tip_percentage = float(request.form['tip_percentage'])
	except ValueError:
		error_message['errors'].append('The tip must be a number')
	except AssertionError:
		error_message['errors'].append('The tip must be greater than 0')

	try:
		
		result = meal_cost*tip_percentage/100
	except (ValueError, UnboundLocalError):
		return render_template('home.html',error_message=error_message)
	
  	return render_template('results.html', result=result)

 
if __name__ == '__main__':
	app.run(debug=True)
