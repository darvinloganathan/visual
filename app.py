from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('try3.html')
if __name__ == "__main__":
    app.run()
    
