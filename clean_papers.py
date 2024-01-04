## Now we want to put our list of papers and their content into a format that can be embedded 
import fetch_papers
import pandas as pd
import os 
from openai import OpenAI

#os.environ["OPENAI_API_KEY"] = "ENTER HERE"

## Function that embedds our text from the papers and creates a column of vectors to use later
### This follows the documentation given by OpenAI
def get_embedding(text, model = "text-embedding-ada-002"):
    client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))
    text = text.replace("\n", " ")
    text = text.replace("Title:", "")
    text = text.replace("Summary:","")
    return client.embeddings.create(input= [text], model = model).data[0].embedding

## We can run our function for collecting the papers and then save it as a data frame with a single 'combined' column
### This follows the documentation from OpenAI Cookbook

## We then can run the embedding function to create the database of embedded vectors to use in the chat bot
def clean_papers():
    df = pd.DataFrame({"combined":fetch_papers.fetch_papers()})
    df['ada_embedding'] = df.combined.apply(lambda x: get_embedding(x, model="text-embedding-ada-002"))
    return df 