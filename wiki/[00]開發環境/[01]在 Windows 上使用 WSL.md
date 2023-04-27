# 在 Windows 上使用 Ubuntu Subsystem for Windows (WSL)

如果你想要在 Windows 上使用 Ubuntu Linux，那麼 Ubuntu Subsystem for Windows (WSL) 是一個非常好的選擇。本文將帶你了解 WSL 的基礎知識，以及如何安裝和使用 WSL。

## 介紹 Ubuntu Subsystem for Windows (WSL)

### 什麼是 WSL？

WSL 是一種 Windows 的功能，它允許你在 Windows 上運行 Linux 發行版。這是一種非常方便的解決方案，因為你可以在 Windows 上使用 Linux 的指令行界面，並且可以安裝和運行許多常用的 Linux 軟體和套件。

### WSL 有什麼優點？

WSL 有以下優點：

- 方便：WSL 讓你可以在 Windows 上運行 Linux 發行版，而不需要安裝和設置虛擬機或雙啟動系統。
- 兼容性：WSL 使用與 Linux 發行版相同的內核，因此它可以更好地支持 Linux 軟體和套件。
- 速度：WSL 與虛擬機相比速度更快，因為它使用了虛擬化技術。

## 安裝 WSL

### 系統要求

在安裝 WSL 之前，你需要確認你的 Windows 系統已經更新到最新版本，並且已經啟用了虛擬化技術。

虛擬化技術在 intel 叫 VT，在 AMD 叫 SVM。

### 安裝步驟

以下是安裝 WSL 的步驟：

1. 開啟 Windows 功能

   在 Windows 中，開啟「控制台」並找到「程式集」，然後選擇「開啟或關閉 Windows 功能」。在功能清單中找到「Windows Subsystem for Linux」，勾選它，然後按下「確定」。

2. 安裝 Ubuntu 兩種方法
   ![wsl](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202304271439504.png)

   1. 打開 Microsoft Store，搜尋 Ubuntu，選擇 Ubuntu 並安裝。
   2. 使用 [Chocolatey](/wiki/[00]開發環境/[00]使用%20Chocolatey%20管理%20Windows%20上的軟體) 安裝

      ```shell
       choco install wsl-ubuntu-2004
      ```

3. 開啟 Ubuntu

   在開始菜單中找到 Ubuntu，點擊打開它。第一次開啟時，你需要設置一個用戶名和密碼。

   現在你已經成功安裝了 WSL。

## 使用 WSL

### 更新 WSL 並切換為 WSL2

![update](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202304271542128.png)

可以使用 Microsoft Store 更新，也可以使用指令

```shell
wsl --update
wsl --set-version Ubuntu-20.04 2
```

### 啟動 WSL

啟動 WSL 很簡單。只需打開終端機，輸入以下指令：

```shell
wsl
```

這將啟動 WSL 的 Ubuntu 版本。你可以開始在其中輸入指令。

### 基本指令介紹

在 WSL 中，你可以使用許多常用的 Linux 指令。以下是一些常見的指令：

- `ls`: 列出當前目錄中的文件和資料夾。
- `cd`: 更改當前目錄。
- `mkdir`: 建立新的資料夾。
- `rm`: 刪除文件或資料夾。
- `sudo`: 使用超級使用者權限執行指令。
- `apt-get`: 安裝和管理軟體包的指令。

### 安裝軟體與套件

在 WSL 中安裝軟體和套件非常容易。你可以使用以下指令來安裝軟體包：

```shell
sudo apt-get update
sudo apt-get install package-name
```

其中 `package-name` 是你想要安裝的軟體包的名稱。

## 與 Windows 的互動

WSL 可以與 Windows 檔案系統和應用程式進行互動。以下是一些常見的互動方式：

### 訪問 Windows 檔案系統

在 WSL 中，你可以使用以下指令訪問 Windows 檔案系統：

```bash
cd /mnt/c
```

這將讓你進入 C 槽的根目錄。

### 訪問 Windows 應用程式

你可以在 WSL 中啟動 Windows 應用程式，例如瀏覽器和文本編輯器。只需在 WSL 中輸入以下指令即可啟動應用程式：

```bash
explorer.exe .
```

這將打開 Windows 資源管理器，並顯示當前目錄的內容。

### 設定網路

WSL 可以與 Windows 共享網路設定。在 WSL 中，你可以使用以下指令來設定網路：

```bash
sudo nano /etc/wsl.conf
```

這將打開 wsl.conf 文件，你可以在其中設定網路。

## 常見問題與疑難排解

在使用 WSL 過程中，你可能會遇到一些問題。以下是一些常見的問題和解決方法：

- 啟動 WSL 失敗：檢查你的系統是否已啟用虛擬化技術。
- 無法訪問 Windows 檔案系統：請確保你有足夠的權限訪問檔案系統。
- 無法訪問網路：檢查你的網路設定是否正確。

## 結論

WSL 是一個非常方便的解決方案，讓你可以在 Windows 上運行 Linux 程式和指令。通過本教學，你現在應該已經知道如何安裝和使用 WSL，以及如何與 Windows 進行互動。現在你可以開始在 WSL 中進行開發和測試了。

如果你遇到了任何問題或有任何建議，請在下面的評論區留言，我們將盡快回復你。希望這篇文章對你有所幫助，謝謝你的閱讀！
