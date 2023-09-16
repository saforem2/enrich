"""
enrich/__init__.py
"""
from __future__ import absolute_import, annotations, division, print_function
import logging
import os
from typing import Optional
import warnings
# import torch

# from mpi4py import MPI
# from rich.logging import RichHandler
from enrich.logging import RichHandler
import tqdm
from rich import print


os.environ['PYTHONIOENCODING'] = 'utf-8'

def get_file_logger(
        name: Optional[str] = None,
        level: str = 'INFO',
        rank_zero_only: bool = True,
        fname: Optional[str] = None,
        # rich_stdout: bool = True,
) -> logging.Logger:
    # logging.basicConfig(stream=DummyTqdmFile(sys.stderr))
    import logging
    fname = 'output' if fname is None else fname
    log = logging.getLogger(name)
    if rank_zero_only:
        fh = logging.FileHandler(f"{fname}.log")
        if RANK == 0:
            log.setLevel(level)
            fh.setLevel(level)
        else:
            log.setLevel('CRITICAL')
            fh.setLevel('CRITICAL')
    else:
        fh = logging.FileHandler(f"{fname}-{RANK}.log")
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
        rank_zero_only: bool = True,
        **kwargs,
) -> logging.Logger:
    log = logging.getLogger(name)
    # log.handlers = []
    # from rich.logging import RichHandler
    # from l2hmc.utils.rich import get_console, is_interactive
    # format = "[%(asctime)s][%(name)s][%(levelname)s] - %(message)s"
    # if rank_zero_only:
    #     if RANK != 0:
    #         log.setLevel('CRITICAL')
    #     else:
    #         log.setLevel(level)
    log.set_level(level)
    # if RANK == 0:
    console = get_console(
        markup=True,  # (WORLD_SIZE == 1),
        redirect=(WORLD_SIZE > 1),
        **kwargs
    )
    if console.is_jupyter:
        console.is_jupyter = False
    # log.propagate = True
    # log.handlers = []
    # use_markup = (
    # WORLD_SIZE == 1
    # and not is_interactive()
    # )
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
