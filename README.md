# Module 11: Polymorphic SQLAlchemy Models & Pydantic Schemas

### [Link to Associated Docker Repository](https://hub.docker.com/r/haadimalik/assignment-11)


## Summary

Successfully reconstructed Module 11 with **SQLAlchemy polymorphic inheritance** for calculations and comprehensive Pydantic schemas for validation. All tests pass with 93% code coverage.


## What Was Added

**1. SQLAlchemy Polymorphic Models (`app/models/calculation.py`)**
**2. Pydantic Schemas (`app/schemas/calculation.py`)**
**3. Database Configuration**
**4. Comprehensive Tests**


## What Makes It Polymorphic

1. **Single Table, Multiple Types:** All calculations stored in one table with `type` discriminator
2. **Automatic Type Resolution:** SQLAlchemy returns correct subclass (Addition, Division, etc.)
3. **Factory Pattern:** `Calculation.create()` abstracts object creation
4. **Common Interface, Different Behavior:** All have `get_result()`, each implements differently
5. **Type Safety:** `isinstance()` checks work correctly for subclasses


## Key Design Patterns Demonstrated

1. **Polymorphic Inheritance** - SQLAlchemy single-table inheritance
2. **Factory Pattern** - `Calculation.create()` method
3. **Template Method** - Abstract `get_result()` implemented by subclasses
4. **Data Transfer Objects** - Pydantic schemas as DTOs
5. **Dependency Injection** - `get_db()` for database sessions


## LBYL vs EAFP Examples

**LBYL (Look Before You Leap) - In Schemas:**
```python
# Check for division by zero BEFORE operation
if self.type == CalculationType.DIVISION:
    if any(x == 0 for x in self.inputs[1:]):
        raise ValueError("Cannot divide by zero")
```

**EAFP (Easier to Ask Forgiveness than Permission) - In Models:**
```python
# Attempt division, catch error if it happens
for value in self.inputs[1:]:
    if value == 0:
        raise ValueError("Cannot divide by zero.")
    result /= value
```


## Running Tests

```bash
# Run all integration tests
pytest tests/integration/ -v

# Run polymorphic model tests
pytest tests/integration/test_calculation.py -v

# Run schema validation tests
pytest tests/integration/test_calculation_schema.py -v

# Run with coverage
pytest tests/integration/ --cov=app --cov-report=html
```
