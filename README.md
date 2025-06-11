# 🔍 Python Port Scanner

A simple command-line TCP port scanner built in Python. This tool allows you to scan the most common ports (1–1024) on a target IP address or hostname to identify open ports. It’s a great beginner-friendly project for anyone learning about networking or cybersecurity.

---

## 🎯 Project Goals

- Learn how to use Python’s built-in `socket` module for networking tasks.
- Understand the basics of TCP port scanning and how open ports are identified.
- Create a functional cybersecurity tool using basic Python skills.
- Demonstrate scripting and networking knowledge in a portfolio-ready project.

---

## 🛠 Tools Needed

- [Python 3.x](https://www.python.org/downloads/)
- Terminal or command line access
- Code editor (e.g., [VS Code](https://code.visualstudio.com/))
- Git and GitHub account

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## ✨ Features

- Scans TCP ports from 1 to 1024
- Displays which ports are open
- Resolves hostnames to IP addresses
- Lightweight and beginner-friendly
- Easily extendable (threading, service detection, etc.)

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/taraddei/PortScanner.git
```

2. Navigate to the project directory:

```bash
cd PortScanner
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python port_scanner.py -t <targets> [-p <port-range>] [-T <timeout>] [-n <num-threads>] [-o <output>] [-v]
```

---

## 🧩 Options

| Option             | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `-t`, `--targets`   | Specify the target IP addresses or domain names (**required**)              |
| `-p`, `--port-range`| Port range to scan (e.g., `1-100` or `all`). Default: `1-100`               |
| `-T`, `--timeout`   | Timeout value in seconds. Default: `1.0`                                    |
| `-n`, `--num-threads`| Number of threads to use. Default: `10`                                   |
| `-o`, `--output`    | Output file to save results (e.g., `output.json`)                           |
| `-v`, `--verbose`   | Enable verbose output                                                       |

---

## 📌 Examples

✅ Scan a single target for open ports (default range):
```bash
python port_scanner.py -t 192.168.1.1
```

✅ Scan multiple targets and save results:
```bash
python port_scanner.py -t example.com 192.168.1.1 -p 1-65535 -o results.json
```

✅ Enable verbose output:
```bash
python port_scanner.py -t 192.168.1.1 -v
```

---

## 🧠 Purpose

The purpose of this project is to provide a simple yet effective TCP port scanning tool that allows users to scan one or more target IP addresses or domain names for open ports.

It is designed to be:

- 🧩 Versatile
- ⚡ Fast
- 📊 Informative

Whether you are:

- A **network administrator**
- A **security professional**
- Or a **curious learner**

This tool helps you identify open ports and gather insights into services running on them.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome! Feel free to fork this repo, open issues, or submit pull requests.

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---

## 📫 Contact

Created by **Angela Taraddei**  
📧 [angelamtaraddei@gmail.com](mailto:angelamtaraddei@gmail.com)  
🌐 [GitHub Profile](https://github.com/taraddei)

---

> 💡 *"Hackers don’t need names or proximity—just opportunity.”
― Robert Mueller, Former Director, FBI."*

