# 使用 macOS Mini 建立安全的遠端伺服器

最近我購買了一台 Mac Mini 作為我的遠端伺服器！這是我比較了各種方案後做出的決定，相較於使用昂貴的雲端主機方案，我發現 Mac Mini 提供了更具成本效益的解決方案。我想和大家分享一些我為了提升安全性所做的設定步驟。但在這之前，讓我先分享一下我購買 Mac Mini 的經驗和比較。

我選擇了最便宜的 Mac Mini，我使用了 BTS 方案購買，售價只有台幣 15,700 元，而且還附贈了一副 AirPods 2！這款 Mac Mini 配備了 8 核心 CPU、10 核心 GPU、8GB 統一記憶體和 256GB SSD 儲存裝置。它搭載了 M2 晶片，具有出色的效能和低能耗特性，這也是我選擇它作為遠端伺服器的原因之一。

相較於昂貴的雲端主機方案，Mac Mini 提供了更經濟實惠的解決方案。舉例來說，在 Scaleway 網站上，他們提供了使用 Apple M1 晶片的雲主機，每小時價格約為 0.11 歐元。而在 Azure 或 AWS 上使用類似配置的主機，每年的費用接近 10 萬台幣。考量到成本和性能的平衡，我最終選擇了購買 Mac Mini 作為我的遠端伺服器。

這款 Mac Mini 不僅價格優惠，還具有其他優勢。首先，它具有非常低的功耗且不易發熱，非常適合作為伺服器使用。這意味著我可以長時間運行伺服器應用程式，同時節省能源成本並降低散熱問題。

此外，這款 Mac Mini 搭載了 M2 晶片的架構，這帶來了額外的優勢。M2 晶片採用統一記憶體架構，使我能夠將 Mac Mini 視為擁有 8GB 顯存的顯示卡，從而能夠更好地應對需要大量記憶體資源的 AI 模型的訓練。

現在，我想分享一下為了加強 Mac Mini 的安全性所採取的步驟。

## 1. 產生 SSH 金鑰對

首先，在我的本地機器上，我使用以下命令生成了 SSH 金鑰對：

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

這個命令生成了一個新的 RSA 金鑰對，並以我的電子郵件地址作為標籤。為了增加安全性，我選擇了 4096 位的金鑰長度。

系統會要求我指定金鑰的儲存位置，我選擇了預設的位置（通常是 `~/.ssh/id_rsa`）。在這個過程中，我選擇不設定密碼，這樣在使用金鑰時就不需要每次輸入密碼。

## 2. 將公鑰複製到遠程主機

有了 SSH 金鑰對後，我將公鑰複製到我的 Mac Mini。我使用以下命令：

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub user@host
```

這個命令將我的公鑰複製到遠程主機的 `~/.ssh/authorized_keys` 文件中。輸入遠程主機的密碼驗證後，公鑰就會被成功複製到主機上。

## 3. SSH 安全設定

為了提高 SSH 的安全性，我修改了 `/etc/ssh/sshd_config` 文件的設定。

我使用以下命令打開該文件：

```bash
sudo nano /etc/ssh/sshd_config
```

在文件中，我新增或修改了以下行：

```text
PubkeyAuthentication yes
PasswordAuthentication no
ChallengeResponseAuthentication no
```

這些設定將 SSH 設置為只接受公鑰認證，禁止使用密碼登入和挑戰回應驗證。這提高了伺服器的安全性。

另外，我還將 SSH 的默認端口從 22 改為一個非標準端口。這樣做可以防止許多針對標準 SSH 端口的自動化攻擊。

## 4. 更改 SSH 預設端口

在 `sshd_config` 文件

中，找到 `#Port 22` 這一行，刪除 `#` 並

將 `22` 改為你想要的端口。同時，在 `/etc/services` 文件中對應地更改端口：

```bash
sudo nano /etc/services
```

找到 `ssh 22/tcp` 這一行，將 `22` 改為你在 `sshd_config` 文件中設定的新端口。

## 5. VNC 只接受本地連接

為了增加 VNC 的安全性，我將其設置為只接受本地主機的連接。我使用了以下命令：

```bash
sudo defaults write /Library/Preferences/com.apple.RemoteManagement.plist VNCOnlyLocalConnections -bool yes
```

這個命令將 `VNCOnlyLocalConnections` 的值設置為 `yes`，表示 macOS 只接受來自本地主機的 VNC 連接。

## 6. SSH 隧道

為了安全地訪問 VNC，我建立了一個 SSH 隧道。以下是具體的操作步驟：

```bash
ssh -L 5900:localhost:5900 user@host -p port
```

這個命令將本地的 5900 端口映射到遠程主機的 5900 端口，所有的 VNC 數據將通過加密的 SSH 隧道進行傳輸，這樣可以防止數據在網路上被攔截或竊取。

## 7. SMB 安全設定

為了增加 SMB（Server Message Block）的安全性，我也通過 SSH 隧道進行設定。以下是具體的操作步驟：

```bash
ssh -L 8445:localhost:445 user@host -p port
```

這個命令將本地的 8445 端口映射到遠程主機的 445 端口，所有的 SMB 數據將通過加密的 SSH 隧道進行傳輸，這樣可以防止數據在網路上被攔截或竊取。

## 8. 配置防火牆

最後，為了進一步加強安全性，我使用 Murus Lite 工具來配置 macOS 內建的防火牆。我將所有的 TCP 和 UDP 連接預設為封鎖狀態，然後只允許特定的連接通過：

- 允許來自本地主機的 VNC 和 SMB 連接
- 開放 80 和 443 端口，以提供 HTTP 和 HTTPS 服務

透過以上的步驟，我成功地將我的 Mac Mini 轉變為一台安全的遠端伺服器。這些步驟不僅提升了 SSH、VNC 和 SMB 服務的安全性，還加強了整體伺服器的安全性。然而，請記住安全性是一個持續的過程，需要定期審查和更新系統。你也可以考慮使用防火牆、入侵檢測系統和安全信息事件管理（SIEM）工具等措施來進一步提升安全性。感謝閱讀，祝你成功建立一個安全的遠端伺服器！