import pandas as pd
from io import StringIO


def csvToListDict(s: str):
    df = pd.read_csv(StringIO(s))
    return list(df.to_dict().items())