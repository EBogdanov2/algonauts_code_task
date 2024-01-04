#Llama-2 Research Bot

The main use for the chat bot is to collect academic research on Llama-2 and then quickly diseminate this information through a chat bot. 

## Requirements

The package requirements are all in the requirements.txt file.

You can use the following command to quickly get started:
    pip install -r requirements.txt

##Launching the bot
First if you are using a terminal or bash ensure you are in the project folder directory.
###Bash: 
    $ export OPENAI_API_KEY = "YOUR KEY"
    $ python main.py
###Alternate:
    Open the main.py file in an IDE 
    Add your API key to environment, or uncomment the line os.environ["OPENAI_API_KEY"] = "ENTER HERE" in both main.py and clean_papers.py
    Run main.py in the usual manner

## Interactions with the bot 

You will see in the terminal a prompt of "User:", here you can enter your question about the Llama LLM. 

Ensure your question is as short as possible as there might be issues with tokens if you paste a huge block of text. 

You should formulate your questions using only the base Llama name, not Llama-2. There was not enough time to compare the differences in the ranking calculations between the two cases.

###Sample questions
    What are some use cases for Llama?
    How much computing power is needed to run Llama?
    What are the current downsides to using Llama?
    What are the advantages to using Llama over GPT?