import discord
from discord.ext import commands

class Moderacion(commands.Cog):

	def __init__ (self, fracasobot):
		self.fracasobot = fracasobot

	@commands.command(aliases=['clear', 'borrar'])
	async def borrarMsj(self, ctx, monto=5):
		await ctx.channel.purge(limit=monto)

def setup(fracasobot):
	fracasobot.add_cog(Moderacion(fracasobot))