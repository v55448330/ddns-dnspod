# -*- coding: utf-8 -*-

from getip import get_ip
from config import config
import requests
import logging
import time

def header():
    h = {}
    return h

def get_record():
    url = 'https://dnsapi.cn/Record.List'
    status_code = None
    params = {
        'login_token': config['token_id'] + ',' + config['login_token'],
        'format': 'json',
        'domain': config['domain'] 
    }
    try:
        req = requests.post(url, timeout=5, data=params, headers=header())
        status_code = req.status_code
        resp = req.json()
        if resp['status']['code'] != "1":
            logging.warning("get_record_id FAILED, error: [%s] %s" % (status_code, resp['status']['message']))
            return None
            
    except Exception as e:
        logging.warning("get_record_id FAILED, error: [%s] %s" % (status_code, str(e)))
        return None

    # print(resp)
    records = resp.get('records', {})
    for item in records:
        if item.get('name') == config['sub_domain']:
            return { 'record_id': item.get('id'), 'record_ip': item.get('value') }
    return None

def modify_record(id, ip):
    url = 'https://dnsapi.cn/Record.Modify'
    status_code = None
    params = {
        'login_token': config['token_id'] + ',' + config['login_token'],
        'format': 'json',
        'domain': config['domain'],
        'sub_domain': config['sub_domain'],
        'record_line': '默认',
        'record_type': 'A',
        'record_id': id,
        'value': ip
    }
    try:
        req = requests.post(url, timeout=5, data=params, headers=header())
        status_code = req.status_code
        resp = req.json()
        if resp['status']['code'] != "1":
            logging.warning("modify_record FAILED, error: [%s:%s][%s] %s" % (id, ip, status_code, resp['status']['message']))
            return None
            
    except Exception as e:
        logging.warning("modify_record FAILED, error: [%s:%s][%s] %s" % (id, ip, status_code, str(e)))
        return None

    logging.info("modify_record SUCCESSED, info: [%s.%s => %s][%s] ok" % (config['sub_domain'], config['domain'], ip, status_code))
    # print(resp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s : %(message)s')
    logging.info("watching ip for ddns: %s.%s" % (config['sub_domain'], config['domain']))

    while True:
        record = get_record()
        current_ip = get_ip()
        record_ip = record.get('record_ip')
        record_id = record.get('record_id')
        interval = int(config['interval'])
        if current_ip:
            if current_ip != record_ip:
                logging.info('ip address change detected [%s][%s]' % (record_ip, current_ip))
                modify_record(record_id, current_ip)
            else:
                logging.info('no change of ip address')
        else:
            logging.error('get current ip FAILED.')
        
        logging.info('wait %s seconds and try again', str(interval))
        time.sleep(interval)

