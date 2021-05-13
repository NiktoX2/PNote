# note-pythone

Библиотека PyQt5 > pip install PyQt5\
Для упаковки использовались pyinstaller > pip install pyinstaller\
Упаковка\
pyinstaller -D -F -w Note.py ^ \
--exclude-module _bz2 ^ \
--exclude-module _decimal ^ \
--exclude-module _hashlib ^ \
--exclude-module _lzma ^ \
--exclude-module _socket ^ \
--exclude-module asyncio ^ \
--exclude-module email ^ \
--exclude-module xml ^ \
--exclude-module xmlrpc ^ \
--exclude-module html ^ \
--exclude-module http ^ \
--exclude-module logging ^ \
--exclude-module pydoc_data ^ \
--exclude-module test ^ \
--exclude-module tkinter ^ \
--exclude-module unittest ^ \
--exclude-module urllib \
Пазмер > 32Mb
