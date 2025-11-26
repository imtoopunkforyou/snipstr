import contextlib
import sys
import typing
from types import ModuleType
from unittest.mock import patch

try:
    from typing_extensions import Self as SelfFromExtensions
except ImportError:
    SelfFromExtensions = type('Self', (), {})


def _create_mock_typing_module() -> ModuleType:
    mock_typing = ModuleType('typing')
    mock_typing.Self = SelfFromExtensions

    with contextlib.suppress(AttributeError, TypeError):
        for attr in dir(typing):
            if not attr.startswith('_'):
                setattr(mock_typing, attr, getattr(typing, attr))

    mock_typing.Self = SelfFromExtensions
    return mock_typing


def _remove_modules_from_cache() -> None:
    modules_to_remove = ['snipstr.base', 'snipstr.snipstr']
    for module_name in modules_to_remove:
        if module_name in sys.modules:
            del sys.modules[module_name]


def _restore_modules(
    original_base: object | None,
    original_snipstr: object | None,
    original_typing: object | None,
) -> None:
    if original_base:
        sys.modules['snipstr.base'] = original_base
    if original_snipstr:
        sys.modules['snipstr.snipstr'] = original_snipstr
    if original_typing:
        sys.modules['typing'] = original_typing


def test_self_import_python_311_plus():
    original_base = sys.modules.get('snipstr.base')
    original_snipstr = sys.modules.get('snipstr.snipstr')
    original_typing = sys.modules.get('typing')

    _remove_modules_from_cache()

    try:
        mock_typing = _create_mock_typing_module()

        with (
            patch.object(sys, 'version_info', (3, 11, 0)),
            patch.dict(sys.modules, {'typing': mock_typing}),
        ):
            # Import after mocking
            import snipstr.base  # noqa: PLC0415
            import snipstr.snipstr  # noqa: F401, PLC0415

            # If we get here, the import worked
            # and the Python 3.11+ path was executed
            assert True
    finally:
        _restore_modules(original_base, original_snipstr, original_typing)
