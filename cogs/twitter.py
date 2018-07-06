# This is a dice rolling cog for a Discord bot. It supports all basic mathematical operations:
# addition, subtraction, multiplication, division, and parentheses. It also includes support for
# dice rolls. E.g. "1d20+6"
# Author: ryanalexanderhughes@gmail.com
# Based on: https://ruslanspivak.com/lsbasi-part1/ by Ryslan Spivak

from discord.ext import commands
import twitter

class TwitterCog:
    def __init__(self, bot):
        self.bot = bot
        self.channel = "announcements"
        self.already_posted = set()
        self.start_time
        posts = api.GetUserTimeline(screen_name="broccoligamedev")
        for s in posts:
            self.already_posted.add(s)
    async def check_twitter_feed():
        while True:
            posts = api.GetUserTimeline(screen_name="broccoligamedev")
            for s in posts:
                if s not in already_posted:
                    print(s.text)
            await asyncio.sleep(10)

def setup(bot):
    bot.loop.create_task(status_task())
    bot.add_cog(TwitterCog(bot))
