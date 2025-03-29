package org.es4;

import java.math.BigInteger;
import java.util.ArrayList;

public class Es4 {
    private final long E = 17459243613L;
    private final long N = 66624478857659L;
    private final long LONG_MAX_VALUE = 9223372036854775807L;

    private final ArrayList<Long>  listC;

    //BigInteger bigint = new BigInteger("19223372036854775807");

    public Es4()
    {
        listC = new ArrayList<Long>();
        Leggi_c();
    }

    /**
     * banale lettura dell'input
     */
    private void Leggi_c()
    {
        //listC.add(995272558L);
        listC.add(35784176028369L);
        listC.add(63561241316534L);
        listC.add(40946911928892L);
        listC.add(56405696498538L);
        listC.add(38978109180990L);
        listC.add(16444276162313L);
        listC.add(38053979586003L);
        listC.add(57562671757853L);
    }

    public void decodifica()
    {
        for(int i = 0; i < 8; i++) {
            BigInteger m = Calcola_m(listC.get(i), E, N);
            String riga = Converti_UTF8(m);
            System.out.print(riga);
        }

    }

    public String Converti_UTF8(BigInteger m)
    {
        byte[] num = m.toByteArray();
        return new String(num);
    }

    private static BigInteger Calcola_m(Long c, long e, long n) {
        // Converti n, c, e in oggetti BigInteger
        BigInteger bigN = BigInteger.valueOf(n);
        BigInteger bigC = BigInteger.valueOf(c);
        BigInteger bigE = BigInteger.valueOf(e);

        // Calcola l'inverso moltiplicativo di e modulo n
        BigInteger inverseE = bigE.modInverse(bigN);

        // Calcola m come c * (inverso di e modulo n) mod n
        BigInteger m = bigC.multiply(inverseE).mod(bigN);

        return m;
    }
}