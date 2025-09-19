from risk_calculator import MortgageRiskCalculator	# type: ignore
def test_scenarios():
    calc = MortgageRiskCalculator()
	
	# Test high-risk scenario (like 2022)
    user_inputs = {
		'monthly_income': 5000,
	    'monthly_debt': 2000,  # High DTI
	    'monthly_savings': 200,  # Low savings
		}
    economic_inputs = {
	    'current_rate': 7.5,
	    'rate_6_months_ago': 5.0,  # Rapid rate increase
	    'current_inflation': 8.0,  # High inflation
	    }
    high_risk_result = calc.calculate_overall_risk(user_inputs,economic_inputs)
    print("High Risk Scenario:", high_risk_result)
    
if __name__ == "__main__":
	test_scenarios()
