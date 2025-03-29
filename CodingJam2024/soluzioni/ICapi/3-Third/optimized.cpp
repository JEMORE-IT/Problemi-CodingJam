#include <iostream>
#include <vector>
#include <ctime>
using namespace std;
int index_of_split(std::vector<int>& P, int k) {
    int s = 0;
    for (int i = 0; i < P.size(); i++) {
        s += P[i];
        if (s > k) {
            return i - 1;
        }
    }
    return 0;
}

int main() {
    int r = 1000000000; // Numero di giri
    int k = 100;        // Quanti ne stanno
    // r = 4;
    // k = 6;
    // std::vector<int> P = {1, 4, 2, 1};
    std::vector<int> P = {2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 2, 2, 7, 4, 2, 3, 2, 8, 12, 2, 2, 2, 7, 4, 2, 3, 2, 8, 12, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 2, 4, 2, 3, 4, 2, 1, 2, 1, 3, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2, 5, 17, 9, 7, 4, 2, 3, 8, 8, 2};
    // std::vector<int> P = P_test;
    clock_t t = 0;
    long long grams_of_pancetta = 0;

    for (int i = 0; i < r; i++) {
        int split_index = index_of_split(P, k);
        std::vector<int> can_fit(P.begin(), P.begin() + split_index + 1);
        std::vector<int> cannot_fit(P.begin() + split_index + 1, P.end());

        for (int j = 0; j < can_fit.size(); j++) {
            grams_of_pancetta += can_fit[j];
        }

        P = cannot_fit;
        P.insert(P.end(), can_fit.begin(), can_fit.end());

        if (i % 1000000 == 0) {
            std::cout << "ciclo" << std::endl;
            std::cout << "Delta " << (double)(clock() - t) / CLOCKS_PER_SEC << std::endl;
            t = clock();
        }
    }
    std::cout << grams_of_pancetta << std::endl;
    return 0;
}
