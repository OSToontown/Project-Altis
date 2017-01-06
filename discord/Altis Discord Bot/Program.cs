using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Discord;
using System.Net;

namespace Altis_Discord_Bot
{
    class Program
    {
        public bool SERVER_STATUS = false;
        public string SERVER_REASON = "Security Revamp";
        static void Main(string[] args) => new Program().Start();
        public MessageEventArgs serverObj;
        private DiscordClient _client;
        public string[]  badWords = {"shit","piss","fuck","cunt","nigger","nigga"};

        public void Start()
        {
            _client = new DiscordClient();

            _client.MessageReceived += async (s, e) =>
            {
                serverObj = e;
                if (!e.Message.IsAuthor)
                {
                    if (e.Message.Text.Contains("up"))
                        if (!SERVER_STATUS)
                            await e.Channel.SendMessage("@" + e.User.Name.ToString() + " The server is currently offline for a " + SERVER_REASON);
                        else
                            await e.Channel.SendMessage("@" + e.User.Name.ToString() + " The server is currently online! Hop in and join us!");
                }
                if(e.Message.User.Roles.Count() == 0)
                {
                    foreach (string x in badWords)
                    {
                        if (e.Message.Text.Contains(x))
                        {
                            await e.Channel.SendMessage(e.User.Name.ToString() + " was kicked for bad language!");
                            await e.Message.User.Kick();
                        }
                    }

                }

            };

            _client.UserBanned += async (s, e) => {
                var logChannel = e.Server.FindChannels("logs").FirstOrDefault();
                await logChannel.SendMessage($"User Banned: {e.User.Name}");
            };

            _client.UserUnbanned += async (s, e) => {
                var logChannel = e.Server.FindChannels("logs").FirstOrDefault();
                await logChannel.SendMessage($"User Un-Banned: {e.User.Name}");
            };

            _client.ExecuteAndWait(async () => {
                await _client.Connect("MjY3MDE4ODkzNzMyNzQxMTIw.C1GIdw.W46npMbaOd3k-vyaClwym_QI39Q", TokenType.Bot);
            });

            
        }


    }
}
