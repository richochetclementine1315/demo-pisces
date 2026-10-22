import importlib
import io
import pickle
from unittest.mock import patch


def test_load_data_returns_pickled_value():
    payload = {"status": "ok"}
    stream = io.BytesIO()
    pickle.dump(payload, stream)
    stream.seek(0)

    with patch("builtins.input", return_value="0"), patch("requests.get"):
        target = importlib.import_module("pisces_target")

    assert target.load_data(stream) == payload
