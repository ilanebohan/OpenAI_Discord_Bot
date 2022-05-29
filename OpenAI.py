import os
import openai

openai.api_key = "Your API-Key" # OpenAI API Key

start_sequence = "\nAI:"
restart_sequence = "\n\nUser:"
session_prompt = "OpenAI is a chatbot that reluctantly answers questions.\n\n###\nUser: How many pounds are in a kilogram?\nOpenAI: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\n###\nUser: What does HTML stand for?\nUser: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\n###\nOpenAI: When did the first airplane fly?\nUser: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\n###\nUser: Who was the first man in space?\nOpenAI:"



def askQuestion(question, chat_log=None):
  prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
  response = openai.Completion.create(
    engine="text-davinci-002", # DAVINCI : text-davinci-002, CURIE : text-curie-001, ADA : text-ada-001, BABBAGE : text-babbage-001
    prompt=prompt_text,
    temperature=0.9,
    max_tokens=150, # Set the max_tokens sent back from OpenAI (1000 tokens = 750 words) /!\ Over the free trial, it cost money visit : https://openai.com/api/pricing/ for more infos /!\
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=["\n"]
  )
  result = response['choices'][0]['text']
  return str(result)


def append_interaction_to_chat_log(question, answer, chat_log=None): # Append the question and answer to the chat log
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

