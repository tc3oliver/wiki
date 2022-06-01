# 利用 Let’s Encrypt 來自動簽署並更新 SSL 憑證

1. 安裝 Certbot

   ```bash
   sudo apt install certbot python3-certbot-nginx
   ```

2. Wildcard 憑證 (DNS 驗證方式)

    ```bash
    certbot certonly \
    --manual \
    -d "*.example.com" \
    -d example.com \
    --preferred-challenges dns
    ```

    - -manual：手動安裝憑證。
    - d 接上要申請的網域：萬用字元(\*)是給子網域用，父網域要單獨申請。
    - -preferred-challenges dns：使用 DNS 方式申請（Wildcard 只能用此方式）。

    會收到一個網址及一段 hash code，先不要按 Enter

    ```bash
    _acme-challenge.example.com
    一段 hash code
    ```

    注意！有幾個 -d 就會有幾組 hash code，一次只會顯示一組。

    到 DNS 服務商去增加 TXT 紀錄，名稱為 \_acme-challenge，類型為 TXT，值為那段 hash code

    設定好後可以使用以下指令，確認是否成功

    ```bash
    dig -t txt _acme-challenge.example.com
    ```

    我使用 AWS Route 53 不允許我設定兩組一樣的 Record，最後我只有設定 `*.example.com`

## 更新

### AWS Route 53

清除舊的

```bash
sudo apt purge certbot python3-certbot-nginx python3-certbot-apache
sudo apt autoremove
```

安裝 certbot

```bash
sudo apt install certbot python3-certbot-dns-route53
```

建立 aws credentials，這邊有一個坑，因為我們使用 certbot 指令需要 sudo 權限，所以建立在 user 的 credential 會吃不到，要先切到 `sudo su`

```bash
sudo su
mkdir ~/.aws/
vim ~/.aws/credentials
[default]
aws_access_key_id=xxx
aws_secret_access_key=xxx
```

生成憑證

```bash
sudo certbot certonly \
--dns-route53 \
-d "*.example.com" \
-d "example.com"
```

### 成功

![截圖](https://cdn.jsdelivr.net/gh/tc3oliver/ImageHosting/img/202206010923491.png)

### 參考資料

[http://blog.tonycube.com/2019/02/lets-encrypt-wildcard.html](http://blog.tonycube.com/2019/02/lets-encrypt-wildcard.html)

[https://medium.com/learn-or-die/利用-lets-encrypt-來自動簽署並更新-ssl-憑證-wildcard-26b49114bf73](https://medium.com/learn-or-die/%E5%88%A9%E7%94%A8-lets-encrypt-%E4%BE%86%E8%87%AA%E5%8B%95%E7%B0%BD%E7%BD%B2%E4%B8%A6%E6%9B%B4%E6%96%B0-ssl-%E6%86%91%E8%AD%89-wildcard-26b49114bf73)
