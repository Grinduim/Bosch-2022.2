using Microsoft.AspNetCore.Mvc;

namespace tokenServer.Controllers;

[ApiController]
[Route("main")]
public class MainController : ControllerBase
{

    [HttpPost("connect")]
    public object Connect(
        [FromServices] CryptoService crypto,
        [FromBody] User user
    )
    {
        var token = crypto.GetToken(user);
        return new
        {
            Message = "Sucess",
            token = token
        };
    }

    [HttpPost("changename")]
    public object ChangeName([FromServices] CryptoService crypto, [FromBody] ChangeNameParametres parametres)
    {
        User user = null;
        try{
            var token = parametres.Token;
            user = crypto.Validate<User>(token);
        }
        catch{
            return new {
                Message= "Invalid Token",

            };
        }

        if(!user.IsAdm){
            return new {
                Message = "Invalid Access Level"
            };
        }

        user.Name = parametres.NewName;
        var newToken = crypto.GetToken(user);
        
        return new {
            Message = "Sucess",
            Token = newToken
        };
    }
}
