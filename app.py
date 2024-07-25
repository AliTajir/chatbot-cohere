from flask import Flask, request, jsonify, render_template
import cohere

app = Flask(__name__)

# Replace with your Cohere API key
cohere_client = cohere.Client('KFvTQsTojOdu1Vdp2sZJqbaQx0BKJLHdEORtDYbc')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = cohere_client.generate(
        # model='xlarge',  # You can use different models like 'medium' or 'small'
        prompt=user_input,
        max_tokens=50
    )
    answer = response.generations[0].text.strip()
    return jsonify({'response': answer})

if __name__ == '__main__':
    app.run(debug=True)
