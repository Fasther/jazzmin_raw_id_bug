# Admin InLine/raw_id_field select bug

## Login details
Login details:
Login: jazzmin
Pass: test

# How to reproduce this bug (general):
- Modals: Enabled
- Two models, with FK
- Use inline admin with raw_id field
- Add new instance of the model and go to choose the value from the raw_id field
- It cannot be done

# How to reproduce it in this test app:
- go to change screen for company, Workers tab
- click "Add another worker"
- Try to pick Supervisor from modal. It does nothing.
