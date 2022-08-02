using static System.Convert;

public class CryptoService
{
    private string getRandomString(int seed, int size)
    {
        int base64BitCount = size * 6;
        int bytesCount = (int)Math.Ceiling(base64BitCount / 8.0);
        byte[] randData = new byte[bytesCount];

        Random rand = new Random(seed);
        rand.NextBytes(randData);

        var randString = ToBase64String(randData);

        return randString;
    }

    private int getSeedByTime(TimeSpan period)
    {
        var start =  new DateTime(1970,1,1);
        var now =  DateTime.Now;
        var timeElapsed = now - start;

        var currentEpoch =(int) (timeElapsed/period);
        var millis = (int)period.TotalMinutes;
        var magicNumberA = 1432;
        var magicNumberB = 9732;
        var seed =  unchecked(currentEpoch * millis * magicNumberA + magicNumberB);
        return seed;
    }

    public string GetInteralKey(TimeSpan period, int size){
        int seed =  getSeedByTime(period);
        string randomString = getRandomString(seed,size);
        return randomString;
    }
}