import tempfile, os
from sqlite_utils import init, set_kv, get_all
def test_db():
    db = tempfile.NamedTemporaryFile(delete=False).name
    init(db); set_kv(db, "a", "1"); set_kv(db, "b", "2")
    data = get_all(db)
    assert data == {"a":"1","b":"2"}
