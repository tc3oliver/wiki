# 如何在 ASP.NET Core 中使用 Swashbuckle 和 XML 註解顯示 Swagger UI？

在 ASP.NET Core 開發中，Swashbuckle 是一個流行的套件，可用於自動生成 Swagger 文件和 Swagger UI。但是，Swagger UI 默認不會顯示 XML 註解。本文將介紹如何使用 Swashbuckle 和 XML 註解顯示 Swagger UI。

## 步驟一：安裝 Swashbuckle.AspNetCore 套件

首先，在您的 ASP.NET Core 專案中安裝 Swashbuckle.AspNetCore 套件。可以使用 NuGet 套件管理器或命令行安裝，具體命令如下：

```
dotnet add package Swashbuckle.AspNetCore
```

## 步驟二：配置 Swagger 和 XML 註解

在 `Startup.cs` 文件中的 `ConfigureServices` 方法中，添加以下程式碼以配置 Swagger 和 XML 註解：

```csharp
using System.IO;
using System.Reflection;
using Microsoft.OpenApi.Models;

// ... 其他 using 語句 ...

public void ConfigureServices(IServiceCollection services)
{
    // ... 其他服務配置 ...

    // 添加 Swagger 並設置 XML 註解路徑
    services.AddSwaggerGen(c =>
    {
        c.SwaggerDoc("v1", new OpenApiInfo { Title = "My API", Version = "v1" });

        // 獲取應用程式所在目錄的 XML 註解文件的路徑
        var xmlFile = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
        var xmlPath = Path.Combine(AppContext.BaseDirectory, xmlFile);

        // 啟用 XML 註解
        c.IncludeXmlComments(xmlPath);
    });
}
```

在上面的程式碼中，我們首先添加了 Swagger 文件（`SwaggerDoc`），然後獲取了應用程式所在目錄的 XML 註解文件的路徑。最後，我們啟用了 XML 註解，以便 Swagger UI 可以讀取和顯示它們。

## 步驟三：啟用 Swagger 和 Swagger UI

在 `Startup.cs` 文件中的 `Configure` 方法中，添加以下程式碼以啟用 Swagger 和 Swagger UI：

```csharp
using Microsoft.AspNetCore.Builder;

// ... 其他 using 語句 ...

public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    // ... 其他應用程式配置 ...

    // 啟用中間件以提供生成的 Swagger 作為 JSON 終結點
    app.UseSwagger();

    // 啟用中間件以提供 Swagger UI，可用於瀏覽和測試 API
    app.UseSwaggerUI(c =>
    {
        c.SwaggerEndpoint("/swagger/v1/swagger.json", "My API V1");
    });

    // ... 其他應用程式配置 ...
}
```

在上面的程式碼中，我們啟用了兩個中間件。第一個是 `UseSwagger()`，它提供了生成的 Swagger 文件作為JSON 終結點。第二個是 `UseSwaggerUI()`，它提供了 Swagger UI，用於瀏覽和測試 API。在 `SwaggerEndpoint` 方法中，我們指定了 Swagger 文件的路徑和標題。

## 步驟四：啟用 XML 註解輸出

最後，啟用專案的 XML 註解輸出。打開您的專案文件（通常是 `.csproj` 文件），並添加以下內容：

```xml
<PropertyGroup>
  <GenerateDocumentationFile>true</GenerateDocumentationFile>
  <NoWarn>$(NoWarn);1591</NoWarn>
</PropertyGroup>
```

在上面的程式碼中，`GenerateDocumentationFile` 設置為 `true`，以啟用 XML 註解輸出。`NoWarn` 設置為 `$(NoWarn);1591`，以忽略缺少 XML 註解的警告。

完成上述步驟後，您的 API 的 XML 註解將顯示在 Swagger UI 中。現在，您可以輕鬆地查看和測試您的 API。

總結

在本文中，我們介紹了如何在 ASP.NET Core 中使用 Swashbuckle 和 XML 註解顯示 Swagger UI。這是一個非常有用的技巧，可以幫助您更好地了解和測試您的 API。