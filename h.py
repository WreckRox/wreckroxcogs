import discord
from discord.ext import commands

class Help:
	"""Shows the commands of SuperBot"""
	
	def __init__(self, bot):
		self.bot = bot
		
	@commands.group(pass_context=True)
	async def h(self, ctx):
		"""Shows the commands of SuperBot"""
		server = "https://discord.gg/A3PEwgw"

		boi = (
			"This is the list of commands which most of the users use on regular\n"
			"basis Do `!help <command>` for more information on the command.")
		
		help = (
			"!h\n"
			"!help")
		help2 = (
			"Shows this message\n"
			"Shows more commands with more stuff lol  ")
			#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
		audio = (
			"!play\n"
			"!pause\n"
			"!skip\n"
			"!prev\n"
			"!stop\n"
			"!song\n"
			"!queue\n"
			"!yt")
		audio2 = (
			"Plays a song / link\n"
			"Pauses the playing song\n"
			"Votes to skip song.\n"
			"Goes back to previous song\n"
			"Stops song\n"
			"Shows information about current song\n"
			"Shows song queue\n"
			"Searches from YouTube and adds to queue.")
			#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
		fun = (
			"!away\n"
			"!c\n"
			"!kill\n"
			"!insult\n"
			"!flip\n"
			"!8\n"
			"!rps\n"
			"!throw\n"
			"!lmgtfy\n"
			"!calc\n"
			"!choose\n")
		fun2 = (
			"Tells the bot that you are away\n"
			"Talk with Cleverbot. Mention also works.\n"
			"Kill anyone\n"
			"Insult anyone\n"
			"Flip coin (or user)\n"
			"Ask 8 ball a question\n"
			"Play Rock Paper Scissors\n"
			"Throw stuff at user\n"
			"Generates LMGTFY Link\n"
			"Calculate stuff\n"
			"Choose between several items\n")
			#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
		leveler = (
			"!profile\n"
			"!rank\n"
			"!lvlset\n"
			"!profileinfo\n")
		leveler2 = (
			"Shows user profile.\n"
			"Shows user rank.\n"
			"Change your leveler settins (Global One)\n"
			"Shows more detailed info about any user.")
			#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

		econ = (
			"!bank register\n"
			"!payday\n"
			"!bank balance\n"
			"!bank transfer\n"
			"!slot")
		econ2 = (
			"Creates account at SuperBot Bank\n"
			"Gives you some $$$\n"
			"Shows your bank balance lmao\n"
			"Transfers your $$$ to another user\n"
			"Play slot with your money(Gambling). . .")
			#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
		bot = (
			"!info\n"
			"!stats\n"
			"!userinfo\n"
			"!uptime\n"
			"!updates\n"
			"!modhelp\n")
		bot2 = (
			"Shows bot information.\n"
			"Shows bot's statistics.\n"
			"Shows information related to user\n"
			"Shows for how long the bot was online for\n"
			"Shows the latest updates of SuperBot\n"
			"Shows the mod and owner commands.\n"
			"(^ONLY WORKS FOR USERS WITH \n"
			"`KICK MEMBERS` PERMISSION)")
			#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
		ot = (
			"Join the [SuperBot Community]({}) for more news and support!"
			"".format(server))

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Bot Commands", value=str(boi), inline=False)
		embed.add_field(name="Help", value=help)
		embed.add_field(name="Description", value=help2, inline=True)
		embed.add_field(name="Audio", value=audio)
		embed.add_field(name="Description", value=audio2)
		embed.add_field(name="Fun and Utils", value=fun, inline=True)
		embed.add_field(name="Description", value=fun2)
		embed.add_field(name="Economy", value=econ, inline=True)
		embed.add_field(name="Description", value=econ2, inline=True)
		embed.add_field(name="Leveler", value=leveler, inline=True)
		embed.add_field(name="Description", value=leveler2, inline=True)
		embed.add_field(name="Bot", value=bot, inline=True)
		embed.add_field(name="Description", value=bot2, inline=True)
		embed.add_field(name="Others", value=ot, inline=False)

		if ctx.invoked_subcommand is None:
			try:	
				await self.bot.say(":page_facing_up: **Check your private messages!**")
				await self.bot.whisper(embed=embed)
		
			except:
				await self.bot.say("A WILD EXCEPT APPEARED!")

	@h.command()
	async def play(self):
		"""Audio"""

		boi = (
			"!play <url_or_search_terms>\n\n"
			"Plays a link / searches and play")

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Audio", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")

	@h.command()
	async def pause(self):
		"""Audio"""

		boi = (
			"!pause\n\n"

			"Pauses the current song, `!resume` to continue."
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Audio", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")

	@h.command()
	async def skip(self):
		"""Audio"""

		boi = (
			"![skip|next]\n\n"

			"Skips a song, using the set threshold if the requester isn't a mod or admin. Mods, admins and bot owner are not counted in the vote threshold."
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Audio", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")

	@h.command()
	async def prev(self):
		"""Audio"""

		boi = (
			"!prev\n\n"

			"Goes back to the last song"
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Audio", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")

	@h.command()
	async def stop(self):
		"""Audio"""

		boi = (
			"!stop\n\n"

			"Stops a currently playing song or playlist. CLEARS QUEUE."
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Audio", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")
	
	@h.command()
	async def song(self):
		"""Audio"""

		boi = (
			"!song\n\n"

			"Provides information about the current song"
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Audio", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")

	@h.command()
	async def queue(self):
		"""Audio"""

		boi = (
			"!queue\n\n"

			"Gives you the list of the songs in current queue"
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Audio", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")

	@h.command()
	async def yt(self):
		"""Audio"""

		boi = (
			"!yt <search>\n\n"

			"Searches for a video in YouTube and adds it to queue"
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="YT", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")

	@h.command()
	async def away(self):
		"""Fun and Utils"""

		boi = (
			"!away\n\n"

			"Tells the bot that you are away\n"
			"Usage: `!away <MESSAGE>`"
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Fun and Utils", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")

	@h.command()
	async def c(self):
		"""Fun and Utils"""

		boi = (
			"!c\n\n"

			"Talk with cleverbot!\n"
			"Usage: `!c <MESSAGE>` or <@257136385956249600> <MESSAGE>"
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Fun and Utils", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")

	@h.command()
	async def kill(self):
		"""Fun and Utils"""

		boi = (
			"!kill\n\n"

			"Kill someone!\n"
			"Usage: `!kill @USER`"
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Fun and Utils", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")

	@h.command()
	async def insult(self):
		"""Fun and Utils"""

		boi = (
			"!insult\n\n"

			"Insult someone!\n"
			"Usage: `!insult @USER`"
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Fun and Utils", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")

	@h.command()
	async def flip(self):
		"""Fun and Utils"""

		boi = (
			"!flip\n\n"

			"Flip a coin or a user!\n"
			"Usage: `!flip` or `!flip @USER`"
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.add_field(name="Fun and Utils", value=str(boi), inline=False)

		try:	
			await self.bot.say(embed=embed)
		
		except:
			await self.bot.say("A WILD EXCEPT APPEARED!")
	
def setup(bot):
	bot.add_cog(Help(bot))