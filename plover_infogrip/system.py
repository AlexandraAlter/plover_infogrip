"""
"""

from dataclasses import dataclass

from plover.system import english_stenotype

KEYS = ('M-', 'A-', 'C-', '1-', '2-', '3-', '4-')

IMPLICIT_HYPHEN_KEYS = ()
SUFFIX_KEYS = ()
NUMBER_KEY = ''
NUMBERS = {}

UNDO_STROKE_STENO = None

ORTHOGRAPHY_RULES = english_stenotype.ORTHOGRAPHY_RULES
ORTHOGRAPHY_RULES_ALIASES = english_stenotype.ORTHOGRAPHY_RULES_ALIASES

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        'M-': ('res1', 'res2'),
        'A-': ('O-', '-E'),
        'C-': ('A-', '-U'),
        '1-': ('H-', 'R-', '-F', '-R'),
        '2-': ('P-', 'W-', '-P', '-B'),
        '3-': ('T-', 'K-', '-L', '-G'),
        '4-': ('S1-', 'S2-', '-T', '-S'),

        'no-op': (
            '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C',
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
