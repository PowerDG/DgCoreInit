# ABP入门系列（16）——通过webapi与系统进行交互





# ABP入门系列（16）——通过webapi与系统进行交互

​             ![96](https://upload.jianshu.io/users/upload_avatars/2799767/3883b7da-8419-443f-882e-be41a8a9ab6a.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/96/h/96) 

​             [圣杰](https://www.jianshu.com/u/39ec0e6b1844)                          

​                                                    0.1                                                 2017.04.23 11:42*               字数 1875             阅读 14320评论 2喜欢 16

> **ABP入门系列目录——学习Abp框架之实操演练 源码路径：Github-LearningMpaAbp**

------

# 1. 引言

上一节我们讲解了[如何创建微信公众号模块](https://www.jianshu.com/p/1e6efd9be629)，这一节我们就继续跟进，来讲一讲公众号模块如何与系统进行交互。
 微信公众号模块作为一个独立的web模块部署，要想与现有的【任务清单】进行交互，我们要想明白以下几个问题：

1. 如何进行交互？
    ABP模板项目中默认创建了webapi项目，其**动态webapi技术**允许我们直接访问appservice作为webapi而不用在webapi层编写额外的代码。所以，自然而然我们要通过webapi与系统进行交互。
2. 通过webapi与系统进行交互，如何确保安全？
    我们知道暴露的webapi如果不加以授权控制，就如同在大街上裸奔。所以在访问webapi时，我们需要通过身份认证来确保安全访问。
3. 都有哪几种身份认证方式？
    第一种就是大家熟知的cookie认证方式；
    第二种就是token认证方式：在访问webapi之前，先要向目标系统申请令牌（token)，申请到令牌后，再使用令牌访问webapi。Abp默认提供了这种方式；
    第三种是基于OAuth2.0的token认证方式：OAuth2.0是什么玩意？建议先看看[OAuth2.0 知多少](https://www.jianshu.com/p/a57bda33e992)以便我们后续内容的展开。OAuth2.0认证方式弥补了Abp自带token认证的短板，即无法进行token刷新。

基于这一节，我完善了一个demo，大家可以直接访问[http://shengjietest.azurewebsites.net/](https://link.jianshu.com?t=http://shengjietest.azurewebsites.net/)进行体验。



![img](https://upload-images.jianshu.io/upload_images/2799767-aa93576e4cb9bde1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/692)

demo

下面我们就以【通过webapi请求用户列表】为例看一看三种认证方式的具体实现。

# 2. Cookie认证方式

Cookie认证方式的原理就是：在访问webapi之前，通过登录目标系统建立连接，将cookie写入本地。下一次访问webapi的时候携带cookie信息就可以完成认证。

## 2.1. 登录目标系统

这一步简单，我们仅需提供用户名密码，Post一个登录请求即可。
 我们在微信模块中创建一个`WeixinController`：

```
public class WeixinController : Controller
{
    private readonly IAbpWebApiClient _abpWebApiClient;
    private string baseUrl = "http://shengjie.azurewebsites.net/";
    private string loginUrl = "/account/login";
    private string webapiUrl = "/api/services/app/User/GetUsers";
    private string abpTokenUrl = "/api/Account/Authenticate";
    private string oAuthTokenUrl = "/oauth/token";
    private string user = "admin";
    private string pwd = "123qwe";

    public WeixinController()
    {
        _abpWebApiClient = new AbpWebApiClient();
    }
}
```

其中`IAbpWebApiClient`是对`HttpClient`的封装，用于发送 HTTP 请求和接收HTTP 响应。

下面添加`CookieBasedAuth`方法，来完成登录认证，代码如下：

```
public async Task CookieBasedAuth()
{
    Uri uri = new Uri(baseUrl + loginUrl);
    var handler = new HttpClientHandler() { AutomaticDecompression = DecompressionMethods.None, UseCookies = true };

    using (var client = new HttpClient(handler))
    {
        client.BaseAddress = uri;
        client.DefaultRequestHeaders.Accept.Add(new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("application/json"));

        var content = new FormUrlEncodedContent(new Dictionary<string, string>()
        {
            {"TenancyName", "Default"},
            {"UsernameOrEmailAddress", user},
            {"Password", pwd }
        });
                
        var result = await client.PostAsync(uri, content);

        string loginResult = await result.Content.ReadAsStringAsync();

        var getCookies = handler.CookieContainer.GetCookies(uri);

        foreach (Cookie cookie in getCookies)
        {
            _abpWebApiClient.Cookies.Add(cookie);
        }
    }
}
```

这段代码中有几个点需要注意：

1. 指定`HttpClientHandler`属性`UseCookie = true`，使用Cookie；
2.  `client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));`用来指定接受的返回值；
3. 使用`FormUrlEncodedContent`进行传参；
4. 使用`var getCookies = handler.CookieContainer.GetCookies(uri);`获取返回的Cookie，并添加到`_abpWebApiClient.Cookies`的集合中，以便下次直接携带cookie信息访问webapi。

## 2.2. 携带cookie访问webapi

服务器返回的cookie信息在登录成功后已经填充到`_abpWebApiClient.Cookies`中，我们只需post一个请求到目标api即可。

```
public async Task<PartialViewResult> SendRequestBasedCookie()
{
    await CookieBasedAuth();
    return await GetUserList(baseUrl + webapiUrl);
}

private async Task<PartialViewResult> GetUserList(string url)
{
    try
    {
        var users = await _abpWebApiClient.PostAsync<ListResultDto<UserListDto>>(url);

        return PartialView("_UserListPartial", users.Items);
    }
    catch (Exception e)
    {
        ViewBag.ErrorMessage = e.Message;
    }

    return null;
}
```

# 3. Token认证方式

Abp默认提供的token认证方式，很简单，我们仅需要post一个请求到`/api/Account/Authenticate`即可请求到token。然后使用token即可请求目标webapi。
 但这其中有一个问题就是，如果token过期，就必须使用用户名密码重写申请token，体验不好。

## 3.1. 请求token

```
public async Task<string> GetAbpToken()
{
    var tokenResult = await _abpWebApiClient.PostAsync<string>(baseUrl + abpTokenUrl, new
    {
        TenancyName = "Default",
        UsernameOrEmailAddress = user,
        Password = pwd
    });
    this.Response.SetCookie(new HttpCookie("access_token", tokenResult));
    return tokenResult;
}
```

这段代码中我们将请求到token直接写入到cookie中。以便我们下次直接从cookie中取回token直接访问webapi。

## 3.2. 使用token访问webapi

从cookie中取回token，在请求头中添加`Authorization = Bearer token`，即可。

```
public async Task<PartialViewResult> SendRequest()
{
    var token = Request.Cookies["access_token"]?.Value;
    //将token添加到请求头
    _abpWebApiClient.RequestHeaders.Add(new NameValue("Authorization", "Bearer " + token));

    return await GetUserList(baseUrl + webapiUrl);
}
```

这里面需要注意的是，abp中配置`app.UseOAuthBearerAuthentication(AccountController.OAuthBearerOptions);`使用的是`Bearer token`，所以我们在请求weiapi时，要在请求头中假如`Authorization`信息时，使用`Bearer token`的格式传输token信息（**Bearer后有一个空格！**）。

# 4. OAuth2.0 Token认证方式

OAuth2.0提供了token刷新机制，当服务器颁发的token过期后，我们可以直接通过`refresh_token`来申请token即可，不需要用户再录入用户凭证申请token。

## 4.1. Abp集成OAuth2.0

在WebApi项目中的Api路径下创建`Providers`文件夹，添加`SimpleAuthorizationServerProvider`和`SimpleRefreshTokenProvider`类。
 其中`SimpleAuthorizationServerProvider`用来验证客户端的用户名和密码来颁发token；`SimpleRefreshTokenProvider`用来刷新token。

```
public class SimpleAuthorizationServerProvider : OAuthAuthorizationServerProvider, ITransientDependency
{
    private readonly LogInManager _logInManager;

    public SimpleAuthorizationServerProvider(LogInManager logInManager)
        {
            _logInManager = logInManager;
        }

    public override Task ValidateClientAuthentication(OAuthValidateClientAuthenticationContext context)
        {
            string clientId;
            string clientSecret;
            if (!context.TryGetBasicCredentials(out clientId, out clientSecret))
            {
                context.TryGetFormCredentials(out clientId, out clientSecret);
            }
            var isValidClient = string.CompareOrdinal(clientId, "app") == 0 &&
                                string.CompareOrdinal(clientSecret, "app") == 0;
            if (isValidClient)
            {
                context.OwinContext.Set("as:client_id", clientId);
                context.Validated(clientId);
            }
            else
            {
                context.SetError("invalid client");
            }

            return Task.FromResult<object>(null);
        }

    public override async Task GrantResourceOwnerCredentials(OAuthGrantResourceOwnerCredentialsContext context)
        {
            var tenantId = context.Request.Query["tenantId"];
            var result = await GetLoginResultAsync(context, context.UserName, context.Password, tenantId);
            if (result.Result == AbpLoginResultType.Success)
            {
                //var claimsIdentity = result.Identity;                
                var claimsIdentity = new ClaimsIdentity(result.Identity);
                claimsIdentity.AddClaim(new Claim(ClaimTypes.Name, context.UserName));
                var ticket = new AuthenticationTicket(claimsIdentity, new AuthenticationProperties());
                context.Validated(ticket);
            }
        }

    public override  Task GrantRefreshToken(OAuthGrantRefreshTokenContext context)
        {
            var originalClient = context.OwinContext.Get<string>("as:client_id");
            var currentClient = context.ClientId;

            // enforce client binding of refresh token
            if (originalClient != currentClient)
            {
                context.Rejected();
                return Task.FromResult<object>(null);
            }

            // chance to change authentication ticket for refresh token requests
            var newId = new ClaimsIdentity(context.Ticket.Identity);
            newId.AddClaim(new Claim("newClaim", "refreshToken"));

            var newTicket = new AuthenticationTicket(newId, context.Ticket.Properties);
            context.Validated(newTicket);

            return Task.FromResult<object>(null);
        }

    private async Task<AbpLoginResult<Tenant, User>> GetLoginResultAsync(OAuthGrantResourceOwnerCredentialsContext context,
        string usernameOrEmailAddress, string password, string tenancyName)
        {
            var loginResult = await _logInManager.LoginAsync(usernameOrEmailAddress, password, tenancyName);

            switch (loginResult.Result)
            {
                case AbpLoginResultType.Success:
                    return loginResult;
                default:
                    CreateExceptionForFailedLoginAttempt(context, loginResult.Result, usernameOrEmailAddress, tenancyName);
                    //throw CreateExceptionForFailedLoginAttempt(context,loginResult.Result, usernameOrEmailAddress, tenancyName);
                    return loginResult;
            }
        }

    private void CreateExceptionForFailedLoginAttempt(OAuthGrantResourceOwnerCredentialsContext context, 
        AbpLoginResultType result, string usernameOrEmailAddress, string tenancyName)
        {
            switch (result)
            {
                case AbpLoginResultType.Success:
                    throw new ApplicationException("Don't call this method with a success result!");
                case AbpLoginResultType.InvalidUserNameOrEmailAddress:
                case AbpLoginResultType.InvalidPassword:
                    context.SetError(L("LoginFailed"), L("InvalidUserNameOrPassword"));
                    break;
                //    return new UserFriendlyException(("LoginFailed"), ("InvalidUserNameOrPassword"));
                case AbpLoginResultType.InvalidTenancyName:
                    context.SetError(L("LoginFailed"), L("ThereIsNoTenantDefinedWithName", tenancyName));
                    break;
                //    return new UserFriendlyException(("LoginFailed"), string.Format("ThereIsNoTenantDefinedWithName{0}", tenancyName));
                case AbpLoginResultType.TenantIsNotActive:
                    context.SetError(L("LoginFailed"), L("TenantIsNotActive", tenancyName));
                    break;
                //    return new UserFriendlyException(("LoginFailed"), string.Format("TenantIsNotActive {0}", tenancyName));
                case AbpLoginResultType.UserIsNotActive:
                    context.SetError(L("LoginFailed"), L("UserIsNotActiveAndCanNotLogin", usernameOrEmailAddress));
                    break;
                //    return new UserFriendlyException(("LoginFailed"), string.Format("UserIsNotActiveAndCanNotLogin {0}", usernameOrEmailAddress));
                case AbpLoginResultType.UserEmailIsNotConfirmed:
                    context.SetError(L("LoginFailed"), L("UserEmailIsNotConfirmedAndCanNotLogin"));
                    break;
                    //    return new UserFriendlyException(("LoginFailed"), ("UserEmailIsNotConfirmedAndCanNotLogin"));
                    //default: //Can not fall to default actually. But other result types can be added in the future and we may forget to handle it
                    //    //Logger.Warn("Unhandled login fail reason: " + result);
                    //    return new UserFriendlyException(("LoginFailed"));
            }
        }

    private static string L(string name, params object[] args)
        {
            //return new LocalizedString(name);
            return IocManager.Instance.Resolve<ILocalizationService>().L(name, args);
        }
}
public class SimpleRefreshTokenProvider : IAuthenticationTokenProvider, ITransientDependency
{
    private static ConcurrentDictionary<string, AuthenticationTicket> _refreshTokens = new ConcurrentDictionary<string, AuthenticationTicket>();

    public Task CreateAsync(AuthenticationTokenCreateContext context)
        {
            var guid = Guid.NewGuid().ToString("N");

            // maybe only create a handle the first time, then re-use for same client
            // copy properties and set the desired lifetime of refresh token
            var refreshTokenProperties = new AuthenticationProperties(context.Ticket.Properties.Dictionary)
            {
                IssuedUtc = context.Ticket.Properties.IssuedUtc,
                ExpiresUtc = DateTime.UtcNow.AddYears(1)
            };
            var refreshTokenTicket = new AuthenticationTicket(context.Ticket.Identity, refreshTokenProperties);

            //_refreshTokens.TryAdd(guid, context.Ticket);
            _refreshTokens.TryAdd(guid, refreshTokenTicket);

            // consider storing only the hash of the handle
            context.SetToken(guid);

            return Task.FromResult<object>(null);
        }

    public Task ReceiveAsync(AuthenticationTokenReceiveContext context)
        {
            AuthenticationTicket ticket;
            if (_refreshTokens.TryRemove(context.Token, out ticket))
            {
                context.SetTicket(ticket);
            }

            return Task.FromResult<object>(null);
        }

    public void Create(AuthenticationTokenCreateContext context)
        {
            throw new NotImplementedException();
        }

    public void Receive(AuthenticationTokenReceiveContext context)
        {
            throw new NotImplementedException();
        }
}
```

以上两段代码我就不做过多解释，请自行走读。

紧接着我们在Api目录下创建`OAuthOptions`类用来配置OAuth认证。

```
public class OAuthOptions
{
    /// <summary>
    /// Gets or sets the server options.
    /// </summary>
    /// <value>The server options.</value>
    private static OAuthAuthorizationServerOptions _serverOptions;

    /// <summary>
    /// Creates the server options.
    /// </summary>
    /// <returns>OAuthAuthorizationServerOptions.</returns>
    public static OAuthAuthorizationServerOptions CreateServerOptions()
    {
        if (_serverOptions == null)
        {
            var provider = IocManager.Instance.Resolve<SimpleAuthorizationServerProvider>();
            var refreshTokenProvider = IocManager.Instance.Resolve<SimpleRefreshTokenProvider>();
            _serverOptions = new OAuthAuthorizationServerOptions
            {
                TokenEndpointPath = new PathString("/oauth/token"),
                Provider = provider,
                RefreshTokenProvider = refreshTokenProvider,
                AccessTokenExpireTimeSpan = TimeSpan.FromSeconds(30),
                AllowInsecureHttp = true
            };
        }
        return _serverOptions;
    }
}
```

从中我们可以看出，主要配置了以下几个属性：

- TokenEndpointPath ：用来指定请求token的路由；
- Provider：用来指定创建token的Provider；
- RefreshTokenProvider：用来指定刷新token的Provider；
- AccessTokenExpireTimeSpan ：用来指定token过期时间，这里我们指定了30s，是为了demo 如何刷新token。
- AllowInsecureHttp：用来指定是否允许http连接。

创建上面三个类之后，我们需要回到Web项目的`Startup`类中，配置使用集成的OAuth2.0，代码如下：

```csharp
public void Configuration(IAppBuilder app)
{
    //第一步：配置跨域访问
    app.UseCors(CorsOptions.AllowAll);

    app.UseOAuthBearerAuthentication(AccountController.OAuthBearerOptions);

    //第二步：使用OAuth密码认证模式
    app.UseOAuthAuthorizationServer(OAuthOptions.CreateServerOptions());

    //第三步：使用Abp
    app.UseAbp();
    
    //省略其他代码
}
```

其中配置跨越访问时，我们需要安装`Microsoft.Owin.Cors`Nuget包。

至此，Abp集成OAuth的工作完成了。

## 4.2. 申请OAuth token

我们在Abp集成OAuth配置的申请token的路由是`/oauth/token`，所以我们将用户凭证post到这个路由即可申请token：

```csharp
public async Task<string> GetOAuth2Token()
{
    Uri uri = new Uri(baseUrl + oAuthTokenUrl);
    var handler = new HttpClientHandler() { AutomaticDecompression = DecompressionMethods.None };

    using (var client = new HttpClient(handler))
    {
        client.BaseAddress = uri;
        client.DefaultRequestHeaders.Accept.Add(new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("application/json"));

        var content = new FormUrlEncodedContent(new Dictionary<string, string>()
        {
            {"grant_type", "password"},
            {"username", user },
            {"password", pwd },
            {"client_id", "app" },
            {"client_secret", "app"},
        });

        //获取token保存到cookie，并设置token的过期日期                    
        var result = await client.PostAsync(uri, content);
        string tokenResult = await result.Content.ReadAsStringAsync();

        var tokenObj = (JObject)JsonConvert.DeserializeObject(tokenResult);
        string token = tokenObj["access_token"].ToString();
        string refreshToken = tokenObj["refresh_token"].ToString();
        long expires = Convert.ToInt64(tokenObj["expires_in"]);

        this.Response.SetCookie(new HttpCookie("access_token", token));
        this.Response.SetCookie(new HttpCookie("refresh_token", refreshToken));
        this.Response.Cookies["access_token"].Expires = Clock.Now.AddSeconds(expires);

        return tokenResult;
    }
}
```

在这段代码中我们指定的`grant_type = password`，这说明我们使用的是OAuth提供的**密码认证模式**。其中`{"client_id", "app" }, {"client_secret", "app"}`（搞过微信公众号开发的应该对这个很熟悉）用来指定客户端的身份和密钥，这边我们直接写死。
 通过OAuth的请求的token主要包含四部分：

- token：令牌
- refreshtoken：刷新令牌
- expires_in：token有效期
- token_type：令牌类型，我们这里是Bearer

为了演示方便，我们直接把token信息直接写入到cookie中，实际项目中建议写入数据库。

## 4.3. 刷新token

如果我们的token过期了怎么办，咱们可以用`refresh_token`来重新获取token。

```
public async Task<string> GetOAuth2TokenByRefreshToken(string refreshToken)
{
    Uri uri = new Uri(baseUrl + oAuthTokenUrl);
    var handler = new HttpClientHandler() { AutomaticDecompression = DecompressionMethods.None, UseCookies = true };

    using (var client = new HttpClient(handler))
    {
        client.BaseAddress = uri;
        client.DefaultRequestHeaders.Accept.Add(new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("application/json"));

        var content = new FormUrlEncodedContent(new Dictionary<string, string>()
        {
            {"grant_type", "refresh_token"},
            {"refresh_token", refreshToken},
            {"client_id", "app" },
            {"client_secret", "app"},
        });

        //获取token保存到cookie，并设置token的过期日期                    
        var result = await client.PostAsync(uri, content);

        string tokenResult = await result.Content.ReadAsStringAsync();

        var tokenObj = (JObject)JsonConvert.DeserializeObject(tokenResult);
        string token = tokenObj["access_token"].ToString();
        string newRefreshToken = tokenObj["refresh_token"].ToString();
        long expires = Convert.ToInt64(tokenObj["expires_in"]);

        this.Response.SetCookie(new HttpCookie("access_token", token));
        this.Response.SetCookie(new HttpCookie("refresh_token", newRefreshToken));
        this.Response.Cookies["access_token"].Expires = Clock.Now.AddSeconds(expires);

        return tokenResult;
    }
}
```

这段代码较直接使用用户名密码申请token的差别主要在参数上，`{"grant_type", "refresh_token"},{"refresh_token", refreshToken}`。

## 4.4. 使用token访问webapi

有了token，访问webapi就很简单了。

```
public async Task<ActionResult> SendRequestWithOAuth2Token()
{
    var token = Request.Cookies["access_token"]?.Value;
    if (token == null)
    {
        //throw new Exception("token已过期");
        string refreshToken = Request.Cookies["refresh_token"].Value;
        var tokenResult = await GetOAuth2TokenByRefreshToken(refreshToken);
        var tokenObj = (JObject)JsonConvert.DeserializeObject(tokenResult);
        token = tokenObj["access_token"].ToString();
    }

    _abpWebApiClient.RequestHeaders.Add(new NameValue("Authorization", "Bearer " + token));

    return await GetUserList(baseUrl + webapiUrl);
}
```

这段代码中，我们首先从cookie中取回`access_token`，若`access_token`为空说明token过期，我们就从cookie中取回`refresh_token`重新申请token。然后构造一个`Authorization`将token信息添加到请求头即可访问目标webapi。

# 5. 总结

本文介绍了三种不同的认证方式进行访问webapi，并举例说明。文章不可能面面俱到，省略了部分代码，请直接参考源码。若有纰漏之处也欢迎大家留言指正。

> 本文主要参考自以下文章：
>  *使用OAuth打造webapi认证服务供自己的客户端使用 ABP中使用OAuth2(Resource Owner Password Credentials Grant模式) Token Based Authentication using ASP.NET Web API 2, Owin, and Identity*