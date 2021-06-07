import discord 
from discord.ext import commands
from imdb import IMDb 

class Peliculas (commands.Cog):

	def __init__ (self, fracasobot):
		self.fracasobot = fracasobot

	@commands.command()
	async def bpelicula(self, ctx, *, busqueda):
		objImdb = IMDb()
		coincidencias = objImdb.search_movie(busqueda)
		impresionPeliculas = "```Coincidencias:"
		for x in coincidencias:
			impresionPeliculas += "\n{}\t - {}".format(x.movieID, x['title'])

		impresionPeliculas += "```"
		await ctx.send(impresionPeliculas)

	@commands.command()
	async def pelicula(self, ctx, idpelicula):

		objImdb = IMDb()
		filme = objImdb.get_movie(idpelicula)

		def nombreRol(ListaPersonas, separador = ', '):
			recipienteNombres = []
			for persona in ListaPersonas:
				nombre = persona.get('name', '')
				if persona.currentRole:
					nombre += '({})'.format(persona.currentRole)
				recipienteNombres.append(nombre)
			return separador.join(recipienteNombres)

		tituloFilme = filme['title']
		añoFilme = filme['year']
		urlFilme = objImdb.get_imdbURL(filme)
		coverFilme = filme['cover']
		ratingFilme = filme['rating']
		listaGeneros = filme['genres']
		generoFilme = ', '.join(listaGeneros)

		   
		plotFilme = filme['plot'][0]
		
		if not plotFilme:
			plotFilme = filme['plot summary'][0]
			if plotFilme:
				plotFilme = [plotFilme]

		i = plotFilme.find('::')
		if i != -1:
			plotFilme = plotFilme[:i]

		listaDirectores = filme['director']
		directoresFilme = nombreRol(listaDirectores)

		listaCast = filme['cast']
		listaCast = listaCast[:5]
		castFilme = nombreRol(listaCast)

		embedFilme = discord.Embed(
			author = IMDb,
			title = "{} ({})".format(tituloFilme, añoFilme),
			url = urlFilme,
			image = "https://m.media-amazon.com/images/M/MV5BMjA2MTEzMzkzM15BMl5BanBnXkFtZTgwMjM2MTM5MDI@._V1_SY150_CR0,0,101,150_.jpg",
			description = plotFilme)

		embedFilme.set_author(name = 'IMDb', icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/640px-IMDB_Logo_2016.svg.png")
		embedFilme.set_image(url = coverFilme)
		embedFilme.add_field(name = "Director", value = directoresFilme, inline = False)
		embedFilme.add_field(name = "Cast", value = castFilme, inline = False)
		embedFilme.add_field(name = "Genre", value = generoFilme )
		embedFilme.add_field(name = 'Rating', value = str(ratingFilme))

		await ctx.send(embed = embedFilme)


def setup(fracasobot):
	fracasobot.add_cog(Peliculas(fracasobot))

