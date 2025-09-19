import datetime

class MortgageRiskCalculator:
    def __init__(self):
        # Based on your findings - these are the key risk factors
        self.risk_factors = {
            'interest_rate_trend': 0,      # Rising rates = higher risk
            'inflation_level': 0,          # High inflation = higher risk  
            'personal_savings': 0,         # Low savings = higher risk
            'debt_to_income': 0,          # High DTI = higher risk
            'home_price_trend': 0,        # Rapidly rising prices = higher risk
            'job_stability': 0            # Low stability = higher risk
        }
    
    def calculate_interest_rate_risk(self, current_rate, rate_6_months_ago):
        """
        Risk increases if rates are rising rapidly
        Based on your finding that 2022 was transition year from low to high rates
        """
        rate_change = current_rate - rate_6_months_ago
        
        if rate_change > 2.0:  # Rapid increase like 2022
            return 4  # High risk
        elif rate_change > 1.0:
            return 3  # Moderate-high risk
        elif rate_change > 0.5:
            return 2  # Moderate risk
        else:
            return 1  # Low risk
    
    def calculate_inflation_risk(self, current_inflation):
        """
        Based on your finding that 2022 had peak inflation
        """
        if current_inflation > 8.0:  # Peak 2022 levels
            return 4
        elif current_inflation > 5.0:
            return 3
        elif current_inflation > 3.0:
            return 2
        else:
            return 1
    
    def calculate_savings_risk(self, monthly_savings, monthly_income):
        """
        You found low savings rates contributed to 2022 vintage problems
        """
        if monthly_income == 0:
            return 4
        
        savings_rate = (monthly_savings / monthly_income) * 100
        
        if savings_rate < 5:  # Very low like post-2022
            return 4
        elif savings_rate < 10:
            return 3
        elif savings_rate < 20:
            return 2
        else:
            return 1
    
    def calculate_dti_risk(self, monthly_debt, monthly_income):
        """
        Based on DTI analysis in your paper
        """
        if monthly_income == 0:
            return 4
            
        dti = (monthly_debt / monthly_income) * 100
        
        if dti > 45:  # High DTI tail from your data
            return 4
        elif dti > 36:
            return 3
        elif dti > 28:
            return 2
        else:
            return 1
    
    def calculate_overall_risk(self, user_inputs, economic_inputs):
        """
        Combine all risk factors into overall score
        """
        # Calculate individual risk scores
        interest_risk = self.calculate_interest_rate_risk(
            economic_inputs['current_rate'], 
            economic_inputs['rate_6_months_ago']
        )
        
        inflation_risk = self.calculate_inflation_risk(
            economic_inputs['current_inflation']
        )
        
        savings_risk = self.calculate_savings_risk(
            user_inputs['monthly_savings'],
            user_inputs['monthly_income']
        )
        
        dti_risk = self.calculate_dti_risk(
            user_inputs['monthly_debt'],
            user_inputs['monthly_income']
        )
        
        # Weight the factors (based on your findings)
        weighted_score = (
            interest_risk * 0.25 +      # Interest rate trend - major factor
            inflation_risk * 0.20 +     # Inflation - major factor  
            savings_risk * 0.25 +       # Personal savings - major factor
            dti_risk * 0.30             # Debt-to-income - most important personal factor
        )
        
        return {
            'overall_score': round(weighted_score, 1),
            'individual_scores': {
                'interest_rate': interest_risk,
                'inflation': inflation_risk,
                'savings': savings_risk,
                'debt_to_income': dti_risk
            }
        }
    
    def get_advice(self, risk_score):
        """
        Provide advice based on risk score
        """
        if risk_score >= 3.5:
            return {
                'level': 'HIGH RISK',
                'color': 'red',
                'advice': [
                    "Consider waiting if possible - current conditions resemble problematic 2022 vintage",
                    "If you must buy, ensure you have 6+ months emergency savings",
                    "Avoid adjustable rate mortgages",
                    "Consider a smaller home to keep payments manageable",
                    "Shop aggressively for the lowest rate possible"
                ]
            }
        elif risk_score >= 2.5:
            return {
                'level': 'MODERATE RISK',
                'color': 'orange', 
                'advice': [
                    "Proceed with caution - some concerning economic signals",
                    "Build larger emergency fund before purchasing",
                    "Lock in fixed rate quickly if you decide to buy",
                    "Consider homes below your maximum budget",
                    "Monitor economic indicators closely"
                ]
            }
        elif risk_score >= 1.5:
            return {
                'level': 'LOW-MODERATE RISK',
                'color': 'yellow',
                'advice': [
                    "Generally favorable conditions for buying",
                    "Maintain strong emergency fund",
                    "Shop around for best mortgage rates",
                    "Consider market timing in your local area"
                ]
            }
        else:
            return {
                'level': 'LOW RISK',
                'color': 'green',
                'advice': [
                    "Good time to buy based on economic conditions",
                    "Take advantage of favorable market timing",
                    "Still maintain emergency savings",
                    "Consider longer-term fixed rate mortgages"
                ]
            }

