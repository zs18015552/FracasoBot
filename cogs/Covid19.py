import discord
from discord.ext import commands
from covid import Covid

class Covid19(commands.Cog):

	def __init__(self, fracasobot):
		self.fracasobot = fracasobot
	
	@commands.command(aliases = ['jcovid'])
	async def covidJohnsHopkins(self, ctx, *, busqueda):
		if (busqueda == 'españa'):
			busqueda = 'spain'	

		covid = Covid()
		impresionDatos = ""

		embedCovid = discord.Embed(
			title = "COVID-19",
			colour = discord.Colour.red(),
			url = "https://coronavirus.jhu.edu/map.html"
		)

		try:
			casosPais = covid.get_status_by_country_name(busqueda)
			pais = str(casosPais['country'])
			confirmados = '**Confirmados:** ' + str(casosPais['confirmed']) + '\n'
			activos = '**Activos:** ' + str(casosPais['active']) + '\n'
			defunciones = '**Defunciones:** ' + str(casosPais['deaths']) + '\n'
			recuperados = '**Recuperados:** ' + str(casosPais['recovered'])

			impresionDatos = confirmados + activos + defunciones + recuperados
		
		except ValueError as ve:
			impresionDatos = "Pais no encuentrado. El comando solo admite nombre en inglés."
		
		finally:
			embedCovid.add_field(name = pais, value= impresionDatos)	
			embedCovid.set_author(name = "Johns Hopkins University", icon_url = "https://upload.wikimedia.org/wikipedia/en/thumb/0/09/Johns_Hopkins_University's_Academic_Seal.svg/1920px-Johns_Hopkins_University's_Academic_Seal.svg.png")
			embedCovid.set_thumbnail(url = "https://www.european-radiology.org/content-er/uploads/2020/02/corona-cell-1080.png")
			embedCovid.set_footer(text = "Conserven la Sana Distancia :c")

			await ctx.send(embed = embedCovid)

	@commands.command(aliases = ['wcovid'])
	async def covidWorldometers(self, ctx, *, busqueda):
		if (busqueda == 'españa'):
			busqueda = 'spain'	

		covid = Covid(source = 'worldometers')
		impresionDatos = ""

		embedCovid = discord.Embed(
			title = "COVID-19",
			colour = discord.Colour.red(),
			url = "https://www.worldometers.info/coronavirus/"
		)

		try:
			casosPais = covid.get_status_by_country_name(busqueda)
			pais = str(casosPais['country'])
			confirmados= '\n**Confirmados:** ' + str(casosPais['confirmed']) + '\n'
			nuevosCasos = '**Nuevos Casos:** ' + str(casosPais['new_cases']) + '\n'
			activos = '**Activos:** ' + str(casosPais['active']) + '\n'
			criticos = '**Estado crítico:** ' + str(casosPais['critical']) + '\n'
			nuevasDefunciones = '**Nuevas defunciones:** ' + str(casosPais['new_deaths']) + '\n'
			defunciones = '\n**Defunciones:** ' + str(casosPais['deaths']) + '\n'
			recuperados = '**Recuperados:** ' + str(casosPais['recovered']) + '\n'

			pruebas = '\n**Pruebas realizadas:** ' + str(casosPais['total_tests'])

			impresionDatos = confirmados + nuevosCasos + activos + criticos + nuevasDefunciones + defunciones + recuperados + pruebas
		
		except ValueError as ve:
			impresionDatos = "El comando admite solo nombres en inglés."
			pais = "Pais no encuentrado."
		
		finally:
			embedCovid.add_field(name = pais, value= impresionDatos)	
			embedCovid.set_author(name = "Worldometers", icon_url = "https://pbs.twimg.com/profile_images/692017015872167940/1fnJPzxM.png")
			embedCovid.set_thumbnail(url = "https://www.european-radiology.org/content-er/uploads/2020/02/corona-cell-1080.png")
			embedCovid.set_footer(text = "Conserven la Sana Distancia :c")

			await ctx.send(embed = embedCovid)

def setup(fracasobot):
	fracasobot.add_cog(Covid19(fracasobot))