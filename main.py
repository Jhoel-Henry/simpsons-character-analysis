import requests
import pandas as pd
import matplotlib.pyplot as plt

URL = "https://thesimpsonsapi.com/api/characters"
response = requests.get(URL)

data = response.json()

characters = []

for item in data["results"]:
    characters.append(item["name"])

df = pd.DataFrame(characters, columns=["character"])


df["name_length"] = df["character"].apply(len)
df_sorted = df.sort_values(by="name_length", ascending=False)
plt.figure(figsize=(10, 20))  
plt.barh(df_sorted["character"], df_sorted["name_length"])
plt.xlabel("Cantidad de carácteres")
plt.title("Longitud del nombres - The Simpsons")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

