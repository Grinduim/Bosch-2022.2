public class JwtInvalidFormatException : Exception
{
    public override string Message 
        => "O token não está no format x.y.z requerido";
}