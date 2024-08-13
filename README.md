# lmp
A lightweight media player script

## About
The Lightweight Media Player is a CLI script that allows you to browse a media directory using an enumerated directory list. You can customize a number of things in this script including what media player is used to open your file. 

## Usage
### Running
To initialize the script, run:
```bash
lmp
```

### Configuration
By default, the configuration file is stored in ```/etc/lmp/``` as ```lmp.conf```. The configuration file is parsed as an ```ini``` configuartion format with all options under the ```[general]``` tag.

#### Options:
|Option|Type|Default value|Description|
|-|-|-|-|
|```media_path```|```str```|```$HOME/media```|Defines the root directory o your media catalog|
|```media_player```|```str```|```mpv```|Defines your choice of media player|
|```home_symbol```|```str```|```##```|Defines the root directory shorthand|
|```char_cutoff```|```int```|```10```|Defines character cutoff for deeply nested directories|

## Installation

### Arch-based Distros

#### Using ```makepkg```
1. Clone the repositiory by running:
```bash
git clone https://github.com/derekporcelli/lmp.git
```
or
```bash
git clone git@github.com:derekporcelli/lmp.git
```
2. Move into the directory by running:
```bash
cd lmp
```
3. Install the package by running:
```bash
makepkg -si
``` 

#### Using ```pacman```

```bash
git clone https://github.com/derekporcelli/lmp.git
```
or
```bash
git clone git@github.com:derekporcelli/lmp.git
```
2. Move into the directory by running:
```bash
cd lmp
```
3. Install the package by running:
```bash
pacman -U lmp-<version>-x86_64.pkg.tar.zst
``` 