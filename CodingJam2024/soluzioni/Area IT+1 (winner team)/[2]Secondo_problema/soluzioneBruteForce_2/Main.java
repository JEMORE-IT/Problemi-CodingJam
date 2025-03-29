import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

public class Main {

    static void checkIter(List<Pulcino> fila) {

        for (Pulcino i : fila) {

            if (i.vede) {

                i.seduto = !i.seduto;

            }

        }

        for (Pulcino i : fila) {

            int index = fila.indexOf(i);
            if (index != 0) {
                boolean tuttiAbbassati = true;
                for (int x = 0; x < index; x++) {
                    if (!fila.get(x).seduto) {

                        tuttiAbbassati = false;

                        break;

                    }

                }
                if(!tuttiAbbassati)
                    break;
                i.vede = tuttiAbbassati;
            }

        }

        fila.get(0).vede = true;

    }


    static boolean vede(int n, int k) {

        List<Pulcino> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {

            list.add(new Pulcino());

        }

        list.get(0).vede = true;


        for (int i = 0; i < k; i++) {
            checkIter(list);
        }

        for (Pulcino c : list) {
            if (!c.seduto) {
                return false;

            }

        }

        return true;

    }


    public static AtomicInteger vedes = new AtomicInteger(0);


    public static void main(String[] args) throws IOException, ExecutionException, InterruptedException {
        //  System.out.println(vede(1, 0));
        // System.out.println(vede(1, 1));
        //System.out.println(vede(2, 1));
        //System.out.println(vede(2, 3));
        //System.out.println(vede(4, 47));
        System.out.println(vede(4, 7));

        int lines = 0;

        List<CompletableFuture<Void>> voids = new ArrayList<>();

        FileInputStream fs = new FileInputStream("test.txt");
        BufferedReader br = new BufferedReader(new InputStreamReader(fs));

        ExecutorService e = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());

        while (true) {

            final int l = ++lines;
            String s = br.readLine();
            if (s == null) break;
            String[] ns = s.split(" ");

            voids.add(CompletableFuture.runAsync(() -> {

                System.out.println(l);
                boolean v = vede(Integer.valueOf(ns[0]), Integer.valueOf(ns[1]));

                if (v) {

                    vedes.incrementAndGet();

                }

            }, e));

        }

        CompletableFuture.allOf(voids.toArray(new CompletableFuture[0])).get();

        System.out.println(vedes.get());

    }
}