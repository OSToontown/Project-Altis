using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Discord;
using Discord.Commands;

namespace discordCSBOT
{
    class FunCommands
    {

        public void Start(DiscordClient bot)
        {

 // :(
        }


        // generate a random number xd
        private int RandomNumber(int min, int max)
        {
            Random random = new Random();
            return random.Next(min, max);
        }
    }
}
