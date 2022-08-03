namespace Exceptions;
public class JWTInvalidSignatureException : Exception 
{
    public override string Message => "O token é invalido ou já expirou";
}