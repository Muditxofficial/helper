merged = {"BENE": {}, "NAME": {}, "ADR": {}}


# Generalized merge function to check FOWN, LOWn, and Valid_date for any section (BENE, NAME, ADR)
def merge_section(section_key, dict1, dict2):
    for key, data1 in dict1.items():
        if key in dict2:
            data2 = dict2[key]

            # Check if FOWN and LOWn match and Valid_date is True
            if (
                data1["FOWN"] == data2["FOWN"]
                and data1["LOWn"] == data2["LOWn"]
                and data2.get("Valid_date", False)
            ):

                # Merge the dictionaries for this key
                merged[section_key][key] = {
                    "FOWN": data1["FOWN"],
                    "LOWn": data1["LOWn"],
                    "ADMIN": data1["ADMIN"],
                    "LOC": data1.get("LOC", ""),
                    "SEC": data2.get("SEC", ""),
                    "Valid_date": data2.get("Valid_date", False),
                }


# Apply the merge function for each section: NAME, ADR, BENE
merge_section("NAME", Values_API_RES["NAME"], Values2_HS_RES["NAME"])
merge_section("ADR", Values_API_RES["ADR"], Values2_HS_RES["ADR"])
merge_section("BENE", Values_API_RES["BENE"], Values2_HS_RES["BENE"])

# Print the merged result
print(merged)
