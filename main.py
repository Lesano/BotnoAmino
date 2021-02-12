import amino
import json
import time

with open('./config.json') as cjson:
    config = json.load(cjson)
    print("Ficheiro: config.json carregado com sucesso.")

client = amino.Client()

ea = config["email"]
pa = config["passwd"]
comid = config["comuid"]
prefix = config["prefix"]

client.login(ea, pa)

subclient = amino.SubClient(aminoId=comid, profile=client.profile)

@client.callbacks.event("on_text_message")
def on_text_message(data):
    if data.message.content.lower().startswith(f'{prefix}ping'):
        subclient.send_message(message="Pong!", chatId=data.message.chatId)

    if data.message.content.lower().startswith(f'{prefix}perfil'):
        u1 = subclient.get_user_info(data.message.author.userId)
        u2 = u1.nickname
        u3 = u1.createdTime
        u4 = u1.followersCount
        u5 = u1.followingCount
        subclient.send_message(message=f'\nNome:{u2} \nData de entrada na comunidade:{u3} \nSeguidores: {u4} \nSeguindo: {u5}', chatId=data.message.chatId)

@client.callbacks.event("on_group_member_join")
def on_group_member_join(data):
    u1 = subclient.get_user_info(data.message.author.userId).nickname
    subclient.send_message(message=f'Olá {u1}! Desejo-lhe as boas-vindas ao chat, não se esqueça de ler as regras.', chatId=data.message.chatId)
    subclient.start_chat(userId=data.message.author.userId, message="Desejo-lhe as boas-vindas ao chat, não se esqueça de ler as regras.")

@client.callbacks.event("on_group_member_leave")
def on_group_member_leave(data):
    subclient.send_message(message='Espero que tenha gostado, espero te ver em breve...', chatId=data.message.chatId)