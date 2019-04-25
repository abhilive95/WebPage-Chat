# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:45:21 2019

@author: AC38815
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import sys


chatbot = ChatBot(
    "GUI Bot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
            {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'SORRY - Am not yet trained to answer this question',
                    'maximum_similarity_threshold': 0.90

            },
            {
                    'import_path': 'chatterbot.logic.MathematicalEvaluation'
            }
            ],
    database_uri="sqlite:///database.db"
)

def get_response(message):
	#print ('Abhi :',message)
    reply = chatbot.get_response(message)
    if (reply.confidence < 0.98):
        reply = 'Sorry, Am not yet trained to answer this question'      
    else:
        return reply
            
    return reply


#print("hhhhhhhhhhhhh")
#print(sys.argv[1])	
print(get_response(sys.argv[1]))