import re

def eight_hex_to_six_hex(hex_str):
    regex = re.compile(r'^#([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})$')
    if not regex.match(hex_str): return ""
    transparency_modifier = (int(hex_str[7:9], 16)) / 255
    red = 255 - ((255 - int(hex_str[1:3], 16)) * transparency_modifier)
    green = 255 - ((255 - int(hex_str[3:5], 16)) * transparency_modifier)
    blue = 255 - ((255 - int(hex_str[5:7], 16)) * transparency_modifier)
    return ('#%02x%02x%02x' % (int(red), int(green), int(blue))).upper()

while True:
    in_hex = input("Enter an 8-digit hex color code in format \"#RDGRBLTP\", " +
                   "or hit Enter to exit: ")
    if in_hex == "": break
    out_hex = eight_hex_to_six_hex(in_hex)
    if out_hex == "": print("Invalid input, the input must be in format \"#RDGRBLTP\"")
    print("The corresponding 6-digit hex color (without transparency) code is", out_hex)
