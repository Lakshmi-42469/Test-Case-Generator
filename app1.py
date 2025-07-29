from flask import Flask, render_template, request
from test_case_logic import generate_test_case
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    test_cases = []
    if request.method == "POST":
        requirement_text = request.form.get("requirement")
        if requirement_text:
            test_cases = generate_test_case(requirement_text)
    
    return render_template("index.html", test_cases=test_cases)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
