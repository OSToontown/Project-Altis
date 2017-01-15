using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Discord;
using Discord.Commands;
using Discord.API;
using Discord.API.Client.Rest;

namespace discordCSBOT
{
    class UsefulCommands
    {
        public void Start(DiscordClient bot)
        {
            bot.GetService<CommandService>().CreateCommand("2fa")
                .Description("Help on how to use 2 factor authentication")
                .Do(async msg =>
                {
                    await msg.Channel.SendMessage("https://www.youtube.com/watch?v=kWD0i1zyo50");
                });
        }
    }
}
