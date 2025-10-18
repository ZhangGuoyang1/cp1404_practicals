COLOR_TO_CODE = {"Amber": "#ffbf00", "Aqua": "#00ff00", "Baby Blue": "#89cff0", "Black": "#000000", "Canary": "#ffff99",
                "Bistro":"#3d2b1f", "Bitter Lime": "#bfff00", "Blond": "#faf0be", "Burgundy": "#800020", "Camel": "#c19a6b",}

print(COLOR_TO_CODE)
colour_name = input("Enter colour name:").title()
while colour_name != "":
    try:
        print(colour_name, "is", COLOR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name:").title()
