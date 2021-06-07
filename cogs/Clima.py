import discord
from discord.ext import commands
from configparser import ConfigParser
import requests


class Clima(commands.Cog):

	def __init__(self, fracasobot):
		self.fracasobot = fracasobot

	@commands.command()
	async def clima(self, ctx, *, consulta="Mexico"):
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=es'
		archivoConfig = 'config.ini'
		config = ConfigParser()
		config.read(archivoConfig)
		api_key = config['api_key']['key']

		embedClima = discord.Embed(
			author = "Fracasín",
			colour = discord.Colour.gold()
		)

		try: 
			resultado = requests.get(url.format(consulta, api_key))
			jsonDatosClima = resultado.json()
			ciudad = jsonDatosClima['name']
			pais = jsonDatosClima['sys']['country']
			idPais = jsonDatosClima['id']
			iconoClima = jsonDatosClima['weather'][0]['icon']
			descripcionClima = jsonDatosClima['weather'][0]['main']
			temperaturaKelvin = jsonDatosClima['main']['temp']
			temperaturaCelsius = temperaturaKelvin - 273.15
			sensacionTermicaK = jsonDatosClima['main']['feels_like']
			sensacionTermicaC = sensacionTermicaK - 273.15


			urlIcono = 'https://openweathermap.org/img/wn/{}@2x.png'
			urlPagina = 'https://openweathermap.org/city/{}'		
		except ValueError as ve:
			ciudad = 'No hay información'
			pais = ':('

			idPais = 2643743
			iconoClima = '09d'
			temperaturaKelvin = 'No hay información'
			descripcionClima = ':('
			temperaturaCelsius = 'No hay información'
			sensacionTermica = 'No hay información'

		finally:
			embedClima.set_image(url = urlIcono.format(iconoClima))
			embedClima.add_field(name = '{}, {}'.format(ciudad, pais), value = descripcionClima, inline = False)
			embedClima.add_field(name = 'Temperatura', value = '{:.1f} °C'.format(temperaturaCelsius))
			embedClima.add_field(name = 'Sensación Térmica', value = '{:.1f} °C'.format(sensacionTermicaC))
			embedClima.set_author(name = 'OpenWeather', url = urlPagina.format(idPais), icon_url = 'https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png')
			embedClima.set_footer(text = 'FIST INC')
			await ctx.send(embed = embedClima)


def setup(fracasobot):
	fracasobot.add_cog(Clima(fracasobot))