# Qbit_Disable

A Python script that will pause qbittorrent torrents outside of the active hours and re-enable them during active hours


## Contents
* [How It Works](#How_It_Works)
* [Installation](#Installation)


## How It Works
Every 60 seconds a connection is made to the qbittorrent webapi, which requires the webUI to be enabled, then either pauses or resumes a torrent based on the hour.
With this implementation a torrent is allowed to connect and start downloading untill the 60 second check in which it will be paused untill active hours.
Also if the user manually pauses a torrent during active hours it will be overriden and resumed.
Confirmed to work only on Windows.


## Installation
### Manual Install  
 1. Extract .zip
 2. Open a CMD window
 3. Enter each command bellow
>       pip install pyyaml
>       pip install qbittorrent-api
 4. For autolaunch, create a shortcut of the client.pyw and insert into your startup folder
> “C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp”
 5. Open config.txt to configure the active hours and qbittorent crednetials/ IP address/ Port. 




