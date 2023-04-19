<!--
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2023/4/19 17:23
# @Author: doi
# @email : me@coo.lol
# @File  : README.md
-->

# Gmail Scanner

Gmail Scanner is a Gmail mailbox scanner.

## Description

Gmail Scanner has a multi-process mode that is very fast, and how fast it is depends on the performance of your machine.

The program will return only one results:

- `Unregistered`: It means that the Gmail is not registered or is **blocked**.

## Update

### 1.0.1

- Fixed some bug

### 1.0.0

- Record results to a csv file.

## Usage

**You need to install `gmail_scanner` before.**

```bash
pip install gmail_scanner
```

### Lite Mode

1. Create a new `.py` file with the following codes.

```python
from gmail_scanner.gmail_scanner import check_one_gmail

# Only Print Unregistered Result
# admin is email prefix
check_one_gmail(f"admin001")
```

2. If you want to scan a lots of Gmail, you can use the following codes.

```python
from gmail_scanner.gmail_scanner import scan_int_single, scan_int_multi

# single process mode(slow) to scan 6-digit gmail mailboxes
start_num = 0
end_num = 999999
email_length = 6
output_file = f'results.csv'
scan_int_single(start_num, end_num, email_length, output_file)

# multi process mode(fast) to scan 6-digit gmail mailboxes
start_num = 0
end_num = 999999
email_length = 6
output_file = f'results.csv'
batch_num = 1000
process_num = 20
scan_int_multi(start_num, end_num, email_length, output_file, batch_num, process_num)

```

## PyPi

<a href="https://pypi.org/project/GmailScanner/"><img src="https://img.shields.io/badge/Pypi-000000?style=for-the-badge&logo=pypi&logoColor=red" /></a>

## Docker

```bash
git clone https://github.com/Annihilater/gmail_scanner
cd gmail_scanner
cp .env.example .env
touch results.csv

# edit the .env file

docker-compose up -d
```

## Author

**GmailScanner** © [coo](https://github.com/Annihilater), Released under the [MIT](./LICENSE) License.<br>

