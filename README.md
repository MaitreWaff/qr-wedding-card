# qr-wedding-card


This script helped me a lot, when facing a time constraint, preparing my weeding, I was in need to generate to the fly invitation card for my guess.

I used a python script that read an Excel file, and generate on the fly some QR Code with all needed information to identify guess and direct them toward
the table reserved for them

All credit goes to @MaitreWaff.


Python Version

Python 3.9.17


Pip List of Installed Packages

Package           Version
----------------- ------------
et-xmlfile        1.1.0
openpyxl          3.1.2
Pillow            9.5.0
pip               23.0.1
pypng             0.20220715.0
qrcode            7.4.2
setuptools        58.1.0
typing_extensions 4.7.1
wheel             0.40.0



Run the script

# git clone https://github.com/MaitreWaff/qr-wedding-card.git

# cd qr-wedding-card

# docker build . -t qrcodegen

On Windows
# docker run -it -v .\BilletsNumeriques:/usr/src/app/invits qrcodegen python /usr/src/app/qrCodeGenerator.py

On Linux or Mac

# docker run -it -v ./BilletsNumeriques:/usr/src/app/invits qrcodegen python /usr/src/app/qrCodeGenerator.py

This way, docker will create the container and execute the python script qrCodeGenerator.py.
The python code will look into the current folder for an excel file named "invitations.xlsx" and create all the QR Codes in the ./BilletsNumeriques folder.

# python ./qrCodeGenerator.py


docker build . -t waffoluc/qrcodegen

docker run -it -v ./invits:/usr/src/app/invits waffoluc/qrcodegen sh


# docker run -it -v ./invits:/usr/src/app/invits qrcodegen sh
# python qrCodeGenerator.py
/usr/src/app/qrCodeGenerator.py:20: DeprecationWarning: ANTIALIAS is deprecated and will be removed in Pillow 10 (2023-07-01). Use LANCZOS or Resampling.LANCZOS instead.
  logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
# exit
# ls -l invits
Guess 1-Faire-Part_Tedy_and_MaitreWaff.png
Guess VIP 1-Faire-Part_Tedy_and_MaitreWaff.png
MaitreWaff & Teedy-Faire-Part_Tedy_and_MaitreWaff.png
