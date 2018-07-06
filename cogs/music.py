from discord.ext import commands
from random import randint

MUSIC_STATE_IDLE = "IDLE"
MUSIC_STATE_PAUSED = "PAUSE"
MUSIC_STATE_PLAYING = "PLAYING"

class MusicCog:
    def __init__(self, bot):
        self.bot = bot
        self.text_channel = "music"
        self.voice_channel = "Music Bot"

    @commands.command()
    async def play(self, context, arg):
        await context.send(":game_die: Rolling: {}\nResult: {}".format(lexer.fancy_string, result))
    async def skip():
        pass
    async def disconnect():
        pass
    async def pause():
        pass
    async def playlist():
        pass
    async def current():
        pass
    async def repeat():
        pass


"""
@bot.client.command(pass_context=True)
async def skip(context):
    message = context.message
    server = message.server
    if not (server in bot.music_players):
        return
    music = bot.music_players[server]
    if music.current_player:
        music.current_player.stop()
        await bot.send_message(
            music.channel,
            'Skipped **{}**.'.format(music.current_player.title)
        )
    else:
        await bot.send_message(
            music.channel,
            ':warning: Nothing to skip.'
        )

@bot.client.command(pass_context=True)
async def disconnect(context):
    message = context.message
    server = message.server
    if not (server in bot.music_players):
        return
    music = bot.music_players[server]
    await disconnect(music)
    await bot.send_message(
        music.channel,
        'Bye.'
    )
    
@bot.client.command(pass_context=True)
async def pause(context):
    message = context.message
    server = message.server
    if not (server in bot.music_players):
        return	
    music = bot.music_players[server]
    if music.state == "PLAYING":
        await bot.send_message(
            music.channel,
            'Pausing playback.'
        )
        music.state = "PAUSED"
        music.current_player.pause()
        music.timeout_time = time.time()
    elif music.state == "PAUSED":
        await bot.send_message(
            music.channel,
            'Resuming playback.'
        )
        music.state = "PLAYING"
        music.current_player.resume()
    else:
        await bot.send_message(
            music.channel,
            ':warning: No current song.'
        )
        
@bot.client.command(pass_context=True)
async def playlist(context):
    message = context.message
    server = message.server

@bot.client.command(pass_context=True)
async def current(context):
    message = context.message
    server = message.server
    if not (server in bot.music_players):
        return
    music = bot.music_players[server]
    if music.current_player:
        await bot.send_message(
            music.channel,
            'Currently playing **{}**.'.format(music.current_player.title)
        )
    else:
        await bot.send_message(
            music.channel,
            ':warning: No current song.'
        )
    
@bot.client.command
async def repeat(pass_context=True):
    message = context.message
    server = message.server
    if not (server in bot.music_players):
        return
    music = bot.music_players[server]
    music.repeat = not music.repeat
    if music.repeat:
        await bot.send_message(
            music.channel,
            'Repeat on.'
        )
    else:
        await bot.send_message(
            music.channel,
            'Repeat off.'
        )
"""

"""

async def play_song(music):
    music.current_player = music.queue[0]
    await bot.send_message(
        music.channel,
        ':musical_note: Now playing **{}.**'.format(music.current_player.title)
    )
    music.state = "PLAYING"
    music.current_player.start()

async def done_playing(music):
    music.current_player = None
    if not music.repeat:
        music.queue.pop(0)
    music.state = "IDLE"
    music.timeout_time = time.time()

async def disconnect(music):
    music.state = "FINISHED"
    if music.voice:
        await music.voice.disconnect()
    if music.current_player:
        music.current_player.stop()
    del bot.music_players[music.server]

async def handle_timeout(music):
    if time.time() >= music.timeout_time + 30 and music.num_songs_loading == 0:
        await disconnect(music)
        await bot.send_message(
            music.channel,
            ":warning: Leaving due to inactivity."
        )
"""
def setup(bot):
    discord.opus.load_opus("libopus-0.dll")
    if discord.opus.is_loaded():
        log("opus loaded.")
    else:
        log("error: opus failed to load.")
        return
    bot.add_cog(DiceCog(bot))
