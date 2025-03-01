# skype7-voicemail-listener
This is an attempt to build a Skype 7 interface to be able to listen to voicemails. The proposed steps would be the following
- Set up specific hostfiles that will redirect all Skype traffic to a destination machine
- Set up a destination machine w/ SSL termination
- On any login from the Skype client give a +OK (maybe save username?)
- Have "pending" messages that would be downloaded voicemails that could be played in the client

# Blogging
- https://www.unliterate.net/index.php/2022/10/02/listening-to-skype-voicemail-dat-files/
- https://www.unliterate.net/index.php/2024/04/30/still-trying-to-listen-to-skype-voicemails/

# How to Skype 7
Firstly I've done the following:
- Using [Oracle VM VirtualBox](https://www.virtualbox.org/) i've installed Windows XP SP3 in a virtualized environment
- Installed [Google Chrome 49.0.2623.112](https://archive.org/download/49.0.2623.112ChromeInstaller/49.0.2623.112_chrome_installer.exe) for downloading
- Installed [Skype skype_7.0.0.102](http://www.skaip.org/skype-7-0-0-102-for-windows) as my Client
- Installed [Wireshark 1.10.14](https://2.na.dl.wireshark.org/win32/all-versions/Wireshark-win32-1.10.14.exe) for packet inspection

and i've made sure that all of those programs run and happily execute.

# Setting up the Server
Currently this is what is in development. At this juncture we're at packet capture.

# Audio Codecs
Until the server routine is set up there will be attempts to containerize or convert source dat files using random software. This is a list of what's failed when attempted with the necessary software and/or codec:

| Codec | Application | Notes |
| --- | --- | --- |
| Signed 8-bit PCM | Audacity | Import -> Raw Data |
| Signed 16-bit PCM | Audacity | Import -> Raw Data |
| Signed 24-bit PCM | Audacity | Import -> Raw Data |
| Signed 32-bit PCM | Audacity | Import -> Raw Data |
| Unsigned 8-bit PCM | Audacity | Import -> Raw Data |
| 32-bit float | Audacity | Import -> Raw Data |
| 32-bit float | Audacity | Import -> Raw Data |
| U-Law | Audacity | Import -> Raw Data |
| A-Law | Audacity | Import -> Raw Data |
| GSM 6.10 | Audacity | Import -> Raw Data |
| 12-bit DWVW | Audacity | Import -> Raw Data |
| 16-bit DWVW | Audacity | Import -> Raw Data |
| 24-bit DWVW | Audacity | Import -> Raw Data |
| 16kbps NMS ADPCM | Audacity | Import -> Raw Data |
| 24kbps NMS ADPCM | Audacity | Import -> Raw Data |
| 32kbps NMS ADPCM | Audacity | Import -> Raw Data |
| dfpwm | ffmpeg | forced decoder |
| g722 | ffmpeg | forced decoder |
| g723_1 | ffmpeg | forced decoder |
| g729 | ffmpeg | forced decoder |
| gsm | ffmpeg | forced decoder |
| iLBC 20ms | ffmpeg | [Costas Katsavounidis](https://www.linkedin.com/pulse/sayhi-saved-audio-messages-ilbc-files-costas-katsavounidis/) |
| iLBC 20ms | ffmpeg | [Costas Katsavounidis](https://www.linkedin.com/pulse/sayhi-saved-audio-messages-ilbc-files-costas-katsavounidis/) |

Note that codecs for all attempts are configured as monaural, and sampling rates ~8k or bitrates around 8k/16k.
