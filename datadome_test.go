package utils

import "testing"

func TestGetDataDome(t *testing.T) {
	testDdv := "4.25.0"
	testDdk := "your datadome key"
	testUrl := "https://test.com"
	datadome, err := GetDataDome(testDdv, testDdk, testUrl)
	if err != nil {
		t.Error(err)
	}
	t.Log(datadome)
}

func TestGetDataDomeCookie(t *testing.T) {
	testDdv := "4.25.0"
	testDdk := "your datadome key"
	testUrl := "https://test.com"
	datadome, err := GetDataDomeCookie(testDdv, testDdk, testUrl)
	if err != nil {
		t.Error(err)
	}
	t.Log(datadome)
}
