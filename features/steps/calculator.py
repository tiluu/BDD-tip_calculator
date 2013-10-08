@when(u'I go to the tip calculator')
def step_impl(context):
    context.browser.get('http://127.0.0.1:5000/')

@when(u'I submit the form with a valid total and tip percentage')
def step_impl(context):
	br = context.browser
	br.get('http://127.0.0.1:5000/')
	meal_cost = br.find_element_by_name("meal_cost")
	meal_cost.send_keys("30")
	tip_percentage = br.find_element_by_name("tip_percentage")
	tip_percentage.send_keys("20")
	br.find_element_by_id("submit").click()

@then(u'I should see the results page')
def step_impl(context):
    assert context.browser.title == "Tip calculator"

@when(u'I enter the meal cost is $50')
def step_impl(context):
	br = context.browser
	br.get('http://127.0.0.1:5000/')
	meal_cost = br.find_element_by_name("meal_cost")
	meal_cost.send_keys("50")

@when(u'I enter the tip is 20%')
def step_impl(context):
	br = context.browser
	tip_percentage = br.find_element_by_name("tip_percentage")
	tip_percentage.send_keys("20")

@when(u'I submit the form')
def step_impl(context):
	br = context.browser
	br.find_element_by_id("submit").click()

@then(u'I should see the tip amount is $10 on results page')
def step_impl(context):
	br = context.browser
	result = br.find_element_by_id('results')
