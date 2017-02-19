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

            bot.GetService<CommandService>().CreateCommand("ban")
                .Parameter("user", ParameterType.Required)
                .Parameter("reason", ParameterType.Multiple)
                .Do(async msg =>
                {
                    IEnumerable<Role> requiredRoles = bot.GetServer(261646233913917443).FindRoles("Management Team", true);
                    if (msg.Message.User.HasRole(requiredRoles.First<Role>())){
                        await msg.Message.MentionedUsers.First().SendMessage($"{msg.Message.User.Name} banned {msg.Message.MentionedUsers.First().Name} for reason ({msg.GetArg("reason")})");
                        await bot.GetServer(261646233913917443).Ban(msg.Message.MentionedUsers.First());
                        await bot.GetServer(261646233913917443).GetChannel(267022933547941890).SendMessage($"{msg.Message.User.Name} banned {msg.Message.MentionedUsers.First().Name} for reason ({msg.GetArg("reason")})");
                    }
                });
        }
    }
}
