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
                .Parameter("reason", ParameterType.Unparsed)
                .Do(async msg =>
                {
                    IEnumerable<Role> requiredRoles = bot.GetServer(261646233913917443).FindRoles("Moderation Team", false);
                    foreach (Role role in requiredRoles)
                    {
                        if (msg.Message.MentionedUsers.First().HasRole(role)) { await msg.Channel.SendMessage($"You can't ban that person, {msg.Message.User.Mention}!"); return; }
                          if (msg.Message.User.HasRole(role))
                        {
                            
                            await bot.GetServer(261646233913917443).Ban(msg.Message.MentionedUsers.First());
                            await bot.GetServer(261646233913917443).GetChannel(267022933547941890).SendMessage($"{msg.Message.User.Name} banned {msg.Message.MentionedUsers.First().Name} for reason ({msg.GetArg("reason")})");
                            await msg.Message.Delete();
                            return;
                        }
                        else
                        {
                            await msg.Channel.SendMessage($"You do not have permisson to run that command, {msg.Message.User.Mention}!");
                            return;
                        }
                    }
                    await msg.Channel.SendMessage($"You do not have permisson to run that command, {msg.Message.User.Mention}!");

                });
        }
    }
}
