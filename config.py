#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2023/4/19 17:23
# @Author: doi
# @email : me@coo.lol
# @File  : config.py
"""
config model
"""
import yaml

with open("config.yml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

# one
CHECK_ONE = config['check_one']['turn_on']
ONE_OUTPUT_FILE = config['check_one']['output_file']
ONE_EMAIL_LENGTH = config['check_one']['email_length']
ONE_EMAIL_PREFIX_INT = str(config['check_one']['email_prefix_int']).zfill(ONE_EMAIL_LENGTH)

# single
CHECK_MANY_BY_SINGLE = config['check_many_by_single']['turn_on']
SINGLE_OUTPUT_FILE = config['check_many_by_single']['output_file']
SINGLE_START_NUM = config['check_many_by_single']['start_num']
SINGLE_END_NUM = config['check_many_by_single']['end_num']
SINGLE_EMAIL_LENGTH = config['check_many_by_single']['email_length']

# multi
CHECK_MANY_BY_MULTI = config['check_many_by_multi']['turn_on']
MULTI_OUTPUT_FILE = config['check_many_by_multi']['output_file']
MULTI_START_NUM = config['check_many_by_multi']['start_num']
MULTI_END_NUM = config['check_many_by_multi']['end_num']
MULTI_EMAIL_LENGTH = config['check_many_by_multi']['email_length']
MULTI_BATCH_NUM = config['check_many_by_multi']['batch_num']
MULTI_PROCESS_NUM = config['check_many_by_multi']['process_num']

# multi specific
CHECK_MANY_BY_MULTI_SPECIFIC = config['check_many_by_multi_specific']['turn_on']
SPECIFIC_MULTI_OUTPUT_FILE = config['check_many_by_multi_specific']['output_file']
SPECIFIC_MULTI_FORMAT = config['check_many_by_multi_specific']['format']
SPECIFIC_MULTI_BATCH_NUM = config['check_many_by_multi_specific']['batch_num']
SPECIFIC_MULTI_PROCESS_NUM = config['check_many_by_multi_specific']['process_num']
