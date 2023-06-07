"""
enrich/__init__.py
"""
from __future__ import absolute_import, annotations, division, print_function
from typing import Dict
from rich.style import Style

DARK = {
    "red": "#FF5252",
    "pink": "#EB53EB",
    "cyan": "#09A979",
    "blue": "#2094F3",
    "green": "#69DB7C",
    "orange": "#FD971F",
    "magenta": "#FF00FF",
    "blue_grey": "#7D8697",
    "light_pink": "#F06292",
}

RED_ = "#FF5252"
ORANGE_ = "#FD971F"

GREEN_ = "#69DB7C"
CYAN_ = "#09A979"
DARK_GREEN_ = "#14AC3C"
INFO_ = "#00B0FF"
URL_ = "#119EDE"
BLUE_ = "#2094F3"

PURPLE_ = "#AE81FF"
PURPLE_ALT_ = "#9775FA"
LIGHT_PINK_ = "#F06292"
ATTR_ = "#F06292"
PINK_ = "#EB53EB"
MAGENTA_ = "#FF00FF"

WHITE_ = "#F8F8F8"
BLACK_ = "#161616"
LIGHT_GREY_ = "#bdbdbd"
GREY_ = "#838383"

GREEN = Style(color=DARK["green"])
PINK = Style(color=PINK_)
BLUE = Style(color=BLUE_)
RED = Style(color=DARK["red"])
MAGENTA = Style(color=MAGENTA_)
CYAN = Style(color=DARK["cyan"])
GREY_MED = "#838383"


STYLES: Dict[str, Style] = {
    'url': Style(underline=True, color="blue"),
    'num': BLUE,
    # 'repr.number': Style(color="#69DB7C"),
    # 'num': Style(color="#69DB7C"),
    # 'repr.number': Style(color="#69DB7C"),
    'log.level.warn': Style(color="yellow"),
    'log.level.warning': Style(color="yellow"),
    'logging.level.warn': Style(color="yellow"),
    'logging.level.warning': Style(color="yellow"),
    "log.path": Style(color="#909090", dim=True, bold=False),
    'log.time': Style(color='#696969'),
    'logging.time': Style(color='#696969'),
    "hidden": Style(color="#383b3d", dim=True),
    # "num": Style(color='#409CDC', bold=True),
    # 'repr.number': Style(color='#409CD0', bold=False),
    "none": Style.null(),
    "reset": Style(
        color="default",
        bgcolor="default",
        dim=False,
        bold=False,
        italic=False,
        underline=False,
        blink=False,
        blink2=False,
        reverse=False,
        conceal=False,
        strike=False,
    ),
    "dim": Style(dim=True),
    "bright": Style(dim=False),
    "bold": Style(bold=True),
    "strong": Style(bold=True),
    "code": Style(reverse=True, bold=True),
    "italic": Style(italic=True),
    "emphasize": Style(italic=True),
    "underline": Style(underline=True),
    "blink": Style(blink=True),
    "blink2": Style(blink2=True),
    "reverse": Style(reverse=True),
    "strike": Style(strike=True),
    "black": Style(color="black"),
    "red": Style(color=DARK["red"]),
    "green": Style(color=DARK["green"]),
    "yellow": Style(color="yellow"),
    "magenta": Style(color=DARK["magenta"]),
    "cyan": Style(color=DARK["cyan"]),
    "white": Style(color="white"),
    "inspect.attr": Style(color="yellow", italic=True),
    "inspect.attr.dunder": Style(color="yellow", italic=True, dim=True),
    "inspect.callable": Style(bold=True, color=DARK["red"]),
    "inspect.async_def": Style(italic=True, color="bright_cyan"),
    "inspect.def": Style(italic=True, color="bright_cyan"),
    "inspect.class": Style(italic=True, color="bright_cyan"),
    "inspect.error": Style(bold=True, color=DARK["red"]),
    "inspect.equals": Style(),
    "inspect.help": Style(color=DARK["cyan"]),
    "inspect.doc": Style(dim=True),
    "inspect.value.border": GREEN,
    "live.ellipsis": Style(bold=True, color=DARK["red"]),
    "layout.tree.row": Style(dim=False, color=DARK["red"]),
    "layout.tree.column": Style(dim=False, color=BLUE_),
    "logging.keyword": Style(bold=True, color="yellow"),
    "logging.level.notset": Style(dim=True),
    "logging.level.debug": GREEN,
    # "logging.level.info": Style(color=BLUE_),
    # "logging.level.warning": Style(color="yellow"),
    # "log.level.warn": Style(color="yellow"),
    # "log.level.warning": Style(color="yellow"),
    "logging.level.error": Style(color=DARK["red"], bold=True),
    "logging.level.critical": Style(color=DARK["red"], bold=True, reverse=True),
    "log.level": Style.null(),
    # "log.time": Style(color=DARK["cyan"], dim=True),
    "log.message": Style.null(),
    'repr.attr': Style(color=DARK['blue_grey']),
    'repr.attrib_name': Style(color=DARK['blue_grey']),
    "repr.attrib_equal": Style(bold=True, color=ORANGE_),
    "repr.attrib_value": Style(color=MAGENTA_, italic=False),
    "repr.ellipsis": Style(color="yellow"),
    "repr.indent": Style(color=DARK["green"], dim=True),
    "repr.error": Style(color=DARK["red"], bold=True),
    "repr.str": Style(color="green", italic=False, bold=False),
    "repr.brace": Style(bold=True),
    "repr.comma": Style(bold=True),
    "repr.ipv4": Style(bold=True, color="bright_green"),
    "repr.ipv6": Style(bold=True, color="bright_green"),
    "repr.eui48": Style(bold=True, color="bright_green"),
    "repr.eui64": Style(bold=True, color="bright_green"),
    "repr.tag_start": Style(bold=True),
    "repr.tag_end": Style(bold=True),
    "repr.tag_name": Style(color="bright_magenta", bold=True),
    "repr.tag_contents": Style(color="default"),
    'repr.number': Style(color=BLUE_),
    "repr.number_complex": Style(color=DARK["cyan"], bold=True, italic=False),  # same
    "repr.bool_true": Style(color="bright_green", italic=True),
    "repr.bool_false": Style(color="bright_red", italic=True),
    "repr.none": Style(color=MAGENTA_, italic=True),
    "repr.url": Style(underline=True, color="bright_blue", italic=False, bold=False),
    "repr.uuid": Style(color="bright_yellow", bold=False),
    "repr.call": Style(color=MAGENTA_, bold=True),
    "repr.path": Style(color="green"),
    "repr.filename": Style(color="magenta"),
    "rule.line": Style(color="bright_green"),
    "rule.text": Style.null(),
    "json.brace": Style(bold=True),
    "json.bool_true": Style(color="bright_green", italic=True),
    "json.bool_false": Style(color="bright_red", italic=True),
    "json.null": Style(color=MAGENTA_, italic=True),
    "json.number": Style(color=DARK["cyan"], bold=True, italic=False),
    "json.str": Style(color=DARK["green"], italic=False, bold=False),
    "json.key": Style(color=BLUE_, bold=True),
    "prompt": Style.null(),
    "prompt.choices": Style(color=MAGENTA_, bold=True),
    "prompt.default": Style(color=DARK["cyan"], bold=True),
    "prompt.invalid": Style(color=DARK["red"]),
    "prompt.invalid.choice": Style(color=DARK["red"]),
    "pretty": Style.null(),
    "scope.border": Style(color=BLUE_),
    "scope.key": Style(color="yellow", italic=True),
    "scope.key.special": Style(color="yellow", italic=True, dim=True),
    "scope.equals": Style(color=DARK["red"]),
    "table.header": Style(bold=True),
    "table.footer": Style(bold=True),
    "table.cell": Style.null(),
    "table.title": Style(italic=True),
    "table.caption": Style(italic=True, dim=True),
    "traceback.error": Style(color=DARK["red"], italic=True),
    "traceback.border.syntax_error": Style(color="bright_red"),
    "traceback.border": Style(color=DARK["red"]),
    "traceback.text": Style.null(),
    "traceback.title": Style(color=DARK["red"], bold=True),
    "traceback.exc_type": Style(color="bright_red", bold=True),
    "traceback.exc_value": Style.null(),
    "traceback.offset": Style(color="bright_red", bold=True),
    "bar.back": Style(color="grey23"),
    "bar.complete": Style(color=DARK["green"]),
    "bar.finished": Style(color=ORANGE_),
    "bar.pulse": Style(color="rgb(249,38,114)"),
    "progress.description": Style.null(),
    "progress.filesize": Style(color=DARK["green"]),
    "progress.filesize.total": Style(color=DARK["green"]),
    "progress.download": Style(color=DARK["green"]),
    "progress.elapsed": Style(color="yellow"),
    "progress.percentage": Style(color=MAGENTA_),
    "progress.remaining": Style(color=DARK["cyan"]),
    "progress.data.speed": Style(color=DARK["red"]),
    "progress.spinner": Style(color=DARK["green"]),
    "status.spinner": Style(color=DARK["green"]),
    "tree": Style(),
    "tree.line": Style(),
    "markdown.paragraph": Style(),
    "markdown.text": Style(),
    "markdown.em": Style(italic=True),
    "markdown.emph": Style(italic=True),  # For commonmark backwards compatibility
    "markdown.strong": Style(bold=True),
    "markdown.code": Style(bold=True, color=LIGHT_GREY_, bgcolor=BLACK_),
    "markdown.code_block": Style(color=WHITE_, bgcolor=BLACK_),
    "markdown.block_quote": Style(color=MAGENTA_),
    "markdown.list": Style(color=DARK["cyan"]),
    "markdown.item": Style(),
    "markdown.item.bullet": Style(color="yellow", bold=True),
    "markdown.item.number": Style(color="yellow", bold=True),
    "markdown.hr": Style(color="yellow"),
    "markdown.h1.border": Style(),
    "markdown.h1": Style(bold=True),
    "markdown.h2": Style(bold=True, underline=True),
    "markdown.h3": Style(bold=True),
    "markdown.h4": Style(bold=True, dim=True),
    "markdown.h5": Style(underline=True),
    "markdown.h6": Style(italic=True),
    "markdown.h7": Style(italic=True, dim=True),
    "markdown.link": Style(color="bright_blue", underline=True),
    "markdown.link_url": Style(color=BLUE_, underline=True),
    "markdown.s": Style(strike=True, color="white", dim=True),
    "iso8601.date": Style(color=BLUE_),
    "iso8601.time": Style(color=MAGENTA_),
    "iso8601.timezone": Style(color="yellow"),
}
