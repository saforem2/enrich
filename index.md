# `enrich`
Sam Foreman
2024-01-27

<details open>
<summary>
<b style="font-size:1.25em;"><code>rich</code> 🤝
<code>logging</code></b>
</summary>

`enrich` provides a generalized
[`RichHandler`](https://github.com/saforem2/enrich/blob/main/src/enrich/handler.py#L28)
that allows for [`rich`](https://github.com/Textualize/rich) style
highlights **without line breaks**

<!-- ::: {layout="[[35, -5, 35]]" layout-valign="bottom" style="display: flex; text-align:center; align-items: flex-end;"} -->

<div class="columns" style="display:flex;">

<div class="column" width="35%">

<img
src="https://github.com/saforem2/enrich/blob/main/assets/dark.png?raw=true"
class="stretch" />

</div>

<div class="column" width="35%">

<img
src="https://github.com/saforem2/enrich/blob/main/assets/light.png?raw=true"
class="stretch" />

</div>

</div>

<details>
<summary>
<b>🤷🏻‍♂️ Ambivalent<b>
</summary>

<img
src="https://github.com/saforem2/enrich/blob/main/assets/logs/amvbivalent.png"
class="stretch" alt="ambivalent" />

<img
src="https://github.com/saforem2/enrich/blob/main/assets/logs/ambivalent-transparent.png"
class="stretch" alt="ambivalent-transparent" />

</details>
<details>
<summary>
<b>😻 Catpuccin Latte<b>
</summary>

<img
src="https://github.com/saforem2/enrich/blob/main/assets/logs/catpuccin-latte.png"
class="stretch" alt="catpuccin-latte" /> <img
src="https://github.com/saforem2/enrich/blob/main/assets/logs/catpuccin-latte-transparent.png"
class="stretch" alt="catpuccin-latte-transparent" />

</details>
<details>
<summary>
<b>😈 Doom One<b>
</summary>

<img
src="https://github.com/saforem2/enrich/blob/main/assets/logs/doom-one.png"
class="stretch" alt="doom-one" /> <img
src="https://github.com/saforem2/enrich/blob/main/assets/logs/doom-one-transparent.png"
class="stretch" alt="doom-one-transparent" />

</details>
</details>

## Setup

- `logging.config.dictConfig(...)`:

  ``` python
  import yaml
  with Path('logconf.yaml').open('r') as stream:
      config = yaml.load(stream, Loader=yaml.FullLoader)
  log_config = logging.config.dictConfig(config)
  log = logging.getLogger(__name__)
  log.setLevel('INFO')
  ```

- Where `logconf.yaml`:

  ``` yaml
  ---
  # logconf.yaml
  handlers:
    term:
      class: enrich.handler.RichHandler
      show_time: true
      show_level: true
      enable_link_path: false
      level: DEBUG
  root:
    handlers: [term]
  disable_existing_loggers: false
  ...
  ```

<details closed>
<summary>
<h1>
Original README
</h1>
</summary>

## Original `README`

## Console with redirect support

Our Console class adds one additional option to rich.Console in order to
redirect `sys.stdout` and `sys.stderr` streams using a FileProxy.

``` python
from enrich.console import Console
import sys

console = Console(
    redirect=True,  # <-- not supported by rich.console.Console
    record=True)
sys.write("foo")

# this assert would have passed without redirect=True
assert console.export_text() == "foo"
```

## Console with implicit soft wrapping

If you want to produce fluid terminal output, one where the client
terminal decides where to wrap the text instead of the application, you
can now tell the Console constructor the soft_wrap preference.

``` python
from enrich.console import Console
import sys

console = Console(soft_wrap=True)
console.print(...)  # no longer need to pass soft_wrap to each print
```

## Console.print can also deal with ANSI escapes

Extends Rich Console to detect if original text already had ANSI escapes
and decodes it before processing it. This solves the case where printing
output captured from other processes that contained ANSI escapes would
brake.
[upstream-404](https://github.com/willmcgugan/rich/discussions/404)

## Soft-wrapping logger

Rich logger assumes that you always have a fixed width console and it
does wrap logged output according to it. Our alternative logger does
exactly the opposite: it ignores the columns of the current console and
prints output using a Console with soft wrapping enabled.

The result are logged lines that can be displayed on any terminal or web
page as they will allow the client to decide when to perform the
wrapping.

``` python
import logging
from enrich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("Text that we do not want pre-wrapped by logger: %s", 100 * "x")
```

</details>

## <span class="pink-text"></span> Appendix

> [!TIP]
>
> ### <span style="color: #FF5252;"><span class="quarto-shortcode__" data-is-shortcode="1" data-raw="{{&lt; iconify material-symbols ecg-heart &gt;}}"><span class="quarto-shortcode__-param" data-is-shortcode="1" data-value="iconify" data-raw="iconify"></span> <span class="quarto-shortcode__-param" data-is-shortcode="1" data-value="material-symbols" data-raw="material-symbols"></span> <span class="quarto-shortcode__-param" data-is-shortcode="1" data-value="ecg-heart" data-raw="ecg-heart"></span></span> Status</span>
>
> <pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #7f7f7f; text-decoration-color: #7f7f7f; font-style: italic">Last Updated</span>: <span style="color: #f06292; text-decoration-color: #f06292; font-weight: bold">01</span><span style="color: #f06292; text-decoration-color: #f06292">/</span><span style="color: #f06292; text-decoration-color: #f06292; font-weight: bold">27</span><span style="color: #f06292; text-decoration-color: #f06292">/</span><span style="color: #f06292; text-decoration-color: #f06292; font-weight: bold">2024</span> <span style="color: #7f7f7f; text-decoration-color: #7f7f7f">@</span> <span style="color: #1a8fff; text-decoration-color: #1a8fff; font-weight: bold">10:19:36</span>
> </pre>
> <!-- [[![](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fsaforem2.github.io&count_bg=%2300CCFF&title_bg=%23303030&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)]{style="text-align:center;"} -->
> <p align="center">
> <a href="https://hits.seeyoufarm.com"><img align="center" src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fsamforeman.me&count_bg=%2300CCFF&title_bg=%23303030&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>
> </p>
