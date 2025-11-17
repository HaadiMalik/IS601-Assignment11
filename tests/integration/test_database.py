# tests/integration/test_database.py
import pytest
from unittest.mock import MagicMock
from app.database import get_db, get_engine, get_sessionmaker

@pytest.fixture
def mock_db_session():
    """Fixture to mock the database session"""
    mock_db = MagicMock()
    yield mock_db

def test_get_db_closes_session(mock_db_session):
    """Ensure that the get_db function properly closes the session."""
    # Patch the SessionLocal to return our mocked session
    with pytest.MonkeyPatch.context() as m:
        m.setattr("app.database.SessionLocal", lambda: mock_db_session)
        
        db = next(get_db())  # This will call the patched SessionLocal
        
        # Simulate some database operations (if needed)
        # e.g., db.query(...)

        # Ensure the close method is called once
        db.close.assert_called_once()



def test_get_engine_creates_engine():
    """Test if get_engine creates a valid SQLAlchemy engine."""
    engine = get_engine()
    assert engine is not None
    assert hasattr(engine, "connect")
    

def test_get_sessionmaker_creates_sessionmaker():
    """Test if get_sessionmaker creates a valid sessionmaker."""
    engine = get_engine()
    sessionmaker = get_sessionmaker(engine)
    assert sessionmaker is not None
    assert hasattr(sessionmaker, "class_")