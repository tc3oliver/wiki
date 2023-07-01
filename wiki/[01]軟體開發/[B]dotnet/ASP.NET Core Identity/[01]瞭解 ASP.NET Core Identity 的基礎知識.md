# 瞭解 ASP.NET Core Identity 的基礎知識

ASP.NET Core Identity 是一個用於管理使用者身份驗證和授權的框架，讓開發者可以快速地構建安全的應用程式。本篇文章將介紹 Identity 架構的基本概念，並教你如何建立一個簡單的 ASP.NET Core Identity 應用程式。

## 1. 瞭解 Identity 架構的基本概念

Identity 架構是一種用於管理身份驗證和授權的框架。它包含以下基本概念：

### 1. 使用者 (User)

使用者是代表應用程式中註冊使用者的物件，每個使用者都有唯一的識別碼 (Id) 和其他屬性，如使用者名稱、密碼、電子郵件地址等。使用者是身份驗證的主體，應用程式可以通過使用者來授權對資源的訪問。

### 2. 角色 (Role)

角色是用於對使用者進行分組和授權的物件。角色可以用來表示不同的使用者類型，如管理員、編輯、訪客等。通常，一個使用者可以屬於多個角色，這些角色可以基於權限進行分組，以便更方便地管理使用者的訪問權限。

### 3. 聲明 (Claim)

聲明是用於描述使用者的特定屬性的物件。聲明可以用來存儲應用程式特定的資訊，如使用者的偏好設定、購物車內容等。在身份驗證期間，應用程式可以通過聲明來驗證使用者的身份。

### 4. 策略 (Policy)

策略是用於定義應用程式中特定操作的授權規則的物件。策略可以基於角色、聲明或其他自定義規則來控制使用者訪問資源的權限。通常，應用程式會使用多個策略來定義不同的授權規則，以便更好地控制使用者對資源的訪問權限。

### 5. 使用者儲存庫 (User Store)

使用者儲存庫是用於存儲使用者資訊的資料庫，如使用者名稱、密碼等。使用者儲存庫通常是應用程式中的一個組件，負責執行與使用者相關的 CRUD 操作，如創建、更新、刪除等。

### 6. 角色儲存庫 (Role Store)

角色儲存庫是用於存儲角色資訊的資料庫，角色是一種將權限分組的方式，以便更方便地管理使用者的訪問權限。角色儲存庫通常包含角色名稱、權限等屬性，並且負責執行與角色相關的 CRUD 操作。

### 7. 密碼驗證器 (Password Validator)

密碼驗證器是用於檢查使用者密碼是否符合安全要求的組件。密碼驗證器通常會檢查密碼強度、密碼是否過期等因素，以確保使用者的密碼符合安全要求。

### 8. 使用者管理器 (User Manager)

使用者管理器是用於執行與使用者相關的 CRUD 操作的組件，如創建、更新、刪除等。使用者管理器通常是應用程式中的一個組件，負責管理使用者的身份驗證和授權。

### 9. 簽名管理器 (SignIn Manager)

簽名管理器是用於管理使用者的身份驗證和登出操作的組件。簽名管理器負責創建、驗證和刪除使用者簽名，以確保應用程式的安全性和可靠性。

Identity 架構提供了一組標準的組件和概念，用於管理身份驗證和授權。這些組件和概念可以幫助開發人員更容易地實現應用程式的安全性和可靠性，從而保護使用者和敏感資料的安全。

## 2. 建立一個簡單的 ASP.NET Core Identity 應用程式

接下來，我們將透過以下步驟建立一個簡單的 ASP.NET Core Identity 應用程式：

1. **安裝必要的套件：** 開始前，請確保已安裝 .NET Core SDK。然後，使用以下命令安裝 ASP.NET Core Identity 相關的套件：

   ```csharp
   dotnet add package Microsoft.AspNetCore.Identity.EntityFrameworkCore
   dotnet add package Microsoft.AspNetCore.Identity.UI
   ```

2. **建立資料庫上下文 (DbContext)：** 建立一個繼承自 `IdentityDbContext` 的類別，這將幫助我們設置 Identity 所需的資料庫表格。在這個類別中，我們可以自定義應用程式的使用者和角色類型：

   ```csharp
   using Microsoft.AspNetCore.Identity;
   using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
   using Microsoft.EntityFrameworkCore;

   public class ApplicationUser : IdentityUser
   {
       // 自定義應用程式使用者類型的額外屬性
       public string FullName { get; set; }
   }

   public class ApplicationRole : IdentityRole
   {
       // 自定義應用程式角色類型的額外屬性
       public string Description { get; set; }
   }

   public class ApplicationDbContext : IdentityDbContext<ApplicationUser, ApplicationRole, string>
   {
       public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
           : base(options)
       {
       }

       // 若有其他實體類型，可在此加入 DbSet
   }
   ```

3. **註冊 Identity 服務：** 在 Program.cs 檔案中，將 Identity 服務添加到應用程式的依賴注入容器中。同時，設定資料庫上下文類別和資料庫連接字串。

   ```csharp
   using Microsoft.AspNetCore.Identity;
   using Microsoft.EntityFrameworkCore;

   var builder = WebApplication.CreateBuilder(args);

   builder.Services.AddIdentity<ApplicationUser, ApplicationRole>()
           .AddEntityFrameworkStores<ApplicationDbContext>()
           .AddDefaultTokenProviders();
   ```

4. **配置 Identity：** 在 Program.cs 檔案中，將 Identity 中介軟體添加到應用程式的請求管道中。記得在 `UseRouting()` 和 `UseEndpoints()` 之間加入 `UseAuthentication()` 和 `UseAuthorization()`。

   ```csharp
    app.UseRouting();

    app.UseAuthentication();
    app.UseAuthorization();

    app.UseEndpoints();
   ```

5. **建立使用者和角色管理控制器：** 可以使用 Visual Studio 或其他相關工具，建立一個新的 MVC 控制器，用於管理應用程式的使用者和角色。這個控制器將包含用於新增、編輯、刪除使用者和角色的相關操作。

完成上述步驟後，你已經成功建立了一個簡單的 ASP.NET Core Identity 應用程式，並自定義了應用程式的使用者和角色類型。你可以進一步擴展這個應用程式，加入更多的功能，如登入、登出、註冊等。
