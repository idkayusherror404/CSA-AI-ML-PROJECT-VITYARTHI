# Oil Reserve Calculator - Backend
# Run: pip install flask flask-cors
# Run: python app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    # Get values from frontend
    area       = float(data['area'])        # acres
    thickness  = float(data['thickness'])   # feet
    porosity   = float(data['porosity'])    # percent
    water_sat  = float(data['water_sat'])   # percent

    # Convert percent to decimal
    porosity  = porosity / 100
    water_sat = water_sat / 100

    # STOIIP Formula (standard petroleum engineering formula)
    # STOIIP = 7758 * Area * Thickness * Porosity * (1 - WaterSaturation) / 1.2
    stoiip = 7758 * area * thickness * porosity * (1 - water_sat) / 1.2

    # Recovery Factor - simple estimate based on porosity
    if porosity > 0.20:
        recovery_factor = 0.40   # good reservoir
    elif porosity > 0.12:
        recovery_factor = 0.25   # average reservoir
    else:
        recovery_factor = 0.10   # poor reservoir

    # Recoverable oil
    recoverable = stoiip * recovery_factor

    # Convert barrels to million barrels
    stoiip_mm      = round(stoiip / 1000000, 2)
    recoverable_mm = round(recoverable / 1000000, 2)

    return jsonify({
        'stoiip':      stoiip_mm,
        'recoverable': recoverable_mm,
        'recovery_factor': int(recovery_factor * 100)
    })

if __name__ == '__main__':
    print("Server running at http://localhost:5000")
    app.run(port=5000)
