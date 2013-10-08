Feature: Confirming that the tip calculator form works

	Scenario: check that the form submits successfully
		When I go to the tip calculator
		And I submit the form with a valid total and tip percentage
		Then I should see the results page


	Scenario: check that tip value is correct
		When I go to the tip calculator
		And I enter the meal cost is $50 
		And I enter the tip is 20%
		And I submit the form
		Then I should see the tip amount is $10 on results page

	
		