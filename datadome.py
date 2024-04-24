import random
import time
import base64

from browserforge.fingerprints import Screen, FingerprintGenerator


class DataDome:
    def __init__(self, ddv="4.25.0", ddk="your datadome key"):
        self.__ddv = ddv
        self.__ddk = ddk
        self.__screen = Screen(
            min_width=1280, max_width=5120, min_height=720, max_height=2880
        )
        self.__headers = FingerprintGenerator(
            browser=("chrome", "firefox", "safari", "edge"),
            os=("windows", "macos"),
            device="desktop",
            locale=("zh-CN", "en"),
            screen=self.__screen,
            http_version=2,
            strict=True,
            mock_webrtc=True,
        )
        self.__temps = self.__headers.generate()

    def build(self, url):
        stcfp = f"""ps://js.datadome.co/tags.js?id={self.__ddk}:2:90854)
    at https://js.datadome.co/tags.js?id={self.__ddk}:2:53225"""
        return {
            "headers": {
                "Content-type": "application/x-www-form-urlencoded",
                "Host": "api-js.datadome.co",
                "Origin": url,
                "Referer": url,
                "Accept-Encoding": self.__temps.headers.get("Accept-Encoding"),
                "Accept-Language": self.__temps.headers.get("Accept-Language"),
                "Sec-Ch-Ua": self.__temps.headers.get("sec-ch-ua"),
                "Sec-Ch-Ua-Mobile": self.__temps.headers.get("sec-ch-ua-mobile"),
                "Sec-Ch-Ua-Platform": self.__temps.headers.get("sec-ch-ua-platform"),
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "User-Agent": self.__temps.headers.get("User-Agent"),
                "Upgrade-Insecure-Requests": self.__temps.headers.get(
                    "Upgrade-Insecure-Requests"
                ),
            },
            "payload": {
                "ddv": self.__ddv,
                "eventCounters": [],
                "jsType": "ch",
                "ddk": self.__ddk,
                "request": "%2F",
                "responsePage": "origin",
                "cid": "null",
                "Referer": url,
                "jsData": {
                    "ttst": f"{random.randint(10, 99)}.{random.randint(1000000000000, 9000000000000)}",
                    "ifov": "false",
                    "hc": self.__temps.navigator.hardwareConcurrency,
                    "br_oh": self.__temps.screen.outerHeight,
                    "br_ow": self.__temps.screen.outerWidth,
                    "ua": self.__temps.headers.get("User-Agent"),
                    "wbd": "false",
                    "dp0": "true",
                    "tagpu": f"{random.randint(10, 99)}.{random.randint(1000000000000, 9000000000000)}",
                    "wdif": "false",
                    "wdifrm": "false",
                    "npmtm": "false",
                    "br_h": self.__temps.screen.height,
                    "br_w": self.__temps.screen.width,
                    "isf": "false",
                    "nddc": 1,
                    "rs_h": self.__temps.screen.availHeight,
                    "rs_w": self.__temps.screen.availWidth,
                    "rs_cd": 24,
                    "phe": "false",
                    "nm": "false",
                    "jsf": "false",
                    "lg": self.__temps.navigator.language,
                    "pr": self.__temps.screen.devicePixelRatio,
                    "ars_h": self.__temps.screen.availHeight,
                    "ars_w": self.__temps.screen.availWidth,
                    "tz": -480,
                    "str_ss": "true",
                    "str_ls": "true",
                    "str_idb": "true",
                    "str_odb": "false",
                    "plgod": "false",
                    "plg": random.randint(5, 14),
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
                    "vnd": self.__temps.navigator.vendor or "NA",
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
                    "dvm": self.__temps.navigator.deviceMemory,
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
                    "stcfp": base64.b64encode(stcfp.encode("utf-8")),
                    "ckwa": "true",
                    "prm": "true",
                    "tzp": "Asia/Shanghai",
                    "cvs": "true",
                    "usb": "defined",
                    "glvd": self.__temps.videoCard.vendor or "NA",
                    "glrd": self.__temps.videoCard.renderer or "NA",
                    "wwl": "false",
                    "jset": int(time.time()),
                },
            },
        }

    @staticmethod
    def cookies(cookie_str):
        parts = cookie_str.split("; ")
        cookie_dict = {}
        for part in parts:
            if "=" in part:
                key, value = part.split("=", 1)
                cookie_dict[key.lower()] = value

        cookie_key = "datadome"
        cookie_value = cookie_dict.get(cookie_key)
        cookie_domain = cookie_dict.get("domain")
        cookie_path = cookie_dict.get("path")

        return {
            "key": cookie_key,
            "value": cookie_value,
            "domain": cookie_domain,
            "path": cookie_path,
        }
