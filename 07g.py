galaxy_a56_network = ["GSM", "HSPA", "LTE", "5G"]

for band in galaxy_a56_network:
    if band == "LTE":
        continue
    print(band)