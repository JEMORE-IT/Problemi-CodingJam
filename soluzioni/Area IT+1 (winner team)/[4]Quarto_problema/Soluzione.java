import java.math.BigInteger;
import java.nio.charset.StandardCharsets;

public class Soluzione {

    static void toString_(byte[] bytes) {

        String utf8String = new String(bytes, StandardCharsets.UTF_8);

        System.out.print(utf8String);

    }


    public static void main(String[] args) {

        BigInteger test = new BigInteger("280997636129");

        //   toString_(test.toByteArray());  //questo printa "Alè!"


        String[] input = "35784176028369 63561241316534 40946911928892 56405696498538 38978109180990 16444276162313 38053979586003 57562671757853".split(" ");

        BigInteger e = new BigInteger("17459243613");
        BigInteger n = new BigInteger("66624478857659");

        BigInteger d = e.modInverse(n);

        for (String i : input) {

            BigInteger c = new BigInteger(i);
            BigInteger r = c.multiply(d).mod(n);

            toString_(r.toByteArray());
        }


    }

}
