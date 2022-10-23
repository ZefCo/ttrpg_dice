#include <vector>
#include <iostream>
#include <map>
#include "HeaderFiles/Seeder.h"
#include "NRHeaderFiles/ran3cpp.h"

int seed1;
int seed2;


// generates a random number between [min, max). Default is [0, 1]
int rand_int(double rval, int min = 0, int max = 2) {

    int rnt = min + ((max - min) * rval);

    return rnt;

}



double rvalue(int min, int max) {

    seed1 = gen_seed();
    seed2 = gen_seed();

    std::map<int, double> rlist;

    for (int i = 0; i < 100; i++) {
        rlist[i] = NR::ran3(seed1);
    }

    int index = rand_int(NR::ran3(seed2), 0, 101);

    double rval = rlist[index];

    return rval;

}