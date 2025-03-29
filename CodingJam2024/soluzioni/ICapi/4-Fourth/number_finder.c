#include <stdint.h>   
#include <stdio.h>
#include <time.h>
void print(__int128 x) {
    if (x < 0) {
        putchar('-');
        x = -x;
    }
    if (x > 9) print(x / 10);
    putchar(x % 10 + '0');
}

int main() {
    clock_t start_time, end_time;
    double execution_time;
    start_time = clock();
    __int128 e_f = 17459243613;
    __int128 n_f = 66624478857659;
    __int128 x, y, z;
    __int128 x_f, y_f, w_f, z_f, M_f, d_f;
    for (x = 1024; x < 4096; x++) {
        for (y = 1024; y < 4096; y++) {
            for (z = 1024; z < 4096; z++) {
                if( ((x*y-1)*n_f) == (e_f *( x*y*z -z+y) - 1)){
                    x_f = x;
                    y_f = y;
                    z_f = z;
                    M_f = x_f * y_f - 1;
                    w_f = (e_f - x_f) / (M_f);
                    d_f = z*(x*y-1)+y;
                }
            }
        }
    }
    end_time = clock();
    printf("x : ");
    print(x_f);
    printf("\n");
    printf("y : ");
    print(y_f);
    printf("\n");
    printf("w : ");
    print(w_f);
    printf("\n");
    printf("z : ");
    print(z_f);
    printf("\n");
    printf("M : ");
    print(M_f);
    printf("\n");
    printf("d : ");
    print(d_f);
    printf("\n");
    printf("e : ");
    print(e_f);
    printf("\n");
    printf("n : ");
    print(n_f);
    printf("\n");
    execution_time = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    printf("Execution time: %f seconds\n", execution_time);
    return 0;
}