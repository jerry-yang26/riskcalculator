from flask import Flask, render_template, request, jsonify
from risk_calculator import MortgageRiskCalculator # type: ignore

app = Flask(__name__)
calculator = MortgageRiskCalculator()

@app.route('/')
def index():
    return render_template('index.html')
///
@app.route('/calculate', methods=['POST'])
def calculate_risk():
    try:
        # Get user inputs
        user_data = {
            'monthly_income': float(request.form.get('monthly_income', 0)),
            'monthly_debt': float(request.form.get('monthly_debt', 0)),
            'monthly_savings': float(request.form.get('monthly_savings', 0)),
        }
        
        # Get economic inputs (in real app, these would be fetched from APIs)
        economic_data = {
            'current_rate': float(request.form.get('current_rate', 7.0)),
            'rate_6_months_ago': float(request.form.get('rate_6_months_ago', 6.5)),
            'current_inflation': float(request.form.get('current_inflation', 3.5)),
        }
        
        # Calculate risk
        result = calculator.calculate_overall_risk(user_data, economic_data)
        advice = calculator.get_advice(result['overall_score'])
        
        return jsonify({
            'success': True,
            'risk_score': result['overall_score'],
            'individual_scores': result['individual_scores'],
            'advice': advice
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
///
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
