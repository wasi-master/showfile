from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Other,
    Punctuation,
    String,
    Text,
    Whitespace
)

DARK_GREY = "#2D2A2E"
LIGHT_GREY= "#69676c"
RED = "#FF6188"
GREEN = "#A9DC76"
YELLOW = "#FFD866"
ORANGE = "#FC9867"
PURPLE = "#AB9DF2"
CYAN = "#78DCE8"
WHITE = "#f7f1ff"

class MonokaiProStyle(Style):
    """
    This style mimics the Monokai Pro color scheme.
    """

    background_color = DARK_GREY
    highlight_color = "#49483e"

    styles = {
        # No corresponding class for the following:
        Text:                      WHITE, # class:  ''
        Error:                     "#FF6188 bg:#1e0010", # class: 'err'

        Comment:                   "italic #69676c", # class: 'c'
        Comment.Multiline:         YELLOW,        # class: 'cm'

        Keyword:                   RED, # class: 'k'
        Keyword.Namespace:         RED, # class: 'kn'
        Keyword.Reserved:          CYAN,   # class: 'kr'
        Keyword.Constant:          PURPLE,   # class: 'kc'

        Operator:                  RED, # class: 'o'

        Punctuation:               WHITE, # class: 'p'

        Name:                      WHITE, # class: 'n'
        Name.Attribute:            GREEN, # class: 'na' - to be revised
        Name.Builtin:              GREEN,        # class: 'nb'
        Name.Builtin.Pseudo:       ORANGE,        # class: 'bp'
        Name.Exception:            CYAN,   # class: 'ne'
        Name.Class:                CYAN, # class: 'nc' - to be revised
        Name.Decorator:            PURPLE, # class: 'nd' - to be revised
        Name.Exception:            "italic #78DCE8", # class: 'ne'
        Name.Function:             GREEN, # class: 'nf'
        Name.Tag:                  RED, # class: ''
        Name.Property:             ORANGE,        # class: 'py'

        Number:                    PURPLE, # class: 'm'

        Literal:                   PURPLE, # class: 'l'
        Literal.Date:              ORANGE, # class: 'ld'

        String:                    YELLOW, # class: 's'
        String.Regex:              ORANGE,        # class: 'sr'

        Generic.Deleted:           YELLOW, # class: 'gd',
        Generic.Emph:              "italic",  # class: 'ge'
        Generic.Inserted:          GREEN, # class: 'gi'
        Generic.Strong:            "bold",    # class: 'gs'
        Generic.Subheading:        LIGHT_GREY, # class: 'gu'
    }
