import easyocr

def convert_to_text(img):
    reader = easyocr.Reader(["en"])
    results = reader.readtext(img)
    return results

results = convert_to_text("ReactFolderStructure.png")

for item in results:
    print(item[1])
