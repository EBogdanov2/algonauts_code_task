## Now we want to put our list of papers and their content into a format that can be embedded 

import fetch_papers
import pandas as pd
import openai

def clean_papers():
    df = pd.DataFrame({"combined":fetch_papers.fetch_papers()})
    return df
