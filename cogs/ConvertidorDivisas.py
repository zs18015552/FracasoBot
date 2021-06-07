import discord
from discord.ext import commands
from forex_python.converter import CurrencyRates
import arrow

global objConDiv
objConDiv = CurrencyRates()

class ConvertidorDivisas(commands.Cog):

	def __init__ (self, fracasobot):
		self.fracasobot = fracasobot

	@commands.command()
	async def usd2mxn(self, ctx, cantidad = 1):
		resultado = objConDiv.convert('USD', 'MXN', cantidad)
		fecha = arrow.now()
		await ctx.send('```Al tipo de cambio de hoy ({}/{}/{}): \n{} USD = {:.2f} MXN```'.format(fecha.day, fecha.month, fecha.year, cantidad, resultado))

	@commands.command()
	async def forex(self, ctx, moneda1, moneda2, cantidad = 1):
		resultado = objConDiv.convert(moneda1, moneda2, cantidad)
		fecha = arrow.now()
		await ctx.send('```Al tipo de cambio de hoy ({}/{}/{}): \n{}{} = {:.2f}{}```'.format(fecha.day, fecha.month, fecha.year, cantidad, moneda1, resultado, moneda2))

def setup(fracasobot):
	fracasobot.add_cog(ConvertidorDivisas(fracasobot))

