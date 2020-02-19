
from consts import *

REPLACE_INTERNATIONAL_QWERTY = [
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
    }
]
