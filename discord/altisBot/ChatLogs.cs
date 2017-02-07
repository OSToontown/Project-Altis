using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Discord;
using System.IO;

namespace discordCSBOT
{
    class ChatLogs
    {
        public void Start(DiscordClient bot)
        {

            bot.MessageReceived += async (s, e) =>
            {
                string currDate = DateTime.Today.ToShortDateString().Replace('/', '_');
                string path = $@"chatlogs/chatlog_{currDate}.txt";
                using (StreamWriter file = new StreamWriter(File.Open(path, System.IO.FileMode.Append)))
                {
                    string author = e.Message.User.Name;
                    string channel = e.Message.Channel.Name;
                    string message = e.Message.RawText;
                    string timestamp = DateTime.Now.ToString();

                    string content = $"{timestamp} ({channel}) {author} sent a message: {message}".Replace('\n', ' ');
                    await file.WriteLineAsync(content);
                }
            };

        }
    }
}
