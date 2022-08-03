namespace Exceptions;

public class JWtInvalidPayload : Exception
{
    public override string Message => "O Payload Estava em formato incorreto ou vazio";
}