# blank

## Field.blank

- If **True**, the field is allowed to be blank. Default is **False**.
<br>

- Note that this is different than **null**, **null** is purely database-related, whereas **blank** is validation-related. If a field has **blank=True**, form validation will allow entry of an emprt value. If a field has **blank=Flase**, the field will be required.

