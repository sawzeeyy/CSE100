#!/usr/bin/python3
# Author: Shuaib Oladigbolu
# F007573P
# Twitter: @_sawzeeyy
# Created on 21/05/2018
import json

filename = 'newQuestions'
multichoice = ['(a)', '(b)', '(c)', '(d)', '(e)']

json_data = open(filename+'.json', encoding='utf-8')
json_data = json.load(json_data)

for count, question in enumerate(json_data):
    print('Question', count + 1 )
    print(question['questiontext']['text'], '\n')
    for index, answer in enumerate(question['answer']):
        if answer['fraction'] == '100':
            print(multichoice[index], answer['text'],'[Answer]')
        else:
            print(multichoice[index],answer['text'])
    print('\n')