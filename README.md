# 🗂️ File Handling Toolkit
> **Five powerful file management utilities — all in one terminal-based Python application for handling large biological files.**

![Python](https://img.shields.io/badge/python-3.10.11-blue)
![OOP](https://img.shields.io/badge/Architecture-OOP-yellow)
![Pathlib](https://img.shields.io/badge/Library-Pathlib-informational)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Table of Contents

- [What Is This](#what-is-this)
- [Tools & Technologies](#tools--technologies)
- [Project Architecture](#project-architecture)
- [Application Workflow](#application-workflow)
- [Sample Output](#sample-output)
- [Exception Handling Strategy](#exception-handling-strategy)
- [Key Concepts Demonstrated](#key-concepts-demonstrated)
- [How to Run](#how-to-run)
- [Future Roadmap](#future-roadmap)
- [Author & Contact](#author--contact)
- [License](#license)

---

## What Is This?

**File Handling Toolkit** is a terminal-based Python application that combines five essential file management utilities into a single menu-driven program.

Whether you need to organize a messy folder, find duplicate files wasting your storage, manage contacts, track file versions, or back up important data — this toolkit handles it all from the command line.

Built entirely in Python using Object-Oriented Programming, each utility is a self-contained class with clean separation of concerns and robust input validation.

> _"Five tools. One program. Zero clutter."_

---

## Tools & Technologies

| Tool | Role |
|------|------|
| **Python 3.10.11** | Core programming language |
| **pathlib** | Modern file system path handling |
| **shutil** | File moving and copying operations |
| **hashlib** | SHA-256 hashing for duplicate detection |
| **shelve** | Persistent contact storage |
| **zipfile** | Compressed backup creation |
| **send2trash** | Safe file deletion to recycle bin |
| **OOP** | Class-based modular architecture |

---

## Project Architecture
```
file-handling/
│
├── main.py                        # Entry point & menu system
│
├── file_organizer.py              # Module 1: File Organizer
│   ├── __init__()                 # Path input
│   ├── path_validation()          # Validates absolute directory path
│   ├── file_scanning()            # Scans & moves files into type folders
│   └── organiztion()              # Orchestrator method
│
├── duplicate_file_finder.py       # Module 2: Duplicate File Finder
│   ├── __init__()                 # Path input & validation
│   ├── path_scanning()            # Groups files by size
│   ├── files_filtering()          # Keeps only size-matched groups
│   ├── hashing()                  # Generate hashes for files (used later to compare content)
│   └── file_finder()              # Orchestrator method
│
├── user_info.py                   # Module 3: Contact Book
│   ├── __init__()                 # Initializes shelve file
│   └── contact_info()             # Add / View / Update / Delete contacts
│
├── versioned_file_manager.py      # Module 4: Version Tracker
│   ├── __init__()                 # Path input
│   ├── path_validation()          # Validates absolute directory path
│   ├── versioned()                # Monitors & copies modified files
│   └── file_manager()             # Orchestrator method
│
├── backup.py                      # Module 5: Backup System
│   ├── __init__()                 # Source & destination input + validation
│   └── back_up_process()          # Creates or appends compressed ZIP backup
│
└── README.md                      # Project documentation

```
---

## Application Workflow
```
Program starts → main.py
        │
        ▼
┌──────────────────────────┐
│        Main Menu         │
│  1. File Organizer       │
│  2. Duplicate Finder     │
│  3. Contact Book         │
│  4. Version Tracker      │
│  5. Backup               │
│  6. Exit                 │
└──────────────────────────┘
        │
        ▼
[ Valid choice 1-5? ] ──No -> [ "Invalid choice" → loop back ]
        │ Yes
        ▼
[ Module class initializes ]
        │
        ▼
[ Path / Input validation ]
Invalid -> [ Re-prompt user ]
        │ Valid
        ▼
[ Core logic executes ]
        │
        ▼
[ Results displayed in terminal ]
        │
        ▼
[ Program exits cleanly ]
```

---

## Sample Output

**Main Menu:**
`Example`

```
Welcome! Choose an option:
1. File organization
2. Duplicated files analysis
3. Contact book
4. Versional file managing
5. Backup
6. Exit
Enter your choice: 1
```

**File Organizer:**
```
Give a path: /home/user/Downloads
It is a valid absolute directory path.
Files moved into: PDF  PNG  MP4  DOCX  ZIP  NoExtension
```

**Duplicate Finder:**
```
Give a path: /home/user/Documents
Duplicate files:
  Index 1: /home/user/Documents/report.pdf
  Index 2: /home/user/Documents/report1.pdf
Enter the numbers of the files you want to delete, separated by commas (or press Enter to skip): 2
Deleted: /home/user/Documents/backup/report1.pdf
```

**Contact Book:**
```
What do you want to choose first:
 Add / View / Update / Delete / Exit
add
Enter your name: Alax
Enter your phone number: 123456
Enter your email: alax@email.com
Contact "Alax" added successfully.
```

**Version Tracker:**
```
Give a path: /home/user/Projects
It is a valid absolute directory path.
Monitoring for file changes every 5 seconds...
Versioned copy saved: report_2025_01_28.docx
```

**Backup:**
```
Give a source path: /home/user/Projects
Give a destination path: /home/user/Backups
Backup completed: /home/user/Backups/backup_25_01_28.zip
```

---

## Exception Handling Strategy

| Scenario | Handling |
|----------|----------|
| Invalid directory path | Re-prompts user until valid path is entered |
| Non-absolute path entered | Rejected with clear message |
| Invalid backup source path | `ValueError` raised, caught in `main.py` |
| Invalid backup destination path | `ValueError` raised, caught in `main.py` |
| Duplicate index out of range | Bounds check applied, user notified |
| Non-integer input in duplicate menu | `ValueError` caught, item skipped gracefully |
| Version folder already exists | Handled with `exist_ok=True` |
| Backup ZIP already exists | Opens in append mode, skips existing files |
| Contact not found | Prints clear message, returns to menu |
| Invalid contact menu option | Prints error, loops back to menu |
| Invalid main menu choice | Prints error, loops back to menu |

---

## Key Concepts Demonstrated

1. **Object-Oriented Programming**: Each utility is a clean, self-contained class
2. **File System Operations**: `pathlib` and `shutil` for modern path handling
3. **SHA-256 Hashing**: Accurate duplicate detection beyond just file size
4. **Persistent Storage**: `shelve` for contact data that survives program restarts
5. **ZIP Compression**: Incremental backup with append mode support
6. **Input Validation**: Multi-level validation with re-prompt loops
7. **Exception Handling**: `ValueError` raised in constructors, caught in `main.py`
8. **Safe Deletion**: `send2trash` sends files to recycle bin, not permanent delete
9. **Version Tracking**: Modification time comparison for file change detection

---

## How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/file-handling.git
cd file-handling
```

**2. Install required library:**
```bash
pip install send2trash
```

**3. Run:**
```bash
python main.py
```

**4. How to use:**
- Choose a number from the menu (1–6)
- Follow the terminal prompts for each tool
- Enter **absolute paths** when asked (e.g. `C:\User\Alax\Doc` on Windows)
- Contact book data is saved automatically between sessions

---

## Future Roadmap

| Feature | Description |
|---------|-------------|
| 📊 Summary Report | Show count of files organized, duplicates removed, space saved |
| 🔍 Search in Contacts | Search contact book by name or phone number |
| 📁 Recursive Organizer | Organize files inside subfolders as well |

---

## Author & Contact

**Sana Aziz Sial**  
Biotechnologist and Bioinformatician
- 🎓 [University of Veterinary and Animal Sciences](https://www.uvas.edu.pk/)
- 📧 [Email](sanaazizsial@gmail.com)
- 🐙 [GitHub](https://github.com/genome-miner)
- 🔗 [LinkedIn](in/sana-aziz-sial-73b189265)

---

<div align="center">

⭐ If you found this useful, consider giving it a star!

_Built with Python & Biopython • Enzyme data from Bio.Restriction_

</div>


## License

This project is licensed under the [MIT License](https://github.com/genome-miner/file_handling/blob/main/LICENSE).
