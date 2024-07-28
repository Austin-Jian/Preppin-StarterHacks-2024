from flask import Flask, request, jsonify, render_template
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from PIL import Image
import openai
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/MealPlanNow.html')
def MealPlanNow():
    return render_template('MealPlanNow.html')

@app.route('/surveyChoices.html')
def surveyChoices():
    return render_template('surveyChoices.html')

@app.route('/survey.html')
def survey():
    return render_template('survey.html')

@app.route('/survey1.html')
def survey1():
    return render_template('survey1.html')

@app.route('/survey2.html')
def survey2():
    return render_template('survey2.html')


@app.route('/extract', methods=['POST'])
def extract():
    data = request.json
    items = data.get('items', [])
    
    # Process the list items as needed
    print("Extracted items:", items)
    
    prompt = f"Given these items, {items} give me 3 links that follow to three compeetly different specific recipe websites that uses these foods, then a list of the name of the dish that eash reipce makes. Format it such that on the first line is just the three links seperated by just commas, no spaces. Then, on the next line, give me the three titles of the recicpes separated by commas no spaces. DO NOT have a number such as 1. in front nof each line. There should be a total of two lines in the output text"

    response = client.chat.completions.create(
    model="gpt-4o",
    
    messages=[
        {
        "role": "system",
        "content": prompt}
    ],
    temperature=0.7,
    max_tokens=1000,
    top_p=1
    )
    data = response.choices[0].message.content
    print(data)

    links = list((data.split('\n'))[0].split(","))
    titles = list((data.split('\n'))[-1].split(","))
    print(links)
    print(links[0])
    print(links[1])
    # Return a response

    infos = {
        't1': titles[0],
        't2':titles[1],
        't3':titles[2],
        'l1':links[0],
        'l2':links[1],
        'l3':links[2]
    }

    return jsonify(infos)



@app.route('/upload', methods=['POST'])
def upload():
    imagefile = request.files.get('file')
        #imagefile = request.files.get('imagefile', '')
    content = request.form.get("myFile")
    img = Image.open(imagefile)
    print("YESYESYEYSEYEYSY")
    text = tess.image_to_string(img, config='--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"')
    print(text)
    return jsonify({"status": "success", "text": text})



if __name__ == '__main__':
    app.run(debug=True)