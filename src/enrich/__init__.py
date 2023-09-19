"""
enrich/__init__.py
"""
from __future__ import absolute_import, annotations, division, print_function
import logging
import os
from typing import Optional
from enrich.console import get_console
from enrich.handler import RichHandler
from enrich.config import STYLES

os.environ['PYTHONIOENCODING'] = 'utf-8'


def get_file_logger(
        name: Optional[str] = None,
        level: str = 'INFO',
        rank_zero_only: bool = True,
        fname: Optional[str] = None,
) -> logging.Logger:
    import logging
    fname = 'output' if fname is None else fname
    log = logging.getLogger(name)
    fh = logging.FileHandler(f"{fname}.log")
    log.setLevel(level)
    fh.setLevel(level)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        "[%(asctime)s][%(name)s][%(levelname)s] - %(message)s"
    )
    fh.setFormatter(formatter)
    log.addHandler(fh)
    return log


def get_logger(
        name: Optional[str] = None,
        level: str = 'INFO',
        **kwargs,
) -> logging.Logger:
    import logging
    log = logging.getLogger(name)
    log.setLevel(level)
    console = get_console(
        markup=True,
        redirect=False,
        **kwargs
    )
    if console.is_jupyter:
        console.is_jupyter = False
    log.addHandler(
        RichHandler(
            omit_repeated_times=False,
            level=level,
            console=console,
            show_time=True,
            show_level=True,
            show_path=True,
            # markup=use_markup,
            enable_link_path=False,
        )
    )
    if (
            len(log.handlers) > 1
            and all([i == log.handlers[0] for i in log.handlers])
    ):
        log.handlers = [log.handlers[0]]
    return log


def print_styles():
    import argparse
    parser = argparse.ArgumentParser()
    from rich.text import Text
    from enrich.console import Console
    parser.add_argument("--html", action="store_true", help="Export as HTML table")
    args = parser.parse_args()
    html: bool = args.html
    from rich.table import Table
    console = Console(record=True, width=120) if html else Console()
    table = Table("Name", "Styling")
    for style_name, style in STYLES.items():
        table.add_row(Text(style_name, style=style), str(style))

    console.print(table)
    if html:
        outfile = 'enrich_styles.html'
        print(f'Saving to `{outfile}`')
        with open(outfile, 'w') as f:
            f.write(console.export_html(inline_styles=True))


if __name__ == "__main__":  # pragma: no cover
    print_styles()
