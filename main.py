from clean_papers import clean_papers, get_embedding
import os 
import openai
import tiktoken
from openai import OpenAI
from scipy import spatial

#os.environ["OPENAI_API_KEY"] = "ENTER HERE"

## This is our main program file that will run the chat bot

## We start by defining the client for the OpenAI using our API key, mine is saved in the environment so you should do the same to run this
client = OpenAI(
api_key = os.environ.get("OPENAI_API_KEY")) 

## Load our database of academic papers
research_df = clean_papers()

## This is a ranked search function to determine the best article that corresponds to the question inputed by the user
## I used a spatial distance calculation to determine which article is the most similar to the question and will be used by the bot to respond
## What this does is take the 3 most relevant articles and appends them to an intro prompt. The model will then read in the intro prompt and try to answer the question

### Again followed the documentation in the OpenAI cookbook
def ranked_research(question, df, n=2):

    intro = "Use the below articles to answer the subsequent quesiton. Do not copy and paste the whole text."
    question_f = f"\n\n Question: {question}"
    question_embedded = get_embedding(question, model = "text-embedding-ada-002")
    df['similarity'] = df.ada_embedding.apply(lambda x: 1- spatial.distance.cosine(x, question_embedded))
    res = df.sort_values('similarity', ascending = False)

    for i in range(0,n):
        art = res['combined'][i]
        intro += art
    return intro + question_f

## This is the actual function for running the chat bot. It takes the question as an input and then returns the three most related articles with the specified prompt to answer.
def chatbot():

    ## For GPT 3.5 according to the cookbook, there is no need to be specific for the "content" as it only pays attention in latter iterations
    messages = [
        {"role": "system", "content": "Assistant with summarizing current literature on Llama-2"},
    ]
    
    while True:

        message = input("User: ")

        if message.lower() == "quit":
            break

        message = ranked_research(message, df=research_df, n=2)
        messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = messages,
            temperature=0
        )

        chat_message = response.choices[0].message.content
        print(f"Bot: {chat_message}")

## Runs the function for the chat bot
if __name__ == "__main__":
    print("Start chatting with the bot (type 'quit' to end)")
    chatbot()