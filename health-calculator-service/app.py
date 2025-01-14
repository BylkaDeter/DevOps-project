from flask import Flask, request, jsonify
from health_utils import calculate_bmi , calculate_bmr 

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    """
    Endpoint to calculate BMI.
    Expects a JSON payload with 'height' (meters) and 'weight' (kg).
    Returns the calculated BMI.
    """
    try:
        data = request.get_json()
        height = data.get('height')
        weight = data.get('weight')

        if height is None or weight is None:
            return jsonify({"error": "Both 'height' and 'weight' are required."}), 400

        bmi_value = calculate_bmi(height, weight)
        return jsonify({"bmi": round(bmi_value, 2)})
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while calculating BMI.", "details": str(e)}), 500


@app.route('/bmr', methods=['POST'])
def bmr():
    """
    Endpoint to calculate BMR.
    Expects a JSON payload with 'height' (cm), 'weight' (kg), 'age' (years), and 'gender'.
    Returns the calculated BMR.
    """
    try:
        data = request.get_json()
        height = data.get('height')
        weight = data.get('weight')
        age = data.get('age')
        gender = data.get('gender')

        if None in [height, weight, age, gender]:
            return jsonify({"error": "All fields ('height', 'weight', 'age', and 'gender') are required."}), 400

        bmr_value = calculate_bmr(height, weight, age, gender)
        return jsonify({"bmr": round(bmr_value, 2)})
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while calculating BMR.", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)