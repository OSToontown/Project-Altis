<img src="https://raw.githubusercontent.com/NormalNed/ToontownStride/master/resources/phase_3/etc/icon.ico" align="right" width="200"/>

# Toontown Stride
September build of Toontown Stride, that just works.

# ❓ What is Toontown Stride
Toontown Stride is a Community Focused Toontown Server. We are going to keep up this tradition finishing and polishing Toontown Stride for the community.
# 🔨 Setting Up

Support is currently being worked on for MacOS and Non Arch Based Linux Distros
## 💻 Windows

### Installing Panda
To get the source running you need to install the [Panda3D](https://github.com/NormalNed/ToontownStride/blob/master/Panda3D-1.11.0.exe) located in this repo.

### Installing Pip Dependencies
The next part is to get our Dependencies. To get them open a Command Prompt Window inside of the Toontown Stride folder and run
```bash
ppython -m pip install -r requirements.txt
```

### Running the Game
Now run the [Start.bat](Start.bat) file to launch the game.

## 🐧 Linux
### Gathering Basic Dependencies
##### Arch / Manjaro
```yay -S xorg-server  xterm  libgl  python  openssl  libjpeg  libpng  freetype2  gtk2  libtiff  nvidia-cg-toolkit  openal  zlib  libxxf86dga  assimp  bullet  eigen  ffmpeg  fmodex  libxcursor  libxrandr  git  opencv  libgles  libegl```

##### Debian / Ubuntu / Linux Mint
```sudo apt-get install build-essential xterm pkg-config fakeroot python-dev libpng-dev libjpeg-dev libtiff-dev zlib1g-dev libssl-dev libx11-dev libgl1-mesa-dev libxrandr-dev libxxf86dga-dev libxcursor-dev bison flex libfreetype6-dev libvorbis-dev libeigen3-dev libopenal-dev libode-dev libbullet-dev nvidia-cg-toolkit libgtk2.0-dev libassimp-dev libopenexr-dev```

### Getting Python 2

The First step to get this Source running is obtaining a version of Python 2. The Python we use is located [here](https://github.com/NormalNed/python) but feel free to use the one in your package manager (should be **python2**)

### Installing Pip

Once you get the Python installed you need to type these following commands to install Pip
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python2 get-pip.py
```

### Installing Pip Dependencies
The next part is to get our Dependencies. Open a Terminal inside of the Stride Project and follow these instructions below.
```bash
pip2.7 install -r requirements.txt
```

### Installing "our" Panda 3D
We use a version of Astron Panda3D that is upstream code from the main repo. To set it up follow these instructions

```bash
git clone https://github.com/NormalNed/panda3d.git
cd panda3d
python2 makepanda/makepanda.py --everything --installer --no-egl --no-gles --no-gles2 --no-opencv --threads=4
sudo python2 makepanda/installpanda.py
sudo ldconfig
```

### Running the Game
Now run the [Start.sh](Start.sh) file to launch the game.

# 📝 Notice

This repository contains code derived from the [BigNed repository.](https://github.com/BigNed/ToontownStride)

BigNed is operated by rocketprogrammer, toonjoey, Jeeperpretzel, and EliasTDev.

