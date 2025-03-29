package org.es2;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Es2 {
    BufferedReader reader;
    String line;
    long ris;

    public Es2(String path) throws FileNotFoundException {
        reader = new BufferedReader(new FileReader(path));
        ris = 0;
        line = "";
    }

    public void leggiFile() throws IOException {
        line = reader.readLine();

        while(line != null){
            String[] numeriArray = line.split("\\s+");
            double n = Integer.parseInt(numeriArray[0]);
            double k = Integer.parseInt(numeriArray[1]);

            if((k + 1) % Math.pow(2, n) == 0){
                ris += 1;
            }
            line = reader.readLine();
        }
    }

    public long getRis()
    {
        return ris;
    }
}
