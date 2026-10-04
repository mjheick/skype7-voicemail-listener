# skype7-voicemail-listener
A script derived from Claude Sonnet 5.5 that converts Skype 7 Voicemail .dat files to playable wav.

# Usage
Clone down the repo
```
git@github.com:mjheick/skype7-voicemail-listener.git
```

Execute the program
```
python3 dat_to_wav.py file1.dat [file2.dat ...]
```

# ffmpeg
You'll need [ffmpeg](https://ffmpeg.org/) installed (and present in your path) to make the final conversion from g.729 to PCM format.

You can download that from [ffmpeg.org](https://ffmpeg.org/download.html)

# Historical Walk
- [Listening to Skype Voicemail .dat files](https://www.unliterate.net/index.php/2022/10/02/listening-to-skype-voicemail-dat-files/)
- [Still trying to listen to Skype Voicemails…](https://www.unliterate.net/index.php/2024/04/30/still-trying-to-listen-to-skype-voicemails/)
- [Decoding and Listening to Skype Voicemail .dat Files]()

# Thanks
- Scott Nickell <scott.nickell@gmail.com>

