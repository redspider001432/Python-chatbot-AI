from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
from flask import Flask,render_template, request
import json


with open('data.json','r') as file:
    brain = json.load(file)

app = Flask(__name__)




spider = ChatBot('spider',read_only=False,logic_adapters=[
    {
    "import_path":"chatterbot.logic.BestMatch",
    "default_response":"I don't know it Yet I am still in developmenet!!",
    "maximum_threshold":1 
    }
])
Trainer = ListTrainer(spider)
Talk = ChatterBotCorpusTrainer(spider)
for pair in brain['pairs']:
    response = pair['answers']
    Trainer.train([pair['questions']]+ response)
Talk.train('chatterbot.corpus.english')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def spider_response():
    txt = request.args.get('userMessage')
    if txt == '':
        txt = 'Please Say Something'
        return txt
    return str(spider.get_response(txt))


# while True:
#     stranger = input('Stranger: ')
#     print(spider.get_response(stranger))


if __name__ == '__main__':
    app.run(debug=False)