import os
import requests
import json 
from flask import Flask, render_template, request
from groq import Groq   
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_food_recommendations(mood):
    chat_completion = client.chat.completions.create(
        messages=[ 
            {
                "role": "user",
                "content": f'''Recommend food based on the following mood: 
                {mood} 
                Provide the real life existing food recommendations in JSON format, with a "food_recommendations" field. 
                Each item in the list should include the food name and a URL to a recipe for that food.
                Make sure the url to recipe is a search onhttps://www.allrecipes.com/search?q="food"
                Give response only in json nothing else
                also add emojis before food name which relates a bit to the food
                The format must be strictly follow:
                food_recommendations: [
                    {{ "food": "food_name", "recipe_url": "working_url_to_recipe" }} ,
                    ...
                ]
                ''' ,
            }
        ],
        model='llama3-70b-8192'
    )
    food_recommendations = chat_completion.choices[0].message.content
    try:
        food_json = json.loads(food_recommendations)
        return food_json.get('food_recommendations', [])
    except json.JSONDecodeError:
        return ["Error parsing food recommendations"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mood = request.form['mood']
        food_recommendations = get_food_recommendations(mood)
        return render_template('index.html', food_recommendations=food_recommendations)
    return render_template('index.html', food_recommendations=None)

if __name__ == '__main__':
    app.run(debug=True)
