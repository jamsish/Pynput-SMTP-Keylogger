Demo only! Do not use for malicious purposes, obviously.

Put home.ico and RealAzzSpoofPublic into a folder together and build into an exe using PyInstaller with this prompt in a terminal:

py -m PyInstaller --clean --noconfirm --onefile --windowed --icon=home.ico --add-data "home.ico;." RealAzzSpoofPublic.py   

Made by jamsish
