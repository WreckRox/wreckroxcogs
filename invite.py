import discord
from discord.ext import commands

class ChillCord:
	"""Gives the ChillCord invite URL"""
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def chillcord(self):
		"""Gives you the Chillcord invite URL"""
		
		inv = "https://discord.gg/j2ewrv7"

		one = ("ChillCord is a place where you can discuss about almost anything. You can also take part in some giveaways!\n"
			"ChillCord Invite Link: **[CLICK HERE]({})**"
			"".format(inv))
			
		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="ChillCord", value=one, inline=False)
		
		try:
			 await self.bot.say(embed=embed)
	    
		except:
			await self.bot.say("I need the `Embed Links` Permission in order to do that!")
		
def setup(bot):
	bot.add_cog(ChillCord(bot))