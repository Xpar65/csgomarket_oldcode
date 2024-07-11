#include "Skin.h"
#include <iostream>

Skin::Skin(double skinFloat, int skinWearID, double price, int wear, int collectionID, bool statTrak)
: skinFloat(skinFloat), skinWearID(skinWearID), price(price), wear(wear), collectionID(collectionID) {}

void Skin::PrintSkinDetails(){
    std::cout<<"skinWearID: "<<skinWearID<<" Float: "<<skinFloat<<" Wear: "<<wear<<" Collection: ";
    std::cout<<collectionID<<" Price: "<<price<<" Stat_Trak: "<<statTrak;
}