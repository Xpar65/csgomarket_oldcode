import random

class casetype:
    def __init__(self, casename: str, skintypes: list) -> None:
        self.casename = casename
        self.skintypes = skintypes
        skintree = [[]]*6
        for i in self.skintypes :
            skintree[i.rval - 1].append(i)
        self.skintree = skintree

    def __str__(self) -> str:
        return self.casename

"""
class caselisting(casetype):
    def __init__(self, casename, skintree, price, buy) -> None:
        super().__init__(casename, skintree)
        self.price = float(price)

        if buy == "buy" :
            self.buy = True
        elif buy == "sell" :
            self.buy == False

    def __str__(self) -> str:
        if self.buy == True :
            return "Buy " + self.casename + " price = $" + str(self.price)
        else :
            return "Sell " + self.casename + " price = $" + str(self.price)
"""

class skintype:
    def __init__(self, name: str, rval: int, minflt: float, maxflt: float) -> None:
        self.name = name
        if 0 <= minflt <= 1 and 0 <= maxflt <= 1 :
            if minflt <= maxflt :
                self.minflt = minflt
                self.maxflt = maxflt
            else :
                raise Exception(("Max Float must be greater than Min Float for " + self.name))
        else :
            raise Exception(("Min Float and Max Float must be between 0 and 1 for " + self.name))
        self.rval = rval
        if self.rval  in range(1,7) :
            self.rarity = ["Other", "Covert", "Classified", "Restricted", "Mil-spec", "Industrial", "Consumer"][self.rval]
        else :
            self.rarity = "Other"

    def __str__(self) -> str:
        return self.name
    
    def find_case(self) -> casetype :
        for case in [Revolution_Case] :
            if self in case.skintypes :
                return case
        return None
    def tradeouts(self) -> list :
        if self.find_case() == None :
            return []
        else :
            return [skin for skin in self.find_case().skintypes if skin.rval == self.rval - 1]
    def neighbours(self) -> list :
        if self.find_case() == None :
            return []
        else :
            return [skin for skin in self.find_case().skintypes if skin.rval == self.rval and skin != self]     
    def tradeins(self) -> list :
        if self.find_case() == None :
            return []
        else :
            return [skin for skin in self.find_case().skintypes if skin.rval == self.rval + 1]
            
class skin:
    def __init__(self, skintype: skintype, flt: float, StatTrak: bool = False, Souvenir: bool = False) -> None:
        self.skintype = skintype

        if self.skintype.minflt <= flt <= self.skintype.maxflt :
            self.flt = flt
            if 0 <= self.flt < 0.07 :
                self.wear = "Factory New"
            elif 0.07 <= self.flt < 0.15 :
                self.wear = "Minimal Wear"
            elif 0.15 <= self.flt < 0.38 :
                self.wear = "Field-Tested"
            elif 0.38 <= self.flt < 0.45 :
                self.wear = "Well-Worn"
            elif 0.45 <= self.flt <= 1 :
                self.wear = "Battle-Scarred"
            else :
                raise Exception("Float value for " + self.skintype.name() + " must be between 0 and 1")
        else :
            raise Exception("Float not in Float Range")    
        self.StatTrak = StatTrak
        self.Souvenir = Souvenir
        
    def __str__(self) -> str:
        return self.skintype.name() + " float = " + str(self.flt) + " StatTrak = " + str(self.StatTrak)

class skinlisting:
    def __init__(self, skin: skin, price: float, buy: bool) -> None:
        self.skin = skin
        self.price = price
        self.buy = buy
    def __str__(self) -> str:
        if self.buy :
            return "Buy " + skin().__str__ + " price = $" + str(self.price)
        else :
            return "Sell " + skin().__str__ + " price = $" + str(self.price)

SCAR_20_Fragments = skintype("SCAR-20|Fragments", 4, 0.00, 0.78)
P250_Re_built = skintype("P250|Re.built", 4, 0.00, 0.90)
Tec_9_Rebel = skintype("Tec-9|Rebel", 4, 0.00, 1.00)
MAG_7_Insomnia = skintype("MAG-7|Insomnia", 4, 0.00, 1.00)
MP9_Featherweight = skintype("MP9|Featherweight", 4, 0.00, 1.00)
SG_553_Cyberforce = skintype("SG 553|Cyberforce", 4, 0.00, 0.90)
MP5_SD_Liquidation = skintype("MP5-SD|Liquidation", 4, 0.00, 1.00)
MAC_10_Sakkaku = skintype("MAC-10|Sakkaku", 3, 0.21, 0.79)
R8_Revolver_Banana_Cannon = skintype("R8 Revolver|Banana Cannon", 3, 0.00, 1.00)
Glock_18_Umbral_Rabbit = skintype("Glock-18|Umbral Rabbit", 3, 0.00, 0.75)
P90_Neoqueen = skintype("P90|Neoqueen", 3, 0.00, 0.60)
M4A1_S_Emphorosaur_S = skintype("M4A1-S|Emphorosaur-S", 3, 0.00, 0.80)
P2000_Wicked_Sick = skintype("P2000|Wicked Sick", 2, 0.00, 1.00)
UMP_45_Wild_Child = skintype("UMP-45|Wild Child", 2, 0.00, 1.00)
AWP_Duality = skintype("AWP|Duality", 2, 0.00, 0.70)
AK_47_Head_Shot = skintype("AK-47|Head Shot", 1, 0.00, 1.00)
M4A4_Temukau = skintype("M4A4|Temukau", 1, 0.00, 0.80)

Revolution_Case = casetype("Revolution Case", [SCAR_20_Fragments, P250_Re_built, Tec_9_Rebel, MAG_7_Insomnia, MP9_Featherweight, SG_553_Cyberforce, MP5_SD_Liquidation, MAC_10_Sakkaku, R8_Revolver_Banana_Cannon, Glock_18_Umbral_Rabbit, P90_Neoqueen, M4A1_S_Emphorosaur_S, P2000_Wicked_Sick, UMP_45_Wild_Child, UMP_45_Wild_Child, AWP_Duality, AK_47_Head_Shot, M4A4_Temukau])

my_skintype = skintype("SCAR-20|Fragments", 4, 0.00, 0.78)
my_skin = skin(my_skintype, 0.06)
my_skin_listing = skinlisting(my_skin, 50.7, True)

print(my_skin_listing)
print(my_skin)
print(my_skin_listing)

def check_tradeup_inputs(inputs: list) -> None :
    if len(inputs) != 10 :
        raise Exception("Exactly 10 skins must be entered")
    StatTrak = inputs[0].StatTrak
    rval = inputs[0].rval
    if rval not in range(1,7) :
        raise Exception("Rarity must be valid")
    for input in inputs :
        if StatTrak != input.StatTrak :
            raise Exception("You cannot mix StatTrak and non-StatTrak skins")
        if rval != input.rval :
            raise Exception("All skins must have the same rarity")

def tradeupsim(skins: list) -> skin :
    check_tradeup_inputs(skins)
    outlist = []
    avgflt = 0.00
    for input in skins :
        outlist += input.skintype.tradeouts()
        avgflt += input.flt / 10
    outskintype = random.choice(outlist)
    outflt = (outskintype.maxflt - outskintype.minflt)*avgflt + outskintype.minflt
    return skin(outskintype, outflt, skins[0].StatTrak)

def tradeup_outcomes(skins: list) -> list :
    check_tradeup_inputs(skins)
    outlist = []
    avgflt = 0.00
    for input in skins :
        outlist += input.skintype.tradeouts()
        avgflt += input.flt / 10
    reslist = []
    for outskintype in outlist :
        outflt = (outskintype.maxflt - outskintype.minflt)*avgflt + outskintype.minflt
        count = outlist.count(outskintype)
        reslist.append((skin(outskintype, outflt, skins[0].StatTrak), str(100*count/len(outlist))+"%"))
    return list(set(reslist))

    
