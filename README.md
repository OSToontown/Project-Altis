<img src="https://raw.githubusercontent.com/NormalNed/Project-Altis/53168140c5b29f018467bedec35b4e59a83d0609/resources/phase_3.5/etc/transicon.png" align="right" width="200"/>

# Project Altis
Project Altis Beta Source, that just works.

# ❓ What is Project Altis
Project Altis is a Private Server Aimee around adding a crap ton of new features. We are going to keep up this tradition finishing and polishing up Altis for the community.
This project is not related to Corporate Clash. We simply are porting the Altis Codebase and continuing it not adding everything clash did.

# 🔨 Setting Up
Support is currently being worked on for MacOS and Non Arch Based Linux Distros

## 💻 Windows
Run the [Start.bat](Start.bat) file to launch the game.

## 🐧 Linux
### Gathering Basic Dependencies
##### Arch / Manjaro
```yay -S xorg-server  xterm  libgl  python  openssl  libjpeg  libpng  freetype2  gtk2  libtiff  nvidia-cg-toolkit  openal  zlib  libxxf86dga  assimp  bullet  eigen  ffmpeg  fmodex  libxcursor  libxrandr  git  opencv  libgles  libegl```

##### Debian / Ubuntu / Linux Mint
```sudo apt-get install build-essential xterm pkg-config fakeroot python-dev libpng-dev libjpeg-dev libtiff-dev zlib1g-dev libssl-dev libx11-dev libgl1-mesa-dev libxrandr-dev libxxf86dga-dev libxcursor-dev bison flex libfreetype6-dev libvorbis-dev libeigen3-dev libopenal-dev libode-dev libbullet-dev nvidia-cg-toolkit libgtk2.0-dev libassimp-dev libopenexr-dev mongodb libboost-dev libyaml-cpp-dev```

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
