# 使用 npm 在 ASP.NET Core 專案中管理前端庫

1. 在您的 ASP.NET Core 專案的根目錄中建立一個名為 package.json 的檔案。您可以透過執行以下指令來建立 package.json 檔案：

   ```
   npm init
   ```

2. 安裝所需的庫。例如，如果您想要安裝 jQuery 庫，可以使用以下指令：

   ```
   npm install jquery
   ```

   這會在當前專案的 node_modules 目錄下安裝 jQuery 庫，並將其新增到 package.json 檔案中的依賴項清單中。

3. 將庫複製到 wwwroot/lib 目錄中。在 package.json 檔案所在的目錄中，執行以下指令：

   ```
   npm run copy
   ```

   此指令會使用您專案的 copy.js 腳本，將所需的庫從 node_modules 目錄中複製到 wwwroot/lib 目錄中。您需要在專案中建立 copy.js 腳本並將其新增到 package.json 檔案中的 scripts 中，以便自動執行複製操作。例如，您可以建立一個名為 copy.js 的腳本，如下所示：

   ```
   const fs = require('fs');
   const path = require('path');

   const libPath = path.join(__dirname, 'wwwroot/lib');

   fs.mkdirSync(libPath, { recursive: true });

   const modulesToCopy = [
       { src: 'jquery/dist/jquery.min.js', dest: 'jquery/jquery.min.js' },
       // 添加其他庫的專案
   ];

   for (const module of modulesToCopy) {
       const srcPath = path.join(__dirname, 'node_modules', module.src);
       const destPath = path.join(libPath, module.dest);
       fs.copyFileSync(srcPath, destPath);
   }
   ```

   然後，您需要將 copy.js 腳本新增到 package.json 檔案的 scripts 中，如下所示：

   ```
   {
       "name": "my-aspnetcore-app",
       "version": "1.0.0",
       "scripts": {
           "copy": "node copy.js"
       },
       "dependencies": {
           "jquery": "^3.6.0"
       }
   }
   ```

   現在，當您執行 npm run copy 指令時，它會自動將所需的庫從 node_modules 目錄中複製到 wwwroot/lib 目錄中。

使用 npm 在 wwwroot/lib 目錄中安裝和管理庫，需要建立一個 package.json 檔案、使用 npm 安裝所需的庫、建立一個 copy.js 腳本將庫複製到 wwwroot/lib 目錄中，並將 copy.js 新增到 package.json
