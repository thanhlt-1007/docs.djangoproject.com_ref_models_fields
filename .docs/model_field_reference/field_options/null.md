# null

## Field.null

- If **True**, Django will store empty values as **NULL** in the database. Default is **False**.
<br>

- Avoid using **null** on string-based fields such as **CharField** and **TextField**. If a string-based field has **null=Trie**, that means it has two possible values for "no data": **NULL**, and the empty string. In most cases, it's redundant to have two possible values for "no data"; the Django convention is to use the empty string, not NULL. One exception is when a **CharField** has both **unique=True** and **blank=True** set. In this situation, **null=True** is required to avoid unique constraint violants when saving multiple objects with blank values.
<br>

- For both string-based and non-string-based fields, you will also need to set **blank=True** if you wish to permit empty values in forms, as the **null** parameter only affects database storage.
