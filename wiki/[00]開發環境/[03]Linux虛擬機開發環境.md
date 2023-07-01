# 在 Linux 虛擬機上建立開發環境

在進行軟體開發時，建立一個良好的開發環境是非常重要的。以下是在 Linux 虛擬機上建立開發環境的一些建議：

## 安裝 Zsh

Zsh 是一個功能強大且高度可定制的命令行殼層。你可以使用包管理工具安裝 Zsh，具體指令可能因 Linux 發行版而異。例如，在 Ubuntu 上，你可以使用以下指令安裝 Zsh：

```
sudo apt-get install zsh
```

## 安裝 Oh My Zsh

Oh My Zsh 是一個社群驅動的 Zsh 配置框架，提供了豐富的主題和插件。你可以使用以下指令安裝 Oh My Zsh：

```
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

## 安裝 Powerlevel10k 主題

Powerlevel10k 是一個高度可定制的 Zsh 主題，提供了美觀且功能豐富的命令行提示符。你可以按照以下步驟安裝 Powerlevel10k：

1. 從 GitHub 上複製 Powerlevel10k 存儲庫：

   ```
   git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k
   ```

2. 在 `~/.zshrc` 文件中設置 `ZSH_THEME` 為 `powerlevel10k/powerlevel10k` 。

3. 重新載入 Zsh 配置：

   ```
   source ~/.zshrc
   ```

4. 根據提示進行 Powerlevel10k 的初始化設定。

## 安裝 Docker

Docker 是一個強大的容器化平台，用於將應用程序打包成輕量級、可移植的容器。你可以按照以下步驟安裝 Docker：

1. 在 Linux 虛擬機上安裝 Docker 的相關依賴：

   ```
   sudo apt-get update
   sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
   ```

2. 添加 Docker 官方 GPG 金鑰：

   ```
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

3. 添加 Docker 存儲庫：

   ```
   echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

4. 安裝 Docker：

   ```
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
   ```

5. 驗證 Docker 安裝是否成功：

   ```
   sudo docker run hello-world
   ```

## 安裝 Docker Compose

Docker Compose 是一個用於定義和運行多個 Docker 容器的工具，通過一個單獨的配置文件來管理容器間的依賴關係。以下是使用最新的安裝方式來安裝 Docker Compose 的步驟：

1. 下載並安裝 Compose CLI 插件：

   ```
   DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
   mkdir -p $DOCKER_CONFIG/cli-plugins
   curl -SL https://github.com/docker/compose/releases/download/v2.19.1/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
   ```

   這個指令會從 Compose 發行庫中下載最新版本的 Docker Compose 並將其安裝到當前使用者的`$HOME`目錄下。

   如果你想為系統上的所有使用者安裝 Docker Compose，將`~/.docker/cli-plugins`替換為`/usr/local/lib/docker/cli-plugins`。

   如果你想安裝不同版本的 Compose，將`v2.19.1`替換為你想使用的 Compose 版本。

   如果你使用的是不同的架構，將`x86_64`替換為你想使用的架構。

2. 授予執行權限：
   對二進制檔案應用可執行權限：

   ```
   chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
   ```

   或者，如果你選擇為所有使用者安裝 Compose：

   ```
   sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
   ```

3. 測試安裝是否成功：
   ```
   docker compose version
   ```
   如果成功安裝，你應該能夠看到 Docker Compose 的版本信息。

## 安裝 Node.js 和 npm 使用 nvm

[nvm (Node Version Manager)](https://github.com/nvm-sh/nvm) 是一個用於管理 Node.js 版本的工具，它允許你在同一個系統上安裝和切換不同的 Node.js 版本。這是一個更靈活和便於管理 Node.js 的方法。以下是使用 nvm 安裝 Node.js 和 npm 的步驟：

1. 安裝 nvm：

   ```
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | zsh
   ```

2. 重新載入終端或執行以下命令使 nvm 生效：

   ```
   source ~/.zshrc
   ```

3. 列出可用的 Node.js 版本：

   ```
   nvm ls-remote
   ```

   這將列出所有可供安裝的 Node.js 版本。你可以從列表中選擇特定版本來安裝。

4. 安裝特定版本的 Node.js：

   ```
   nvm install <version>
   ```

   將 `<version>` 替換為你想安裝的 Node.js 版本，例如 `nvm install 14.17.0`。

5. 切換使用特定版本的 Node.js：

   ```
   nvm use <version>
   ```

   將 `<version>` 替換為你想使用的 Node.js 版本，例如 `nvm use 14.17.0`。

6. 驗證 Node.js 和 npm 安裝是否成功：

   ```
   node --version
   npm --version
   ```

   確保輸出的版本號與你預期的 Node.js 和 npm 版本相符。

## 安裝 Anaconda

Anaconda 是一個用於科學計算的 Python 發行版，內置了許多常用的科學計算套件。conda 是 Anaconda 的套件管理系統，用於管理不同環境下的套件和依賴。以下是在 Linux 虛擬機上安裝 Anaconda 的步驟：

1. 前往 [Anaconda 下載頁面](https://repo.anaconda.com/archive/) 查看最新版本的 Anaconda 安裝包。你可以在這個頁面中找到適用於 Linux 的版本。

2. 使用下載的安裝包執行以下指令安裝 Anaconda：

   ```
   wget https://repo.anaconda.com/archive/Anaconda3-<version>-Linux-x86_64.sh
   ```

   請將 `<version>` 替換為下載的 Anaconda 版本號。

3. 授予安裝腳本執行權限：

   ```
   chmod +x Anaconda3-<version>-Linux-x86_64.sh
   ```

4. 執行安裝腳本：

   ```
   ./Anaconda3-<version>-Linux-x86_64.sh
   ```

5. 根據安裝程序的提示進行安裝。預設情況下，Anaconda 將安裝在你的用戶目錄下。

6. 安裝完成後，重新載入終端或執行以下指令使 Anaconda 生效：

   ```
   source ~/.zshrc
   ```

7. 驗證 Anaconda 和 conda 安裝是否成功：

   ```
   conda --version
   ```

   確保輸出的版本號與你預期的 Anaconda 版本相符。

