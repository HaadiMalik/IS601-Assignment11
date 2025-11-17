# tests/unit/test_user.py

def test_user_repr_contains_fields():
    from app.models.user import User

    user = User(username="bob", email="bob@example.com")
    rep = repr(user)

    assert "bob" in rep
    assert "bob@example.com" in rep
    assert rep.startswith("<User(")
    assert rep.endswith(")>")