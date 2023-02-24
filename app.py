# from flask import Flask, request, render_template
# import openai

# app = Flask(__name__)

# # Initialize the OpenAI API client with your API key
# openai.api_key = "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"

# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')


# @app.route('/prompt', methods=['POST'])
# def prompt():
#     prompt = request.form.get('prompt')
#     response = openai.Completion.create(
#         engine = "text-davinci-002",
#         prompt = prompt,
#         max_tokens = 1024,
#         n=1,
#         stop = None,
#         temperature = 0.5,
#     )
#     return response.choices[0].text

# if __name__ == '__main__':
#     app.run()

from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Set OpenAI API key
openai.api_key = "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"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/prompt', methods=['POST'])
def prompt():
    try:
        # Get user input
        prompt = request.json['input_text']

        # Generate response using OpenAI API
        response = openai.Completion.create(
            engine = "text-davinci-002",
            prompt = prompt,
            max_tokens = 1024,
            n=1,
            stop = None,
            temperature = 0.5,
        )

        # Return response
        return { 'output_text': response.choices[0].text }

    except Exception as e:
        # Log error
        app.logger.error(str(e))

        # Return error message to user
        return "An error occurred. Please try again later.", 500

if __name__ == '__main__':
    app.run(debug=True)