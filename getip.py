import requests
import logging

def get_ip():
    return (
        get_ip_by_ipip()
        or get_ip_by_taobaoip()
        or get_ip_by_httpbin()
    )

def get_ip_by_ipip():
    url = 'http://myip.ipip.net/ip'
    status_code = None
    try:
        resp = requests.get(url, timeout=5)
        status_code = resp.status_code
        return resp.json().get('ip')
    except Exception as e:
        logging.warning("get_ip_by_ipip FAILED, error: [%s] %s" % (status_code, str(e)))
        return None

def get_ip_by_taobaoip():
    url = 'http://ip.taobao.com/service/getIpInfo2.php?ip=myip'
    status_code = None
    try:
        resp = requests.get(url, timeout=5)
        status_code = resp.status_code
        return resp.json()['data'].get('ip')
    except Exception as e:
        logging.warning("get_ip_by_taobaoip FAILED, error: [%s] %s" % (status_code, str(e)))
        return None

def get_ip_by_httpbin():
    url = 'http://www.httpbin.org/ip'
    status_code = None
    try:
        resp = requests.get(url, timeout=5)
        status_code = resp.status_code
        return resp.json().get('origin').split(',')[0]
    except Exception as e:
        logging.warning("get_ip_by_httpbin FAILED, error: [%s] %s" % (status_code, str(e)))
        return None