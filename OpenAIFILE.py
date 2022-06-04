import os
import openai

openai.api_key = "Your OpenAI API Key" # OpenAI API Key

start_sequence = "\nAI:"
restart_sequence = "\n\nUser:"
ai_session_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nUser: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nUser: I'd like to cancel my subscription.\nAI:"

marv_start_sequence = "\nMarv:"
marv_prompt="Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nMarv: I’m not sure. I’ll ask my friend Google.\nYou: What time is it?\nMarv:"
ai_sarcastic_mode =  False

def create_sql_request(request):
  prompt_text = f'{restart_sequence}: Create a SQL request to {request}: {start_sequence}:'
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

def sarcastic_response(question):
  prompt_text = f'{marv_prompt}{restart_sequence}: {question}{marv_start_sequence}:'
  response = openai.Completion.create(
    engine="text-davinci-002", # DAVINCI : text-davinci-002, CURIE : text-curie-001, ADA : text-ada-001, BABBAGE : text-babbage-001
    prompt=prompt_text,
    temperature=0.5,
    max_tokens=60, # Set the max_tokens sent back from OpenAI (1000 tokens = 750 words) /!\ Over the free trial, it cost money visit : https://openai.com/api/pricing/ for more infos /!\
    top_p=0.3,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["\n"]
  )
  result = response['choices'][0]['text']
  return str(result)

def askQuestion(question):
  prompt_text = f'{ai_session_prompt}{restart_sequence}: {question}{start_sequence}:'
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
    if chat_log is None and ai_sarcastic_mode == False:
        chat_log = ai_session_prompt
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
    if chat_log is None and ai_sarcastic_mode == True:
        chat_log = marv_prompt
        return f'{chat_log}{restart_sequence} {question}{marv_start_sequence}{answer}'
    

