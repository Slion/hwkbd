
from consts import *

REPLACE_INTERNATIONAL_QWERTY = [
    # ROW 1 ###############################################################
    {    
        REPL_KEYCODE: "1",
        REPLACE: [
            (SHIFT,r"'\u00a1'"),            
            (LALT, r"'\u00b9'")
        ]
    },
    {
        REPL_KEYCODE: "2",
        REPLACE: [
            (SHIFT,r"'\u00b2'"),            
            (LALT, r"'\u030b'")
        ]
    },
    {
        REPL_KEYCODE: "3",
        REPLACE: [
            (SHIFT,r"'\u00b3'"),            
            (LALT, r"'\u0304'")
        ]
    },
    {
        REPL_KEYCODE: "4",
        REPLACE: [
            (SHIFT,r"'\u00a4'"),            
            (LALT, r"'\u00a3'")
        ]
    },
    {
        REPL_KEYCODE: "5",
        REPLACE: [
            (SHIFT,r"'\u20ac'"),            
            (LALT, r"'\u0327'")
        ]
    },
    {
        REPL_KEYCODE: "6",
        REPLACE: [
            (SHIFT,r"'\u00bc'"),            
            (LALT, r"'^'")
        ]
    },
    {
        REPL_KEYCODE: "7",
        REPLACE: [
            (SHIFT,r"'\u00bd'"),            
            (LALT, r"'\u031b'")
        ]
    },
    {
        REPL_KEYCODE: "8",
        REPLACE: [
            (SHIFT,r"'\u00be'"),            
            (LALT, r"'\u0328'")
        ]
    },
    {
        REPL_KEYCODE: "9",
        REPLACE: [
            (SHIFT,r"'\u2018'"),            
            (LALT, r"'\u0306'")
        ]
    },
    {
        REPL_KEYCODE: "0",
        REPLACE: [
            (SHIFT,r"'\u2019'"),            
            (LALT, r"'\u030a'")
        ]
    },
    {
        REPL_KEYCODE: "MINUS",
        REPLACE: [
            (SHIFT,r"'\u00a5'"),            
            (LALT, r"'\u0323'")
        ]
    },
    {
        REPL_KEYCODE: "EQUALS",
        REPLACE: [
            (SHIFT,r"'\u00d7'"),            
            (LALT, r"'\u00f7'")
        ]
    },
    # ROW 2 ###############################################################
    {    
        REPL_KEYCODE: "TAB",
        REPLACE: [
            (LALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "GRAVE",
        REPLACE: [
            (SHIFT,r"'\u0303'"), # ~
            (LALT, r"'\u0300'"),            
        ]
    },
    {
        REPL_KEYCODE: "Q",
        REPLACE: [
            (LALT, r"'\u00c4'"),
            (SHIFT_LALT, r"'\u00e4'"),            
        ]
    },
    {
        REPL_KEYCODE: "W",
        REPLACE: [
            (LALT, r"'\u00c5'"),
            (SHIFT_LALT, r"'\u00e5'"),
        ]
    },
    {
        REPL_KEYCODE: "E",
        REPLACE: [
            (LALT, r"'\u00e9'"), # é            
            (SHIFT_LALT, r"'\u00c9'"), # É
            (FN, r"'\u0301'"), # Dead ́           
        ]
    },
    {
        REPL_KEYCODE: "R",
        REPLACE: [
            (FN, r"'\u00a4'"),
            (LALT, r"'\u00a4'"),
        ]
    },
    {
        REPL_KEYCODE: "T",
        REPLACE: [
            (FN, r"'\u00c4'"),
            (LALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "Y",
        REPLACE: [
            (FN, r"'\u00c4'"),
            (LALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "U",
        REPLACE: [
            (FN, r"'\u00c4'"),
            (LALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "I",
        REPLACE: [
            (FN, r"'\u00c4'"),
            (LALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "O",
        REPLACE: [
            (FN, r"'\u00c4'"),
            (LALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "P",
        REPLACE: [
            (FN, r"'\u00c4'"),
            (LALT, r"none"),
        ]
    },
    {
        REPL_KEYCODE: "SEMICOLON",
        REPLACE: [
            (FN, r"'\u00c4'"),
            (LALT, r"none"),
        ]
    },

]

