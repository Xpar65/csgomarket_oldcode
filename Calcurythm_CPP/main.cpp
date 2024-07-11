#include "Skin.h"
#include "SkinWear.h"
#include "Calcurythm.h"

#include <sqlite3.h>
#include <iostream>



int main () {
    const int n = 10;
    Skin * skinsArr[n];
    std::cout<<"Sample input Skins: \n";
    skinsArr[0] = new Skin(0.1, 2, 79.98, 2, 27, true);
    skinsArr[1] = new Skin(0.1, 2, 79.98, 2, 27, true);
    skinsArr[2] = new Skin(0.1, 2, 79.98, 2, 27, true);
    skinsArr[3] = new Skin(0.1, 2, 79.98, 2, 27, true);
    skinsArr[4] = new Skin(0.1, 2, 79.98, 2, 27, true);
    skinsArr[5] = new Skin(0.1, 2, 79.98, 2, 27, true);
    skinsArr[6] = new Skin(0.1, 2, 79.98, 2, 27, true);
    skinsArr[7] = new Skin(0.1, 2, 79.98, 2, 27, true);
    skinsArr[8] = new Skin(0.1, 2, 79.98, 2, 27, true);
    skinsArr[9] = new Skin(0.1, 2, 79.98, 2, 27, true);
    // for (int i = 0; i < n; i++)
    // {
    //     skinsArr[i]->PrintSkinDetails();
    //     std::cout<<std::endl;
    // }
    // std::cout<<std::endl;

    


    SkinWear sw(0.5, 101, 300.0, 2, 50, true, "HashNameExample", 100);
    sw.PrintSkinDetails();
    std::cout<<std::endl;
    return 0;
}