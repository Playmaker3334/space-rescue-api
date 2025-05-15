from flask import Flask, jsonify, make_response
import random

app = Flask(__name__)

# Lista de sistemas y sus códigos de reparación
SYSTEMS = ["navigation", "communications", "life_support", "engines", "deflector_shield"]
REPAIR_CODES = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Variable global para almacenar el sistema dañado actual
current_damaged_system = random.choice(SYSTEMS)

@app.route('/status', methods=['GET'])
def get_status():
    global current_damaged_system
    current_damaged_system = random.choice(SYSTEMS)
    print(f"Status requested. Damaged system set to: {current_damaged_system}")
    return jsonify({"damaged_system": current_damaged_system})

@app.route('/repair-bay', methods=['GET'])
def get_repair_bay():
    global current_damaged_system
    
    repair_code = REPAIR_CODES.get(current_damaged_system)
    if not repair_code:
        print(f"Error: current_damaged_system '{current_damaged_system}' has no repair code.")
        return "Error: Unknown system or repair code not found.", 500
    
    print(f"Repair-bay requested. System: {current_damaged_system}, Code: {repair_code}")
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Repair Bay</title>
</head>
<body>
    <div class="anchor-point">{repair_code}</div>
</body>
</html>"""
    
    response = make_response(html_content)
    response.headers['Content-Type'] = 'text/html'
    return response

@app.route('/teapot', methods=['POST'])
def teapot():
    print("Teapot requested.")
    return "I'm a teapot", 418

if __name__ == '__main__':
    # Producción: No usar debug=True
    app.run(host='0.0.0.0', port=5000)
