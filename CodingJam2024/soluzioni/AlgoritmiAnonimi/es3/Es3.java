package org.es3;

import java.util.Arrays;
import java.util.List;

public class Es3 {
    List<Integer> pulcini;
    int R;
    int K;
    int numGruppi;
    long numPancetta;


    public Es3(Integer[] P, int R, int K)
    {
         pulcini = Arrays.asList(P);
         this.R = R;
         this.K = K;
         this.numGruppi = pulcini.size();
         this.numPancetta = 0;
    }

    private int il_prossimo(int pos){
        if(pos + 1 < numGruppi){
            pos++;
        }else{
            pos = 0;
        }
        return pos;
    }

    public void Pancetta()
    {
        int posGruppo = 0;

        for(int viaggio = 0; viaggio < R; viaggio++){
            int pulciniDentro = 0;
            while(pulciniDentro + pulcini.get(posGruppo) <= K){
                pulciniDentro += pulcini.get(posGruppo);
                numPancetta += pulcini.get(posGruppo);
                posGruppo = il_prossimo(posGruppo);
            }
        }
    }

    public long getPancetta(){return numPancetta;}
}
