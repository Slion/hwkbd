
from consts import *

QWERTY_ALT = [

# ROW 1 ###############################################################
    {
        REPL_KEYCODE: "1",
        REPLACE: [
            #(FN, r"'!'"),
        ]
    },
    {
        REPL_KEYCODE: "2",
        REPLACE: [
            #(FN, r"'@'"),
        ]
    },
    {
        REPL_KEYCODE: "3",
        REPLACE: [
            #(FN, r"'#'"),
        ]
    },
    {
        REPL_KEYCODE: "4",
        REPLACE: [
            #(FN, r"'$'"),
            (LALT, r"'\u20AC'"), # €
        ]
    },
    {
        REPL_KEYCODE: "5",
        REPLACE: [
            #(FN, r"'%'"),
        ]
    },
    {
        REPL_KEYCODE: "6",
        REPLACE: [
            # Circumflex accent dead key 
            (LALT, r"'\u0302'"),
        ]
    },
    {
        REPL_KEYCODE: "7",
        REPLACE: [
            #(FN, r"'&'"),
            (LALT, r"'\u00A3'"), # £
        ]
    },
    {
        REPL_KEYCODE: "8",
        REPLACE: [
            #(FN, r"'*'"),
        ]
    },
    {
        REPL_KEYCODE: "9",
        REPLACE: [
            #(FN, r"'('"),
        ]
    },
    {
        REPL_KEYCODE: "0",
        REPLACE: [
            #(FN, r"')'"),
        ]
    },
    {
        REPL_KEYCODE: "MINUS",
        REPLACE: [
            #(FN, r"'_'"),
        ]
    },
    {
        REPL_KEYCODE: "EQUALS",
        REPLACE: [
            #(FN, r"'+'"),
        ]
    },
# ROW 2 ###############################################################
    {    
        REPL_KEYCODE: "TAB",
        REPLACE: [
        ]
    },
    {    
        REPL_KEYCODE: "GRAVE",
        REPLACE: [           
            # Grave accent dead key 
            (LALT, r"'\u0300'"),
        ]
    },
    {
        REPL_KEYCODE: "Q",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "W",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "E",
        REPLACE: [
            (LALT, r"'\u00E8'"), # è
        ]
    },
    {
        REPL_KEYCODE: "R",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "T",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "Y",
        REPLACE: [
            (LALT, r"'\u00A5'"), # ¥        
        ]
    },
    {
        REPL_KEYCODE: "U",
        REPLACE: [
            # Umlaut dead key 
            (LALT, r"'\u0308'"),
        ]
    },
    {
        REPL_KEYCODE: "I",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "O",
        REPLACE: [
            (LALT, r"'\u0153'"), # œ
        ]
    },
    {
        REPL_KEYCODE: "P",
        REPLACE: [
            #(FN, r"'/'"),
        ]
    },
    {
        REPL_KEYCODE: "SEMICOLON",
        REPLACE: [
            #(FN, r"':'"),
        ]
    },
# ROW 3 ###############################################################
    {    
        REPL_KEYCODE: "BACKSLASH",
        REPLACE: [
            #(FN, r"'|'"),
        ]
    },
    {
        REPL_KEYCODE: "A",
        REPLACE: [            
            (LALT, r"'\u00E6'"), # æ
        ]
    },
    {
        REPL_KEYCODE: "S",
        REPLACE: [
            # ß
            (LALT, r"'\u00df'"),
        ]
    },
    {
        REPL_KEYCODE: "D",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "F",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "G",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "H",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "J",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "K",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "L",
        REPLACE: [
            #(FN, r"'?'"),
        ]
    },
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPLACE: [
            #(FN, r"'\"'"),
            # Accute accent dead key 
            (LALT, r"'\u0301'"),
        ]
    },
    {
        REPL_KEYCODE: "ENTER",
        REPLACE: [
        ]
    },
# ROW 4 ###############################################################
    {    
        REPL_KEYCODE: "LEFT_BRACKET",
        REPLACE: [
            #(FN, r"'{'"),
        ]
    },
    {
        REPL_KEYCODE: "RIGHT_BRACKET",
        REPLACE: [
            #(FN, r"'}'"),
        ]
    },
    {
        REPL_KEYCODE: "Z",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "X",
        REPLACE: [
        ]
    },    
    {
        REPL_KEYCODE: "C",
        REPLACE: [
            # ç
            (LALT, r"'\u00E7'"),
        ]
    },
    {
        REPL_KEYCODE: "V",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "B",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "N",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "M",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "COMMA",
        REPLACE: [
            #(FN, r"'<'"),
        ]
    },
    {
        REPL_KEYCODE: "PERIOD",
        REPLACE: [
            #(FN, r"'>'"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_UP",
        REPLACE: [
            (LALT, r"replace BRIGHTNESS_UP"),
        ]
    },
# ROW 5 ###############################################################
    {    
        REPL_KEYCODE: "ASSIST", #SYM
        REPLACE: [
            # Consume for digit characters and output corresponding unicode 
            (LALT, r"'\uef00'"),
        ]
    },    
    {    
        REPL_KEYCODE: "SPACE",
        REPLACE: [
        ]
    },
    {
        REPL_KEYCODE: "DPAD_LEFT",
        REPLACE: [
            (LALT, r"replace BACK"),            
        ]
    },
    {
        REPL_KEYCODE: "DPAD_DOWN",
        REPLACE: [
            (LALT, r"replace BRIGHTNESS_DOWN"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_RIGHT",
        REPLACE: [
            (LALT, r"replace FORWARD"),
        ]
    }

]


