import numpy as np
import pandas as pd
import re
from metadataFromID import GoodReadsScraper


def munging(df):
    # Capturing genre words from the column with amessy string.
    # Extract words indicating the genre using a regex pattern.
    genr = [re.findall(r'>(\w+)<', str(txt)) for txt in df['genre']]

    # We iterate through the list and seperate words with comma.
    for g, i in zip(genr, range(0, len(genr))):
        df['genre'][i] = ', '.join(g)

    # Grab the number of pages as a integer
    df['pages'] = df['pages'].str.split(expand=True)[0].astype(int)

    # Extract integer value from the reviews count column
    df['count'] = df['count'].str.strip().str.split('\\n', expand=True)[0]

    # Remove extra letters and white spaces
    df['rating'] = df['rating'].str.strip().str.split('\n', expand=True)

    # Remove new line letters and commas.
    # After that converts column into int type.
    df['count'] = df['count'].str.strip().str.split('\\n', expand=True)[0]
    df['count'] = df['count'].str.replace(',', '').astype(int)

    # Remove new line letters from the title column.
    df['title'] = df['title'].str.strip().str.split('\\n', expand=True)[0]

    # Remove new line letters from ratings column and convert to int.
    df['rating'] = df['rating'].str.strip().str.split('\n', expand=True).astype(float)

    # Extract only the year from the published date column.
    df['released'] = df['released'].str.extract('([0-9]{4})')

    return df