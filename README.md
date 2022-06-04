# OpenAI_Discord_Bot

![Alt text](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Alt text](https://img.shields.io/badge/Discord-5865F2.svg?style=for-the-badge&logo=Discord&logoColor=white)
![Alt text](https://img.shields.io/badge/ChatBot-FFD000.svg?style=for-the-badge&logo=ChatBot&logoColor=black)
-------------------------------------------------------------------------------------------------------------------------------

This is just a simple discord bot powered by OpenAI (https://openai.com/), for the moment it can chat a bit and answer some questions.
I'm planning to improve it in the future, following the improvements of OpenAI.

Commands : 

!hello : Just say hello lol

!sqlHelp : See how to use the !sqlRequest {request}  command
!sqlRequest {your request} : Translate natural langage to an SQL Request (use !sqlHelp for more infos)

!sarcastic_enabled = Enable sarcastic mode*
!sarcastic_disabled = Disable sarcastic mode*

!log (admin only) : See the logs (log_user.txt)

!count_request (admin only) : Count the number of request

!shutdown (admin only) : Stop the bot


sarcastic mode* : OpenAI is giving sarcastic type of response 
Example (Normal mode) : 
- You : "What  does HTML stand for ?"
- AI : "Hypertext Markup Langage"

Example (Sarcastic mode) :
- You : "What does HTML stand for ?"
- AI :  "Hypertext Markup Langage. The T is for try to ask better questions in the future."


/!\ Remember, to use this bot, you need an access to OpenAI API (More infos here : https://openai.com/api/) /!\
/!\ Moreover, be careful when sending messages to this bot, the API can cost money and every message sent is a request to the API /!\
