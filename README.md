# Toc2022

## 前言
由於海底疫情肆虐，蟹老闆決定推出線上服務以促進來客率，並藉由線上訂位來避免因違反防疫規定遭到政府罰錢。

## 環境
- ubuntu 20.04
- python 3.8.10

## 使用教學
1. install `pipenv`
```shell
pip3 install pipenv
```
2. install 所需套件
```shell
pipenv install --three
// 若遇到pygraphviz安裝失敗，則嘗試下面這行
sudo apt-get install graphviz graphviz-dev
```
3. 從`.env.sample`產生出一個`.env`，並填入以下兩個資訊

- Line
    - LINE_CHANNEL_SECRET
    - LINE_CHANNEL_ACCESS_TOKEN

4. install `ngrok`

```shell
sudo snap install ngrok
```
5. run `ngrok` to deploy Line Chat Bot locally
```shell
ngrok http 8000
```
6. execute app.py
```shell
python3 app.py
```

## 功能
-加入好友訊息
- 訂位
    - 人數
    - 時間
* 查看菜單
* 查看餐廳位置
* 餐廳人員介紹
* 問卷調查

## 使用示範

### 加入好友訊息
![]( https://img.onl/DqAJfe)

### 訂位
![]( https://img.onl/G7Yol)

### 查看菜單
![]( https://img.onl/C73X5L)
### 查看餐廳位置
![]( https://img.onl/mEPP2x)
### 餐廳人員介紹
![]( https://img.onl/Ce519F) 
### 問卷調查
![]( https://img.onl/wBo1S5)
## FSM
![](https://img.onl/zQ4JtS)
### state說明
- user: 輸入蟹堡王開始使用線上服務
- choose: 選擇需要的服務
- reserve_people:訂位人數
- reserve_time: 訂位時間
- reserve_result: 訂位結果
- menu: 查看菜單
- location: 查看餐廳位置
- employee:餐廳人員介紹


## Bonus


- Deploy on Heroku
![](https://img.onl/UdErez)
- Line API 

- image
- video
