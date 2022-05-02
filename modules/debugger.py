import discord
from discord.ext import commands

class Debugger():
  
  def setup(bot):
    bot.add_cog(RoleReactionManager(bot))