
#include "Skin.h"
#include "SkinWear.h"
#include <sqlite3.h>

#ifndef CALCURYTHM_H  // If SKINWEAR_H is not defined
#define CALCURYTHM_H  // Define SKINWEAR_H

//calcurythm object should be created with an array of input skins.
//when creating it automatically calculates the trades profitabilty
//then a function call for get is profitable can be called
//if it it profitable then the main funciton can get a detailed list of the output skins
//profitabilty etc

class Calcurythm{
    public:
        Calcurythm(Skin * skinsArr, int n);
        sqlite3_stmt* prepareSQLStatement(sqlite3* db, const char* sql); //prepares SQL to be excecuted. Returns sql ouput as stmt* obj. Points to nullpointer if error occurs
        int RetrieveOutputSkinsFromDB(sqlite3 * db, sqlite3_stmt* stmt, SkinWear * OutputSkins);
        SkinWear * GetOutputSkins();
        double GetProfitability();
        double GetisProfitable();

    private:
        Skin * inputSkins;
        SkinWear * OutputSkins;
        double profitabilty;
        bool isProfitable;
};
#endif
