from flask import Flask, render_template, request, redirect, url_for, jsonify
import subprocess
import os

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('add-facial.html')

# Route to trigger the enrollment process
@app.route('/enroll', methods=['POST'])
def enroll():
    name = request.form.get('name')  # Get name from form input
    if name:
        subprocess.run(['python', 'add_faces.py', name])  # Run the enrollment script
        return jsonify({'message': f'Enrollment for {name} complete!'})
    return jsonify({'error': 'Name is required!'}), 400

# Route to trigger the facial recognition test
@app.route('/recognize', methods=['POST'])
def recognize():
    subprocess.run(['python', 'test.py'])  # Run the recognition script
    return jsonify({'message': 'Facial recognition process started!'})

if __name__ == '__main__':
    app.run(debug=True)

subprocess.run(['python', 'add_faces.py'])  # No need to pass name; it's input in the script
subprocess.run(['python', 'test.py'])



