import random
import time
import base64
import json
import argparse

from browserforge.fingerprints import Screen, FingerprintGenerator

class DataDome:
    def __init__(self, ddv, ddk, url):
        self.__ddv = ddv
        self.__ddk = ddk
        self.__url = url
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

    def build(self):
        # DONT CHANGE THIS ==============================================
        stcfp = f"""ps://js.datadome.co/tags.js?id={self.__ddk}:2:90854)
    at https://js.datadome.co/tags.js?id={self.__ddk}:2:53225"""
        # DONT CHANGE THIS ==============================================
        return {
            "headers": {
                "Content-type": "application/x-www-form-urlencoded",
                "Host": "api-js.datadome.co",
                "Origin": self.__url,
                "Referer": self.__url,
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
                "Referer": self.__url,
                "jsData": {
                    "ttst": f"{random.randint(10, 99)}.{random.randint(1000000000000, 9000000000000)}",  # runtime
                    "ifov": "false",
                    "hc": self.__temps.navigator.hardwareConcurrency or "NA",  # Hardware Concurrency
                    "br_oh": self.__temps.screen.outerHeight,  # outer height of the browser window
                    "br_ow": self.__temps.screen.outerWidth,  # outer width of the browser window
                    "ua": self.__temps.headers.get("User-Agent"),  # user agent
                    "wbd": "false",  # determine if it is within an automated testing tool environment
                    "dp0": "true",
                    "tagpu": f"{random.randint(10, 99)}.{random.randint(1000000000000, 9000000000000)}", # could be associated with GPU operations
                    "wdif": "false",  # determine if an iframe's contentWindow is the same as the top-level window object
                    "wdifrm": "false",  # to check if an iframe is within the same context as the main page
                    "npmtm": "false",  # determine if the browser supports plugins
                    "br_h": self.__temps.screen.height,  # browser window height
                    "br_w": self.__temps.screen.width,  # browser window width
                    "isf": "false",  # determine if scrolling has reached the bottom (guess)
                    "nddc": 1,  # datadome cookie status
                    "rs_h": self.__temps.screen.availHeight or "NA",  # available screen height (guess)
                    "rs_w": self.__temps.screen.availWidth or "NA",  # available screen width (guess)
                    "rs_cd": 24,
                    "phe": "false",  # detect if PhantomJS exists
                    "nm": "false",
                    "jsf": "false",
                    "lg": self.__temps.navigator.language or "NA",  # browser language
                    "pr": self.__temps.screen.devicePixelRatio or "NA",  # screen's device pixel ratio
                    "ars_h": self.__temps.screen.availHeight or "NA",  # available screen height (guess)
                    "ars_w": self.__temps.screen.availWidth or "NA",  # available screen width (guess)
                    "tz": -480,  # timezone (new Date().getTimezoneOffset())
                    "str_ss": "true",  # !!window.sessionStorage
                    "str_ls": "true",  # !!window.localStorage
                    "str_idb": "true",  # !!window.indexedDB
                    "str_odb": "false",  # !!window.openDatabase（guess）
                    "plgod": "false",  # Plugin Object Definition
                    "plg": random.randint(5, 14),  # Plugin number（guess）
                    "plgne": "true",  # plugin-related detection
                    "plgre": "true",  # plugin-related detection
                    "plgof": "false",  # plugin-related detection
                    "plggt": "false",  # plugin-related detection
                    "pltod": "false",  # plugin-related detection
                    "hcovdr": "false",  # navigator.hardwareConcurrency
                    "hcovdr2": "false",  # navigator.hardwareConcurrency
                    "plovdr": "false",  # Performance/Load Validation/Detection Result
                    "plovdr2": "false",  # Performance/Load Validation/Detection Result
                    "ftsovdr": "false",  # Feature/Test/Support Validation/Detection Result
                    "ftsovdr2": "false",  # Feature/Test/Support Validation/Detection Result
                    "lb": "false",  # detect if it is a fake browser using navigator.userAgent and navigator.productSub
                    "eva": 33,
                    "lo": "false",  # detect if it is a fake browser by using navigator.userAgent, navigator.oscpu, and navigator.platform
                    "ts_mtp": 0,  # navigator.msMaxTouchPoints touch operation support on the device
                    "ts_tec": "false",  # document.createEvent("TouchEvent")
                    "ts_tsa": "false",  # window.ontouchstart
                    "vnd": self.__temps.navigator.vendor or "NA",  # window.navigator.vendor browser graphics rendering engine provider
                    "bid": "NA",  # window.navigator.browserId（guess）
                    "mmt": "application/pdf,text/pdf",  # window.navigator.mimeTypes
                    "plu": "PDF Viewer,Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,WebKit built-in PDF",
                    # plugins
                    "hdn": "false",  # !!document.hidden
                    "awe": "false",  # !!window.awesomium
                    "geb": "false",  # !!window.geb
                    "dat": "false",  # window.domAutomation
                    "med": "defined",  # window.navigator.mediaDevices supported is indicated as 'defined', unsupported is indicated as 'NA'
                    "aco": "probably",
                    "acots": "false",  # audio/ogg
                    "acmp": "probably",
                    "acmpts": "true",  # audio/mpeg
                    "acw": "probably",
                    "acwts": "false",  # audio/wav
                    "acma": "maybe",
                    "acmats": "false",  # audio/x-m4a
                    "acaa": "probably",
                    "acaats": "true",  # audio/aac
                    "ac3": "",
                    "ac3ts": "false",  # audio/3gpp
                    "acf": "probably",
                    "acfts": "false",  # audio/flac
                    "acmp4": "maybe",
                    "acmp4ts": "false",  # audio/mp4
                    "acmp3": "probably",
                    "acmp3ts": "false",  # audio/mp3
                    "acwm": "maybe",
                    "acwmts": "false",  # audio/wma
                    "ocpt": "false",  # canPlayType
                    "vco": "",
                    "vcots": "false",  # Video Codec Ogg Theora with MSE Support
                    "vch": "probably",
                    "vchts": "true",  # video/mp4
                    "vcw": "probably",
                    "vcwts": "true",  # video/webm
                    "vc3": "maybe",
                    "vc3ts": "false",  # video/3gpp
                    "vcmp": "",
                    "vcmpts": "false",  # video/mpeg
                    "vcq": "",
                    "vcqts": "false",  # video/quicktime
                    "vc1": "probably",
                    "vc1ts": "true",  # video/vc-1
                    "dvm": self.__temps.navigator.deviceMemory or "NA",  # navigator.deviceMemory
                    "sqt": "false",  # support for Sequentum
                    "so": "landscape-primary",  # device screen orientation
                    "wdw": "true",
                    "cokys": "bG9hZFRpbWVzY3NpYXBwL=",  # loadTimescsiapp
                    "ecpc": "false",  # might be detecting the Node environment
                    "lgs": "true",
                    "lgsod": "false",
                    "psn": "true",  # !!window.PermissionStatus
                    "edp": "true",  # !!window.EyeDropper
                    "addt": "true",  # !!window.AudioData
                    "wsdc": "true",  # !!window.WritableStreamDefaultController
                    "ccsr": "true",
                    "nuad": "true",  # !!window.NavigatorUAData
                    "bcda": "true",
                    "idn": "true",  # !(!window.Intl || !Intl.DisplayNames)
                    "capi": "false",  # detect some API capabilities of window.navigator
                    "svde": "false",  # !!window.SVGDiscardElement
                    "vpbq": "true",  # window.VideoPlaybackQuality Web video playback quality
                    "ucdv": "false",
                    "spwn": "false",  # !!window.spawn might be detecting child processes
                    "emt": "false",
                    "bfr": "false",
                    "dbov": "false",  # might be checking for browser debugging
                    "cfpfe": "ZnVuY3Rpb24oKXt2YXIgdD1kb2N1bWVudFsnXHg3MVx4NzVceDY1XHg3Mlx4NzlceDUzXHg2NVx4NmNceDY1XHg2M1x4NzRceDZmXHg3MiddKCdceDYyXHg3Mlx4NmZceDc3XHg3M1x4NjVceDcyXHg2Nlx4NmNceDZmXHg3N1x4MmRceDYzXHg2Zlx4NmVceDc0XHg2",
                    "stcfp": base64.b64encode(stcfp.encode("utf-8")).decode(),  # a stack trace containing ddk
                    "ckwa": "true",  # dd_testcookie
                    "prm": "true",  # navigator.permissions
                    "tzp": "Asia/Shanghai",
                    "cvs": "true",  # canvas
                    "usb": "defined",  # window.navigator.usb
                    "glvd": self.__temps.videoCard.vendor or "NA",  # webgl UNMASKED_VENDOR_WEBGL
                    "glrd": self.__temps.videoCard.renderer or "NA",  # webgl UNMASKED_RENDERER_WEBGL
                    "wwl": "false",
                    "jset": int(time.time()),
                },
            },
        }

    def output_json(self):
        data = self.build()
        return json.dumps(data, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fuck DataDome")
    parser.add_argument("--ddv", type=str, required=True, help="DataDome Version")
    parser.add_argument("--ddk", type=str, required=True, help="DataDome Key")
    parser.add_argument("--url", type=str, required=True, help="Target Website Url")
    args = parser.parse_args()

    datadome = DataDome(ddv=args.ddv, ddk=args.ddk, url=args.url)
    json_data = datadome.output_json()
    print(json_data)
