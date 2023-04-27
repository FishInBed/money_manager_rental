## 錢錢管家 Money Chambler

### 簡介 Introduction
&emsp;&emsp;這是一個為了合租團體設計的 linebot，在被加到line群組後可以幫忙記帳並在月底結算團體中每個人需要收到多少錢或再付多少錢。他除了是你的記帳助手之外，更是你的討債好幫手。
&emsp;&emsp;This is a linebot designed for flatmates who are troubled about setteling payments with each other. Once the chatbot is invited to a line group, it can be used to help track the spending. What's more, it can help announce who should pay more to others and who should recieve more from others at the end of the month. This chatbot is not only a payment tracker but also a friendly debt collector for you.

| &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | 
| :--------: | :--------: | :--------: |
| <img src="https://user-images.githubusercontent.com/31921056/234792497-a02cf02f-fc0b-4d0b-bf75-bc9645ef56e6.jpg" width="300"/> | <img src="https://user-images.githubusercontent.com/31921056/234793540-9d6bfa8a-dfd9-40e4-a892-d840fef5b37d.jpg" width="300"/> | <img src="https://user-images.githubusercontent.com/31921056/234794925-f07b29d1-311d-4607-9948-3719f1301988.png" width="300"/> |


### 重要檔案 Important Files and Folders

* <code>image</code>: 儲存linebot會用的圖片<br>
stores the images used in the linebot interface
* <code>models</code>: linebot中各項功能的原始碼<br>
The python codes of each of the function in the linebot 
* <code>main.py</code>: 執行機器人的主要檔案<br>
The python code that runs the whole chatbot
* <code>Procfile</code>: 用來定義指令如何在heroku上執行的檔案<br>
Used to define how the instructions are run on heroku
* <code>requirements.txt</code>: 用來記錄機器人運作需要安裝的套件及版本<br>
Used to specify the packages that must be installed to make the linebot work and the versions of them
* <code>config.ini</code>: 用來記錄你的api，讓機器人可以連接到line上面<br>
Used to specify your channel access token and secret to connect heroku and line

本機器人參考[從LINE BOT到資料視覺化：賴田捕手](https://ithelp.ithome.com.tw/users/20120178/ironman/2654)系列文章中之教學構建而成。<br>
This chatbot is based on the tutorial of how to build a chatbot introduced in [從LINE BOT到資料視覺化：賴田捕手](https://ithelp.ithome.com.tw/users/20120178/ironman/2654).
