import discord
from discord.ext import commands
import random
import os

description = '''An awkward attempt at making a discord bot'''
bot = commands.Bot(command_prefix='?', description=description)


def load_game_suggestions():
    '''
    :return: tries to load a dict of suggestions from a file,
    otherwise returns empty dict
    '''
    suggestions = {}
    os.chdir(os.path.expanduser('~/bothelper/'))
    try:
        suggestions = load_data('suggestions')
    except:
        pass
    return suggestions


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# DON'T FORGET TO CHANGE NICK BACK TO NAME IN SUGGEST and uncomment save data
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def save_data(data, filename):
    '''
    :param data: data to be stored into a file
    :param filename: filename to save data to
    :return: None, saves dict as a file for future usage
    '''
    with open(filename, 'w') as file:
        file.write(str(data))

def load_data(filename):
    '''
    :param filename: file from which to load the data
    :return: returns eval() of the file contents
    '''
    data = ''
    try:
        with open(filename) as file:
            data = eval(file.read())
        return data
    except(FileNotFoundError):
        print('File not found')
    except:
        print('Something went wrong during data evaluation')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def games():
    """Prints games suggested so far"""
    message = ''
    try:
        for name in suggestions:
            message+='```\r'+'Suggested by '+name+':'
            for game in suggestions[name]:
                message+='\r'+game
            message+='```'
        await bot.say(message)
    except:
        await bot.say('Nothing has been suggested so far')

@bot.command(pass_context=True)
async def suggest(data):
    """Adds game suggestion"""
    name = str(data.message.author.nick)
    game = ' '.join(data.message.content[9:].split())
    if name in suggestions:
        suggestions[name].add(game)
    else:
        suggestions[name]= {game}
    await bot.say(name+' suggested '+game)
    await bot.say(str(suggestions))
    save_data(suggestions,'suggestions')


if __name__ == '__main__':
    suggestions = load_game_suggestions()
    bot.run('MzQ3ODQxOTExNjE4MjczMjkz.DHeSCg.Dqbmw8CecxiBHIqKbooRbkLlVWc')