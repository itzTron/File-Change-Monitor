# File Change Monitor
*COMPANY*: CODTECH IT SOLUTIONS |
*NAME*: TANMOY NASKAR |
*INTERN ID*: CT08VMU |
*DOMAIN*: Cyber Security & Ethical Hacking. | 
*DURATION*: 4 WEEKS |
*MENTOR*: NEELA SANTOSH |

## Description
The **File Change Monitor** is a Python script that monitors changes in specified files. It calculates and compares hash values to detect modifications and logs events such as file modifications and deletions.

## Features
- Monitors file modifications in real-time
- Detects file deletions
- Logs changes to a file (`file_changes.log`)
- Supports both command-line arguments and interactive input
- Graceful exit using `Ctrl + C`

---

## Installation
### **Prerequisites**
Ensure you have **Python 3** installed. Check by running:
```bash
python3 --version
```

### **Clone the Repository**
```bash
git clone https://github.com/itzTron/File-Change-Monitor.git
cd file_monitor_1.py
```

---

## Usage

## Give permission:
```bash
chmod +x file_monitor_1.py
```
### **1. Running the Script with Command-Line Arguments**
Run the script and specify the files you want to monitor:
```bash
python3 file_monitor_1.py /path/to/file1 /path/to/file2
```
## Example Image:
![Image](https://github.com/user-attachments/assets/b03dedcf-6c47-458b-87ac-b0decb8617c1)
Example:
```bash
python3 file_monitor_1.py /home/user/document.txt /var/log/syslog
```

### **2. Running the Script with Interactive Input**
Simply run the script without arguments:
```bash
python3 file_monitor_1.py
```
It will prompt you to enter file paths:
```
Enter file names to monitor (comma-separated):
/home/user/document.txt, /var/log/syslog
```
## Example Image:
![Image](https://github.com/user-attachments/assets/67f21168-3123-4c78-b056-bd6493da28ba)
---

## Stopping the Script
To stop monitoring, press:
```bash
Ctrl + C
```
It will print:
```
Monitoring stopped by user.
```

---

## Log File
All file changes are logged in `file_changes.log`. To view the log:
```bash
cat file_changes.log
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## Contact
For any inquiries, please reach out via email: tanmoyn681@gmail.com or open an issue in this repository.

