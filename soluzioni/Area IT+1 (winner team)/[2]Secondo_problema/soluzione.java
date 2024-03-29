import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class Soluzione {

    public static void main(String[] args) throws Exception {
        int sum = 0;

        FileInputStream fs = new FileInputStream("test.txt");
        BufferedReader br = new BufferedReader(new InputStreamReader(fs));

        while (true) {
            final String s = br.readLine();
            if (s == null) break;
            final String[] ns = s.split(" ");
            final int n = Integer.valueOf(ns[0]);
            final int k = Integer.valueOf(ns[1]);
            final int ln = (int) Math.pow(2, n);

    
            if ((k - ln + 1) % ln == 0) {
                sum++;
            }
        }
        System.out.println(sum);
    }
}
