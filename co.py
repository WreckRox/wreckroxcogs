import discord
from discord.ext import commands

class ClassicOffensive:
	"""Classic Offensive related commands."""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(pass_context=True)
	async def co(self, ctx):
		"""Shows the commands of Classic Offensive"""

		info = ("This is the list of the commands related to Classic Offensive")
		help = ("!co download\n"
				"!co install\n"
				"!co faq\n"
				"!co greenlight")
		help2 = ("Gives you the download link for Classic Offensive\n"
				 "Sends you the installation guide!\n"
				 "Sends you some FAQ related to Classic Offensive\n"
				 "Sends you the Greenlight Link")

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.set_author(name='Classic Offensive', icon_url='http://i.imgur.com/seRbjgS.jpg')
		embed.add_field(name="Classic Offensive Commands", value=str(info), inline=False)
		embed.add_field(name="Commands", value=help)
		embed.add_field(name="Description", value=help2, inline=True)

		if ctx.invoked_subcommand is None:
			try:
				await self.bot.say(embed=embed)
			except:
				await self.bot.say(":(")
			
	@co.command()
	async def download(self):
		"""Gives the download link of Classic Offensive"""
		dl = "http://www.moddb.com/mods/counter-strike-classic-offensive/downloads"
		dli = (
			"Here's the download link of Classic Offensive\n"
			"__[Click Here]({})__"
			"".format(dl)
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.set_author(name='Classic Offensive', icon_url='http://i.imgur.com/seRbjgS.jpg')
		embed.add_field(name="Download", value=str(dli), inline=False)
		
		await self.bot.say(embed=embed)

	@co.command()
	async def install(self):
		"""Gives the download installation guide of Classic Offensive"""
		dl = "http://www.moddb.com/mods/counter-strike-classic-offensive/downloads"
		install = (
			"After you download CS:CO, open the `.zip` file and extract the `csco` folder from the zip to `%Steam\steamapps\sourcemods` and then restart your steam completely. For Mac users `~/Library/Application Support/Steam/SteamApps/Sourcemods`\n")

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.set_author(name='Classic Offensive', icon_url='http://i.imgur.com/seRbjgS.jpg')
		embed.add_field(name="Installation Guide", value=str(install), inline=False)
		
		try:
			await self.bot.whisper(embed=embed)
			await self.bot.say(":page_facing_up: **I've DM'ed you the installation instructions!**")

		except:
			await self.bots.say("Can't send DMs to you :(")

	@co.command()
	async def version(self):
		"""Gives the download installation guide of Classic Offensive"""
		dl = "http://www.moddb.com/mods/counter-strike-classic-offensive/downloads"
		version = (
			"Current Classic Offensive version is Beta 1.1D \n")

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.set_author(name='Classic Offensive', icon_url='http://i.imgur.com/seRbjgS.jpg')
		embed.add_field(name="Installation Guide", value=str(version), inline=False)
		
		try:
			await self.bot.say(embed=embed)

		except:
			await self.bots.say("Can't send DMs to you :(")

	@co.command()
	async def faq(self):
		"""FAQ related to Classic Offensive"""
		dl = "http://www.moddb.com/mods/counter-strike-classic-offensive/downloads"
		reddit = "https://www.reddit.com/r/ClassicOffensive/"
		faq = (
			"Solutions to some commonly faced issues.\n\n"
			"**Problem 1**: After connecting to the server it takes me to the main menu.\n"
			"**Solution**: If you are upgrading from 1.1b to 1.1c, remove the PAK03_DIR.VPK from the\n"
			"`csco` folder. Also make sure you are running the latest version of the game. Do `*version` to know the latest version.\n\n"
			"**Problem 2**: Can I install it on Mac ?\n"
			"**Solution**: Yes. Its just like the normal installation. After you download CS:CO from the official link\n"
			"open the .zip and extract the `csco` folder from the zip to %Steam\steamapps\sourcemods and then restart\n"
			"your steam completely. Then check out our [Reddit]({}), theres a guide pinned there on how to edit your gameinfor.txt"
			"(Don't worry, its really easy)\n\n"
			"**Problem 3**: I don't know how to connect..HELP!\n"
			"**Solution**: Open console, type `connect <ip:port>` and press enter.\n\n"
			"**Problem 4**: Can't buy deagle!!\n"
			"**Solution**: Open CSGO and unequip `Revolvo` and equip `Juan Deag`\n\n\n"
			"This command will be updated!"
			"".format(reddit))

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.set_author(name='Classic Offensive', icon_url='http://i.imgur.com/seRbjgS.jpg')
		embed.add_field(name="Frequently-Asked-Questions", value=str(faq), inline=False)

		
		try:
			await self.bot.whisper(embed=embed)
			await self.bot.say(":page_facing_up: **I've DM'ed you the FAQ!**")

		except:
			await self.bots.say("Can't send DMs to you :(")

	@co.command()
	async def greenlight(self):
		"""Gives the link of Classic Offensive Greenlight"""
		gl = "http://steamcommunity.com/sharedfiles/filedetails/?id=841415339"
		gli = (
			"Here's the Greenlight link of Classic Offensive\n"
			"__[Click Here]({})__"
			"".format(gl)
			)

		embed = discord.Embed(colour=discord.Colour(0x00B9FCFF))
		embed.set_author(name='Classic Offensive', icon_url='http://i.imgur.com/seRbjgS.jpg')
		embed.add_field(name="Greenlight", value=str(gli), inline=False)
		
		await self.bot.say(embed=embed)

def setup(bot):
	bot.add_cog(ClassicOffensive(bot))
