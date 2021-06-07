import discord
from discord.ext import commands
import random 

class Prediccion(commands.Cog):

	def __init__(self, fracasobot):
		self.fracasobot = fracasobot

	@commands.command(aliases = ['8ball', 'bola8', 'bolocho'])
	async def _8ball(self, ctx, *, pregunta):
		respuestas = ['● En mi opinión, sí',
					  '● Es cierto',
					  '● Es decididamente así',
					  '● Probablemente',
					  '● Buen pronóstico',
					  '● Todo apunta a que sí',
					  '● Sin duda',
					  '● Sí',
					  '● Sí - definitivamente',
					  '● Debes confiar en ello',
					  '● Respuesta vaga, vuelve a intentarlo',
					  '● Pregunta en otro momento',
					  '● Será mejor que no te lo diga ahora',
					  '● No puedo predecirlo ahora',
					  '● Concéntrate y vuelve a preguntar',
					  '● Puede ser',
					  '● No cuentes con ello',
					  '● Mi respuesta es no',
					  '● Mis fuentes me dicen que no',
					  '● Las perspectivas no son buenas',
					  '● Muy dudoso']
		await ctx.send(f'> Pregunta: {pregunta}')
		await ctx.send(random.choice(respuestas))

def setup(fracasobot):
	fracasobot.add_cog(Prediccion(fracasobot))