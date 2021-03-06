# ChatBot
A simple Artificial Intelligent Chatbot

## Prerequisites
1. Python 3.7
2. HTML
3. CSS
4. Chatterbot, Spacy, Flask, chatterbot-corpus (Python Libraries)

### Libraries installed
pip install chatterbot  
pip install chatterbot-corpus  
python -m spacy download en_core_web_sm  
python -m spacy link en_core_web_lg en  

## Problem Statement
Deploy a chatbot as a web application using Flask method, HTML and CSS. The chatterbot package in python is used to build a chatbot.

## Deploy Chatbot

A Chatterbot library is used for building the chatbot.Chatterbot is a Python library to generates responses for users. It uses a lot of pre-trained machine learning algorithms to give a variety of responses. The chatbot should be designed to be language-independent. He must be trained in several languages. The chatbot is made up of data provided by the user.

Another important python library used is spacy, an NLP toolkit in Python very popular in English nature language processing. 

The SQLStorageAdapter allows ChatterBot to store conversation data in any database supported by the SQL Alchemy ORM

## app.py
This contains the code to deploy the chatbot using flask.

## index.html and style.css
Create an html file inside a new folder, templates/index.html. The HTML and CSS work as the base of this chatbot

## Run the app.py
Run the flask app “app.py” by running the following statement below in terminal.

python app.py

![alt text](https://github.com/sabdha/ChatBot/blob/main/Screenshot%202021-02-16%20232926.png)

## Future work

We can create personal questions and answers inside a folder and can be used along with the chatterbot corpus.
Also there are many powerful bot development frameworks, tools, and platforms that can be used to implement smart chatbot programs.
We can use machine learning with Python to develop a chatbot

### References

Part of this code is taken from

https://damanpreets26.medium.com/creating-a-simple-chatbot-with-flask-202083c1b3d6  
https://thecleverprogrammer.com/2020/08/21/deploy-a-chatbot-with-python/  

