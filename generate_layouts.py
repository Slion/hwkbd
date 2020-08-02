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
from qwerty_shift_alias import *
from qwerty_fn import *
from qwerty_fn_custom import *
from qwerty_alt import *
from qwerty_international import *


#
REMAP_SWAP_ALT_FN = r"""
# Swap alt and fn
# Alt is now Fn
map key 464 ALT_LEFT
# Fn is now Alt
map key 56 FUNCTION
"""


SWAP_ALT_FN = [
    ("lalt", "fn"),
    ("fn", "lalt")
]

SWAP_TAB_FIX = [
    {
        REPL_KEYCODE: "TAB",
        REPLACE: [
            ("lalt:", "fn:"),
        ]
    },
]

GENERATED_LAYOUTS = [
    {
        # Process our QWERTY template
        INPUT: "pro1_qwerty_template.kcm",
        OUTPUT: "pro1_qwerty_us_template.kcm",                
        REPLACE:    REPLACE_PRINTED_QWERTY+
                    QWERTY_FN_PRINTED+
                    QWERTY_FN_CUSTOM+
                    REPLACE_FX_QWERTY+
                    QWERTY_ALT,
        ADD: REMAP_FX                    
    },
    {
        # Process our US template 
        # That's the basic US layout
        INPUT: "pro1_qwerty_us_template.kcm",
        OUTPUT: "pro1_qwerty_us.kcm", 
        IS_SOURCE_GENERATED: True,               
        REPLACE: CLEANUP_TEMPLATE,  
    },    
    {
        # Swapping alt and fn
        INPUT: "pro1_qwerty_us.kcm",
        OUTPUT: "pro1_qwerty_us_fn_tab_tmp.kcm", 
        IS_SOURCE_GENERATED: True,               
        REPLACE: SWAP_ALT_FN,  
        ADD: REMAP_SWAP_ALT_FN                    
    },
    {
        # Somehow modifying the same line twice in the same run does not work.
        # So we had to take an extra step to patch our TAB
        INPUT: "pro1_qwerty_us_fn_tab_tmp.kcm",
        OUTPUT: "pro1_qwerty_us_fn_tab.kcm", 
        IS_SOURCE_GENERATED: True,               
        REPLACE: SWAP_TAB_FIX,  
    },
    {
        # Process our US template adding shift alias
        # That's enabling the use of the Shift key to access most Fn characters
        INPUT: "pro1_qwerty_us_template.kcm",
        OUTPUT: "pro1_qwerty_us_shift_alias.kcm", 
        IS_SOURCE_GENERATED: True,               
        REPLACE: QWERTY_SHIFT_ALIAS + CLEANUP_TEMPLATE,  
    },
    {
        # Swapping alt and fn
        INPUT: "pro1_qwerty_us_shift_alias.kcm",
        OUTPUT: "pro1_qwerty_us_shift_alias_fn_tab_tmp.kcm", 
        IS_SOURCE_GENERATED: True,               
        REPLACE: SWAP_ALT_FN,  
        ADD: REMAP_SWAP_ALT_FN                    
    },
    {
        # Somehow modifying the same line twice in the same run does not work.
        # So we had to take an extra step to patch our TAB
        INPUT: "pro1_qwerty_us_shift_alias_fn_tab_tmp.kcm",
        OUTPUT: "pro1_qwerty_us_shift_alias_fn_tab.kcm", 
        IS_SOURCE_GENERATED: True,               
        REPLACE: SWAP_TAB_FIX,  
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
