from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
 	return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
	try: 
		meal_cost = request.form['meal_cost']
		tip_percentage = request.form['tip_percentage']
		result = meal_cost*tip_percentage

  	return render_template('results.html', result=result)

 
if __name__ == '__main__':
	app.run(debug=True)
