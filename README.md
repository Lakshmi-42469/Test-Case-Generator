# 🧪 Test Case Generator (Rule-Based)

This is a simple **Flask web application** that generates test cases from natural language requirement descriptions using **rule-based logic** (non-AI version). It's useful for testers and QA professionals to quickly derive basic test cases from user stories or features.


## 🚀 Features

- Accepts plain-text requirements
- Generates structured test cases
- Web-based user interface using Flask + HTML
- No AI/ML dependency – lightweight and fast


## 📁 Project Structure

TestCaseGenerator/
├── app.py                # Flask backend
├── test_case_logic.py    # Logic to generate test cases
├── templates/
│   └── index.html        # Frontend UI
└── README.md             # Project info


## 🛠️ Technologies Used

- Python 3.x
- Flask
- HTML/CSS (Jinja2 templating)


## 🖥️ How to Run Locally

1. Clone this repository or download the ZIP:
git clone https://github.com/YOUR_USERNAME/test-case-generator.git
cd test-case-generator


2. Install dependencies:
pip install flask

3. Run the Flask app:
python app.py

4. Open in browser:
http://127.0.0.1:5000


## 📝 Example Input

The user must login using email and password. Submit button should trigger validation. If fields are empty, show error.

### 🔍 Example Output

TC_001: Enter valid email and password -> Login Successful  
TC_002: Enter invalid password -> Show Error Message  
TC_003: Leave email field -> Show required field message  
TC_004: Click submit without filling fields -> Show error message  


## 🤝 Contributing

Feel free to fork and enhance the project:
- Export test cases as CSV or PDF  
- Add support for complex scenarios  
- Improve UI styling  

## 📄 License

This project is open-source under the [MIT License](LICENSE).

⭐ If you found this project helpful, please give it a star on GitHub!
