#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2023/4/19 17:23
# @Author: doi
# @email : me@coo.lol
# @File  : config.py
"""
config model
"""
import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

CHECK_ONE = os.getenv('CHECK_ONE')
CHECK_ONE = True if CHECK_ONE.lower() == 'true' else False

CHECK_MANY_BY_SINGLE = os.getenv('CHECK_MANY_BY_SINGLE')
CHECK_MANY_BY_SINGLE = True if CHECK_MANY_BY_SINGLE.lower() == 'true' else False

CHECK_MANY_BY_MULTI = os.getenv('CHECK_MANY_BY_MULTI')
CHECK_MANY_BY_MULTI = True if CHECK_MANY_BY_MULTI.lower() == 'true' else False

# one
ONE_OUTPUT_FILE = os.getenv('ONE_OUTPUT_FILE')
ONE_EMAIL_LENGTH = int(os.getenv('ONE_EMAIL_LENGTH'))
ONE_EMAIL_PREFIX_INT = str(os.getenv('ONE_EMAIL_PREFIX_INT')).zfill(ONE_EMAIL_LENGTH)

# single
SINGLE_OUTPUT_FILE = os.getenv('SINGLE_OUTPUT_FILE')
SINGLE_START_NUM = int(os.getenv('SINGLE_START_NUM'))
SINGLE_END_NUM = int(os.getenv('SINGLE_END_NUM'))
SINGLE_EMAIL_LENGTH = int(os.getenv('SINGLE_EMAIL_LENGTH'))

# multi
MULTI_OUTPUT_FILE = os.getenv('MULTI_OUTPUT_FILE')
MULTI_START_NUM = int(os.getenv('MULTI_START_NUM'))
MULTI_END_NUM = int(os.getenv('MULTI_END_NUM'))
MULTI_EMAIL_LENGTH = int(os.getenv('MULTI_EMAIL_LENGTH'))
MULTI_BATCH_NUM = int(os.getenv('MULTI_BATCH_NUM'))
MULTI_PROCESS_NUM = int(os.getenv('MULTI_PROCESS_NUM'))
