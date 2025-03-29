package org.es2;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class App {
    final static String path = "/Users/barack/IdeaProjects/CodingJam_UNIMORE/src/main/java/org/es2/input.txt";
    public static void main(String[] args) throws IOException {
        Es2 esercizio2 = new Es2(path);

        esercizio2.leggiFile();

        System.out.println(esercizio2.getRis());
    }
}
