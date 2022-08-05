using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Authorization;

namespace tokenServer.Controllers;

[ApiController]
[Route("api")]
public class MainController : ControllerBase
{
    [HttpPost("connect")]
    public object Connect(
        [FromServices]CryptoService crypto,
        [FromBody]User user)
    {
        try
        {
            var token = crypto.GetToken(user);
            return new {
                Message = "Success",
                Token = token
            };
        }
        catch
        {
            return new {
                Message = "Fail"
            };
        }
    }

    [HttpPost("changename")]
    public object ChangeName(
        [FromServices]CryptoService crypto,
        [FromBody]ChangeNameParameters parameters
    )
    {
        User user = null;
        try
        {
            var token = parameters.Token;
            user = crypto.Validate<User>(token);
        }
        catch (Exception ex)
        {
            return new {
                Message = ex.Message,
            };
        }

        if (!user.IsAdm)
        {
            return new {
                Message = "Invalid Access Level"  
            };
        }

        user.Name = parameters.NewName;
        var newToken = crypto.GetToken(user);
        return new {
            Message = "Success",
            Token = newToken
        };
    }
}