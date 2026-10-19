# CSV Task Processor 🐍

A beginner-friendly Python project that reads tasks from a CSV file, validates their data, converts valid rows into Python objects, and exports the results to JSON.

Built as a hands-on exercise in Python fundamentals, file handling, data validation, and Git/GitHub.

## ✨ Features

- **Read CSV files** using Python's built-in `csv` module.
- **Validate task data** before processing it.
- **Skip invalid tasks**, such as tasks with non-numeric IDs, empty titles, or unsupported status and priority values.
- **Use a `Task` class** to represent each valid task as a Python object.
- **Export JSON** using Python's built-in `json` module.
- **Handle missing input files** with a helpful error message.

## 🛠️ Built With

- Python 3
- `csv` — read structured data from CSV files.
- `json` — export structured data to JSON.
- Object-oriented programming (OOP)

No third-party Python packages are required.

## 📁 Project Structure

```text
csv-task-processor/
├── main.py       # Main Python program
├── tasks.csv     # Input tasks
├── tasks.json    # Generated JSON output
├── .gitignore    # Files Git should ignore
└── README.md     # Project documentation
```

*Adjust the Python filename above if your main script has a different name.*

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/soudii22/csv-task-processor.git
cd csv-task-processor
```

### 2. Prepare the input file

Create a `tasks.csv` file with the following headers and sample data:

```csv
id,title,status,priority
1,Learn Python,pending,high
2,Study SQL,done,medium
3,Build API,pending,low
```

### 3. Run the program

If your script is named `main.py`, run:

```bash
python main.py
```

The program processes the CSV file and generates `tasks.json` containing the valid tasks.

## 📋 Data Validation Rules

| Field | Accepted values |
|---|---|
| `id` | Numeric ID |
| `title` | Non-empty text |
| `status` | `pending` or `done` |
| `priority` | `low`, `medium`, or `high` |

Rows that fail these checks are skipped.

## 📄 Example JSON Output

```json
[
    {
        "id": 1,
        "title": "Learn Python",
        "status": "pending",
        "priority": "high"
    },
    {
        "id": 2,
        "title": "Study SQL",
        "status": "done",
        "priority": "medium"
    }
]
```

## 📚 What I Practiced

- Reading and writing files in Python
- Working with CSV and JSON data
- Using classes and objects
- Validating user data
- Using lists and dictionaries
- Handling exceptions
- Managing a project with Git and GitHub

## 🔮 Possible Improvements

- Add unit tests.
- Improve error handling for malformed CSV files.
- Prevent duplicate task IDs.
- Add command-line options for input and output files.
- Separate the task model and processing logic into modules.

---

**Learning by building, one project at a time.** 🚀
