import pandas as pd

df = pd.read_json('mal.json')
df.to_csv(r'mal_data.csv', index=None)