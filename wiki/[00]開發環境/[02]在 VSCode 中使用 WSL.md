# 如何在 Visual Studio Code 中使用 WSL 安裝 Node.js 和 Docker 運行應用程序

本文將介紹在 Visual Studio Code 中如何運行 Node.js 專案與 Docker，並提供以下十個步驟：

1. 安裝 WSL
2. 安裝 WSL 插件
3. 安裝 Node.js 和 Docker
4. 在 WSL 中創建 Node.js 專案
5. 在 VS Code 中遠程連接 WSL
6. 在 VS Code 中打開 Node.js 專案
7. 在 VS Code 中安裝插件
8. 在 VS Code 中設置 Docker
9. 在 VS Code 中建立 Docker 映像
10. 在 VS Code 中運行 Docker 容器

## 步驟一：安裝 WSL

WSL 是 Windows Subsystem for Linux 的縮寫，它是一個在 Windows 上運行 Linux 應用程序的子系統。要安裝 WSL，請按照以下步驟操作：

1. 打開 Windows PowerShell（或命令提示符），以系統管理員身份運行。
2. 執行以下命令以啟用 WSL 功能：

   ```shell
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   ```

3. 完成後，重新啟動系統。
4. 打開 Microsoft Store，搜索 "Linux"。
5. 從 Microsoft Store 下載並安裝你喜歡的 Linux 發行版。

## 步驟二：安裝 WSL 插件

![wsl](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202304271443735.png)

在 Visual Studio Code 中運行 WSL，需要安裝 WSL 插件。請按照以下步驟操作：

1. 打開 Visual Studio Code。
2. 點擊左側的擴展選項。
3. 在搜尋欄中輸入 "WSL"。
4. 點擊 "安裝" 按鈕。

## 步驟三：安裝 Node.js 和 Docker

要在 WSL 中運行 Node.js 專案和 Docker，需要在 WSL 中安裝 Node.js 和 Docker。請按照以下步驟操作：

1. 打開你的 Linux 發行版。
2. 在 Linux 中，執行以下命令以安裝 Node.js：

   ```shell
   sudo apt-get update
   sudo apt-get install nodejs
   ```

3. 在 Linux 中，執行以下命令以安裝 Docker：

   ```shell
   sudo apt-get update
   sudo apt-get install docker.io
   ```

## 步驟四：在 WSL 中創建 Node.js 專案

在 WSL 中創建 Node.js 專案，請按照以下步驟操作：

1. 在 WSL 中打開終端機。

2. 創建一個新的文件夾以存儲你的 Node.js 專案。

3. 在該文件夾中，執行以下命令以創建一個新的 Node.js 專案：

   ```shell
   npm init
   ```

4. 跟隨提示回答問題，並在最後輸入 "yes" 確認。

5. 完成後，你會看到生成的 package.json 文件。

## 步驟五：在 VS Code 中遠程連接 WSL

![new wsl window](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202304271601040.png)

在 Visual Studio Code 中，運行 WSL 需要遠程連接。請按照以下步驟操作：

1. 打開 Visual Studio Code。
2. 按下 "Ctrl + Shift + P"（Windows 和 Linux），或 "Cmd + Shift + P"（Mac）。
3. 在搜索欄中輸入 "New WSL Window"，然後按 Enter。
4. 等待 Visual Studio Code 與 WSL 之間的連接建立。

![](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202304271604199.png)

連線成功後在左下角會看到 `WSL: Ubuntu`

## 步驟六：在 VS Code 中打開 Node.js 專案

在 Visual Studio Code 中打開 Node.js 專案，請按照以下步驟操作：

1. 在 Visual Studio Code 中，打開命令面板，並輸入 "File: Open Folder"。
2. 選擇剛剛在 WSL 中創建的 Node.js 專案文件夾。
3. 在 Visual Studio Code 中打開 package.json 文件。

## 步驟七：在 VS Code 中安裝插件

在 Visual Studio Code 中，運行 Node.js 專案需要安裝相關插件。請按照以下步驟操作：

1. 在 Visual Studio Code 中，按下 "Ctrl + Shift + X"（Windows 和 Linux），或 "Cmd + Shift + X"（Mac）。
2. 在搜索欄中輸入 "Node.js"，然後按 Enter。
3. 選擇 "Node.js Extension Pack"，然後按 "Install" 按鈕。
4. 在終端機輸入 `npm install express` 安裝 express
5. 建立 `server.js`

   ```javascript
   'use strict'

   const express = require('express')

   // Constants
   const PORT = 8080
   const HOST = '0.0.0.0'

   // App
   const app = express()
   app.get('/', (req, res) => {
     res.send('Hello World')
   })

   app.listen(PORT, HOST, () => {
     console.log(`Running on http://${HOST}:${PORT}`)
   })
   ```

## 步驟八：在 VS Code 中設置 Docker

在 Visual Studio Code 中，運行 Docker 需要設置相關插件。請按照以下步驟操作：

1. 在 Visual Studio Code 中，按下 "Ctrl + Shift + X"（Windows 和 Linux），或 "Cmd + Shift + X"（Mac）。
2. 在搜索欄中輸入 "Docker"，然後按 Enter。
3. 選擇 "Docker"，然後按 "Install" 按鈕。

## 步驟九：在 VS Code 中建立 Docker 映像

在 Visual Studio Code 中建立 Docker 映像，請按照以下步驟操作：

1. 建立 Dockerfile

   ```dockerfile
   FROM node:16

   # Create app directory
   WORKDIR /usr/src/app

   # Install app dependencies
   # A wildcard is used to ensure both package.json AND package-lock.json are copied
   # where available (npm@5+)
   COPY package*.json ./

   RUN npm install
   # If you are building your code for production
   # RUN npm ci --omit=dev

   # Bundle app source
   COPY . .

   EXPOSE 8080
   CMD [ "node", "server.js" ]
   ```

2. 打開終端機，並切換到你的 Node.js 專案文件夾。
3. 在終端機中，執行以下命令以創建一個 Docker 映像：

   ```shell
   docker build -t app .
   ```

4. 等待映像創建完成。

## 步驟十：在 VS Code 中運行 Docker 容器

在 Visual Studio Code 中運行 Docker 容器，請按照以下步驟操作：

1. 在 Visual Studio Code 中，打開你的 Node.js 專案。
2. 打開終端機，並切換到你的 Node.js 專案文件夾。
3. 在終端機中，執行以下命令以運行 Docker 容器：

   ```shell
   docker run -p 8080:8080 app
   ```

4. 等待容器啟動。
5. 在瀏覽器中，訪問 [http://localhost:8080](http://localhost:8080)，你應該能夠看到你的 Node.js 應用程序運行中的頁面。

這些步驟應該能夠幫助你在 WSL 中設置和運行 Node.js 應用程序，以及使用 Docker 進行容器化部署。請注意，這些步驟僅僅是提供了一個基本的流程，實際上根據你的特定情況可能需要進行調整和修改。
