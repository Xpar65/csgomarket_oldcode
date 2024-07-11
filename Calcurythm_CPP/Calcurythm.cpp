#include "Calcurythm.h"
#include "Skin.h"
#include "SkinWear.h"
#include <iostream>
#include <sqlite3.h>
#define QUOTE(...) #__VA_ARGS__ //used for created multiline SQL statements easily. Preprocessor converts them into single line char*

Calcurythm::Calcurythm(Skin * skinsArr, int n){
    //should be recieving an array of 10 skins (n=10)
    if(n != 10){
        std::cout<<"n is not equal to 10"<<std::endl;
    }


}

sqlite3_stmt* Calcurythm::prepareSQLStatement(sqlite3* db, const char* sql) {
    sqlite3_stmt* stmt;
    int dataBaseFlag = sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);

    if (dataBaseFlag != SQLITE_OK) {
        std::cerr << "SQL prepare failed: " << sqlite3_errmsg(db) << std::endl;
        return nullptr;  // Return nullptr to indicate failure
    }

    return stmt;  // Return the prepared statement
}

int Calcurythm::RetrieveOutputSkinsFromDB(sqlite3 * db, sqlite3_stmt* stmt, SkinWear * OutputSkins){
    const char * sql = QUOTE(
        SELECT * FROM SkinWear
        
    );
}


SkinWear * Calcurythm::GetOutputSkins(){
    return this->OutputSkins;
}
double Calcurythm::GetProfitability(){
    return this->profitabilty;
}
double Calcurythm::GetisProfitable(){
    return this->isProfitable;
}