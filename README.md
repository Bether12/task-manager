# Task Manager

A desktop task management application built with Python and Tkinter, demonstrating object-oriented design, data persistence, and modern GUI development.

## Overview

This application provides a complete task management system with a clean graphical user interface. It supports full CRUD operations, priority-based organization, and seamless data persistence using JSON. The project was developed to showcase proficiency in both command-line logic (previous C++ version) and desktop GUI development using Python's standard library.

Key technical highlights include:

- Modular architecture following a basic MVC pattern
- Custom `Task` class with proper encapsulation and serialization
- Persistent storage with automatic JSON read/write
- CSV import/export functionality for interoperability
- Responsive Treeview interface with horizontal and vertical scrolling

## Features

- Add tasks with configurable priority levels (1 = High, 2 = Medium, 3 = Low)
- Mark tasks as completed with state management
- Delete tasks with proper index synchronization
- Interactive `ttk.Treeview` table
- Modal dialog for task creation using `Toplevel`
- Automatic data persistence in `tasks.json`
- Full CSV import and export with proper header handling
- Menu bar with file operations and external links

## Technologies Used

- **Python 3.8+**
- **Tkinter + ttk** (native GUI toolkit)
- **JSON** for structured data persistence
- **csv** module for interoperable data exchange
- **datetime** for automatic timestamp management
- Object-Oriented Programming with custom classes and methods

## Project Structure

```text
task-manager/
├── main.py          # Application entry point
├── gui           # GUI layer (Tkinter views and controllers)
    ├── app.py
├── datahandler          # Data layer (persistence and business logic)
    ├── data.py
├── model         # Domain model (Task class with serialization)
    ├── task.py
├── tasks.json       # Persistent storage (auto-generated)
└── README.md
```

## Installation and Execution

### Prerequisites (Ubuntu / Linux)

```bash
sudo apt update
sudo apt install python3-tk
```

## Requirements

- **Python 3.8 or higher**
- **Tkinter** (included by default with Python installations on Windows and macOS)
- On Linux: `python3-tk` package must be installed (`sudo apt install python3-tk`)

The application is fully cross-platform and has been tested on:

- Windows
- macOS
- Linux (Ubuntu)

## Running the application (Ubuntu/Linux)

```bash
git clone https://github.com/Bether12/task-manager.git
cd task-manager
python3 main.py
```
