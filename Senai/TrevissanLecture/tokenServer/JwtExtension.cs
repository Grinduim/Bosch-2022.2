using Microsoft.AspNetCore.Authorization;

public static class JwtExtension
{
    public static void AddJwt(
        this WebApplicationBuilder builder, 
        int internalKeySize, TimeSpan updatePeriod)
    {
        builder.Services.AddSingleton<CryptoService>(p =>
        {
            var service = new CryptoService();
            service.InternalKeySize = internalKeySize;
            service.UpdatePeriod = updatePeriod;
            return service;
        });

        // builder.Services.AddSingleton<IAuthorizationHandler, JwtHandler>();

        // builder.Services.AddAuthorization(options =>
        // {
        //     options.AddPolicy("JwtToken", policy =>
        //     {
        //         policy.AddRequirements(new JwtRequirement());
        //     });
        // });
    }
}