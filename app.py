# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 11:15:12 2021

@author: dhany
"""
#Chatterbot is a Python library that generates responses for users.
#It uses a lot of pre-trained machine learning algorithms to give a variety of responses. 
#It’s easy to create chatbots using the chatterbot library in Python.
#The chatbot should be designed to be language-independent. He must be trained in several languages.
#The chatbot is made up of data provided by the user.
#https://damanpreets26.medium.com/creating-a-simple-chatbot-with-flask-202083c1b3d6
#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#spacy a NLP toolkit in Python very popular in English nature language processing.
#https://clay-atlas.com/us/blog/2020/05/12/python-en-package-spacy-error/
import spacy


spacy.load("en_core_web_sm")
app = Flask(__name__)
#create chatbot
#The SQLStorageAdapter allows ChatterBot to store conversation data in any database
# supported by the SQL Alchemy ORM
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english") #train the chatter bot for english

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))

if __name__ == "__main__":
    app.run()
