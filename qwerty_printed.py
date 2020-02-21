
from consts import *

# Interrestingly it looks like we don't need to specify the capslock, weird.

REPLACE_PRINTED_QWERTY = [

# ROW 1 ###############################################################
    {
        REPL_KEYCODE: "1",
        REPLACE: [
            (BASE, r"'1'"),
            (FN, r"'!'"),
        ]
    },
    {
        REPL_KEYCODE: "2",
        REPLACE: [
            (BASE, r"'2'"),
            (FN, r"'@'"),
        ]
    },
    {
        REPL_KEYCODE: "3",
        REPLACE: [
            (BASE, r"'3'"),
            (FN, r"'#'"),
        ]
    },
    {
        REPL_KEYCODE: "4",
        REPLACE: [
            (BASE, r"'4'"),
            (FN, r"'$'"),
        ]
    },
    {
        REPL_KEYCODE: "5",
        REPLACE: [
            (BASE, r"'5'"),
            (FN, r"'%'"),
        ]
    },
    {
        REPL_KEYCODE: "6",
        REPLACE: [
            (BASE, r"'6'"),
            (FN, r"'\u0302'"),
        ]
    },
    {
        REPL_KEYCODE: "7",
        REPLACE: [
            (BASE, r"'7'"),
            (FN, r"'&'"),
        ]
    },
    {
        REPL_KEYCODE: "8",
        REPLACE: [
            (BASE, r"'8'"),
            (FN, r"'*'"),
        ]
    },
    {
        REPL_KEYCODE: "9",
        REPLACE: [
            (BASE, r"'9'"),
            (FN, r"'('"),
        ]
    },
    {
        REPL_KEYCODE: "0",
        REPLACE: [
            (BASE, r"'0'"),
            (FN, r"')'"),
        ]
    },
    {
        REPL_KEYCODE: "MINUS",
        REPLACE: [
            (BASE, r"'-'"),
            (FN, r"'_'"),
        ]
    },
    {
        REPL_KEYCODE: "EQUALS",
        REPLACE: [
            (BASE, r"'='"),
            (FN, r"'+'"),
        ]
    },
# ROW 2 ###############################################################
    {    
        REPL_KEYCODE: "TAB",
        REPLACE: [
            (BASE, r"'\t'"),
            (FN, r"replace APP_SWITCH"),
        ]
    },
    {    
        REPL_KEYCODE: "GRAVE",
        REPLACE: [
            (BASE, r"'`'"),
            (FN, r"'~'"),
        ]
    },
    {
        REPL_KEYCODE: "Q",
        REPLACE: [
            (BASE, r"'q'"),
            (SHIFT, r"'Q'"),
        ]
    },
    {
        REPL_KEYCODE: "W",
        REPLACE: [
            (BASE, r"'w'"),
            (SHIFT, r"'W'"),
        ]
    },
    {
        REPL_KEYCODE: "E",
        REPLACE: [
            (BASE, r"'e'"),
            (SHIFT, r"'E'"),
        ]
    },
    {
        REPL_KEYCODE: "R",
        REPLACE: [
            (BASE, r"'r'"),
            (SHIFT, r"'R'"),
        ]
    },
    {
        REPL_KEYCODE: "T",
        REPLACE: [
            (BASE, r"'t'"),
            (SHIFT, r"'T'"),
        ]
    },
    {
        REPL_KEYCODE: "Y",
        REPLACE: [
            (BASE, r"'y'"),
            (SHIFT, r"'Y'"),
        ]
    },
    {
        REPL_KEYCODE: "U",
        REPLACE: [
            (BASE, r"'u'"),
            (SHIFT, r"'U'"),
        ]
    },
    {
        REPL_KEYCODE: "I",
        REPLACE: [
            (BASE, r"'i'"),
            (SHIFT, r"'I'"),
        ]
    },
    {
        REPL_KEYCODE: "O",
        REPLACE: [
            (BASE, r"'o'"),
            (SHIFT, r"'O'"),
        ]
    },
    {
        REPL_KEYCODE: "P",
        REPLACE: [
            (BASE, r"'p'"),
            (FN, r"'/'"),
            (SHIFT, r"'P'"),
        ]
    },
    {
        REPL_KEYCODE: "SEMICOLON",
        REPLACE: [
            (BASE, r"';'"),
            (FN, r"':'"),
        ]
    },
# ROW 3 ###############################################################
    {    
        REPL_KEYCODE: "BACKSLASH",
        REPLACE: [
            (BASE, r"'\u005c'"),
            (FN, r"'|'"),
        ]
    },
    {
        REPL_KEYCODE: "A",
        REPLACE: [
            (BASE, r"'a'"),
            (SHIFT, r"'A'"),
            #(LALT, r"'à'"),
        ]
    },
    {
        REPL_KEYCODE: "S",
        REPLACE: [
            (BASE, r"'s'"),
            (SHIFT, r"'S'"),
            #(LALT, r"'ß'"),
        ]
    },
    {
        REPL_KEYCODE: "D",
        REPLACE: [
            (BASE, r"'d'"),
            (SHIFT, r"'D'"),
        ]
    },
    {
        REPL_KEYCODE: "F",
        REPLACE: [
            (BASE, r"'f'"),
            (SHIFT, r"'F'"),
        ]
    },
    {
        REPL_KEYCODE: "G",
        REPLACE: [
            (BASE, r"'g'"),
            (SHIFT, r"'G'"),
        ]
    },
    {
        REPL_KEYCODE: "H",
        REPLACE: [
            (BASE, r"'h'"),
            (SHIFT, r"'H'"),
        ]
    },
    {
        REPL_KEYCODE: "J",
        REPLACE: [
            (BASE, r"'j'"),
            (SHIFT, r"'J'"),
        ]
    },
    {
        REPL_KEYCODE: "K",
        REPLACE: [
            (BASE, r"'k'"),
            (SHIFT, r"'K'"),
        ]
    },
    {
        REPL_KEYCODE: "L",
        REPLACE: [
            (BASE, r"'l'"),
            (SHIFT, r"'L'"),
        ]
    },
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPLACE: [
            (BASE, r"'\''"),
            (FN, r"'\"'"),
            (SHIFT, r"'\u0301'"),            
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
            (BASE, r"'['"),
            (FN, r"'{'"),
        ]
    },
    {
        REPL_KEYCODE: "RIGHT_BRACKET",
        REPLACE: [
            (BASE, r"']'"),
            (FN, r"'}'"),
        ]
    },
    {
        REPL_KEYCODE: "Z",
        REPLACE: [
            (BASE, r"'z'"),
            (SHIFT, r"'Z'"),
        ]
    },
    {
        REPL_KEYCODE: "X",
        REPLACE: [
            (BASE, r"'x'"),
            (SHIFT, r"'X'"),
        ]
    },    
    {
        REPL_KEYCODE: "C",
        REPLACE: [
            (BASE, r"'c'"),
            (SHIFT, r"'C'"),
        ]
    },
    {
        REPL_KEYCODE: "V",
        REPLACE: [
            (BASE, r"'v'"),
            (SHIFT, r"'V'"),
        ]
    },
    {
        REPL_KEYCODE: "B",
        REPLACE: [
            (BASE, r"'b'"),
            (SHIFT, r"'B'"),
        ]
    },
    {
        REPL_KEYCODE: "N",
        REPLACE: [
            (BASE, r"'n'"),
            (SHIFT, r"'N'"),
        ]
    },
    {
        REPL_KEYCODE: "M",
        REPLACE: [
            (BASE, r"'m'"),
            (SHIFT, r"'M'"),
        ]
    },
    {
        REPL_KEYCODE: "COMMA",
        REPLACE: [
            (BASE, r"','"),
            (FN, r"'<'"),
        ]
    },
    {
        REPL_KEYCODE: "PERIOD",
        REPLACE: [
            (BASE, r"'.'"),
            (FN, r"'>'"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_UP",
        REPLACE: [
        ]
    },
# ROW 5 ###############################################################
    {    
        REPL_KEYCODE: "SPACE",
        REPLACE: [
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


