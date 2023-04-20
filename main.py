#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2023/4/19 15:05
# @Author: doi
# @email : me@coo.lol
# @File  : t1.py
import datetime

from config import CHECK_ONE, CHECK_MANY_BY_SINGLE, CHECK_MANY_BY_MULTI, ONE_EMAIL_PREFIX_INT, ONE_OUTPUT_FILE, \
    SINGLE_START_NUM, SINGLE_END_NUM, SINGLE_EMAIL_LENGTH, SINGLE_OUTPUT_FILE, MULTI_START_NUM, MULTI_END_NUM, \
    MULTI_EMAIL_LENGTH, MULTI_OUTPUT_FILE, MULTI_BATCH_NUM, MULTI_PROCESS_NUM, CHECK_MANY_BY_MULTI_SPECIFIC, \
    SPECIFIC_MULTI_FORMAT, SPECIFIC_MULTI_OUTPUT_FILE, SPECIFIC_MULTI_BATCH_NUM, SPECIFIC_MULTI_PROCESS_NUM
from gmail_scanner.gmail_scanner import check_one_gmail, scan_int_single, scan_int_multi, scan_int_multi_specific


def main():
    start_time = datetime.datetime.now()
    if CHECK_ONE:
        check_one_gmail(ONE_EMAIL_PREFIX_INT, ONE_OUTPUT_FILE)

    if CHECK_MANY_BY_SINGLE:
        scan_int_single(SINGLE_START_NUM, SINGLE_END_NUM, SINGLE_EMAIL_LENGTH, SINGLE_OUTPUT_FILE)

    if CHECK_MANY_BY_MULTI:
        scan_int_multi(MULTI_START_NUM, MULTI_END_NUM, MULTI_EMAIL_LENGTH, MULTI_OUTPUT_FILE, MULTI_BATCH_NUM,
                       MULTI_PROCESS_NUM)

    if CHECK_MANY_BY_MULTI_SPECIFIC:
        scan_int_multi_specific(SPECIFIC_MULTI_FORMAT,
                                SPECIFIC_MULTI_OUTPUT_FILE,
                                SPECIFIC_MULTI_BATCH_NUM,
                                SPECIFIC_MULTI_PROCESS_NUM)

    spent = datetime.datetime.now() - start_time
    print(f"spent: {spent}")


if __name__ == '__main__':
    main()
