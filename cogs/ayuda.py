import discord
from discord.ext import commands
import random 

class Ayuda(commands.Cog):

	def __init__(self, fracasobot):
		self.fracasobot = fracasobot

	@commands.command(aliases = ['halp', 'aiura'])
	async def ayuda(self, ctx, consulta = 'todo'):
		embedAyuda = discord.Embed(
			author = "Fracasín",
			title = "FIST INC (Fracasín Information Service & Technologies Incorporated)",
			colour = discord.Colour.greyple()
		)

		if (consulta == 'todo'):
			embedAyuda.add_field(name = 'Ping:', value= "Regresa 'Pong!' junto con valor de latencia. \n**Sintaxis:** \n.ping", inline = False)
			embedAyuda.add_field(name = '8ball: ', value= "Regresa respuesta propia de una bola mágica 8 ante una pregunta formulada. \n**Sintaxis:** \n.8ball + Pregunta \n **Aliases:** \nbolocho, bola8", inline = False)
			embedAyuda.add_field(name = 'wcovid: ', value = "Regresa cifras generales de casos COVID-19 provenientes de Worldometer. \n**Sintaxis:** \n.wcovid + Nombre del país(Inglés) \n**Aliases:** \ncovidWorldometers ", inline = False)
			embedAyuda.add_field(name = 'jcovid: ', value = "Regresa cifras generales de casos COVID-19 provenientes de la Universidad de JohnsHopkins. \n**Sintaxis:** \n.jcovid + Nombre del país(Inglés)\n**Aliases:** \ncovidJohnsHopkins ", inline = False)

		elif (consulta == 'ping'):
			embedAyuda.add_field(name = 'Ping:', value= "Regresa 'Pong!' junto con valor de latencia. \n**Sintaxis:** \n.ping")

		elif (consulta == '8ball'):
			embedAyuda.add_field(name = '8ball: ', value= "Regresa respuesta propia de una bola mágica 8 ante una pregunta formulada. \n**Sintaxis:** \n.8ball + Pregunta \n **Aliases:** \nbolocho, bola8")

		elif (consulta == 'wcovid'):
			embedAyuda.add_field(name = 'wcovid: ', value = "Regresa cifras generales de casos COVID-19 provenientes de Worldometer. \n**Sintaxis:** \n.wcovid + Nombre del país(Inglés) \n**Aliases:** \ncovidWorldometers ")

		elif (consulta == 'jcovid'):
			embedAyuda.add_field(name = 'jcovid: ', value = "Regresa cifras generales de casos COVID-19 provenientes de la Universidad de JohnsHopkins. \n**Sintaxis:** \n.jcovid + Nombre del país(Inglés) \n**Aliases:** \ncovidJohnsHopkins ")

		else:
			embedAyuda.add_field(name = 'Error' , value = "Comando no existente. \n\n**Sugerencias de comandos a:** \nfracasin@gmail.com")

		await ctx.send(embed = embedAyuda)


def setup(fracasobot):
	fracasobot.add_cog(Ayuda(fracasobot))