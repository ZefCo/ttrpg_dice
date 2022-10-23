#include "HeaderFiles/Seeder.h"
#include <vector>
#include <iostream>
#include <map>
#include "NRHeaderFiles/ran3cpp.h"

int seed1;
int seed2;


int rand_int(double rval, int min = 0, int max = 2) {

    int rnt = min + ((max - min) * rval);

    return rnt;

}



int main() {

    seed1 = gen_seed();
    seed2 = gen_seed();

    std::map<int, double> rlist;

    for (int i = 0; i < 100; i++) {
        rlist[i] = NR::ran3(seed1);
    }

    int index = rand_int(NR::ran3(seed2), 0, 101);

    double rval = rlist[index];

    int dice_value = rand_int(rval, 0, 7);

    std::cout << "Dice Rolled = " << dice_value << std::endl;

}