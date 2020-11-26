import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as {0}'.format(self.user))

    async def on_message(self, message):
        # print('Message from {0.author}: {0.content}'.format(message))
        ids = [
            451428172811206699, #Lilian
            332178573391691777 #misa
        ]
        if message.author.id in ids:
            await message.delete()
        # await message.channel.send(message.content)

client = MyClient()
client.run('NjE5NTMzMzQyNjY4NDg4NzU3.XXJnYw.xwkUrZjsdW9oQqe0nvwoCZyyaEA')