#ifndef SKIN_H  // If SKIN_H is not defined
#define SKIN_H  // Define SKIN_H

class Skin {
    public:
        Skin(double skinFloat, int skinWearID, double price, int wear, int collectionID, bool statTrak);
        void PrintSkinDetails();
    protected:
        double skinFloat;
        int skinWearID;
        double price;
        int wear; // 1 = FN, 2 = MW, etc.
        int collectionID;
        bool statTrak;
};

#endif
