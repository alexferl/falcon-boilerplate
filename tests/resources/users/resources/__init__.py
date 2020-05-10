import pytest

try:
    import fastjsonschema as jsonschema
except ImportError:
    jsonschema = None

try:
    import jsonschema
except ImportError:
    jsonschema = None

skip_missing_dep = pytest.mark.skipif(
    jsonschema is None, reason="fastjsonschema or jsonschema dependency not found"
)
