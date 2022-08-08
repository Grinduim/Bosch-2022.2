public class JwtInvalidPayloadException : Exception
{
    public override string Message 
        => "O payload estava em formato incorreto ou foi corrompido.";
}