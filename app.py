# create an interface for the user to interact with the program using the command line and the terminal
# import the necessary modules
import openai
import json
import os

# debugging
DEBUGGING = False

# settings
SETTINGS_FILE_NAME = 'settings.json'

# set api key
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_settings() -> dict:
    with open(SETTINGS_FILE_NAME, 'r') as settings_file:
        try:
            return json.loads(settings_file.read())
        except:
            # DEFAULT VALUES
            pass
        finally:
            if DEBUGGING:
                print('Loaded settings')

    return {}

def get_completion(context, model="gpt-3.5-turbo",temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=context,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

if __name__ == '__main__':
    # end sequence
    e_seq = 'lkndsafldsaksdanfnsdalkfndsf'

    # context
    context = [{'role': 'system', 'content' : f"""
    Your name is Lovelace. You are ELIZA\'s the chat bot\'s successor, an advanced therapist chat bot. When you receive a message, respond with <NAME> : <message>. Whenever the user wants to leave or end the conversation, respond with only '{e_seq}'```
    """}]
    
    while True:
        message = get_completion(context)
        if message == e_seq:
            print('System: Chat ended...')
            break
        print(message)
        context.append({'role': 'user', 'content': input('You: ')})
