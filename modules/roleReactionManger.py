import discord
from discord.ext import commands

class RoleReactionManager():
    def __init__(self, bot):
        self.bot = bot

    roleEmojis = ['⌨️','🎥','📷','✏️','🖥️']

    @bot.command()
    async def reactHere(ctx, args):
        message = await ctx.send(args)
        message_id = message.id

    @commands.Cog.listener()
    async def on_raw_reaction_add(payload):
        
        if payload.message_id == message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            
            if emoji == roleEmojis[0]:
                role = discord.utils.get(guild.roles, name="Developer")
            elif emoji == roleEmojis[1]:
                role = discord.utils.get(guild.roles, name="Photographer")
            elif emoji == roleEmojis[2]:
                role = discord.utils.get(guild.roles, name="Videographer")
            elif emoji == roleEmojis[3]:
                role = discord.utils.get(guild.roles, name="Writer")
            elif emoji == roleEmojis[4]:
                role = discord.utils.get(guild.roles, name="Designer")
            else:
                print(f"{emoji} is not configured to work with this message")
                
            print(f"Assigning {role} to {member}")
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(payload):

        if payload.message_id == message_id:
            member = payload.member.guild
            emoji = payload.emopji.name
            if emoji == roleEmojis[0]:
                role = discord.utils.get(guild.roles, name="Pacific")
            elif emoji == roleEmojis[1]:
                role = discord.utils.get(guild.roles, name="Mountain")
            elif emoji == roleEmojis[2]:
                role = discord.utils.get(guild.roles, name="Central")
            elif emoji == roleEmojis[3]:
                role = discord.utils.get(guild.roles, name="Eastern")
            elif emoji == roleEmojis[4]:
                role = discord.utils.get(guild.roles, name="Atlantic")
            else:
                print(f"{emoji} is not configured to work with this message")

            print(f"removing {role} to {member}")
            await member.add_roles(role)


    def setup(bot):
        bot.add_cog(RoleReactionManager(bot))

