import requests

#参照するオープンデータ：e-gov 法令検索
#エンドポイント：https://laws.e-gov.go.jp/api/1/
#機能：日本の法令を検索できる
#課題で取得したデータ：日本国憲法（XML形式）
#使い方：low_id に法令IDを指定する

#エンドポイント
API_URL  = "https://laws.e-gov.go.jp/api/1/lawdata/"

#データの種類：日本国憲法
law_id = "321CONSTITUTION";   

#response = requests.get(API_URL, params=params)
response = requests.get(API_URL + law_id)
# Process the response
print(response.text)