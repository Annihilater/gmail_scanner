#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2023/4/19 17:17
# @Author: doi
# @email : me@coo.lol
# @File  : gmail_scanner.py
import json
import time

import requests

from multiprocessing import Pool

from tqdm import tqdm


def current_time() -> str:
    """
    get current time
    :return:
    """
    current_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return current_time_str


def check_one_gmail(email_prefix: str, output_file: str = None) -> dict:
    """
    Check if a Gmail account has been registered.
    Write the check result to a file.
    :param email_prefix:
    :param output_file:
    :return:
    """
    url = "https://accounts.google.com/_/signup/webusernameavailability?hl=zh-CN&_reqid=1249874&rt=j"

    payload = f'flowEntry=SignUp&' \
              f'flowName=GlifWebSignIn&' \
              f'continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&' \
              f'f.req=%5B%22AEThLlx3MQIns_WOcEOy509Q8eFfe35zJfR2iiwvA-oBR8Wc2' \
              f'-6cfNt2gXDaDgj_JKeqWSJpuqoVYmAmmpkTgh7qznFL8vp69P0RHq6X63oHW_ONZEg0qk70AUvSHbp3geJ79ZjhfOoBLRgbHifKog' \
              f'TSDic-lyVK7FegThgAmTyh6AQDr2xPwfY2FbfjjBJ58DU3B8FpjOSs5rzaSy9Wjj8QGXSNzbvpJw%22%2C%22ji%22%2C%22zi%' \
              f'22%2C%22{email_prefix}%22%2Ctrue%2C%22S-2046227615%3A1681883470118772%22%2C1%5D&' \
              f'at=AFoagUWkNWOkr_V72SFvAU0nhHepNOtNhw%3A1681883470142&' \
              f'azt=AFoagUXPbVtj9mktkNpCyh1RGh_WiYGBDg%3A1681883470142&' \
              f'cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22JP%22%2Cnull%2Cnull' \
              f'%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull' \
              f'%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull' \
              f'%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull' \
              f'%2C0%2Cnull%2Cfalse%2C1%2C%22%22%2Cnull%2Cnull%2C2%5D&gmscoreversion=undefined '
    headers = {
        'X-Same-Domain': '1',
        'Google-Accounts-XSRF': '1',
        'DNT': '1',
        'Pragma': 'no-cache',
        'TE': 'trailers',
        'Cookie': 'NID=511; __Host-GAPS=1:8NujiPpthTsgGZt8eiFI8L2ReL-fp8RgzyCsl_SNmN1VYuZ3GmT3e5Jlz6G9taZL0EO3Do8BkcMyc4ulUSV1QFT1AhBHYQ:j1io_kwbD7fQ3z_G; SID=VgjnIyASrdWeTmCvb3BNbSxexE-4T0QBvNqL6kuKF09FgpMNP9oLnfDJd7De10nsGZQgPA.; __Secure-1PSID=VgjnIyASrdWeTmCvb3BNbSxexE-4T0QBvNqL6kuKF09FgpMNs4HBjMZOxPQ-nfJ7TQy1Ng.; __Secure-3PSID=VgjnIyASrdWeTmCvb3BNbSxexE-4T0QBvNqL6kuKF09FgpMN4RCm_UeeToZPEo6zXQLUvA.; LSID=o.myaccount.google.com|s.JP:VgjnI6JpkLI3Vc8KDhSjvwq_UIwF5Lol0lPxVQ7ofPx2AhSy3s8fDD42XeRN7XEcj7K3ow.; __Host-1PLSID=o.myaccount.google.com|s.JP:VgjnI6JpkLI3Vc8KDhSjvwq_UIwF5Lol0lPxVQ7ofPx2AhSy6kPpiAoan6CQyY0qqT-OUA.; __Host-3PLSID=o.myaccount.google.com|s.JP:VgjnI6JpkLI3Vc8KDhSjvwq_UIwF5Lol0lPxVQ7ofPx2AhSyT7lLAnyWNA0lA6TJydj-Tw.; HSID=Ajk-yzATe2jNQGUdA; SSID=AIBHpZzBVMpc2LnvY; APISID=Szc3ah-hpDwSu9Sa/AYqHmSIGtR4lsX9C9; SAPISID=CgIc7eJAwGJjxgl0/AX5clLxNTpRQpCDAo; __Secure-1PAPISID=CgIc7eJAwGJjxgl0/AX5clLxNTpRQpCDAo; __Secure-3PAPISID=CgIc7eJAwGJjxgl0/AX5clLxNTpRQpCDAo; ACCOUNT_CHOOSER=AFx_qI6unaxNhgcEpZQiKtH1VWlg4pavUBQY3EJcczT76dCrS6FX43I41zgef39RATU89sSWuILmNQz5JslQD_eQ03-hwOI7MDwTAHOHb-2eX-xJVPMMiTNABpLBj8Q51x2L1Si00DRqx6JCiEDSF5QjZxoym-pFMQl4j02Qm-pf5S7kQpseDWUnadQhD1v5J3zS5dR0bGDEptJgpznpxL3FzbgT4n5mTLwP48hEJpCRgjh31W-oOS71LoqFNp180cf_mPKFlJ1iHYrbroMznwTk0-M89dt9EWTfaODC5Gq1k_aOuzzgRc0; SIDCC=AP8dLtztFzrAY59ztvmfWvTSWhjwltwJFX7XiRK2eKQKqLgGqEtirnYS8m3CEOG0mOtzh6nV-w; __Secure-1PSIDCC=AP8dLtx8jtwsxyvmxNylKFEvOZvf7_EFTRuDL1tkEABevIIRtQPbdppCLsIPcPgtS9-TBJKV1g; __Secure-3PSIDCC=AP8dLtwBhwJvXjJFKJnXnM2vTpeh9NPTJi7Tw25rqq1xAMqv-RQ2060rcn-hehyJCs_fMd1YeQ; OTZ=6992807_24_24__24_; 1P_JAR=2023-04-19-02; SEARCH_SAMESITE=CgQIipgB; AEC=AUEFqZe0xU3KL46qACi8KcrYjyMz-vMJ4ldMssx7ywo8o7yCVno7JLUncqc; user_id=112367303070809737794',
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    start_time = time.time()
    response = requests.request("POST", url, headers=headers, data=payload)
    # response.txt example: ')]}\'[[["gf.wuar",2,[]],["e",2,null,null,47]]]'

    if response.status_code == 200:
        txt = response.text
        txt = txt.replace("\n", "")
        txt1 = txt.replace(")]}", "")
        text = txt1[1:]
        data = json.loads(text)
        # 1/True: unregistered，2/False: registered
        status = True if data[0][0][1] == 1 else False
    else:
        status, text = response.status_code, response.text

    if status:
        spent = round(time.time() - start_time, 4)
        text = f"{current_time()},{spent},{email_prefix},{status}\n"

        if output_file is not None:
            with open(output_file, mode='a') as f:
                f.write(text)

    result = {
        "domain": email_prefix,
        "status": status,
        "resp": text,
        "update_time": current_time(),
        "create_time": current_time(),
    }
    return result


def scan_int_single(start: int, end: int, email_length: int, output_file: str) -> None:
    """
    scan digital gmail for single process, slow
    :param start:
    :param end:
    :param email_length:
    :param output_file:
    :return:
    """
    for i in range(start, end):
        email_prefix = str(i).zfill(email_length)
        check_one_gmail(email_prefix, output_file)


def task(args: list) -> None:
    """
    task function for multiprocessing check
    :param args: [email_prefix, output_file]
    :return:
    """
    email_prefix, output_file = args
    check_one_gmail(email_prefix, output_file)


def scan_int_multi(start: int, end: int, email_length: int, output_file: str, batch: int = 1000,
                   processes: int = 4) -> None:
    """
    scan digital gmail for multi process, fast
    Because the number of gmail is too large, it is processed in batches,
    and each batch uses a multi-process method to check whether it is registered
    :param start:
    :param end:
    :param email_length:
    :param output_file:
    :param batch: default 1000, When processing in batches, the number of batches
    :param processes: default 4
    :return:
    """
    log_file_name = f"log/gmail_scanner_{current_time()}.log"

    current_batch = 1
    for i in range(start, end, batch):
        with open(log_file_name, mode='a', encoding='utf8') as f:
            text = f"current_batch: {current_batch} current_num: {i}\n"
            f.write(text)

        args = []
        for j in range(i, i + batch):
            email_prefix = str(j).zfill(email_length)
            args.append([email_prefix, output_file])

        with Pool(processes=processes) as pool:
            list((tqdm(pool.imap(task, args), total=len(args), desc='process')))
        current_batch += 1
