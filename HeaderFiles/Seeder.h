#include <ctime>
#include <chrono>
#include <iostream>


int seed_portion(int OoM = 1) {

    auto timeX = std::chrono::system_clock::now();  // autotype because whatever the fuck this is, typeid().name() seems to hate it.
    auto timeY = std::chrono::system_clock::now();

    int deltaT = (timeY - timeX).count() * (int)OoM;

    return deltaT;


}


int gen_seed() {

    int seedy1 = seed_portion();
    int seedy2 = seed_portion(1000);
    int seedy3 = seed_portion(1000000);

    return -1*(seedy1 + seedy2 + seedy3);


}

