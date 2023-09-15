import easyocr

def convert_to_text(img):
    reader = easyocr.Reader(["en"])
    results = reader.readtext(img)
    return results

img = "ReactFolderStructure.png"
results = convert_to_text(img)

for item in results:
    print(item[1])
