![GitHub User's stars](https://img.shields.io/github/stars/RajKKapadia?style=for-the-badge)
![GitHub followers](https://img.shields.io/github/followers/RajKKapadia?style=for-the-badge)

# Telegram bot tutprial
Hey everyone, I have developed this repositry so that you can learn how to create your Telegram bot and connect it to Openai GPT-3 and Dall-E 2. This bot will reply to text messages and generate image from text.

### Youtube
I have recorded a quick video on the setup of this chat-bot, in case you want to replicate the work, you can watch it [here](https://youtu.be/zxoco9TfNpw).

### What you will need
There are couple of things that you need before you get started following this repository.
* OpenAI API key, since it is open to all, you can create an account [here](https://openai.com/) and access the key.
* You need a telegram bot API key as well, you can get it with interacting with Botfather on Telegeram [here](). Alternatively, you can one of my video on how to create a Telegram bor [here](https://youtu.be/oBQMPmCVY8c).
* API requesting application like Postman, Insomnia, etc.
* NGROK for local testing.
* Account with GitHub and Render for deployment

### How to use it
To replicate the work of this repository and run it locally, you need to follow these steps:
* create a `.env` file inside the root directory, create these environmental variables:
    ```
    TELEGRAM_API_KEY=YOURAPIKEY
    OPENAI_API_KEY=YOURAPIKEY
    ```
* create a virtual environment and activate it before installing the packages
* install all the required dependencies from the `requirements.txt` file
    ```python
    pip install -r requirements.txt
    ```
* run the server with either of the following commands
    ```python
    python run.py
    ```
    ```python
    gunicorn run:app
    ```

### Telegram API help
You can get help on the Telegram API on their official page [here](https://core.telegram.org/bots/api), however, the APIs to follow this repository are as under:

* Set webhook
    - POST request
    - JSON BODY
    ```json
    {
	    "url": "YOURURL/telegram"
    }
    ```
    - url `https://api.telegram.org/botYOURAPIKEY/setWebhook`

* Send message
    - POST request
    - JSON BODY
    ```json
    {
	    "chat_id": 582346178,
	    "text": "From insomania"
    }
    ```
    - url `https://api.telegram.org/botYOURAPIKEY/sendMessage`

* Send photo
    - POST request
    - JSON BODY
    ```json
    {
	    "chat_id": 582346178,
	    "photo": "YOUR IMAGE URL",
	    "caption": "Test from Insomnia"
    }
    ```
    - url `https://api.telegram.org/botYOURAPIKEY/sendPhoto`

# About me
I am `Raj Kapadia`, I am passionate about `AI/ML/DL` and their use in different domains, I also love to build `chatbots` using `Google Dialogflow ES/CX`, I have backend development experience with Python[Flask], and NodeJS[Express] For any work, you can reach out to me at...

* [LinkedIn](https://www.linkedin.com/in/rajkkapadia/)
* [Fiverr](https://www.fiverr.com/rajkkapadia​)
* [Upwork](https://www.upwork.com/freelancers/~0176aeacfcff7f1fc2)
* [Youtube](https://www.youtube.com/channel/UCOT01XvBSj12xQsANtTeAcQ)
