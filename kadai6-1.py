import requests

APP_ID = "89e99bf20f6867a64bf449e1a821a779414d0e13"

#エンドポイント
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

#データの種類：旅券統計 旅券統計（国内）旅券月別・種類別発行数
params = {
    "appId": APP_ID,
    "statsDataId":"0003297740",  
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "limit":"10",   #最大10件まで
    "lang": "J"  # 日本語を指定
}   

#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)