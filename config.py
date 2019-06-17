import os

config = {}

config['token_id'] = os.environ.get('TOKEN_ID','')
config["login_token"] = os.environ.get('LOGIN_TOKEN','')
config["domain"] = os.environ.get('DOMAIN','')
config["sub_domain"] = os.environ.get('SUB_DOMAIN','')
config['interval'] = os.environ.get('INTERVAL', 120)