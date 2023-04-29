# 使用 ASP.NET Core Identity 和 JWT 實作 Web 和 App 共用使用者，打造安全可靠的身分驗證解決方案

## 一、介紹

在現今的數位時代，身分驗證在各類應用程式中扮演著非常重要的角色。透過身分驗證，我們可以確保只有授權的使用者才能訪問特定的資源和功能。本文將介紹 ASP.NET Core Identity 和 JWT（JSON Web Tokens）的基本概念，並展示如何實作 Web 和 App 共用使用者的安全可靠的身分驗證解決方案。

### 介紹身分驗證的重要性

身分驗證是確保應用程式安全的基石。無論是 Web 應用程式還是 App，都需要對使用者身分進行驗證，以防止未經授權的訪問和數據洩露。此外，身分驗證還可以為應用程式提供更好的使用者體驗，例如顯示使用者的個人資訊和偏好設定等。

### 介紹 ASP.NET Core Identity 和 JWT 的基本概念

ASP.NET Core Identity 是一個用於實現身分驗證和授權功能的框架。它提供了一整套用於管理使用者和角色的 API，以及用於處理登入、登出、註冊等操作的內建支持。使用 ASP.NET Core Identity，開發人員可以輕鬆地在應用程式中實現安全可靠的身分驗證解決方案。

JWT（JSON Web Tokens）是一種開放標準，用於在各方之間安全地傳遞 JSON 格式的資訊。JWT 可以對資料進行編碼，生成一個簽名的令牌，從而確保資料在傳輸過程中不會被篡改。在身分驗證方面，JWT 常被用作一種無狀態的授權機制，允許服務器在不需要查詢資料庫的情況下驗證使用者的身分。

## 二、設計和建立資料庫架構

### 設計使用者和身分驗證相關的資料表

在開始實作身分驗證解決方案之前，我們需要先設計使用者和身分驗證相關的資料表。這些資料表將儲存使用者資訊、角色、權限等相關數據。在 ASP.NET Core Identity 中，已經為我們提供了一些內建的資料表結構，例如 `AspNetUsers`、`AspNetRoles`、`AspNetUserRoles` 等。我們可以根據需要進行擴展和自定義。

### 使用 Entity Framework Core Code First 建立資料庫

Entity Framework Core 是一個功能強大的 ORM（物件關聯對映）框架，可以幫助我們更方便地操作資料庫。在本文中，我們將使用 Code First 方法來建立資料庫，這意味著我們首先定義資料表對應的類別，然後根據類別生成資料庫。

首先，在 `Program.cs` 中建立一個新的 `WebApplicationBuilder` 實例，註冊 Entity Framework Core 服務，並指定資料庫連接字串：

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));
```

接著，我們在資料模型類別中添加自定義的屬性，例如：

```csharp
public class ApplicationUser : IdentityUser
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
    // 其他自定義屬性
}
```

然後，在 `ApplicationDbContext` 類別中，我們可以使用 `DbSet` 來定義資料表：

```csharp
public class ApplicationDbContext : IdentityDbContext<ApplicationUser>
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    // 其他自定義資料表
}
```

最後，我們需要使用 EF Core 的遷移功能來生成資料庫。在命令提示字元或終端機中，執行以下命令：

```
dotnet ef migrations add InitialCreate
dotnet ef database update
```

這樣，我們就完成了資料庫架構的設計和建立。

## 三、實作 ASP.NET Core Identity 網頁和 API

### 實作 ASP.NET Core Identity 網頁應用程式

在此部分，我們將實作 ASP.NET Core Identity 網頁應用程式，包括使用者註冊、登入、登出、修改個人資訊等功能。首先，我們需要在 `Program.cs` 文件中註冊 ASP.NET Core Identity 服務：

```csharp
builder.Services.AddIdentity<ApplicationUser, IdentityRole>()
    .AddEntityFrameworkStores<ApplicationDbContext>()
    .AddDefaultTokenProviders();
```

接著，我們可以在控制器中實現相關操作方法。例如，以下是一個簡單的註冊操作方法：

```csharp
[HttpPost]
[AllowAnonymous]
public async Task<IActionResult> Register(RegisterViewModel model)
{
    if (ModelState.IsValid)
    {
        var user = new ApplicationUser { UserName = model.Email, Email = model.Email, FirstName = model.FirstName, LastName = model.LastName };
        var result = await _userManager.CreateAsync(user, model.Password);
        if (result.Succeeded)
        {
            await _signInManager.SignInAsync(user, isPersistent: false);
            return RedirectToAction(nameof(HomeController.Index), "Home");
        }
        AddErrors(result);
    }

    // 出現錯誤，重新顯示註冊頁面
    return View(model);
}
```

對於登入、登出和修改個人資訊等功能，我們可以使用類似的方法來實現。

### 實作 ASP.NET Core Identity Web API

除了網頁應用程式之外，我們還需要實作一個 Web API 來為 App 提供身分驗證和使用者管理功能。在這個 Web API 中，我們將實現獲取使用者資訊、新增使用者、更新使用者等操作。

首先，在 `Program.cs` 中註冊 ASP.NET Core Identity 服務，並設定 JWT 身分驗證選項：

```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            ValidIssuer = builder.Configuration["Jwt:Issuer"],
            ValidAudience = builder.Configuration["Jwt:Audience"],
            IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(builder.Configuration["Jwt:Key"]))
        };
    });

// ...

var app = builder.Build();
```

接著，我們可以在 Web API 控制器中實現相關操作方法。以下是一個簡單的獲取使用者資訊操作方法：

```csharp
[HttpGet("{id}")]
public async Task<IActionResult> GetUserById(string id)
{
    var user = await _userManager.FindByIdAsync(id);

    if (user == null)
    {
        return NotFound();
    }

    return Ok(new { user.Id, user.UserName, user.Email, user.FirstName, user.LastName });
}
```

對於新增使用者、更新使用者等功能，我們可以使用類似的方法來實現。

## 四、使用 JWT 進行身分驗證和授權

在此部分，我們將瞭解 JWT 的概念和使用方法，並實作使用 JWT 的身分驗證和授權功能。

### 瞭解 JWT 的概念和使用方法

JWT 是一種輕量級的身分驗證和授權機制。它允許我們在不需要查詢資料庫的情況下驗證使用者的身分。JWT 由三部分組成：頭部（Header）、有效負載（Payload）和簽名（Signature）。頭部包含令牌的類型和加密算法資訊；有效負載包含一些聲明，如使用者 ID、發行者、過期時間等；簽名則用於確保令牌在傳輸過程中不會被篡改。

### 實作使用 JWT 的身分驗證和授權

在我們的 Web API 中，我們需要實現一個登入操作方法，用於生成 JWT 並將其發送給客戶端。以下是一個簡單的登入操作方法：

```csharp
[HttpPost("login")]
public async Task<IActionResult> Login([FromBody] LoginViewModel model)
{
    if (ModelState.IsValid)
    {
        var user = await _userManager.FindByEmailAsync(model.Email);
        if (user != null)
        {
            var result = await _signInManager.CheckPasswordSignInAsync(user, model.Password, false);
            if (result.Succeeded)
            {
                var token = GenerateJwtToken(user);
                return Ok(new { token });
            }
        }
    }

    return Unauthorized();
}

private string GenerateJwtToken(ApplicationUser user)
{
    var claims = new List<Claim>
    {
        new Claim(JwtRegisteredClaimNames.Sub, user.Id),
        new Claim(JwtRegisteredClaimNames.Jti, Guid.NewGuid().ToString())
    };

    var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_configuration["Jwt:Key"]));
    var creds = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);
    var expires = DateTime.Now.AddDays(Convert.ToDouble(_configuration["Jwt:ExpireDays"]));

    var token = new JwtSecurityToken(
        _configuration["Jwt:Issuer"],
        _configuration["Jwt:Audience"],
        claims,
        expires: expires,
        signingCredentials: creds
    );

    return new JwtSecurityTokenHandler().WriteToken(token);
}
```

接著，我們需要在 Web API 控制器的操作方法上添加 `[Authorize]` 屬性，以保護需要身分驗證的資源：

```csharp
[HttpGet("{id}")]
[Authorize]
public async Task<IActionResult> GetUserById(string id)
{
    // ...
}
```

### 實作 ASP.NET Core Identity Web API 的 JWT 身分驗證和授權

在上述步驟中，我們已經實現了使用 JWT 的身分驗證和授權功能。接下來，我們需要將這些功能應用到我們的 ASP.NET Core Identity Web API 中。

首先，我們需要在 `Program.cs` 文件中的 `WebApplication.CreateBuilder` 方法中註冊 JWT 身分驗證服務，並設定相關選項：

```csharp
using Microsoft.IdentityModel.Tokens;

// ...

var builder = WebApplication.CreateBuilder(args);

// ...

builder.Services.AddAuthentication(options =>
{
    options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
    options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
})
.AddJwtBearer(options =>
{
    options.TokenValidationParameters = new TokenValidationParameters
    {
        ValidateIssuer = true,
        ValidateAudience = true,
        ValidateLifetime = true,
        ValidateIssuerSigningKey = true,
        ValidIssuer = builder.Configuration["Jwt:Issuer"],
        ValidAudience = builder.Configuration["Jwt:Audience"],
        IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(builder.Configuration["Jwt:Key"]))
    };
});

// ...

var app = builder.Build();
```

然後，在我們的 Web API 控制器中，我們可以為需要身分驗證和授權的操作方法添加 `[Authorize]` 屬性：

```csharp
[HttpGet("{id}")]
[Authorize]
public async Task<IActionResult> GetUserById(string id)
{
    // ...
}
```

這樣，我們就完成了使用 JWT 的身分驗證和授權功能的實現。

## 五、實作 App 使用 ASP.NET Core Identity

在此部分，我們將實作 App 的登入和登出功能，並使用 JWT 進行身分驗證和授權。此外，我們還將實現 App 使用者資訊的獲取和更新功能。

### 實作 App 的登入和登出功能

在我們的 App 中，我們需要實現一個登入功能，用於向 ASP.NET Core Identity Web API 發送登入請求並獲取 JWT。登出功能則需要清除客戶端儲存的 JWT。

以下是一個使用 Xamarin.Forms 實現的簡單登入操作方法：

```csharp
public async Task<bool> LoginAsync(string email, string password)
{
    var httpClient = new HttpClient();
    var content = new StringContent(JsonConvert.SerializeObject(new { Email = email, Password = password }), Encoding.UTF8, "application/json");
    var response = await httpClient.PostAsync("https://your-api-url/login", content);

    if (response.IsSuccessStatusCode)
    {
        var json = await response.Content.ReadAsStringAsync();
        var token = JsonConvert.DeserializeObject<TokenResponse>(json);
        _settings.AccessToken = token.AccessToken;
        return true;
    }

    return false;
}
```

### 實作 App 使用者資訊的獲取和更新功能

在 App 中，我們還需要實現一個功能，用於獲取和更新使用者資訊。獲取使用者資訊時，我們需要在請求頭中添加 JWT，以進行身分驗證和授權。

以下是一個使用 Xamarin.Forms 實現的簡單獲取使用者資訊操作方法：

```csharp
public async Task<User> GetUserAsync()
{
    var httpClient = new HttpClient();
    httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", _settings.AccessToken);
    var response = await httpClient.GetAsync("https://your-api-url/users/your-user-id");

    if (response.IsSuccessStatusCode)
    {
        var json = await response.Content.ReadAsStringAsync();
        var user = JsonConvert.DeserializeObject<User>(json);
        return user;
    }

    return null;
}
```

對於更新使用者資訊功能，我們可以使用類似的方法來實現。

## 六、實作 App 與 Web 共用使用者

在此部分，我們將了解 App 和 Web 共用使用者的需求和挑戰，並實作相應的解決方案，包括身分驗證和資料同步。

### 瞭解 App 和 Web 共用使用者的需求和挑戰

在很多情況下，我們希望能讓使用者在 App 和 Web 端使用相同的帳號登入，並共享部分或全部使用者資訊。這樣可以提供一個統一且便捷的使用者體驗。

然而，App 和 Web 通常使用不同的技術堆疊和資料傳輸協議，因此實現共用使用者的解決方案可能面臨一定的挑戰。例如，我們需要確保身分驗證和授權機制能在兩個平台上無縫協作；同時，我們還需要解決資料同步和更新的問題。

### 實作 App 和 Web 共用使用者的解決方案

在本文中，我們使用 ASP.NET Core Identity 和 JWT 來實現一個跨平台的身分驗證和授權機制。這樣，無論使用者在 App 或 Web 端登入，都可以使用相同的帳號並獲得相同的使用者資訊。

為了確保資料同步和更新，我們可以在 App 和 Web 端都實現一個操作方法，用於獲取和更新使用者資訊。這些操作方法應該使用相同的 API 端點，以確保資料的一致性。

以下是一個簡單的資料同步和更新流程：

1. 使用者在 App 端登入，並獲取 JWT。
2. App 使用 JWT 向 Web API 請求獲取使用者資訊。
3. 使用者在 App 端修改個人資訊，並向 Web API 發送更新請求。
4. Web API 將更新後的使用者資訊儲存到資料庫。
5. 使用者在 Web 端登入，並獲取更新後的使用者資訊。

通過這個流程，我們可以確保 App 和 Web 端的使用者資訊始終保持一致。

## 七、部署和測試

在完成所有功能的實現後，我們需要部署 ASP.NET Core Identity Web API 和 App，並對其進行測試。

部署 ASP.NET Core Identity Web API 可以使用多種方法，例如部署到 IIS、Azure 或其他支援 .NET Core 的雲平台。在選擇部署方案時，應該考慮到應用程式的性能需求、成本和擴展性。同樣，部署 App 可以選擇將其上架到 Google Play、App Store 或其他應用市場，以便使用者能夠輕鬆下載和安裝。

在部署完成後，我們需要對 ASP.NET Core Identity Web API 和 App 進行測試，以確保身分驗證和授權功能能夠正常工作。測試應該包括以下幾個方面：

1. 使用者註冊、登入和登出功能。
2. 使用者資訊的獲取和更新功能。
3. JWT 的生成和驗證功能。
4. 身分驗證和授權機制的安全性和效能。

通過進行充分的測試，我們可以確保我們的身分驗證解決方案能夠提供一個安全、可靠且高效的使用者體驗。

## 八、結論

本文介紹了如何使用 ASP.NET Core Identity 和 JWT 實作一個跨平台的身分驗證解決方案，使得 Web 和 App 能夠共用使用者資訊。我們設計和建立了資料庫架構，並實現了網頁應用程式和 API 的身分驗證功能。接著，我們使用 JWT 進行身分驗證和授權，並將其應用到 Web API 中。最後，我們實作了 App 使用 ASP.NET Core Identity 的功能，並解決了資料同步和更新的問題。

身分驗證在現代應用程式中起著至關重要的作用。通過實現一個安全可靠的身分驗證解決方案，我們可以保護使用者資訊，防止未經授權的訪問，並提供一個統一且便捷的使用者體驗。

展望未來，隨著網路技術的不斷發展，身分驗證和授權機制將面臨更多的挑戰和機遇。我們應該繼續關注新的技術趨勢，不斷優化和完善我們的身分驗證解決方案，以滿足不斷變化的應用需求。
