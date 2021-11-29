###########################
# ---- PRIME NUMBERS ---- #
#                         # 
# 2, 3, 5, 7, 11, 13, 17, #
# 19, 23, 29, 31, 37, 41, #
# 43, 47, 53, 59, 61, 67, #
# 71, 73, 79, 83, 89, 97  #
###########################

from HashTable import *

# -- SETUP -- #
def setup():
    tbl = DSAHashTable(20)

    sample = [[14541837,"Karina Rossin"], [14593654,"Mathew Milian"], [14492026,"Christian Mullarkey"], [14397374,"Esmeralda Radovich"], [14824429, "Nelson Tooker"], [14929292, "Neil Brabant"]]

    for i in sample:
        tbl.put(str(i[0]), i[1])
    return tbl

tbl = setup()
# -- TEST HARNESS -- #
print("Next prime after 20: " + str(tbl.findNextPrime(20)))
tbl.display()
print("\n--FINDING 14824429...")
print("Index at 14824429: " + str(tbl._find("14824429")))
print("\n--REMOVING 14824429...")
tbl.remove("14824429")
print("Removed!")
tbl.display()
print("\n--CHECKING IF 14561837 exists")
print(str(tbl.hasKey("14561837")))
print("\n--CHECKING IF 14824429 exists")
print(str(tbl.hasKey("14824429")))
print("\n--PRINTING LOAD FACTOR")
print("Load Factor = " + str(tbl._getLoadFactor()))


