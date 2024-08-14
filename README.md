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

#### Using an AUR Helper
To install the script, run:
```bash
yay -S lmp
```
or
```bash
paru -S lmp
```
