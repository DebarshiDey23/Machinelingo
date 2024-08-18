from flask import Flask, render_template, request, jsonify
from backend.aws_translate import translate_text
from backend.lessons import generate_lesson

app = Flask(__name__)

# Store user progress and selected language
user_data = {
    'language': None,
    'level': 1
}

@app.route('/')
def home():
    return render_template('select_language.html')  # Language selection page

@app.route('/start', methods=['POST'])
def start():
    # Set the user's language preference
    user_data['language'] = request.json.get('language')
    return jsonify({'message': f"Starting lessons in {user_data['language']}!"})

@app.route('/lesson', methods=['GET'])
def lesson():
    # Generate a lesson based on the user's language and level
    lesson_content = generate_lesson(user_data['language'], user_data['level'])
    return jsonify({'lesson': lesson_content})

@app.route('/progress', methods=['POST'])
def progress():
    # Update user level based on their progress
    user_data['level'] += 1
    return jsonify({'message': f"Moving to level {user_data['level']}!"})

if __name__ == '__main__':
    app.run(debug=True)
