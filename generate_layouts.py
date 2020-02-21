#!/usr/bin/python3

# This is called automatically by the build process to generate some
# layouts that are similar to other layouts.

import os
import pathlib
import sys


# Imports
from consts import *
from qwerty_printed import *
from qwerty_fx import *
from qwerty_fn import *
from qwerty_fn_custom import *
from qwerty_international import *


#
SWAP_ALT_FN = r"""
# Swap alt and fn
# Alt is now Fn
map key 464 ALT_LEFT
# Fn is now Alt
map key 56 FUNCTION
"""

DAN_SWE_REPLACE = [
    ("æ", "ö"),
    ("u00e6", "u00f6"),
    ("Æ", "Ö"),
    ("u00c6", "u00d6"),
    ("ø", "ä"),
    ("u00f8", "u00e4"),
    ("Ø", "Ä"),
    ("u00d8", "u00c4"),
]

DAN_NOR_REPLACE = [
    ("æ", "ø"),
    ("u00e6", "u00f8"),
    ("Æ", "Ø"),
    ("u00c6", "u00d8"),
    ("ø", "æ"),
    ("u00f8", "u00e6"),
    ("Ø", "Æ"),
    ("u00d8", "u00c6"),
]



USINTL_ALTGR_REPLACE_APOSTROPHE = [
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPL_OLD: r"'\''",
        REPL_NEW: r"'\u0301'",
        REPL_SKIP: ["alt:", "label:"],
    },
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPL_OLD: "'\"'",
        REPL_NEW: r"'\u0308'",
        REPL_SKIP: ["alt:", "label:"],
    },
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPL_OLD: r"'\u0301'",
        REPL_NEW: r"'\''",
        REPL_SKIP: ["alt:", "label:"],
    },
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPL_OLD: r"'\u0308'",
        REPL_NEW: "'\"'",
        REPL_SKIP: ["alt:", "label:"],
    },
]

USINTL_ALTGR_REPLACE_GRAVE = [
    {
        REPL_KEYCODE: "GRAVE",
        REPL_OLD: r"'`'",
        REPL_NEW: r"'\u0300'",
        REPL_SKIP: ["alt:", "label:"],
    },
    {
        REPL_KEYCODE: "GRAVE",
        REPL_OLD: "'~'",
        REPL_NEW: r"'\u0303'",
        REPL_SKIP: ["alt:", "label:"],
    },
    {
        REPL_KEYCODE: "GRAVE",
        REPL_OLD: r"'\u0300'",
        REPL_NEW: r"'`'",
        REPL_SKIP: ["alt:", "label:"],
    },
    {
        REPL_KEYCODE: "GRAVE",
        REPL_OLD: r"'\u0303'",
        REPL_NEW: "'~'",
        REPL_SKIP: ["alt:", "label:"],
    },
]

USINTL_ALTGR_FN_REPLACE_APOSTROPHE = [
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPL_OLD: r"'\''",
        REPL_NEW: r"'\u0301'",
        REPL_SKIP: ["fn:", "label:"],
    },
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPL_OLD: "'\"'",
        REPL_NEW: r"'\u0308'",
        REPL_SKIP: ["alt:", "label:"],
    },
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPL_OLD: r"'\u0301'",
        REPL_NEW: r"'\''",
        REPL_SKIP: ["fn:", "label:"],
    },
    {
        REPL_KEYCODE: "APOSTROPHE",
        REPL_OLD: r"'\u0308'",
        REPL_NEW: "'\"'",
        REPL_SKIP: ["fn:", "label:"],
    },
]

USINTL_ALTGR_FN_REPLACE_GRAVE = [
    {
        REPL_KEYCODE: "GRAVE",
        REPL_OLD: r"'`'",
        REPL_NEW: r"'\u0300'",
        REPL_SKIP: ["fn:", "label:"],
    },
    {
        REPL_KEYCODE: "GRAVE",
        REPL_OLD: "'~'",
        REPL_NEW: r"'\u0303'",
        REPL_SKIP: ["alt:", "label:"],
    },
    {
        REPL_KEYCODE: "GRAVE",
        REPL_OLD: r"'\u0300'",
        REPL_NEW: r"'`'",
        REPL_SKIP: ["fn:", "label:"],
    },
    {
        REPL_KEYCODE: "GRAVE",
        REPL_OLD: r"'\u0303'",
        REPL_NEW: "'~'",
        REPL_SKIP: ["fn:", "label:"],
    },
]

USINTL_SWAP_ALT_FN = [
    ("lalt", "fn"),
    ("fn", "lalt")
]


USINTL_POL_PROG_REPLACE = [
    ("u00e9", "u0119"),  # é to ę
    ("u00c9", "u0118"),  # É to Ę
    ("u00e1", "u0105"),  # á to ą
    ("u00c1", "u0104"),  # Á to Ą
    {
        REPL_KEYCODE: "S",
        REPL_OLD: r"'\u00df'",
        REPL_NEW: r"'\u015b'",
        REPL_SKIP: ["alt:"],
    },  # ß to ś (except on alt modifier)
    ("u00a7", "u015a"),  # § to Ś
    ("u00f8", "u0142"),  # ø to ł
    ("u00d8", "u0141"),  # Ø to Ł
    ("u00e6", "u017c"),  # æ to ż
    ("u00c6", "u017b"),  # Æ to Ż
    ("u00a9", "u0107"),  # © to ć
    ("u00a2", "u0106"),  # ¢ to Ć
    ("u00f1", "u0144"),  # ñ to ń
    ("u00d1", "u0143"),  # Ñ to Ń
]

GENERATED_LAYOUTS = [
    {
        # Process our printed template expanding Fx characters
        INPUT: "pro1_qwerty_template.kcm",
        OUTPUT: "pro1_qwerty_us.kcm",                
        REPLACE:    REPLACE_PRINTED_QWERTY+
                    QWERTY_FN_PRINTED+
                    QWERTY_FN_CUSTOM+
                    REPLACE_FX_QWERTY+
                    CLEANUP_TEMPLATE,
        ADD: REMAP_FX                    
    },

    #{
        # Swap alt and fn modifiers to enable alt+tab task switching using fn hardware key
    #    INPUT: "pro1_qwerty_international.kcm",
    #    OUTPUT: "pro1_qwerty_international_swapped.kcm",        
    #    IS_SOURCE_GENERATED: True,
    #    REPLACE: USINTL_SWAP_ALT_FN,
    #    REMOVE_KEYCODES: ["TAB"],                 
    #    ADD: SWAP_ALT_FN
    #}    
]

def expand_replacement(rule):
    if isinstance(rule, tuple):
        return {REPL_OLD: rule[0], REPL_NEW: rule[1]}
    return rule

def generate_layout(layout, target_dir):
    pathlib.Path(target_dir).mkdir(parents=True, exist_ok=True)
    layout_dir = os.path.join(os.path.dirname(__file__), "app", "src", "main", "res", "raw")
    source_dir = target_dir if layout.get(IS_SOURCE_GENERATED) else layout_dir
    with \
    open(os.path.join(source_dir, layout[INPUT]), 'r') as src, \
    open(os.path.join(target_dir, layout[OUTPUT]), 'w', encoding="utf-8") as dst:
        remove_this_key = False
        cur_keycode = None
        rules_matched = {KEYCODE_REPLACE: [], REPLACE: [], REMOVE_SCANCODES: [], REMOVE_KEYCODES: []}
        # For each line in our source
        for line in src:
            # Remove lines until we find the next closing curly bracket
            if remove_this_key:
                if line.startswith('}'):
                    remove_this_key = False
                # skip this key
                continue

            # Reset current key code whenever we find a closing curly backet
            if line.startswith('}'):
                cur_keycode = None

            # Comment out specified scan code mapping
            if line.startswith("map key "):
                for scancode in layout.get(REMOVE_SCANCODES, []):
                    if line.startswith("map key {} ".format(scancode)):
                        line = "#" + line
                        # Mark that rule as matched
                        rules_matched[REMOVE_SCANCODES].append(scancode)
                        break

            # We are entering a key block
            if line.startswith("key "):
                # Mark our current key code
                cur_keycode = line.split()[1]
                # Check if we need to remove that key code
                for keycode in layout.get(REMOVE_KEYCODES, []):
                    if line.startswith("key {} ".format(keycode)):
                        remove_this_key = True
                        # Mark that rule as matched
                        rules_matched[REMOVE_KEYCODES].append(keycode)
                        break
                # Move on if we are skipping that keycode
                if remove_this_key:
                    continue

            # For each replace entry in our layout
            for replacement_orig in layout.get(REPLACE, []):
                # If it's a tuple we convert it to a replacement object
                replacement = expand_replacement(replacement_orig)
                # If a key code was specified check that we are matching it and move on if needed
                if REPL_KEYCODE in replacement and cur_keycode != replacement[REPL_KEYCODE]:
                    continue
                # Check if we need to skip that line    
                if any(skip in line for skip in replacement.get(REPL_SKIP, [])):
                    continue
                
                if REPLACE in replacement:
                    # For each replacement applying to current keycode
                    for keyCodeReplacement in replacement.get(REPLACE, []):
                        keyCodeReplacementObj = expand_replacement(keyCodeReplacement)
                        # Do replacement
                        if keyCodeReplacementObj[REPL_OLD] in line:
                            line = line.replace(keyCodeReplacementObj[REPL_OLD], keyCodeReplacementObj[REPL_NEW])
                            # Mark it as matched
                            rules_matched[KEYCODE_REPLACE].append(replacement_orig)                            
                                            
                # Do legacy replacement    
                if REPL_OLD in replacement and replacement[REPL_OLD] in line:
                    line = line.replace(replacement[REPL_OLD], replacement[REPL_NEW])
                    # Mark it as matched
                    rules_matched[REPLACE].append(replacement_orig)
                    break
                
            # Output modified line
            dst.write(line)

        for ruletype in rules_matched.keys():
            for rule in layout.get(ruletype, []):
                if rule not in rules_matched[ruletype]:
                    if ruletype == KEYCODE_REPLACE:
                        # TODO: Should we support match check for every rule? Guess not.
                        continue
                    elif ruletype == REPLACE and REPL_OLD in expand_replacement(rule) and any(ord(c) >= 128 for c in expand_replacement(rule)[REPL_OLD]):
                        # non-ASCII rule, it is just for comments so allow not matching
                        continue
                    # Review that check logic as it looks broken now
                    #raise RuntimeError(f"Rule {rule} for {layout[OUTPUT]} were never executed")

        dst.write(layout.get(ADD, ""))

def generate_layouts(layouts, target_dir):
    for layout in layouts:
        generate_layout(layout, target_dir)

def remove_previous_layouts(target_dir):
    if pathlib.Path(target_dir).exists():
        # for safety, only remove .kcm files
        for path in pathlib.Path(target_dir).iterdir():
            if path.suffix == '.kcm':
                path.unlink()
        pathlib.Path(target_dir).rmdir()

def generate_all_layouts(target_dir):
    # in case layouts are removed, clean the target directory
    remove_previous_layouts(target_dir)

    generate_layouts(layouts=GENERATED_LAYOUTS, target_dir=target_dir)

def main():
    generate_all_layouts(target_dir=sys.argv[1])

if __name__ == "__main__":
    main()
