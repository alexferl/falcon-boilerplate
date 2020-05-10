import pytest

try:
    import fastjsonschema
except ImportError:
    fastjsonschema = None

try:
    import jsonschema
except ImportError:
    jsonschema = None

skip_missing_dep = pytest.mark.skipif(
    fastjsonschema is None and jsonschema is None,
    reason="fastjsonschema or jsonschema dependency not found",
)
