from apify_client import ApifyClient
from itertools import combinations
import os

tik_tok_hashtgs: list = [  #listas de hashtags gerais do tiktok, bom para uma busca diversificada
    "fyp",
    "tiktok",
    "foryoupage",
    "viralvideos",
    "funnyvideos",
    "duet",
    "trending",
    "love",
    "memes",
    "followme",
    "repost",
    "new",
    "music",
    "cute",
    "savagechallenge",
    "levelup",
    "featureme",
    "tiktokfamous",
    "viralpost",
    "slomo",
    "video",
    "foryou",
    "likeforfollow",
    "couplegoals",
    "justforfun",
    "recipe",
    "beautyblogger",
    "DIY",
    "canttouchthis",
    "dancer",
    "dancechallenge",
    "5mincraft",
    "quotes",
    "behindthescenes",
    "goal",
    "weirdpets",
    "ootd",
    "reallifeathome"
]
API_TOKEN = "*********" #API token do apify

client = ApifyClient(API_TOKEN)
import random

for i in range(2):  #quantas chamadas as APIs do apify serão feitas, nesse caso serão 2
    random.shuffle(tik_tok_hashtgs) 
    lista_combi_hash = list(next(combinations(tik_tok_hashtgs, 3))) #cria combinações aleatórias de 3 hashtags do tik tok para procurar
    print(lista_combi_hash) #printa a combinação atual de hashtags que serão utilizados

# Prepare the Actor input
    run_input = {
        "hashtags": tik_tok_hashtgs,
        "resultsPerPage": 5,
        "maxProfilesPerQuery": 5,
        "shouldDownloadVideos": False, #como o web scrapper vai se comportar
        "shouldDownloadCovers": False,
        "shouldDownloadSlideshowImages": False,
        "videoKvStoreIdOrName": "mytiktokvideos",
        "disableEnrichAuthorStats": False,
        "disableCheerioBoost": False,
    }


    run = client.actor("GdWCkxBtKWOsKjdch").call(run_input=run_input) #roda o cliente de web scrapping
 
    csv_content = client.dataset(run["defaultDatasetId"]).download_items(item_format="csv")   
    csv_content_str = csv_content.decode('utf-8') 
    with open("web_scrapper.csv", "a") as f: #salva o output do cliente em um CSV
        f.write(csv_content_str)


import pandas as pd 
import os
import re


def remove_emoji(text:str)-> str:
    text = text.replace("#","") 
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  #remove emotes e outros símbolos que não são tão relevantes para processamento de linguagem
        "\U0001F300-\U0001F5FF" 
        "\U0001F680-\U0001F6FF"  
        "\U0001F700-\U0001F77F"  
        "\U0001F780-\U0001F7FF"  
        "\U0001F800-\U0001F8FF"  
        "\U0001F900-\U0001F9FF"  
        "\U0001FA00-\U0001FA6F"  
        "\U0001FA70-\U0001FAFF"  
        "\U00002702-\U000027B0"  
        "\U000024C2-\U0001F251" 
        "]+"
    )
    return emoji_pattern.sub(r'', text)


boas_colunas: list = ['text', 'diggCount' #colunas de dados utéis e relevantes para a aplicação
    , "musicMeta/musicOriginal","musicMeta/musicName","musicMeta/musicAuthor", "authorMeta/region", "locationCreated"] +  [ f"hashtags/{x}/title" for x in range(6)] +  [ f"hashtags/{x}/name" for x in range(6)]

df = pd.read_csv(os.path.join("web_scrapper.csv"), on_bad_lines='skip') #le o output do web scrapper

print(df.shape)
df2 = df[boas_colunas].copy() #df2 recebe apenas certas colunas do df
df2 = df2.fillna(value="") #troca os valores na por string vazia
df2.rename(columns={'diggCount': 'like_count'}, inplace=True) #trocar diggCOunt por like_count para melhor interpretabilidade
df2 = df2[df2['musicMeta/musicOriginal'] == False] #apenas posts com musica não original são processados 
    
df2 = df2.drop(columns=["musicMeta/musicOriginal","authorMeta/region","locationCreated"], axis=1) #não precisamos mais desses dados 
df2['text'] = df2['text'].apply(remove_emoji)  #remove emotes e figuras
df2 = df2[~df2['text'].duplicated(keep='first')] #remove os duplicados
    
print(df2.shape)
       
if not os.path.exists("ados_tratados_webscr.csv"):
    df2.to_csv("dados_tratados_webscr.csv", mode="a", index=False, header=True) #cria um CSV com header na primeira vez se o arquivo n existir
else:
     df2.to_csv("dados_tratados_webscr.csv", mode="a", index=False, header=False) #cria um CSV sem header

