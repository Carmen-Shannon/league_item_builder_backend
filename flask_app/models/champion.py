import requests
from flask_app.config.mysqlconnection import connectToMySQL as connect


async def get_champion_by_name(user_input):
    champ = requests.get(
        f'https://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion/{user_input}.json')

    champ = champ.json()

    return champ['data'][f'{user_input}']['name']


async def get_all_champions():
    champs = requests.get(
        'https://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion.json')

    champs = champs.json()
    champs = champs['data']

    champ_names_list = []

    for champ in champs:
        champ_names_list.append(champ)

    return champ_names_list
