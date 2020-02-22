
from consts import *

QWERTY_FN_CUSTOM = [

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
            #(FN, r"'^'"),
        ]
    },
    {
        REPL_KEYCODE: "7",
        REPLACE: [
            #(FN, r"'&'"),
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
            (FN, r"replace APP_SWITCH"),
        ]
    },
    {    
        REPL_KEYCODE: "GRAVE",
        REPLACE: [
            #(FN, r"'~'"),
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
        ]
    },
    {
        REPL_KEYCODE: "U",
        REPLACE: [
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
            #(LALT, r"'à'"),
        ]
    },
    {
        REPL_KEYCODE: "S",
        REPLACE: [
            #(LALT, r"'ß'"),
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
            (FN, r"replace PAGE_UP"),
        ]
    },
# ROW 5 ###############################################################
    {    
        REPL_KEYCODE: "ASSIST", #SYM
        REPLACE: [
            # Open Symbol dialog
            (FN, r"'\uef01'"),
        ]
    },    
    {    
        REPL_KEYCODE: "SPACE",
        REPLACE: [
            # Easy way to turn keyboard backlight back on
            (FN, r"replace F6"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_LEFT",
        REPLACE: [
            (FN, r"replace MOVE_HOME"),            
        ]
    },
    {
        REPL_KEYCODE: "DPAD_DOWN",
        REPLACE: [
            (FN, r"replace PAGE_DOWN"),
        ]
    },
    {
        REPL_KEYCODE: "DPAD_RIGHT",
        REPLACE: [
            (FN, r"replace MOVE_END"),
        ]
    }

]


