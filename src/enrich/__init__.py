"""
enrich/__init__.py
"""
from __future__ import absolute_import, annotations, division, print_function
import logging
import os
import yaml
from typing import Optional
from enrich.console import get_console
from enrich.handler import RichHandler as EnrichHandler
from enrich.config import STYLES
import logging.config

os.environ['PYTHONIOENCODING'] = 'utf-8'


def get_enrich_logging_config_as_yaml(
        name: str = 'enrich',
        level: str = 'INFO') -> str:
    return fr"""
    ---
    # version: 1
    handlers:
      {name}:
        (): enrich.handler.RichHandler
        show_time: true
        show_level: true
        enable_link_path: false
        level: {level.upper()}
    root:
      handlers: [{name}]
    disable_existing_loggers: false
    ...
    """


# def get_logging_config_as_yaml(level: str = 'DEBUG') -> str:
#     # >>> import yaml
#     # >>>
#     # >>> names_yaml = """
#     # ... - 'eric'
#     # ... - 'justin'
#     # ... - 'mary-kate'
#     # ... """
#     return fr"""
#     handlers:
#       term:
#         class: enrich.handler.RichHandler
#         show_time: true
#         show_level: true
#         enable_link_path: false
#         level: {level}
#     root:
#       handlers: [term]
#     disable_existing_loggers: false
#     """
#

# def get_logging_config(level: str = 'INFO') -> logging.config.dictConfig:
#     config = yaml.safe_load(get_logging_config_as_yaml(level=level))
#     # with Path('logconf.yaml').open('r') as stream:
#     #     config = yaml.load(stream, Loader=yaml.FullLoader)
#     return logging.config.dictConfig(config)


def get_logger_new(
        name: str,
        level: str = 'INFO',
):
    config = yaml.safe_load(
        get_enrich_logging_config_as_yaml(
            name=name,
            level=level
        ),
    )
    #     #     config = yaml.load(stream, Loader=yaml.FullLoader)
    logging.config.dictConfig(config)
    log = logging.getLogger(name=name)
    log.setLevel(level)
    return log


def get_file_logger(
        name: Optional[str] = None,
        level: str = 'INFO',
        rank_zero_only: bool = True,
        fname: Optional[str] = None,
) -> logging.Logger:
    import logging
    fname = 'output' if fname is None else fname
    log = logging.getLogger(name)
    # if rank_zero_only:
    #     fh = logging.getLogger(name)
    #     if RANK == 0:
    #         log.setLevel(level)
    #         fh.setLevel(level)
    #     else:
    #         log.setLevel('CRITICAL')
    #         fh.setLevel('CRITICAL')
    # else:
    #     fh = logging.FileHandler(f"{fname}-{RANK}.log")
    #     log.setLevel(level)
    #     fh.setLevel(level)
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


def get_active_enrich_handlers(logger: logging.Logger) -> list:
    return (
        [
            (idx, h) for idx, h in enumerate(logger.handlers) if isinstance(
                h,
                EnrichHandler
            )
        ]
    )


def get_logger(
        name: Optional[str] = None,
        level: str = 'INFO',
        markup: Optional[bool] = True,
        redirect: Optional[bool] = False,
        **kwargs,
) -> logging.Logger:
    import logging
    log = logging.getLogger(name)
    log.setLevel(level)
    console = get_console(
        markup=markup,
        redirect=redirect,
        **kwargs
    )
    if console.is_jupyter:
        console.is_jupyter = False
    log.addHandler(
        EnrichHandler(
            omit_repeated_times=False,
            level=level,
            console=console,
            show_time=True,
            show_level=True,
            show_path=True,
            markup=markup,
            enable_link_path=False,
        )
    )
    if (
            len(log.handlers) > 1
            and all([i == log.handlers[0] for i in log.handlers])
    ):
        log.handlers = [log.handlers[0]]
    enrich_handlers = get_active_enrich_handlers(log)
    # enrich_handlers = (
    #     [
    #         (idx, h) for idx, h in enumerate(log.handlers) if isinstance(
    #             h,
    #             EnrichHandler
    #         )
    #     ]
    # )
    found_handlers = 0
    if len(enrich_handlers) > 1:
        for h in log.handlers:
            if isinstance(h, EnrichHandler):
                if found_handlers > 1:
                    log.warning(
                        'More than one `EnrichHandler` in current logger: '
                        f'{log.handlers}'
                    )
                    log.removeHandler(h)
                found_handlers += 1
    if len(get_active_enrich_handlers(log)) > 1:
        log.warning(
            'More than one `EnrichHandler` in current logger: '
            f'{log.handlers}'
        )
    #     log.warning(f'Using {enrich_handlers[-1][1]}')
    #     log.removeHandler(log.handlers[enrich_handlers[-1][0]])
    #     # log.handlers = enrich_handlers[-1]
    # # assert (
    #     len() == 1
    # # )

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


def print_styles_alt(
        html: bool = False,
        txt: bool = False,
):
    from pathlib import Path
    from rich.text import Text
    from enrich.style import DEFAULT_STYLES
    from rich.table import Table
    console = get_console(record=html, width=150)
    table = Table("Name", "Styling")
    styles = DEFAULT_STYLES
    styles |= STYLES
    for style_name, style in styles.items():
        table.add_row(Text(style_name, style=style), str(style))
    console.print(table)
    if html:
        outfile = 'enrich_styles.html'
        print(f'Saving to `{outfile}`')
        with open(outfile, 'w') as f:
            f.write(console.export_html(inline_styles=True))
    if txt:
        file1 = "enrich_styles.txt"
        text = console.export_text()
        # with open(file1, "w") as file:
        with Path(file1).open('w') as file:
            file.write(text)



if __name__ == "__main__":  # pragma: no cover
    print_styles()
