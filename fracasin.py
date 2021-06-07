import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
import arrow

prefijoFracasoBar = '.'
idFracasoBar = ''

fracasobot= commands.Bot(command_prefix = prefijoFracasoBar)
status = cycle(['Saludos a Mamá Pucha', 'Quiero una pollería', 'keoña keoña', 'Sanadistanciando', 'Cookie Run :('])

@fracasobot.event
async def on_ready():
	cambiarStatus.start()
	print('Bot is ready.')

@tasks.loop(seconds=3600)
async def cambiarStatus():
	await fracasobot.change_presence(activity=discord.Game(next(status)))

@fracasobot.command( description = "Regresa 'Pong!' junto con valor de latencia.")
async def ping(ctx):
	await ctx.send(f'´ Pong! {round(fracasobot.latency * 1000)}ms')	

@fracasobot.command( description = 'Regresa los días restantes del año')
async def dias(ctx):
	hoy = arrow.now()
	año = hoy.year
	finAño = arrow.get(año + 1, 1, 1)
	restaDias = finAño - hoy

	await ctx.send('```Al **{}** le quedan **{}** días```'.format(año, restaDias.days+1))

@fracasobot.command( description = "Carga un módulo .py. \n**Sintaxis:** .load + modulo")
async def load(ctx, extension):
	fracasobot.load_extension(f'cogs.{extension}')

@fracasobot.command( description = "Quita un módulo .py. \n**Sintaxis:** .unload + modulo")
async def unload(ctx, extension):
	fracasobot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		fracasobot.load_extension(f'cogs.{filename[:-3]}')

fracasobot.run('NzQwOTk4NjE3MDc0MjM3NTIx.XyxKvQ.1aRHaBfhN--vm-GLjStxsGyxSrM')	