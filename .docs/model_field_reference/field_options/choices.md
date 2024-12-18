# choices

## Field.choices

- A mapping or iterable in the format described below to use as choices for this field. If choices are given, they're enforced by [model validation](https://docs.djangoproject.com/en/5.1/ref/models/instances/#validating-objects) and the default form widge will be a select box with these choices instead of the standard text field.
<br>

- If a mapping is given, the key element is the actual value to be set on the model, and the second element is the human readable name. For example:

```python
YEAR_IN_SCHOOL_CHOICES = {
    "FR": "Freshman",
    "SO": "Sophomore",
    "JR": "Junior",
    "SR": "Senior",
    "GR": "Graduate",
}
```

- You can also pass a sequence consisting itself of it iterables of exactly two item, e.g:

```python
[(A1, B1), (A2, B2), ...]
```

The first element in rach tuple is the actual value to be set on the model, and the second element is the human-readable name. For example:

```python
YEAR_IN_SCHOOL_CHOICES = [
    ("FR", "Freshman"),
    ("SO", "Sophomore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
    ("GR", "Graduate"),
]
```

**choices** can also be defined as a callable that expects no arguments and returns any of the formats described above. For example:

```python
def get_currencies():
    return { i: i for i in settings.CURRENCIES }


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=get_currencies)
```

- Passing a callable for **choices** can be particularly handy when, for example, the choices are:
<br>

    - the result of I/O-bound operations (which could potentially be cached), such as querying a table in the same or an external database, or accessing the choices from a static file.
    <br>

    - a list that is mostly stable but could vary from time to time or from project to project. Examples in this category are using third-party apps that provide a well-known inventory of values, such as currencies, countries, languages, time zones, etc.
    <br>

- Generally, it's best to define choices inside a model class, and to define a suitably-named constant for each value:
