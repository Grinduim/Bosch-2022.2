using Microsoft.AspNetCore.Mvc;

namespace API.Controllers;

[ApiController]
[Route("[controller]")]
public class MainController : ControllerBase
{
    [HttpGet("key")]
    public string GetKey([FromServices]CryptoService crypto){
        return crypto.GetInteralKey(TimeSpan.FromSeconds(1),8*3);
    }
}
