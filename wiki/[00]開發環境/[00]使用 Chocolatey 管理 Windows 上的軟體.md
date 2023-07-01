# 如何使用 Chocolatey 管理 Windows 上的軟體

如果您是 Windows 用戶，您可能會發現安裝、更新和卸載軟體可能會很麻煩。但是，有一個稱為 Chocolatey 的工具可以幫助您輕鬆管理軟體。

本篇文章將介紹如何安裝 Chocolatey，以及如何使用 Chocolatey 來搜索、安裝、更新和卸載軟體。同時，還將介紹如何安裝 Chocolatey GUI，這是一個圖形化界面，讓您更輕鬆地管理軟體。

## 安裝 Chocolatey 的步驟

1. 開啟 PowerShell

   您可以按下 Windows 鍵 + X 鍵，然後選擇「Windows PowerShell (管理員)」，這樣就會開啟 PowerShell。

1. 在 PowerShell 中啟用執行 PowerShell 腳本的權限

   請輸入 `Set-ExecutionPolicy RemoteSigned -scope CurrentUser`，並按 Enter 鍵。這樣可以啟用 PowerShell 以執行 Chocolatey 安裝腳本。

1. 安裝 Chocolatey

   請輸入以下指令，並按 Enter 鍵執行：

   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
   ```

1. 等待安裝完成

   安裝過程需要一些時間，請耐心等待，直到 PowerShell 給出 Chocolatey 安裝完成的提示。

1. 驗證安裝是否成功

   輸入 `choco`，並按 Enter 鍵。如果 Chocolatey 安裝成功，您應該可以看到一個清單，其中包含 Chocolatey 的一些常用命令。

## 使用 Chocolatey 來搜索、安裝、更新和卸載軟體

Chocolatey 是一個包管理器，可以幫助您在 Windows 上快速安裝、更新和卸載軟體包。以下是 Chocolatey 的一些常用操作：

1. 搜索軟體包

   使用以下命令在 Chocolatey 上搜索軟體包：

   ```powershell
   choco search <package_name>
   ```

2. 安裝軟體包

   使用以下命令在 Chocolatey 上安裝軟體包：

   ```powershell
   choco install <package_name>
   ```

   您可以通過添加其他參數來自定義安裝選項，例如指定安裝版本、安裝位置等。

3. 更新軟體包

   使用以下命令在 Chocolatey 上更新已安裝的軟體：

   ```powershell
   choco upgrade <package_name>
   ```

   使用這個命令將會自動更新軟體到最新的可用版本。如果要指定安裝的版本，可以使用 `--version` 參數來指定特定版本號碼。

4. 卸載軟體：使用以下命令在 Chocolatey 上卸載軟體：

   ```powershell
   choco uninstall <package_name>
   ```

   這個命令將會卸載指定的軟體，如果存在相關的依賴關係，也會一併卸載。可以使用 `--force` 參數來強制卸載。

5. 列出已安裝的軟體：使用以下命令在 Chocolatey 上列出已安裝的軟體：

   ```powershell
   choco list --local-only
   ```

   這個命令將會列出所有已安裝的軟體及其版本號碼。如果需要查看特定軟體的詳細信息，可以使用 `choco info` 命令。

6. 列出可更新的軟體：使用以下命令在 Chocolatey 上列出可更新的軟體：

   ```powershell
   choco outdated
   ```

   這個命令將會列出所有已安裝的軟體中有可用更新的軟體，可以使用 `choco upgrade all` 命令來更新所有可用的軟體。

除了以上操作，Chocolatey 還提供了許多其他功能，例如包依賴管理、安裝腳本、安裝程序選項、包創建等等。詳細信息可以參考 Chocolatey 的官方文檔。

## 使用 Chocolatey GUI

Chocolatey GUI 是一個圖形化界面，可以讓用戶更輕鬆地管理軟體。以下是使用 Chocolatey GUI 的步驟：

1. 首先，您需要安裝 Chocolatey，如果您還沒有安裝 Chocolatey，請參考上面的步驟進行安裝。
2. 打開 PowerShell，以系統管理員身份運行以下命令以安裝 Chocolatey GUI：

   ```powershell
   choco install chocolateygui
   ```

3. 安裝完成後，您可以在開始菜單或應用程式清單中找到 Chocolatey GUI 應用程式。
4. 點擊 Chocolatey GUI 圖標啟動應用程式，您可以使用圖形化界面來搜索、安裝、更新和卸載軟體。

如果您安裝了 Chocolatey GUI 但無法在開始菜單或應用程式清單中找到它，可以在 PowerShell 中運行以下命令來重新創建快捷方式：

```powershell
choco upgrade chocolateygui -y --params "'/DesktopIcons=true'"
```

這將創建一個桌面快捷方式和一個開始菜單項目，以便您更方便地訪問 Chocolatey GUI。

## Chocolatey 的常用開發環境

Chocolatey 是一個 Windows 上的軟體管理器，可以讓您在命令提示字元或 PowerShell 中快速安裝和管理各種軟體。

使用以下 PowerShell 腳本：

```powershell
choco install -y python nodejs golang flutter dotnetcore-sdk visualstudio2019community pycharm-professional goland vscode git docker-desktop postman microsoft-teams
```

此腳本將自動安裝 Python、Node.js、Golang、Flutter、.NET SDK 和 Visual Studio、PyCharm、GoLand、Visual Studio Code、Git、Docker、Postman 和 Teams。 

-y 選項將自動確認所有提示，這樣安裝過程將不需要任何人工干預。

![](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202304261352600.png)