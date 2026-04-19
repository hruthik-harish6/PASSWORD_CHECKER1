from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_password(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password): score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", password): score += 1
    
    remarks = ["Very Weak", "Weak", "Fair", "Strong", "Unstoppable"]
    return {"score": score, "remark": remarks[score]}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    result = check_password(data.get('password', ''))
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)