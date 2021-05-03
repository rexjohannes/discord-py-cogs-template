import discord
from discord.ext import commands

class System(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print("System is Ready!")

  @commands.command()
  async def ping(self, ctx):
    await ctx.send("Pong!")

  @commands.command()
  async def invite(self, ctx):
    embed=discord.Embed(title="Invite", description=f"[Click Here!]({discord.utils.oauth_url(self.bot.user.id)})")
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(System(bot))
