
#ifndef SKINWEAR_H  // If SKINWEAR_H is not defined
#define SKINWEAR_H  // Define SKINWEAR_H
#include "Skin.h"
#include <string>

class SkinWear : public Skin {
    public:
    SkinWear(double skinFloat, int skinWearID, double price, int wear, int collectionID, bool statTrak, std::string hashName, int volume);
    void PrintSkinDetails();
    protected:
        std::string hashName;
        int volume;
};

#endif
