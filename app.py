from flask import Flask, render_template
import openai
from config import OPENAI_API_KEY


# APP configuration
app = Flask(__name__)  # Flask application
openai.api_key = OPENAI_API_KEY  # access to OpenAI
client = openai.OpenAI()  # creating an OpenAI client instance


# render index.html interface
@app.route('/')
def index():
    """default interface page (pre-request)"""
    return render_template('index.html')


def ask_openai(openai_client, system_prompt, user_prompt):
    """calls openai"""
    try:
        completion = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )
        return completion.choices[0].message.content
    # debugging
    except Exception as openai_error:
        return f"Unexpected error: {openai_error}"


if __name__ == '__main__':
    app.run(debug=True)
