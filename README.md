# 🛠 System Toolbox

[English](#english) | [Русский](#русский)

---

## English

A set of Python-based console tools for rapid network diagnostics, software management via Winget, and system cleaning. Built for those who prefer automation over routine.

### 🖼 Preview
![Preview](Screen.png)

### 🚀 Key Features

#### 1. Maintenance Tool (`maintenance.py`)
An interactive "Swiss Army knife" for software management:
* **Quick Diagnostic:** Rapid DNS cache flush to fix common connectivity issues.
* **Full Updates Check:** Scans for ALL available updates, including:
    * **Pinned** applications (version-locked).
    * **Unknown** versions (e.g., Brave, Chrome, Roblox).
* **Standard Upgrade:** One-click safe update for regular apps (respects your "Pin" settings).
* **Pin Management:** Freeze specific app versions to prevent unwanted updates.

#### 2. System Cleaner (`cleaner.py`)
A script for deep cleaning temporary files and system junk accumulated during Windows operation.

### 📦 Setup & Usage

**Requirements:**
* [Python 3.x](https://www.python.org/downloads/) installed.
* Windows 10/11 with `winget` (pre-installed by default).

**Run:**
Download the script and run it via terminal:
```bash
python maintenance.py
# or
python cleaner.py
⚠️ Note: Some features (like system component updates) may require running the terminal as Administrator.

Русский
Набор консольных инструментов на Python для быстрой диагностики сети, управления обновлениями через Winget и очистки системы. Создано для тех, кто предпочитает автоматизацию рутине.

🚀 Основные возможности
1. Maintenance Tool (maintenance.py)
Интерактивный комбайн для управления ПО:

Quick Diagnostic: Быстрая очистка DNS-кэша для исправления проблем с сетью.

Full Updates Check: Показывает абсолютно все доступные обновления, включая:

Программы с закрепленной версией (Pinned).

Программы с неизвестной версией (Unknown), такие как Brave, Chrome или Roblox.

Standard Upgrade: Безопасное обновление всех обычных приложений в один клик (не трогает ваши настройки Pin).

Pin Management: Возможность замораживать версии конкретных программ, чтобы Winget их не обновлял.

2. System Cleaner (cleaner.py)
Скрипт для глубокой очистки системы от временных файлов и мусора, который скапливается в процессе работы Windows.

📦 Установка и запуск
Требования:

Установленный Python 3.x.

Windows 10/11 с установленным winget.

Запуск:
Просто скачайте нужный скрипт и запустите его через терминал:

Bash
python maintenance.py
# или
python cleaner.py
⚠️ Важное примечание: Некоторые функции могут потребовать запуск терминала от имени Администратора.
