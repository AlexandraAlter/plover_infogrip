"""
"""

from dataclasses import dataclass

from plover.system import english_stenotype

KEYS = ('M', 'A', 'C', '1', '2', '3', '4')

IMPLICIT_HYPHEN_KEYS = ()
SUFFIX_KEYS = ()
NUMBER_KEY = ''
NUMBERS = {}

UNDO_STROKE_STENO = ''

ORTHOGRAPHY_RULES = english_stenotype.ORTHOGRAPHY_RULES
ORTHOGRAPHY_RULES_ALIASES = english_stenotype.ORTHOGRAPHY_RULES_ALIASES

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        'M': 'res1', 'A': 'O-', 'C': 'A-',
        '1': 'H-', '2': 'P-', '3': 'T-', '4': 'S1-',
        '1': 'R-', '2': 'W-', '3': 'K-', '4': 'S2-',

        'M': 'res2', 'A': '-E', 'C': '-U',
        '1': '-F', '2': '-P', '3': '-L', '4': '-T',
        '1': '-R', '2': '-B', '3': '-G', '4': '-S',

        'no-op': (
            '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'
            '-D', '-Z',
            '*1', '*2', '*3', '*4',
            'Fn', 'pwr',
        ),
    },
} # yapf: disable


DICTIONARIES_ROOT = 'asset:plover_infogrip:assets'
DEFAULT_DICTIONARIES = (
    'infogrip_user.json',
    'infogrip_funcs.json',
    'infogrip_num.json',
    'infogrip_main.json',
)
