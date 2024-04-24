package utils

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log/slog"
	"net/http"
	"net/url"
	"os/exec"
	"visa/pkg/external/httpclient"
	"visa/pkg/external/httpclient/bogdanfinn"
)

type JSData struct {
	TTST     interface{} `json:"ttst"`
	IFOV     interface{} `json:"ifov"`
	HC       interface{} `json:"hc"`
	BrOh     interface{} `json:"br_oh"`
	BrOw     interface{} `json:"br_ow"`
	UA       interface{} `json:"ua"`
	WBD      interface{} `json:"wbd"`
	DP0      interface{} `json:"dp0"`
	TagPU    interface{} `json:"tagpu"`
	WDIF     interface{} `json:"wdif"`
	WDIFRM   interface{} `json:"wdifrm"`
	NPMTM    interface{} `json:"npmtm"`
	BrH      interface{} `json:"br_h"`
	BrW      interface{} `json:"br_w"`
	ISF      interface{} `json:"isf"`
	NDDC     interface{} `json:"nddc"`
	RsH      interface{} `json:"rs_h"`
	RsW      interface{} `json:"rs_w"`
	RsCd     interface{} `json:"rs_cd"`
	PHE      interface{} `json:"phe"`
	NM       interface{} `json:"nm"`
	JSF      interface{} `json:"jsf"`
	LG       interface{} `json:"lg"`
	PR       interface{} `json:"pr"`
	ArsH     interface{} `json:"ars_h"`
	ArsW     interface{} `json:"ars_w"`
	TZ       interface{} `json:"tz"`
	StrSs    interface{} `json:"str_ss"`
	StrLs    interface{} `json:"str_ls"`
	StrIdb   interface{} `json:"str_idb"`
	StrOdb   interface{} `json:"str_odb"`
	PLGOD    interface{} `json:"plgod"`
	PLG      interface{} `json:"plg"`
	PLGNE    interface{} `json:"plgne"`
	PLGRE    interface{} `json:"plgre"`
	PLGOF    interface{} `json:"plgof"`
	PLGGT    interface{} `json:"plggt"`
	PLTOD    interface{} `json:"pltod"`
	HCOVDR   interface{} `json:"hcovdr"`
	HCOVDR2  interface{} `json:"hcovdr2"`
	PLOVDR   interface{} `json:"plovdr"`
	PLOVDR2  interface{} `json:"plovdr2"`
	FTSOVDR  interface{} `json:"ftsovdr"`
	FTSOVDR2 interface{} `json:"ftsovdr2"`
	LB       interface{} `json:"lb"`
	EVA      interface{} `json:"eva"`
	LO       interface{} `json:"lo"`
	TsMtp    interface{} `json:"ts_mtp"`
	TsTec    interface{} `json:"ts_tec"`
	TsTsa    interface{} `json:"ts_tsa"`
	VND      interface{} `json:"vnd"`
	BID      interface{} `json:"bid"`
	MMT      interface{} `json:"mmt"`
	PLU      interface{} `json:"plu"`
	HDN      interface{} `json:"hdn"`
	AWE      interface{} `json:"awe"`
	GEB      interface{} `json:"geb"`
	DAT      interface{} `json:"dat"`
	MED      interface{} `json:"med"`
	ACO      interface{} `json:"aco"`
	ACOTS    interface{} `json:"acots"`
	ACMP     interface{} `json:"acmp"`
	ACMPTS   interface{} `json:"acmpts"`
	ACW      interface{} `json:"acw"`
	ACWTS    interface{} `json:"acwts"`
	ACMA     interface{} `json:"acma"`
	ACMATS   interface{} `json:"acmats"`
	ACA      interface{} `json:"acaa"`
	ACAATS   interface{} `json:"acaats"`
	AC3      interface{} `json:"ac3"`
	AC3TS    interface{} `json:"ac3ts"`
	ACF      interface{} `json:"acf"`
	ACFTS    interface{} `json:"acfts"`
	ACMP4    interface{} `json:"acmp4"`
	ACMP4TS  interface{} `json:"acmp4ts"`
	ACMP3    interface{} `json:"acmp3"`
	ACMP3TS  interface{} `json:"acmp3ts"`
	ACWM     interface{} `json:"acwm"`
	ACWMTS   interface{} `json:"acwmts"`
	OCPT     interface{} `json:"ocpt"`
	VCO      interface{} `json:"vco"`
	VCOTS    interface{} `json:"vcots"`
	VCH      interface{} `json:"vch"`
	VCHTS    interface{} `json:"vchts"`
	VCW      interface{} `json:"vcw"`
	VCWTS    interface{} `json:"vcwts"`
	VC3      interface{} `json:"vc3"`
	VC3TS    interface{} `json:"vc3ts"`
	VCMP     interface{} `json:"vcmp"`
	VCMPTS   interface{} `json:"vcmpts"`
	VCQ      interface{} `json:"vcq"`
	VCQTS    interface{} `json:"vcqts"`
	VC1      interface{} `json:"vc1"`
	VC1TS    interface{} `json:"vc1ts"`
	DVM      interface{} `json:"dvm"`
	SQT      interface{} `json:"sqt"`
	SO       interface{} `json:"so"`
	WDW      interface{} `json:"wdw"`
	COKYS    interface{} `json:"cokys"`
	ECPC     interface{} `json:"ecpc"`
	LGS      interface{} `json:"lgs"`
	LGSOD    interface{} `json:"lgsod"`
	PSN      interface{} `json:"psn"`
	EDP      interface{} `json:"edp"`
	ADDT     interface{} `json:"addt"`
	WSDC     interface{} `json:"wsdc"`
	CCSR     interface{} `json:"ccsr"`
	NUAD     interface{} `json:"nuad"`
	BCDA     interface{} `json:"bcda"`
	IDN      interface{} `json:"idn"`
	CAPI     interface{} `json:"capi"`
	SVDE     interface{} `json:"svde"`
	VPBQ     interface{} `json:"vpbq"`
	UCDV     interface{} `json:"ucdv"`
	SPWN     interface{} `json:"spwn"`
	EMT      interface{} `json:"emt"`
	BFR      interface{} `json:"bfr"`
	DBOV     interface{} `json:"dbov"`
	CFPFE    interface{} `json:"cfpfe"`
	STCFP    interface{} `json:"stcfp"`
	CKWA     interface{} `json:"ckwa"`
	PRM      interface{} `json:"prm"`
	TZP      interface{} `json:"tzp"`
	CVS      interface{} `json:"cvs"`
	USB      interface{} `json:"usb"`
	GLVD     interface{} `json:"glvd"`
	GLRD     interface{} `json:"glrd"`
	WWL      interface{} `json:"wwl"`
	JSET     interface{} `json:"jset"`
}

type Payload struct {
	DDV           interface{} `json:"ddv"`
	EventCounters interface{} `json:"eventCounters"`
	JSType        interface{} `json:"jsType"`
	DDK           interface{} `json:"ddk"`
	Request       interface{} `json:"request"`
	ResponsePage  interface{} `json:"responsePage"`
	CID           interface{} `json:"cid"`
	Referer       interface{} `json:"Referer"`
	JSData        JSData      `json:"jsData"`
}

type Headers struct {
	ContentType             string `json:"Content-type"`
	Host                    string `json:"Host"`
	Origin                  string `json:"Origin"`
	Referer                 string `json:"Referer"`
	AcceptEncoding          string `json:"Accept-Encoding"`
	AcceptLanguage          string `json:"Accept-Language"`
	SecChUa                 string `json:"Sec-Ch-Ua"`
	SecChUaMobile           string `json:"Sec-Ch-Ua-Mobile"`
	SecChUaPlatform         string `json:"Sec-Ch-Ua-Platform"`
	SecFetchDest            string `json:"Sec-Fetch-Dest"`
	SecFetchMode            string `json:"Sec-Fetch-Mode"`
	SecFetchSite            string `json:"Sec-Fetch-Site"`
	UserAgent               string `json:"User-Agent"`
	UpgradeInsecureRequests string `json:"Upgrade-Insecure-Requests"`
}

type JSONData struct {
	Headers Headers `json:"headers"`
	Payload Payload `json:"payload"`
}

type CookieData struct {
	Status int    `json:"status"`
	Cookie string `json:"cookie"`
}

func GetDataDome(ddv string, ddk string, urlStr string) (*JSONData, error) {
	if ddv == "" || ddk == "" {
		return nil, fmt.Errorf("ddv and ddk cannot be empty")
	}
	_, err := url.Parse(urlStr)
	if err != nil {
		return nil, fmt.Errorf("invalid url: %w", err)
	}

	binaryPath := "bin/datadome"
	cmd := exec.Command(binaryPath, "--ddv", ddv, "--ddk", ddk, "--url", urlStr)
	output, err := cmd.CombinedOutput()

	if err != nil {
		slog.Error("Error running DataDome binary:", "error", err)
		return nil, err
	}
	var datadome *JSONData
	jsonerr := json.Unmarshal(output, &datadome)
	if jsonerr != nil {
		slog.Error("Error parsing DataDome output:", "error", jsonerr)
		return nil, jsonerr
	}
	return datadome, nil
}

func GetDataDomeCookie(ddv string, ddk string, urlStr string) (string, error) {
	if ddv == "" || ddk == "" || urlStr == "" {
		return "", fmt.Errorf("ddv, ddk, and urlStr cannot be empty")
	}
	_, err := url.Parse(urlStr)
	if err != nil {
		return "", fmt.Errorf("invalid URL: %w", err)
	}
	datadome, err := GetDataDome(ddv, ddk, urlStr)
	if err != nil {
		slog.Error("Failed to get datadome cookie: ", "error", err)
		return "", err
	}
	client := bogdanfinn.NewStdClient()
	targetUrl := "https://api-js.datadome.co/js/"
	header := make(httpclient.EllisHeaders)
	header.Set("Content-type", datadome.Headers.ContentType)
	header.Set("Host", datadome.Headers.Host)
	header.Set("Origin", datadome.Headers.Origin)
	header.Set("Referer", datadome.Headers.Referer)
	header.Set("Accept-Encoding", datadome.Headers.AcceptEncoding)
	header.Set("Accept-Language", datadome.Headers.AcceptLanguage)
	header.Set("Sec-Ch-Ua", datadome.Headers.SecChUa)
	header.Set("Sec-Ch-Ua-Mobile", datadome.Headers.SecChUaMobile)
	header.Set("Sec-Ch-Ua-Platform", datadome.Headers.SecChUaPlatform)
	header.Set("Sec-Fetch-Dest", datadome.Headers.SecFetchDest)
	header.Set("Sec-Fetch-Mode", datadome.Headers.SecFetchMode)
	header.Set("Sec-Fetch-Site", datadome.Headers.SecFetchSite)
	header.Set("User-Agent", datadome.Headers.UserAgent)
	header.Set("Upgrade-Insecure-Requests", datadome.Headers.UpgradeInsecureRequests)

	// convert datadome.Payload.JSData to a JSON string
	jsDataJSon, err := json.Marshal(datadome.Payload.JSData)
	if err != nil {
		fmt.Println("Error marshaling payload:", err)
		return "", err
	}

	// build the request payload body
	body := url.Values{}
	body.Set("jsData", string(jsDataJSon))
	body.Add("ddv", datadome.Payload.DDV.(string))
	body.Add("jsType", datadome.Payload.JSType.(string))
	body.Add("ddk", datadome.Payload.DDK.(string))
	body.Add("request", datadome.Payload.Request.(string))
	body.Add("responsePage", datadome.Payload.ResponsePage.(string))
	body.Add("cid", datadome.Payload.CID.(string))
	body.Add("Referer", datadome.Payload.Referer.(string))

	response, err := client.Request(http.MethodPost, targetUrl, header, nil, bytes.NewBufferString(body.Encode()))
	if err != nil {
		slog.Error("Failed to request datadome url: ", "error", err)
		return "", err
	}
	defer response.Body.Close()

	if response.StatusCode != 200 {
		slog.Error("Failed to request datadome url: ", "error", response.StatusCode)
		return "", nil
	}

	var cookieResp CookieData
	err = json.NewDecoder(response.Body).Decode(&cookieResp)
	if err != nil {
		return "", err
	}
	// cookieResp.Cookie: datadome=GPv_HAoONj6YRdapOKu3xXgyicK3w3zYkewlAnvK43WXn61ctBzEMqQcIsBFOWlJk2UphTh~3E6HONYQcWOsGokKwT2DXDC8O_HBvPDTvor~j6~NIX4XsUGHj2Iz6mPs; Max-Age=31536000; Domain=.test.com; Path=/; Secure; SameSite=Lax
	return cookieResp.Cookie, nil
}
