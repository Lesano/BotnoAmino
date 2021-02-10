import amino
client = amino.Client()

ea = "seu email"
pa = "sua senha"

client.login(ea, pa)

subclient = amino.SubClient(aminoId="id da comunidade", profile=client.profile)

@client.callbacks.event("on_text_message")
def on_text_message(data):
    if data.message.content.lower().startswith("!ping"):
        subclient.send_message(message="Pong!", chatId=data.message.chatId)
