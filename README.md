[![codecov](https://codecov.io/github/imtoopunkforyou/snipstr/graph/badge.svg?token=65OY6J3HP9)](https://codecov.io/github/imtoopunkforyou/snipstr)
[![tests](https://github.com/imtoopunkforyou/snipstr/actions/workflows/tests.yaml/badge.svg)](https://github.com/imtoopunkforyou/snipstr/actions/workflows/tests.yaml)
[![pypi package version](https://img.shields.io/pypi/v/snipstr.svg)](https://pypi.org/project/snipstr)
[![status](https://img.shields.io/pypi/status/snipstr.svg)](https://pypi.org/project/snipstr)
[![pypi downloads](https://img.shields.io/pypi/dm/snipstr.svg)](https://pypi.org/project/snipstr)
[![supported python versions](https://img.shields.io/pypi/pyversions/snipstr.svg)](https://pypi.org/project/snipstr)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![license](https://img.shields.io/pypi/l/snipstr.svg)](https://github.com/imtoopunkforyou/snipstr/blob/main/LICENSE)  


# snipstr
A lightweight library for easy-to-use text truncation with a friendly interface.

# ⚠️ Attention ⚠️
- In development.  
- May not work as you expect and may cause errors.


### Example
```python
>>> from snipstr import SnipStr
>>> text = 'Python source code and installers are available for download for all versions!'
>>> s = SnipStr(text)
>>> s.snip_to(16).by_side('right').with_replacement_symbol()
>>> str(s)
'Python source...'
```