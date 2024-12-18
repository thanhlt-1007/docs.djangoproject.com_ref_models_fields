# Model field reference

- This document contains all the API references of Field including [field options](https://docs.djangoproject.com/en/5.1/ref/models/fields/#field-options) and [field types](https://docs.djangoproject.com/en/5.1/ref/models/fields/#field-types) Django offers.

## Note

- Fields are defined in **django.db.models.fields**, but for convenience they're imported into **django.db.models**. The standard convention is to use

```python
from django.db import models
```

and refer to field as **models.<Foo>Field**.
