#!/usr/bin/python
import markovify

with open("/home/greg/trump.corpus") as f:
    text = f.read()

text_model = markovify.Text(text, state_size=3)

for i in range(1):
    print(text_model.make_sentence(tries=1000))
