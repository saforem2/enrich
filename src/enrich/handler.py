"""
Implements enriched RichHandler

Based on:

https://github.com/willmcgugan/rich/blob/master/rich/_log_render.py
"""
from datetime import datetime
from typing import Any, Iterable, Optional

from rich.logging import RichHandler as OriginalRichHandler
from rich.text import Text, TextType, Span

from enrich.config import STYLES
from enrich.console import Console
from rich.console import ConsoleRenderable

# from datetime import datetime
# from typing import Any, Iterable, Optional

# from rich.logging import RichHandler as OriginalRichHandler
# from rich.text import Text, TextType, Span


class RichHandler(OriginalRichHandler):
    """Enriched handler that does not wrap."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        # RichHandler constructor does not allow custom renderer
        # https://github.com/willmcgugan/rich/issues/438
        self._log_render = FluidLogRender(
            show_time=kwargs.get("show_time", False),
            show_level=kwargs.get("show_level", True),
            show_path=kwargs.get("show_path", False),
        )  # type: ignore



# class RichHandler(OriginalRichHandler):
#     """Enriched handler that does not wrap."""
#     def __init__(self, *args: Any, **kwargs: Any) -> None:
#         super().__init__(*args, **kwargs)
#         # RichHandler constructor does not allow custom renderer
#         # https://github.com/willmcgugan/rich/issues/438
#         self._log_render = FluidLogRender(
#             show_time=kwargs.get("show_time", False),
#             show_level=kwargs.get("show_level", True),
#             show_path=kwargs.get("show_path", False),
#         )  # type: ignore

class FluidLogRender:  # pylint: disable=too-few-public-methods
    """Renders log by not using columns and avoiding any wrapping."""
    def __init__(
            self,
            show_time: bool = True,
            show_level: bool = True,
            show_path: bool = True,
            time_format: str = "[%Y-%m-%d %H:%M:%S]",

    ) -> None:
        self.show_time = show_time
        self.show_level = show_level
        self.show_path = show_path
        self.time_format = time_format
        self._last_time: Optional[str] = None

    def __call__(  # pylint: disable=too-many-arguments
            self,
            console: Console,  # type: ignore
            renderables: Iterable[ConsoleRenderable],
            log_time: Optional[datetime] = None,
            time_format: str = '[%Y-%m-%d %H:%M:%S]',
            level: TextType = "",
            path: Optional[str] = None,
            line_no: Optional[int] = None,
            link_path: Optional[str] = None,
    ) -> Text:
        result = Text()
        if self.show_time:
            log_time = datetime.now() if log_time is None else log_time
            log_time_display = log_time.strftime(time_format or self.time_format)
            result += Text(log_time_display, style=STYLES['logging.time'])
            self._last_time = log_time_display
        if self.show_level:
            if isinstance(level, Text):
                lstr = level.plain.rstrip(' ')
                style = level.spans[0].style
                level.spans = [Span(0, len(lstr), style)]
                ltext = Text(f'[{lstr}]', style=style)
            elif isinstance(level, str):
                lstr = level.rstrip(' ')
                ltext = Text(f"[{lstr}]", style=f"logging.level.{str(lstr)}")
            else:
                raise TypeError('Unexpected type for level')
            result += ltext
        if self.show_path and path:
            path_text = Text("[", style=STYLES['log.path'])
            path_text.append(
                path, style=(
                    f"link file://{link_path}" + " underline"
                    # + STYLES["repr.url"]
                )
                if link_path else ""
            )
            if line_no:
                path_text.append(":")
                path_text.append(
                    f"{line_no}",
                    style=f"link file://{link_path}#{line_no}" if link_path else "",
                )
            path_text.append("]", style=STYLES['log.path'])
            result += path_text
        result += Text(' - ')
        for elem in renderables:
            result += elem
        return result
