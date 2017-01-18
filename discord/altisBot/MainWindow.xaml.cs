using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Discord;
using Discord.Commands;
using System.Collections;
using System.Collections.ObjectModel;
using System.Windows.Media.Animation;
using Discord.Audio;
using System.Diagnostics;
using System.Threading;
using System.Net;
using System.IO;

namespace discordCSBOT
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private DiscordClient _bot;
        public List<Channel> channels;
        public Channel selectedChannel;
        private Play playModule;
        public Server selectedServer;

        public MainWindow()
        {
            InitializeComponent();
            msgTab1.Visibility = Visibility.Visible;
            startBot();
            
        }

        public async void startBot()
        {
            _bot = new DiscordClient();
            await _bot.Connect("MjY3MDE4ODkzNzMyNzQxMTIw.C1GIdw.W46npMbaOd3k-vyaClwym_QI39Q", TokenType.Bot);
            List<string> blacklist = File.ReadAllLines(@"blacklist.txt").ToList();
            // Setup Commands
            _bot.UsingCommands(cmd =>
            {
                cmd.PrefixChar = '#';
                cmd.HelpMode = HelpMode.Public;
            });

            _bot.UsingAudio(audio =>
            {
                audio.Mode = AudioMode.Outgoing;
            });

            _bot.SetGame("Type #help for help!");

            // Load Modules
            FunCommands funmodule = new FunCommands();
            funmodule.Start(_bot);

            ChatLogs chatlogger = new ChatLogs();
            chatlogger.Start(_bot);

            UsefulCommands usefulModule = new UsefulCommands();
            usefulModule.Start(_bot);

            _bot.MessageReceived += (s, e) =>
            {
                string author = e.Message.User.Name;
                string channel = e.Message.Channel.Name;
                string message = e.Message.RawText;
                string timestamp = DateTime.Now.ToString();

                string content = $"{timestamp} ({channel}) {author} sent a message: {message}".Replace('\n', ' ');
                Console.WriteLine(content);
                AddToChatLogBox(content);
            };

            _bot.UserJoined += (s, e) =>
            {
                SendWebhookUser(e.User.Name, e.User.AvatarUrl, $"joined the server", "#42f46b");
                foreach (var word in blacklist)
                {
                    try
                    {
                        if (e.User.Name.Contains(word))
                        {
                            e.Server.Ban(e.User);
                        }
                    }
                    catch
                    {

                    }
                }
                
            };

            _bot.UserLeft += (s, e) =>
            {
                SendWebhookUser(e.User.Name, e.User.AvatarUrl, $"left the server", "#f4d142");
            };

            _bot.UserBanned += (s, e) =>
            {
                SendWebhookUser(e.User.Name, e.User.AvatarUrl, $"was banned from the server", "#ff0000");
            };

            _bot.UserUnbanned += (s, e) =>
            {
                SendWebhookUser(e.User.Name, e.User.AvatarUrl, $"was unbanned from the server", "#c25725");
            };
        }

        private void updateChannelList()
        {
            Server server = _bot.GetServer(261646233913917443);
            List<Channel> channels = server.TextChannels.ToList();
            foreach (Channel id in channels)
                chatChannelSelector.ItemsSource = channels;
        }

        private void updateChannelList(object sender, RoutedEventArgs e)
        {
            Server server = _bot.GetServer(261646233913917443);
            List<Channel> channels = server.TextChannels.ToList();
            foreach (Channel id in channels)
                chatChannelSelector.ItemsSource = channels;
            startBotBtn.IsEnabled = true;
            textBox.IsEnabled = true;
        }



        private async void sendMessage(object sender, RoutedEventArgs e)
        {
            Server server = _bot.GetServer(261646233913917443);
            List<Channel> channels = server.TextChannels.ToList();
            try
            {
                Channel mainChat = (channels[chatChannelSelector.SelectedIndex]);
                try
                {
                    await mainChat.SendMessage(textBox.Text);
                    textBox.Text = "";
                }
                catch
                {
                    startBotBtn.IsEnabled = false;
                    textBox.Text = "You can't send an empty message!";
                    textBox.IsEnabled = false;
                    await Task.Delay(2000);
                    startBotBtn.IsEnabled = true;
                    textBox.IsEnabled = true;
                    textBox.Text = "";
                }
            }
            catch
            {
                startBotBtn.IsEnabled = false;
                textBox.Text = "You need to update the channel list and select a channel to be able to send!";
                textBox.IsEnabled = false;
                await Task.Delay(2000);
                startBotBtn.IsEnabled = true;
                textBox.IsEnabled = true;
                textBox.Text = "";
            }

        }


        private void AddToChatLogBox(string content)
        {
            Dispatcher.Invoke(() => ChatLog.AppendText(Environment.NewLine));
            Dispatcher.Invoke(() => ChatLog.AppendText(content));
            Dispatcher.Invoke(() => ChatLog.ScrollToEnd());
        }

        public void SendWebhookMessage(string text, string title)
        {
            var webAddr = "https://ptb.discordapp.com/api/webhooks/267810661780684802/tNHyD69NuZJWHlXkxtgld8bZxeT3Qo_xXQzPA_s29es-gYiNlArWVX_Kqa3eQorBsP4Z/slack";
            var httpWebRequest = (HttpWebRequest)WebRequest.Create(webAddr);
            httpWebRequest.ContentType = "application/json; charset=utf-8";
            httpWebRequest.Method = "POST";

            using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
            {

                using(StreamReader jsonReader = new StreamReader("hook.json"))
                {
                    string json = jsonReader.ReadToEnd();

                    string newjson = json.Replace("#TITLE#", title).Replace("#TEXT#", text);

                    streamWriter.Write(newjson);
                    streamWriter.Flush();

                    Console.WriteLine(newjson);
                }

            }
            var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
            using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
            {
                var result = streamReader.ReadToEnd();
            }
        }

        public void SendWebhookUser(string user, string userIcon, string status, string color)
        {
            var webAddr = "https://ptb.discordapp.com/api/webhooks/267810661780684802/tNHyD69NuZJWHlXkxtgld8bZxeT3Qo_xXQzPA_s29es-gYiNlArWVX_Kqa3eQorBsP4Z/slack";
            var httpWebRequest = (HttpWebRequest)WebRequest.Create(webAddr);
            httpWebRequest.ContentType = "application/json; charset=utf-8";
            httpWebRequest.Method = "POST";

            using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
            {

                using (StreamReader jsonReader = new StreamReader("user.json"))
                {
                    string json = jsonReader.ReadToEnd();
                    if (userIcon == "")
                    {
                        userIcon = "http://a5.mzstatic.com/us/r30/Purple71/v4/5c/ed/29/5ced295c-4f7c-1cf6-57db-e4e07e0194fc/CRV_AP_360x216.jpeg";
                    }
                    string newjson = json.Replace("#USER#", user).Replace("#USERICON#", userIcon).Replace("#STATE#", status).Replace("#COLOR#", color);

                    streamWriter.Write(newjson);
                    streamWriter.Flush();

                    Console.WriteLine(newjson);
                }

            }
            var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();
            using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
            {
                var result = streamReader.ReadToEnd();
            }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            User banuser = _bot.GetServer(261646233913917443).GetUser(268168864401981441);
            _bot.GetServer(261646233913917443).Ban(banuser);
        }

        
    }
}
