import discord
from discord.ext import commands
import dict_query
import os
from time import sleep
import random

description = '''An awkward attempt at making a discord bot'''
bot = commands.Bot(command_prefix='$', description=description)

def load_game_suggestions():
    '''
    :return: tries to load a dict of suggestions from a file,
    otherwise returns empty dict
    '''
    suggestions = load_data('suggestions')
    if not suggestions:
        suggestions = {}
    return suggestions


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
    await bot.change_presence(game=discord.Game(name='with turrets'))

@bot.command()
async def games(ctx):
    """Prints games suggested so far grouped by suggestion author's name"""
    message = ''
    if suggestions:
        for name in suggestions:
            message+='```\n'+'Suggested by '+name+':'
            for game in suggestions[name]:
                message+='\n'+game
            message+='```'
        await ctx.send(message)
    else:
        await ctx.send('Nothing has been suggested so far')

@bot.command()
async def list(ctx):
    """Prints games suggested so far in one list"""
    if suggestions:
        set_of_games = set({})
        message = '```\nGames suggested so far:'
        for name in suggestions:
            for game in suggestions[name]:
                set_of_games.add(game)
        for game in set_of_games:
            message+='\n'+game
        message+='```'
        await ctx.send(message)
    else:
        await ctx.send('Nothing has been suggested yet')

@bot.command()
async def suggest(ctx, *, data):
    """Adds a game suggestion"""
    name = str(ctx.author.name)
    game = ' '.join(data.split())
    if name in suggestions:
        suggestions[name].add(game)
    else:
        suggestions[name] = {game}
    await ctx.send(name+' suggested '+game)
    save_data(suggestions, 'suggestions')

@bot.command()
async def remove(ctx, *, data):
    """Removes the game suggestion if the game was suggested by the user issuing the command"""
    name = str(ctx.author.name)
    game = ' '.join(data.split())
    if name in suggestions:
        if game in suggestions[name]:
            suggestions[name].remove(game)
            if suggestions[name] == set({}):
                del suggestions[name]
            save_data(suggestions, 'suggestions')
            await ctx.send('Successfully deleted '+game+' from '+name+'\'s suggestions')
    else:
        await ctx.send('You cannot delete a game you did naaaht suggest')

@bot.command()
async def adminremove(ctx, *, data):
    """Removes the game from every list, command only available to Admin role"""
    role_obj_list = ctx.author.roles
    game = ' '.join(data.split())
    roles = []
    names_to_delete = []
    for role in role_obj_list:
        roles.append(role.name)
    if 'Admin' in roles:
        for name in suggestions:
            if game in suggestions[name]:
                suggestions[name].remove(game)
                if suggestions[name] == set({}):
                    names_to_delete.append(name)
        for name in names_to_delete:
            del suggestions[name]
        save_data(suggestions, 'suggestions')
        await ctx.send('Successfully deleted ' + game + ' from suggestions')
    else:
        await ctx.send(random.choice(rejections))

# @bot.command()
# async def adminwipe(ctx):
#     """Purges the game suggestions list, command only available to Admin role"""
#     role_obj_list = ctx.author.roles
#     roles = []
#     for role in role_obj_list:
#         roles.append(role.name)
#     if 'Admin' in roles:
#         for name in suggestions: #TODO understand what's wrong here
#             del name
#         save_data(suggestions, 'suggestions')
#         await ctx.send('The list is empty now :\'(')
#     else:
#         await ctx.send(random.choice(rejections))


@bot.command(aliases=['miriam', 'Miriam' ,'MIRIAM','GODDAMITMIRIAM', 'word', 'mw', 'Merriam'])
async def merriam(ctx, *, word: str):
    """Queries Merriam-Webster's Collegiate Dictionary for a word definition. Well, tries to at least..."""
    word = ' '.join(word.split())
    # try:
    query_result = dict_query.query_merriam(word, keys['merriam-webster'])
    cases = query_result #the word may have changed if you queried for the past tense for example
    # except:
    #     await ctx.send('Something went wrong during online query')
    # try:
    phrase = dict_query.parse_merriam(cases)
    # except:
    #     await ctx.send('Something went wrong during result parsing')
    if phrase != '' and phrase is not None:
        if len(phrase) >= 2000:
            message_list = dict_query.split_message(phrase)
            # for message in message_list:
            await ctx.send(message_list[0])
            await ctx.send('\_'*20+'\nRead more: '+'https://www.merriam-webster.com/dictionary/'+'%20'.join(word.split(' ')))
        else:
            await ctx.send(phrase)
    else:
        message = await ctx.send('Could not find the word or something went wrong with the request')
        sleep(4)
        await message.delete()

@bot.command()
async def adc(ctx, *, data: str):
    message = ctx.message
    tshootdata = str(message.channel)+' | '+str(isinstance(message.channel, discord.DMChannel))
    # channels = str(str(x)+'; ' for x in bot.get_all_channels())
    await ctx.send(tshootdata)

if __name__ == '__main__':
    keys = load_data('keys')
    rejections = ['Nope', 'Nu-uh', 'You are not my supervisor!', 'Sorry, you are not important enough to do that -_-',
                  'Stop trying that, or I\'ll report you to Nightmom!']
    suggestions = load_game_suggestions()
    bot.run(keys['bot'])
