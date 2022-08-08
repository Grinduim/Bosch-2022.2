namespace Exceptions;
public class InvalidJWTException: Exception
{
    public override string Message => "O token não está no Formato x.y.z requerido";
}