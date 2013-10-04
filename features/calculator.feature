Feature: Confirming that the tip calculator form works

	Scenario: check that the form submits successfully
		When I go to the tip calculator
		And I submit the form with a valid total and tip percentage
		Then I should see the results page


	Scenario: check that tip value is correct
		When I enter the meal cost is $50 and tip is 20%
		Then the tip amount is $10
		