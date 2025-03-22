set1 = {"GSM", "CDMA", "HSPA", "EVDO", "LTE"}
set2 = {"GSM", "HSPA", "LTE"}

set1.symmetric_difference_update(set2)

print(set1)