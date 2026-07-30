# Architecture

```
main.py
    │
    ▼
DictionaryService
    │
    ├────────► EntropyService
    ├────────► ReportService
    ├────────► PasswordRepository
    ├────────► HistoryRepository
    ├────────► Validators
    └────────► TextExporter
```

## Components

### DictionaryService

Checks passwords against a dictionary.

### EntropyService

Calculates password entropy.

### ReportService

Creates formatted reports.

### HistoryRepository

Stores previous password checks.

### Validators

Performs password validation.

### Exporters

Exports reports to text files.
