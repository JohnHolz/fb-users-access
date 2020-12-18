import pandas as pd
import json

def transform_responses(objects = [page_permissions, pages, app_permissions, apps, ad_accounts]):
    objects = list(map(lambda x: json.loads(x.content),objects))
    objects = list(map(lambda x: pd.json_normalize(x['data']),objects))
    return objects

def get_tasks(df,column):
    df = df.explode(column)
    return list(set(df[column].tolist()))

def explode_to_columns(df,column):
    categories = get_tasks(df,column)
    df[categories] = df[column].apply(pd.Series)
    df[categories] = df.iloc[:,-len(categories):].applymap(lambda x: x in categories)    
    return df