# Task Manager CLI

A simple and efficient command-line interface for managing tasks using Python. Supports adding, listing, and updating tasks stored in a JSON file.

---

## 🚀 Features

- ✅ Add tasks with descriptions  
- 📋 List all tasks or filter by status (`TODO`, `IN_PROGRESS`, `DONE`)  
- ✏️ Update task descriptions and statuses  
- 🗃️ Persistent task storage in a JSON file  
- 🖥️ Pretty-printed task lists with `tabulate`

---

## 📦 Requirements

- Python 3.8+
- [`tabulate`](https://pypi.org/project/tabulate/)  
  Install it with:

  ```bash
  pip install tabulate
  ```
  
---
  
## 🛠️ Usage

All commands are run through the CLI using:

```bash
  python task-cli.py <command> [options]
```

## ➕ Add a Task

```bash
  task-cli add "Write unit tests"
```

## ➖ Delete a Task

```bash
  task-cli delete <id>
```

## 📃 List Tasks

```bash
  # List all tasks
  task-cli list
  
  # List only tasks with a specific status
  task-cli list todo
  task-cli list done
  task-cli list in-progress
```

## 📝 Update Task Description

```bash
  task-cli update <id> "New description here"
```

## 🔄 Update Task Status

```bash
  task-cli mark-done <id>
  task-cli mark-in-progress <id>
```

---

# 📁 Task File Example (tasks.json)

```json
  [
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "TODO",
    "createdAt": "2025-05-12 10:00",
    "updatedAt": "2025-05-12 10:00"
  }
]
```
