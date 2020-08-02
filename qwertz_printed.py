
from consts import *

QWERTZ_PRINTED = [

# ROW 1 ###############################################################
    {
        REPL_KEYCODE: "ESCAPE",
        REPLACE: [
            (BASE, r"fallback BACK"),
        ]
    },
    {
        REPL_KEYCODE: "1",
        REPLACE: [
            (BASE, r"'1'"),
            (FN, r"'!'"),
            (SHIFT, r"'!'"),
        ]
    },
    {
        REPL_KEYCODE: "2",
        REPLACE: [
            (BASE, r"'2'"),
            (FN, r"'\"'"),
            (SHIFT, r"'\"'"),
        ]
    },
    {
        REPL_KEYCODE: "3",
        REPLACE: [
            (BASE, r"'3'"),
            (FN, r"'\u00a7'"),
            (SHIFT, r"'\u00a7'"),
        ]
    },
    {
        REPL_KEYCODE: "4",
        REPLACE: [
            (BASE, r"'4'"),
            (FN, r"'$'"),
            (SHIFT, r"'$'"),
        ]
    },
    {
        REPL_KEYCODE: "5",
        REPLACE: [
            (BASE, r"'5'"),
            (FN, r"'%'"),
            (SHIFT, r"'%'"),
        ]
    },
    {
        REPL_KEYCODE: "6",
        REPLACE: [
            (BASE, r"'6'"),
            (FN, r"'&'"),
            (SHIFT, r"'&'"),
        ]
    },
    {
        REPL_KEYCODE: "7",
        REPLACE: [
            (BASE, r"'7'"),
            (FN, r"'/'"),
            (SHIFT, r"'/'"),
        ]
    },
    {
        REPL_KEYCODE: "8",
        REPLACE: [
            (BASE, r"'8'"),
            (FN, r"'('"),
            (SHIFT, r"'('"),
        ]
    },
    {
        REPL_KEYCODE: "9",
        REPLACE: [
            (BASE, r"'9'"),
            (FN, r"')'"),
            (SHIFT, r"')'"),
        ]
    },
    {
        REPL_KEYCODE: "0",
        REPLACE: [
            (BASE, r"'0'"),
            (FN, r"'='"),
            (SHIFT, r"'='"),
        ]
    },
    {
        REPL_KEYCODE: "MINUS",
        REPLACE: [
            (BASE, r"'\u00df'"),
            (FN, r"'?'"),
            (SHIFT, r"'\u1e9e'"),
            (CAPSLOCK, r"'\u1e9e'"),
        ]
    },
    {
        REPL_KEYCODE: "EQUALS",
        REPLACE: [
            (BASE, r"'\u0301'"),
            (FN, r"'\u0300'"),
            (SHIFT, r"'\u0300'"),
        ]
    },
# ROW 2 ###############################################################
    {
        REPL_KEYCODE: "TAB",
        REPLACE: [
            (BASE, r"'\t'"),
        ]
    },
    {
        REPL_KEYCODE: "Q",
        REPLACE: [
            (BASE, r"'q'"),
            (FN, r"'@'"),
            (SHIFT, r"'Q'"),
            (CAPSLOCK, r"'Q'"),
        ]
    },
    {
        REPL_KEYCODE: "W",
        REPLACE: [
            (BASE, r"'w'"),
            (FN, r"'\u0302'"),
            (SHIFT, r"'W'"),
            (CAPSLOCK, r"'W'"),
        ]
    },
    {
        REPL_KEYCODE: "E",
        REPLACE: [
            (BASE, r"'e'"),
            (FN, r"'\u20ac'"),
            (SHIFT, r"'E'"),
            (CAPSLOCK, r"'E'"),
        ]
    },
    {
        REPL_KEYCODE: "R",
        REPLACE: [
            (BASE, r"'r'"),
            (FN, r"'\u00b0'"),
            (SHIFT, r"'R'"),
            (CAPSLOCK, r"'R'"),
        ]
    },
    {
        REPL_KEYCODE: "T",
        REPLACE: [
            (BASE, r"'t'"),
            (SHIFT, r"'T'"),
            (CAPSLOCK, r"'T'"),
        ]
    },
    {
        REPL_KEYCODE: "Y",
        REPLACE: [
            (BASE, r"'y'"),
            (FN, r"'|'"),
            (SHIFT, r"'Y'"),
            (CAPSLOCK, r"'Y'"),
        ]
    },
    {
        REPL_KEYCODE: "U",
        REPLACE: [
            (BASE, r"'u'"),
            (FN, r"'{'"),
            (SHIFT, r"'U'"),
            (CAPSLOCK, r"'U'"),
        ]
    },
    {
        REPL_KEYCODE: "I",
        REPLACE: [
            (BASE, r"'i'"),
            (FN, r"'['"),
            (SHIFT, r"'I'"),
            (CAPSLOCK, r"'I'"),
        ]
    },
    {
        REPL_KEYCODE: "O",
        REPLACE: [
            (BASE, r"'o'"),
            (FN, r"']'"),
            (SHIFT, r"'O'"),
            (CAPSLOCK, r"'O'"),
        ]
    },
    {
        REPL_KEYCODE: "P",
        REPLACE: [
            (BASE, r"'p'"),
            (FN, r"'}'"),
            (SHIFT, r"'P'"),
            (CAPSLOCK, r"'P'"),
        ]
    },
    {
        REPL_KEYCODE: "GRAVE",
        REPLACE: [
            (BASE, r"'\u00fc'"),
            (FN, r"'\u0303'"),
            (SHIFT, r"'\u00dc'"),
            (CAPSLOCK, r"'\u00dc'"),
        ]
    },
    {
        REPL_KEYCODE: "SEMICOLON",
        REPLACE: [
            (BASE, r"'+'"),
            (FN, r"'*'"),
            (SHIFT, r"'*'"),
        ]
    },
# ROW 3 ###############################################################
    {
        REPL_KEYCODE: "A",
        REPLACE: [
            (BASE, r"'a'"),
            (SHIFT, r"'A'"),
            (CAPSLOCK, r"'A'"),
            #(LALT, r"'à'"),
        ]
    },
    {
        REPL_KEYCODE: "S",
        REPLACE: [
            (BASE, r"'s'"),
            (SHIFT, r"'S'"),
            (CAPSLOCK, r"'S'"),
            #(LALT, r"'ß'"),
        ]
    },
    {
        REPL_KEYCODE: "D",
        REPLACE: [
            (BASE, r"'d'"),
            (SHIFT, r"'D'"),
            (CAPSLOCK, r"'D'"),
        ]
    },
    {
        REPL_KEYCODE: "F",
        REPLACE: [
            (BASE, r"'f'"),
            (SHIFT, r"'F'"),
            (CAPSLOCK, r"'F'"),
        ]
    },
    {
        REPL_KEYCODE: "G",
        REPLACE: [
            (BASE, r"'g'"),
            (SHIFT, r"'G'"),
            (CAPSLOCK, r"'G'"),
        ]
    },
    {
        REPL_KEYCODE: "H",
        REPLACE: [
            (BASE, r"'h'"),
            (SHIFT, r"'H'"),
            (CAPSLOCK, r"'H'"),
        ]
    },
    {
        REPL_KEYCODE: "J",
        REPLACE: [
            (BASE, r"'j'"),
            (SHIFT, r"'J'"),
            (CAPSLOCK, r"'J'"),
        ]
    },
    {
        REPL_KEYCODE: "K",
        REPLACE: [
            (BASE, r"'k'"),
            (SHIFT, r"'K'"),
            (CAPSLOCK, r"'K'"),
        ]
    },
    {
        REPL_KEYCODE: "L",
        REPLACE: [
            (BASE, r"'l'"),
            (FN, r"'\''"),
            (SHIFT, r"'L'"),
            (CAPSLOCK, r"'L'"),
        ]
    },
    {
        REPL_KEYCODE: "BACKSLASH",
        REPLACE: [
            (BASE, r"'\u00f6'"),
            (FN, r"'\\'"),
            (SHIFT, r"'\u00d6'"),
            (CAPSLOCK, r"'\u00d6'"),
        ]
    },
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPLACE: [
            (BASE, r"'\u00e4'"),
            (FN, r"'#'"),
            (SHIFT, r"'\u00c4'"),
            (CAPSLOCK, r"'\u00c4'"),
        ]
    },
    {
        REPL_KEYCODE: "ENTER",
        REPLACE: [
            (BASE, r"'\n'"),
        ]
    },
# ROW 4 ###############################################################
    {
        REPL_KEYCODE: "LEFT_BRACKET",
        REPLACE: [
            (BASE, r"'<'"),
            (FN, r"'>'"),
            (SHIFT, r"'>'"),
        ]
    },
    {
        REPL_KEYCODE: "Z",
        REPLACE: [
            (BASE, r"'z'"),
            (SHIFT, r"'Z'"),
            (CAPSLOCK, r"'Z'"),
        ]
    },
    {
        REPL_KEYCODE: "X",
        REPLACE: [
            (BASE, r"'x'"),
            (SHIFT, r"'X'"),
            (CAPSLOCK, r"'X'"),
        ]
    },
    {
        REPL_KEYCODE: "C",
        REPLACE: [
            (BASE, r"'c'"),
            (SHIFT, r"'C'"),
            (CAPSLOCK, r"'C'"),
        ]
    },
    {
        REPL_KEYCODE: "V",
        REPLACE: [
            (BASE, r"'v'"),
            (SHIFT, r"'V'"),
            (CAPSLOCK, r"'V'"),
        ]
    },
    {
        REPL_KEYCODE: "B",
        REPLACE: [
            (BASE, r"'b'"),
            (SHIFT, r"'B'"),
            (CAPSLOCK, r"'B'"),
        ]
    },
    {
        REPL_KEYCODE: "N",
        REPLACE: [
            (BASE, r"'n'"),
            (SHIFT, r"'N'"),
            (CAPSLOCK, r"'N'"),
        ]
    },
    {
        REPL_KEYCODE: "M",
        REPLACE: [
            (BASE, r"'m'"),
            (FN, r"'\u00b5'"),
            (SHIFT, r"'M'"),
            (CAPSLOCK, r"'M'"),
        ]
    },
    {
        REPL_KEYCODE: "COMMA",
        REPLACE: [
            (BASE, r"','"),
            (FN, r"';'"),
            (SHIFT, r"';'"),
        ]
    },
    {
        REPL_KEYCODE: "PERIOD",
        REPLACE: [
            (BASE, r"'.'"),
            (FN, r"':'"),
            (SHIFT, r"':'"),
        ]
    },
    {
        REPL_KEYCODE: "RIGHT_BRACKET",
        REPLACE: [
            (BASE, r"'-'"),
            (FN, r"'_'"),
            (SHIFT, r"'_'"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_UP",
        REPLACE: [
        ]
    },
# ROW 5 ###############################################################
    {
        REPL_KEYCODE: "ASSIST", #SYM
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "SPACE",
        REPLACE: [
            (BASE, r"' '"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_LEFT",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "DPAD_DOWN",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "DPAD_RIGHT",
        REPLACE: [
        ]
    }

]


