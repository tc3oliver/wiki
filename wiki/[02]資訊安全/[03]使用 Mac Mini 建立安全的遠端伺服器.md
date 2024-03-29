# 使用 Mac Mini 建立安全的遠端伺服器

近期我入手了一台 Mac Mini,想把它當成家中的小伺服器來玩玩。對我來說自己組一台小伺服器實在是太有吸引力了!雖然很多人也在做類似的嘗試,但要把小伺服器弄得安全其實还是有許多學問的。所以今天就來分享一下我的設定心得,希望對大家也能有些幫助。

我選擇了一台基本款 M2 Mac Mini,通過 BTS 的方案只花了 15,700 元就入手了,當然還送了一副 AirPods 2,真的是超高 CP 值!這台 Mac Mini 配備 8 核心 CPU、10 核心 GPU,8GB 記憶體以及 256GB SSD,用的是全新 M2 晶片,效能絕對強悍,又能節省電力耗能。正因如此,我覺得它作為小伺服器再適合不過了!

相比起來,要租用雲端服務的費用其實非常高,每個月就要花上幾千塊不是嗎?有了自己的小伺服器就可以大大節省這部分成本。我查過資料,在一些雲服務供應商那邊,使用 Apple M1 配置的虛擬主機,每小時費用就要 0.11 歐元左右。如果一年下來,費用絕對是嚇死人的。所以以成本和效能來看,我覺得還是自組一台 Mac Mini 伺服器最划算!

Mac Mini 不但價格合理,它還有超低功率消耗、發熱量低等優點,代表我可以讓它長時間全速運作,一舉兩得。因此在各方面考量下,我認為它作為我的小伺服器實在是再完美不過了!

此外,M2 晶片使用了統一記憶體架構,這讓我能夠把 Mac Mini 當成擁有 8GB 顯存的顯卡來使用,對我未來想部署需要大量顯存的 AI 模型應用將會很有幫助。

講了那麼多,接下來就讓我分享如何設定 Mac Mini 以強化其安全性吧!

## 1. 產生 SSH 金鑰對

為了登入我的 Mac Mini 伺服器,我需要使用 SSH 金鑰對來進行密碼式登入。

首先,在我的本地機上我利用以下指令產生了一組新的 SSH 金鑰對:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

這行指令會生成一組 RSA 演算法的 SSH 密鑰,並使用我的電子郵件作為標籤。為求安全性,我特別選用了4096位元的金鑰長度。

在執行時,系統會要我設定這組金鑰的儲存路徑,我選用了預設路徑 `~/.ssh/id_rsa` 來保存。

這樣就在我的本地電腦上成功產生了一組 SSH 金鑰,用來和我的 Mac Mini 伺服器進行加密通訊。

## 2. 將公鑰複製到 Mac Mini

在本地電腦產生了 SSH 公鑰和私鑰後,我需要將公鑰傳送到 Mac Mini 伺服器,以便在未來使用公鑰加密演算法進行無密碼登入。

為了實現這個目的,我按照以下步驟操作:

1. 首先使用 SSH 指令連接到 Mac Mini:

   ```bash
   ssh user@host
   ```

2. 輸入 Mac Mini 的登入密碼進行驗證。

3. 驗證通過後,使用 `exit` 命令退出連線。

4. 然後執行 `ssh-copy-id` 指令,將本地公鑰複製到 Mac Mini:

   ```bash
   ssh-copy-id -i ~/.ssh/id_rsa.pub user@host
   ```

5. 再次輸入登入密碼進行驗證。

6. 驗證成功後,公鑰就會自動複製到 Mac Mini 的 `~/.ssh/authorized_keys` 檔案中。

通過這些步驟,我已經成功設定了基於 SSH 公鑰加密的無密碼登入。

## 3. SSH 安全設定

為了提高 SSH 的安全性，我修改了 `/etc/ssh/sshd_config` 文件的設定。

我使用以下命令打開該文件：

```bash
sudo nano /etc/ssh/sshd_config
```

在文件中，我新增或修改了以下行：

```env
PubkeyAuthentication yes
PasswordAuthentication no
ChallengeResponseAuthentication no
```

這些設定將使SSH只接受公鑰認證,禁止使用密碼登入和挑戰回應驗證。這樣可以大幅提高伺服器的安全性。

另外,我還將 SSH 的預設端口從 22 改為一個非標準端口。這種作法可以避免許多針對標準 SSH 端口 22 的自動化攻擊。

通過上述設定,我已經相當程度地強化了連線到我的 Mac Mini 伺服器的安全性。現在只有持有正確私鑰的用戶才可登入,而無法通過密碼或其他方式進行連線。這大大減少了遭到駭客攻擊的風險。

## 4. 更改 SSH 預設端口

在 `sshd_config` 文件

中，找到 `#Port 22` 這一行，刪除 `#` 並

將 `22` 改為你想要的端口。同時，在 `/etc/services` 文件中對應地更改端口：

```bash
sudo nano /etc/services
```

找到 `ssh 22/tcp` 這一行，將 `22` 改為你在 `sshd_config` 文件中設定的新端口。

這樣就允許連線通過新設定的 SSH 端口了。結合前面修改 SSH 設定為只使用公鑰認證的做法,可大幅提升我的 Mac Mini 伺服器的連線安全性。

## 5. 設定 VNC 僅接受本地連線

除了 SSH 以外,我還需要設定 VNC 以提高安全性。

VNC 可以讓我通過圖形界面遠端控制 Mac Mini。為了防止外部連線,我進行了以下設定:

```bash
sudo defaults write /Library/Preferences/com.apple.RemoteManagement.plist VNCOnlyLocalConnections -bool yes
```

這行命令將 VNCOnlyLocalConnections 選項設定為 yes,表示 macOS 僅接受來自本地主機的 VNC 連線。

透過這個設定，VNC 只能在 Mac Mini 的本地環境中進行控制，防止直接從外部進行的 VNC 攻擊。然而，為了實現安全的遠程訪問 VNC 服務，我可以使用 SSH 隧道來進行連接。透過 SSH 隧道，所有的 VNC 流量都會被加密並通過安全的通道傳輸，從而提供了進一步的網路安全保護。這樣，我可以在維持 VNC 服務的安全性的同時，遠程訪問我的小型伺服器。

## 6. 使用 SSH 隧道連接 VNC

為了安全地連接 VNC 服務,我設定了 SSH 隧道:

```bash
ssh -L 5900:localhost:5900 user@host -p port
```

這條命令將本地端的 5900 連接埠對應到遠端主機的 5900 VNC 連接埠。所有的 VNC 流量將通過加密的 SSH 隧道傳輸,防止資料在網路上被攔截。

## 7. 通過 SSH 隧道安全傳輸 SMB

我選擇使用 SMB(伺服器訊息區塊)通訊協定來傳輸檔案,因為它速度快且安全性高。為了進一步提升安全性,我同樣使用 SSH 隧道:

```bash
ssh -L 8445:localhost:445 user@host -p port
```

這能將本地 8445 連接埠對應到遠端 445 SMB 連接埠。所有的 SMB 流量都經過加密的 SSH 隧道安全傳輸,避免在網路上被攔截。

我也在 Mac Mini 上掛載了 4TB SSD 做為儲存裝置,既擴充了空間也提升了效能。

## 8. 配置防火牆

最後，為了進一步加強安全性，我使用 Murus Lite 工具來配置 macOS 內建的防火牆。我將所有的 TCP 和 UDP 連接預設為封鎖狀態，然後只允許特定的連接通過：

- 允許來自本地主機的 VNC 和 SMB 連接
- 開放 80 和 443 端口，以提供 HTTP 和 HTTPS 服務

## 總結

透過 SSH 金鑰登入、SSH 隧道傳輸 VNC 和 SMB、配置防火牆等措施,我相信已可充分保護 Mac Mini 伺服器的安全。當然,資訊安全需要持續強化,大家可以定期更新系統和工具。如果有興趣,不妨玩玩防火牆或入侵偵測系統,讓安全性再上一層樓。

今天就先分享到這邊,希望對想架設自己的小型伺服器感興趣的朋友們有所幫助!安全設定是門大學問,如果有任何問題歡迎留言討論,我會盡力提供意見!祝各位成功部署出安全又穩定的家用小伺服器!
