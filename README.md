# bypass-datadome
use python and go to bypass datadome tag.js

### 🍑 How to use (just v4.25.0)

```python
# use datadome.py

pip install browserforge

datadome = DataDome()
fake_data = datadome.build(website_url)
try:
    # you can use your reuqest client
    response = await self.request(
        "POST",
        "https://api-js.datadome.co/js/",
        data=fake_data["payload"],
        headers=fake_data["headers"]
    )
except Exception as e:
    raise Exception(f"🤺 Failed to get datadome cookies: {e}")
```

    Using bin mode, you can only obtain fake data. Therefore, you need to use your HTTP client to perform a `POST` request.
    Set `fake_data.headers` as your request headers and `fake_data.payload` as the body of the request, then send this data to the endpoint `https://api-js.datadome.co/js/` to obtain the cookies.

```bash
# use datadome_bin.py

pip install browserforge

$ python datadome_bin.py --ddv=4.25.0 --ddk=your_datadome_key -url=https://test.com
$ {
    "headers": {
        "Content-type": "application/x-www-form-urlencoded",
        "Host": "api-js.datadome.co",
        "Origin": "https://test.com",
        "Referer": "https://test.com",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN;q=1.0, en;q=0.9",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Upgrade-Insecure-Requests": "1"
    },
    "payload": {
        "ddv": "4.25.0",
        "eventCounters": [],
        "jsType": "ch",
        "ddk": "your datadome key",
        "request": "%2F",
        "responsePage": "origin",
        "cid": "null",
        "Referer": "https://test.com",
        "jsData": {
            "ttst": "44.2443093732577",
            "ifov": "false",
            "hc": 4,
            "br_oh": 1040,
            "br_ow": 1920,
            "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "wbd": "false",
            "dp0": "true",
            "tagpu": "47.1631073566124",
            "wdif": "false",
            "wdifrm": "false",
            "npmtm": "false",
            "br_h": 1080,
            "br_w": 1920,
            "isf": "false",
            "nddc": 1,
            "rs_h": 1040,
            "rs_w": 1920,
            "rs_cd": 24,
            "phe": "false",
            "nm": "false",
            "jsf": "false",
            "lg": "zh-CN",
            "pr": 1,
            "ars_h": 1040,
            "ars_w": 1920,
            "tz": -480,
            "str_ss": "true",
            "str_ls": "true",
            "str_idb": "true",
            "str_odb": "false",
            "plgod": "false",
            "plg": 14,
            "plgne": "true",
            "plgre": "true",
            "plgof": "false",
            "plggt": "false",
            "pltod": "false",
            "hcovdr": "false",
            "hcovdr2": "false",
            "plovdr": "false",
            "plovdr2": "false",
            "ftsovdr": "false",
            "ftsovdr2": "false",
            "lb": "false",
            "eva": 33,
            "lo": "false",
            "ts_mtp": 0,
            "ts_tec": "false",
            "ts_tsa": "false",
            "vnd": "Google Inc.",
            "bid": "NA",
            "mmt": "application/pdf,text/pdf",
            "plu": "PDF Viewer,Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,WebKit built-in PDF",
            "hdn": "false",
            "awe": "false",
            "geb": "false",
            "dat": "false",
            "med": "defined",
            "aco": "probably",
            "acots": "false",
            "acmp": "probably",
            "acmpts": "true",
            "acw": "probably",
            "acwts": "false",
            "acma": "maybe",
            "acmats": "false",
            "acaa": "probably",
            "acaats": "true",
            "ac3": "",
            "ac3ts": "false",
            "acf": "probably",
            "acfts": "false",
            "acmp4": "maybe",
            "acmp4ts": "false",
            "acmp3": "probably",
            "acmp3ts": "false",
            "acwm": "maybe",
            "acwmts": "false",
            "ocpt": "false",
            "vco": "",
            "vcots": "false",
            "vch": "probably",
            "vchts": "true",
            "vcw": "probably",
            "vcwts": "true",
            "vc3": "maybe",
            "vc3ts": "false",
            "vcmp": "",
            "vcmpts": "false",
            "vcq": "",
            "vcqts": "false",
            "vc1": "probably",
            "vc1ts": "true",
            "dvm": 8,
            "sqt": "false",
            "so": "landscape-primary",
            "wdw": "true",
            "cokys": "bG9hZFRpbWVzY3NpYXBwL=",
            "ecpc": "false",
            "lgs": "true",
            "lgsod": "false",
            "psn": "true",
            "edp": "true",
            "addt": "true",
            "wsdc": "true",
            "ccsr": "true",
            "nuad": "true",
            "bcda": "true",
            "idn": "true",
            "capi": "false",
            "svde": "false",
            "vpbq": "true",
            "ucdv": "false",
            "spwn": "false",
            "emt": "false",
            "bfr": "false",
            "dbov": "false",
            "cfpfe": "ZnVuY3Rpb24oKXt2YXIgdD1kb2N1bWVudFsnXHg3MVx4NzVceDY1XHg3Mlx4NzlceDUzXHg2NVx4NmNceDY1XHg2M1x4NzRceDZmXHg3MiddKCdceDYyXHg3Mlx4NmZceDc3XHg3M1x4NjVceDcyXHg2Nlx4NmNceDZmXHg3N1x4MmRceDYzXHg2Zlx4NmVceDc0XHg2",
            "stcfp": "cHM6Ly9qcy5kYXRhZG9tZS5jby90YWdzLmpzP2lkPTE5RjEzNkNFQkM3RDg2Q0ZGNjM1MTEzQUQyQThFQToyOjkwODU0KQogICAgYXQgaHR0cHM6Ly9qcy5kYXRhZG9tZS5jby90YWdzLmpzP2lkPTE5RjEzNkNFQkM3RDg2Q0ZGNjM1MTEzQUQyQThFQToyOjUzMjI1",
            "ckwa": "true",
            "prm": "true",
            "tzp": "Asia/Shanghai",
            "cvs": "true",
            "usb": "defined",
            "glvd": "Google Inc. (Intel)",
            "glrd": "ANGLE (Intel, Intel(R) UHD Graphics (0x00009B41) Direct3D11 vs_5_0 ps_5_0, D3D11)",
            "wwl": "false",
            "jset": 1713976111
        }
    }
}
```

```bash
# use bin/datadome

$ ./bin/datadome --ddv=4.25.0 --ddk=your_datadome_key -url=https://test.com

$ { ... }
```