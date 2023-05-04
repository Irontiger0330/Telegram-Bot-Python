import os

import openai
from dotenv import load_dotenv
load_dotenv()

# Use your API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_image(prompt: str) -> dict:
    '''
    Call Openai API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict
    '''
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size='1024x1024'
        )
        return {
            'status': 1,
            'url': response['data'][0]['url']
        }
    except:
        return {
            'status': 0,
            'url': ''
        }

def text_complition(prompt: str) -> dict:
    '''
    Call Openai API for text completion
    Parameters:
        - prompt: user query (str)
    Returns:
        - dict
    '''
    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=f'Human: {prompt}\nAI: ',
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }
    