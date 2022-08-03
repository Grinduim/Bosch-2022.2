using System.Security.Cryptography;
using System.Text.Json;
using Exceptions;

using static System.Text.Encoding;
using static System.Convert;

public class CryptoService
{
    public int InternalKeySize { get; set; }
    public TimeSpan UpdatePeriod { get; set; }

    private string getRandomString(int seed, int size)
    {
        int base64BitCount = size * 6; // pqq isso ta acontecendo 
        int bytesCount = (int)Math.Ceiling(base64BitCount / 8.0); // sei q é relacioado ao bit bytes e algo mais
        byte[] randData = new byte[bytesCount]; ///arrudame trevi

        Random rand = new Random(seed);
        rand.NextBytes(randData);

        var randString = ToBase64String(randData);

        return randString;
    }

    private int getSeedByTime(TimeSpan period)
    {
        var start = new DateTime(1970, 1, 1);
        var now = DateTime.Now;
        var timeElapsed = now - start;

        var currentEpoch = (int)(timeElapsed / period);
        var millis = (int)period.TotalMilliseconds;
        var magicNumberA = 1432;
        var magicNumberB = 9732;

        var seed = unchecked(
            currentEpoch * magicNumberA + magicNumberB * millis);

        return seed;
    }

    private string getInternalKey()
    {
        int seed = getSeedByTime(this.UpdatePeriod);
        int size = this.InternalKeySize;
        string randomString = getRandomString(seed, size);
        return randomString;
    }

    public string GetToken<T>(T obj)
    {
        var json = JsonSerializer.Serialize<T>(obj);
        var tokenPayload = getTokenFromPayload(json);
        return tokenPayload;
    }

    private string getTokenFromPayload(string payload)
    {
        var header = "{\"alg\":\"hs256\"}";
        byte[] headerBytes = ASCII.GetBytes(header);
        var base64Header = ToBase64String(headerBytes);
        base64Header = base64Header.Replace("=", "");

        byte[] payloadBytes = ASCII.GetBytes(payload);
        var base64Payload = ToBase64String(payloadBytes);
        base64Payload.Replace("=", "");

        var secret = getInternalKey();
        var key = base64Payload + secret;
        var signature = generateSignature(key);
        base64Payload.Replace("=", "");

        var token = base64Header + "." + base64Payload + "." + signature;
        token.Replace("=", "");
        return token;
    }

    private string generateSignature(string data)
    {
        using (SHA256 sha = SHA256.Create())
        {
            byte[] dataByets = ASCII.GetBytes(data);
            var hash = sha.ComputeHash(dataByets);
            return ToBase64String(hash);
        }
    }

    public T Validate<T>(string token)
    {
        var parts = token.Split('.');

        if(token == null){
            throw new ArgumentNullException(nameof(token));
        }

        if (parts.Length != 3)
            throw new InvalidJWTException();

        string header = parts[0],
                payload = parts[1],
                signature = parts[2];

        var secret = getInternalKey();
        var key = header + payload + secret;
        var expetedSignature = generateSignature(key);

        if (expetedSignature != signature)
            throw new JWTInvalidSignatureException();

        try
        {
            var payloadBytes = FromBase64String(payload);
            var json = ASCII.GetString(payloadBytes);
            var obj = JsonSerializer.Deserialize<T>(json);
            return obj;


        }
        catch
        {
            throw new JWtInvalidPayload();
        }

    }
}