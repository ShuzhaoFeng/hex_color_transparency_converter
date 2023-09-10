import re

eight_digit_hex = re.compile(r'^#([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})$')
six_digit_hex = re.compile(r'^#([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})([0-9A-Fa-f]{2})$')


class InvalidBackground:
    pass


def convert(foreground, background):

    background_red = int(background[1:3], 16)
    background_green = int(background[3:5], 16)
    background_blue = int(background[5:7], 16)

    foreground_red = int(foreground[1:3], 16)
    foreground_green = int(foreground[3:5], 16)
    foreground_blue = int(foreground[5:7], 16)

    foreground_alpha = (int(foreground[7:9], 16)) / 255

    out_red = (1 - foreground_alpha) * background_red + foreground_alpha * foreground_red
    out_green = (1 - foreground_alpha) * background_green + foreground_alpha * foreground_green
    out_blue = (1 - foreground_alpha) * background_blue + foreground_alpha * foreground_blue

    return ('#%02x%02x%02x' % (int(out_red), int(out_green), int(out_blue))).upper()


def run():
    try:
        background_color = input("To set the background color, enter an 8-digit hex color code in format" +
                                 "\"#RDGRBL\", or hit enter to leave it as default (#FFFFFF): ")

        if background_color == "":
            background_color = "#FFFFFF"
        elif not six_digit_hex.match(background_color):
            print("Invalid input, the input must be in format \"#RDGRBL\"")
            raise InvalidBackground

        while True:
            foreground_color = input("Enter an 8-digit hex color code in format \"#RDGRBLTP\", " +
                                     "or hit Enter to exit: ")

            if foreground_color == "":
                break

            if not eight_digit_hex.match(foreground_color):
                print("Invalid input, the input must be in format \"#RDGRBLTP\"")

            out = convert(foreground_color, background_color)

            print("The corresponding 6-digit hex color code is", out)
    except InvalidBackground:
        run()


run()
