import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print("Ich habe mich eingeloggt. Beep bop.")


@client.command(aliases=["h", "hilfe", ])
async def _help(ctx):
    embed = discord.Embed(color=0xffdd00)
    embed.add_field(name="Beep Beep", value="Hilfemenü für:" + "[" + ctx.author.mention + "]", inline=False)
    embed.add_field(name="1: $beepBob", value="Testbefehl", inline=False)
    embed.add_field(name="2: $showLog",
                    value="Zeigt wie oft der Bot aufgerufen wurde, nur für User mit der -testbot- Rolle.", inline=False)
    embed.add_field(name="3: $ping", value="Zeigt deinen Ping an.", inline=False)
    embed.add_field(name="4: $clear -arg-", value="Löscht die Anzahl der angegebenen Nachrichten", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def beepBob(ctx):
    embed = discord.Embed(color=0xffdd00)
    embed.add_field(name="Beep Beep! BOBderBOT v2", value="[" + ctx.author.mention + "]", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    embed = discord.Embed(color=0xffdd00)
    embed.add_field(name="Beep Beep! BOBderBOT v2",
                    value="[" + ctx.author.mention + "]" + " Deine Latenz liegt bei: " + str(
                        round((client.latency * 1000) / 2)), inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=["cls", "löschen"])
async def clear(ctx, ammount=5):
    await ctx.channel.purge(limit=ammount + 1)


@client.command(aliases=["rtt"])
async def roulette(ctx, bid):
    bid_param = -3
    if bid.lower() == "black":
        bid_param = -2
    elif bid.lower() == "red":
        bid_param = -2
    else:
        try:
            bid_param = int(bid)
        except:
            embed = discord.Embed(color=0xffdd00)
            embed.add_field(name="Beep Beep! Roulette", value="Ungültige Eingabe!", inline=False)
            await ctx.send(embed=embed)
            return
    result = random.randint(0, 36)
    if bid_param == -1:
        won = result % 2 == 0 and not result == 0
    elif bid_param == -2:
        won = result % 2 == 1
    else:
        won = result == bid_param
    if won:
        embed = discord.Embed(color=0xffdd00)
        embed.add_field(name="Beep Beep! Roulette", value="$$ Du hast gewonnen! $$", inline=False)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(color=0xffdd00)
        embed.add_field(name="Beep Beep! Roulette", value="Leider verloren", inline=False)
        await ctx.send(embed=embed)


@client.event
async def on_member_join(member):
    print(str(member) + "has joined a Server")


@client.event
async def on_member_remove(member):
    print(str(member) + "has left a server")


client.run("")
