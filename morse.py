import sys
import argparse

def get_morse_code(char):
    code = {
        "A": '.-',
        "J": '.--- ',
        "S": '...',
        "B": '-...',
        "K": '-.-',
        "T": '-',
        "C": '-.-.',
        "L": '.-..',
        "U": '..-',
        "D": '-..',
        "M": '--',
        "V": "...-",
        "E": ".",
        "N": "-.",
        "W": ".--",
        "F": "..-.",
        "O": "---",
        "X": "-..-",
        "G": "--.",
        "P": ".--.",
        "Y": "-.--",
        "H": "....",
        "Q": "--.-",
        "Z": '--..',
        "I": '..',
        'R': '.-.',
    }
    try:
        return code[char]
    except KeyError:
        return ''


def get_text(fname):
    with open(fname) as fhandle:
        text = [line for line in fhandle]
    return text


def change_line_to_morse(text: str):
    result = ''
    text = text.upper()
    splitted_text = text.split()
    for word in splitted_text:
        for letter in word:
            code = get_morse_code(letter)
            result += code
            if code != '':
                result += ' '
        if any([letter.isalpha() for letter in word]):
                result += '/ '
    return result[:-3]


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE')
    args = parser.parse_args(arguments[1:])
    fname = args.FILE
    translated = []
    for line in get_text(fname):
        translated.append(change_line_to_morse(line))
    for line in translated:
        print(line)


if __name__ == "__main__":
    main(sys.argv)
