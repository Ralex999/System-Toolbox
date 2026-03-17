# 🛠 System Maintenance & Diagnostic Tool (SMDT)

A lightweight, modular utility for Windows system optimization, diagnostic reporting, and package management automation. 

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

## 📖 Overview
This tool automates routine system administration tasks, combining low-level network diagnostics with high-level software management via Winget integration.

## 🖼 Preview
![App Screenshot](System-Toolbox-main.png)

## 🚀 Key Features
- **Interactive Menu:** Simple console interface for quick navigation.
- **Quick Diagnostic:** Combined DNS cache flushing and automatic Temporary File cleanup.
- **Software Management:** Fully automated Winget updates (including pinned/unknown apps) and "pin" management.
- **System Hygiene:** Deep cleanup of temporary directories and system logs via `cleaner.py`.

## 🛠 Installation & Usage
1. Ensure you have **Python 3.8+** installed.
2. Clone the repository:
```bash
git clone [https://github.com/Ralex999/System-Toolbox.git](https://github.com/Ralex999/System-Toolbox.git)
cd System-Toolbox
Run the desired tool (Administrator recommended):

Bash
python maintenance.py
# or
python cleaner.py
Created by Ralex999
