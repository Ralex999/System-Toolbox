# 🛠 System Maintenance & Diagnostic Tool (SMDT)

A lightweight, modular utility for Windows system optimization, diagnostic reporting, and package management automation. 

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

## 📖 Overview
This tool automates routine system administration tasks, combining low-level network diagnostics with high-level software management via Winget and PowerShell integration.

## 🚀 Key Features
- **Network Diagnostic:** Instant DNS cache flushing and Winsock reset.
- **Hardware Monitoring:** Thermal and power consumption tracking via platform-specific metrics.
- **Software Management:** Fully automated Winget updates, including application "pinning" to prevent unwanted version changes.
- **System Hygiene:** Automated cleanup of temporary directories and system logs.
- **Stability:** Quick creation of system restore points before critical changes.

## 🛠 Installation
1. Ensure you have Python 3.8+ installed.
2. Clone the repository:
```bash
git clone [https://github.com/Ralex999/Technical-Notes.git](https://github.com/Ralex999/Technical-Notes.git)
cd Technical-Notes
python maintenance.py
