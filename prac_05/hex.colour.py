COLOUR_TO_CODE = {"AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a", "AliceBlue": "#f0f8ff",
                "AlizarinCrimson": "#e32636", "Amarath": "#e52b50", "Amber": "#ffbf00",
                "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "Apricot": "#fbceb1",
                "Aqua": "#00ffff"}
print(COLOUR_TO_CODE)

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_TO_CODE.get(colour_name)}")
    colour_name = input("Enter a colour name: ")
