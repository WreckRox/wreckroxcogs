import discord
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils import checks

class Moderation_Help:
	"""Shows SuperBot's Moderation and Owner Help!"""
	
	def __init__(self, bot):
		self.bot = bot
	@checks.admin_or_permissions(kick_members=True)	
	@commands.command()
	async def modhelp(self):
		"""Shows SuperBot's Moderation and Owner Help!"""
		server = "https://discord.gg/A3PEwgw"
		
		boi = (
			"These are the commands which can only be used by the \n"
			"server moderators and server owner!")
		help = (
			"!kick\n"
			"!ban\n"
			"!reason\n"
			"!softban\n"
			"!mute\n"
			"!unmute\n"
			"!filter\n"
			"!punish\n"
			"!lspunish\n"
			"!unpunish\n")
		help2 = (
			"Kicks an user from server\n"
			"Bans an user from server\n"
			"Adds a reason to mod-log (If any)\n"
			"Kicks user deleting 1 day worth of messages.\n"
			"Mutes any user.\n"
			"Unmutes a muted user.\n"
			"Filters anything (Has to be stated)\n"
			"Punishes an user\n"
			"List of punished users\n"
			"Ends punishment of an user.")
		owner = (
			"!audioset\n"
			"!modset\n"
			"!economyset\n"
			"!welcomeset")
		owner2 = (
			"Set the server-side settings for audio.\n"
			"Set the server-side moderation settings of bot.\n"
			"Change the server-side economy settings of bot.\n"
			"Change the server welcoming settings.")
		ot = (
			"Join the [SuperBot Community]({}) for more news and support!"
			"".format(server))
			
		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Bot Commands", value=str(boi), inline=False)
		embed.add_field(name="Moderation", value=help)
		embed.add_field(name="Description", value=help2, inline=True)
		embed.add_field(name="Owner", value=owner)
		embed.add_field(name="Description", value=owner2)
		embed.add_field(name="Others", value=ot, inline=False)
		
		try:
			await self.bot.say(":page_facing_up: **Check your private messages!**")
			await self.bot.whisper(embed=embed)
	    
		except:
			await self.bot.say("ERROR!! Can't send DM to you ;-; Pls allow strangers to send DM :V")
		
def setup(bot):
	bot.add_cog(Moderation_Help(bot))