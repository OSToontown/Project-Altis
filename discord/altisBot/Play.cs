using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Discord;
using Discord.Commands;
using Discord.Audio;
using System.Diagnostics;
using System.Threading;
using System.Windows.Controls;
using System.Windows;
using System.IO;
namespace discordCSBOT
{
    class Play
    {
        public string filePath;
        public void Start(DiscordClient bot)
        {

            // Play File command
            bot.GetService<CommandService>().CreateCommand("playfile")
                .Description("play an file")
                .Parameter("file", ParameterType.Required)
                .Do(async msg =>
                {
                    IAudioClient voiceClient = await bot.GetService<AudioService>().Join(msg.User.VoiceChannel);
                    PlayFile(voiceClient, msg.GetArg("file"));
            });

            // Play Youtube command
            bot.GetService<CommandService>().CreateCommand("play")
                .Description("play an're youtube videoxd")
                .Parameter("url", ParameterType.Required)
                .Do(async msg =>
                {
                    IAudioClient voiceClient = await bot.GetService<AudioService>().Join(msg.User.VoiceChannel);
                    DownloadVideoFromYoutubeAndThenContinueToPlayIt(voiceClient, msg.GetArg("url"), msg.Channel);
                });
        }

        private void DownloadVideoFromYoutubeAndThenContinueToPlayIt(IAudioClient voiceClient, string url, Channel channel)
        {
            string urlToDownload = url;
            string newFilename = Guid.NewGuid().ToString();
            Console.WriteLine(newFilename);
            string mp3OutputFolder = "C:/Users/Drew/Desktop/DiscordBot/Recode/cs/audio/cache/";
            filePath = mp3OutputFolder + newFilename + ".mp3";
            Downloader downloader = new Downloader(urlToDownload, newFilename, mp3OutputFolder);
            channel.SendMessage($"Downloading `{url}`...");

            downloader.ProgressDownload += (s, e) =>
            {
                Console.WriteLine(e.Percentage);
            };
                
                // downloader_ProgressDownload;
            downloader.FinishedDownload += (s, e) =>
            {
                channel.SendMessage($"Download complete!");
                Console.WriteLine("Download Complete");
                channel.SendMessage($"Now Playing: `{url}`!");
                PlayFile(voiceClient, filePath);
            };
            downloader.Download();

        }

        static void downloader_ProgressDownload(object sender, ProgressEventArgs e)
        {
            Console.WriteLine(e.Percentage);
        }

        public void PlayFile(IAudioClient ac, string path)
        {
            var process = Process.Start(new ProcessStartInfo
            { // FFmpeg requires us to spawn a process and hook into its stdout, so we will create a Process
                FileName = "ffmpeg",
                Arguments = $"-i {path} " +
                "-f s16le -ar 48000 -ac 2 pipe:1",
                UseShellExecute = false,
                RedirectStandardOutput = true
            });
            Thread.Sleep(200); // Sleep for a few seconds to FFmpeg can start processing data.

            int blockSize = 3840;
            byte[] buffer = new byte[blockSize];
            int byteCount;

            while (true)
            {
                byteCount = process.StandardOutput.BaseStream
                        .Read(buffer, 0, blockSize);

                if (byteCount == 0) // FFmpeg did not output anything
                    break; // Break out of the while(true) loop, since there was nothing to read.

                ac.Send(buffer, 0, byteCount);

            }
            ac.Wait(); // Wait for the Voice Client to finish sending data


        }


    }
}
