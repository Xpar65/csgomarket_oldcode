#include "SkinWear.h"
#include <string>
#include <iostream>

SkinWear::SkinWear(double skinFloat, int skinWearID, double price, int wear, int collectionID, bool statTrak, std::string hashName, int volume)
: Skin(skinFloat, skinWearID, price, wear, collectionID, statTrak), hashName(hashName), volume(volume) {
}

void SkinWear::PrintSkinDetails(){
    Skin::PrintSkinDetails();
    std::cout<<" HashName: "<<hashName<<" Volume: "<<volume;
}


