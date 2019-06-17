## 使用 
```
docker run -d --restart=always \
    -e 'TOKEN_ID=<you API token id>' \
    -e 'LOGIN_TOKEN=<you API token>' \
    -e 'DOMAIN=<you domain>' \
    -e 'SUB_DOMAIN=<you sub Domain>' \
    -e 'INTERVAL'=120 \
    v55448330/ddns-dnspod:v0.1
```
> 创建 DNSPOD.cn API Token 请参考 [文档](https://support.dnspod.cn/Kb/showarticle/tsid/227/)
