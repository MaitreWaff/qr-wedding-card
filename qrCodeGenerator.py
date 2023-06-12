import qrcode
import openpyxl

from openpyxl import Workbook, load_workbook
from PIL import Image

def qrCodeGenerate(nom, place, table, theme):

    mrs = "MaitreWaff"
    miss = "Teedy"

    Logo_link = 'lovers.jpg'

    logo = Image.open(Logo_link)

    basewidth = 100

    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    logo = logo.resize((512, 512), Image.LANCZOS)


    features = qrcode.QRCode(version=1, 
                             error_correction=qrcode.constants.ERROR_CORRECT_H,
                             box_size=40, 
                             border=3)


    features.add_data(f"*********************************************")
    features.add_data("\n")
    features.add_data(f"      Welcome to the Weeding of      ")
    features.add_data("\n")
    features.add_data(f"            {miss} & {mrs}            ")
    features.add_data("\n")
    features.add_data(f"*********************************************")
    features.add_data("\n")
    features.add_data(">> Billet d'Invitation Pour <<")
    features.add_data("\n")
    features.add_data(f" - Name: {nom}")
    features.add_data("\n")
    features.add_data(f" - Table: {table}")
    features.add_data("\n")
    features.add_data(f" - Places: {place}")
    features.add_data("\n")
    features.add_data(f" - Them: {theme}")
    features.add_data("\n")
    features.add_data(f" - Location: Banquet Place Details")

    features.make(fit=True)


    QRcolor = (64, 224, 208)
    generate_image = features.make_image(fill_color=QRcolor, back_color="black").convert('RGB')

    pos = ((generate_image.size[0] - logo.size[0]) // 2,
           (generate_image.size[1] - logo.size[1]) // 2)
    
    generate_image.paste(logo, pos)

    generate_image.save(f"invits/{nom}-Faire-Part_Tedy_and_MaitreWaff.png")


def main():
    book = load_workbook('invitations.xlsx')

    sheet = book.active


    rows = sheet.rows

    headers = [cell.value for cell in next(rows)]

    all_rows = []


    for row in rows:
        data = {}
        for title, cell in zip(headers, row):
            data[title] = cell.value
        
        all_rows.append(data)

    for row in all_rows:
        if row['Noms'] is not None:
            qrCodeGenerate(row['Noms'], row['Nbre de places'], row['Table'], row['Theme'])


main()