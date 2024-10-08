# Define the two dictionaries
Values_API = {
    "101234": {"FINE": "mudit", "LATE": "choudhary", "ADS": "BEN", "INT": "ADR"},
    "14322": {"FINE": "kajak", "LATE": "NEON", "ADS": "LCZ", "INT": "ADR"},
    "101234owner": {
        "FINE_OWNER": "TRIPLE",
        "LATE_OWNER": "VINCE",
        "INT": "ADR",
        "GEND": "MALE",
    },
    "14322owner": {"FINE_OWNER": "TRIPLE2", "LATE_OWNER": "VINCE2", "INT": "ADR"},
}

Values_VS = {
    "101234": {
        "FINE": "mudit",
        "LATE": "choudhary",
        "ADS": "BEN",
        "INT": "ADR",
        "FINE_OWNER": "TRIPLE",
        "LATE_OWNER": "VINCE",
        "VALID_DATE": True,
    },
    "14322": {
        "FINE": "kajak",
        "LATE": "NEON",
        "ADS": "LCZ",
        "INT": "ADR",
        "FINE_OWNER": "TRIPLE2",
        "LATE_OWNER": "VINCE2",
        "VALID_DATE": True,
    },
}


# Function to compare specific keys in both dictionaries
def compare_specific_keys(api_dict, vs_dict):
    results = {}

    # Step 1: Compare "FINE" and "LATE" for matching keys
    for key in api_dict:
        if key in vs_dict and not key.endswith("owner"):  # Skip owner keys
            common_comparison = {}
            # Compare only "FINE" and "LATE"
            for sub_key in ["FINE", "LATE"]:
                if sub_key in api_dict[key] and sub_key in vs_dict[key]:
                    common_comparison[sub_key] = (
                        api_dict[key][sub_key] == vs_dict[key][sub_key]
                    )
            results[key] = common_comparison

    # Step 2: Compare "FINE_OWNER" and "LATE_OWNER" for "owner" keys
    for key in api_dict:
        if key.endswith("owner"):  # Only consider owner keys
            base_key = key.replace("owner", "")  # Get the base key like "101234"
            if base_key in vs_dict:  # Ensure the base key exists in Values_VS
                owner_comparison = {}
                # Compare only "FINE_OWNER" and "LATE_OWNER"
                for sub_key in ["FINE_OWNER", "LATE_OWNER"]:
                    if sub_key in api_dict[key] and sub_key in vs_dict[base_key]:
                        owner_comparison[sub_key] = (
                            api_dict[key][sub_key] == vs_dict[base_key][sub_key]
                        )
                results[key] = owner_comparison

    return results


# Run the comparison
comparison_result = compare_specific_keys(Values_API, Values_VS)

# Display the comparison results
for key, value in comparison_result.items():
    print(f"Comparing {key}:")
    for sub_key, match in value.items():
        print(f"  {sub_key}: {'Match' if match else 'No match'}")
#####new


# Function to compare specific keys and append all values from Values_API when all match
def compare_and_append_all_with_strict_and(api_dict, vs_dict):
    matching_dict = {}  # New dictionary to store matches

    # Step 1: Compare "FINE" and "LATE" for matching keys (non-owner keys)
    for key in api_dict:
        if key in vs_dict and not key.endswith("owner"):  # Skip owner keys
            # Using AND logic: Both "FINE" and "LATE" must match
            fine_match = api_dict[key].get("FINE") == vs_dict[key].get("FINE")
            late_match = api_dict[key].get("LATE") == vs_dict[key].get("LATE")

            # Step 2: Compare "FINE_OWNER" and "LATE_OWNER" for "owner" keys
            owner_key = key + "owner"  # Create corresponding owner key
            fine_owner_match = api_dict.get(owner_key, {}).get("FINE_OWNER") == vs_dict[
                key
            ].get("FINE_OWNER")
            late_owner_match = api_dict.get(owner_key, {}).get("LATE_OWNER") == vs_dict[
                key
            ].get("LATE_OWNER")

            # Check if all four conditions are met
            if fine_match and late_match and fine_owner_match and late_owner_match:
                # Append all values from Values_API for this key
                matching_dict[key] = api_dict[key]  # Append only if all match

    return matching_dict


# Run the comparison and append matches to a new dict
matching_result = compare_and_append_all_with_strict_and(Values_API, Values_VS)

# Display the matching dictionary
print("Matching values from Values_API (with strict AND logic for all conditions):")
print(matching_result)

# Iterate over the "result" dictionary
for key, value in data["result"].items():
    print(f"Key: {key}")
    for sub_key, sub_value in value.items():
        if isinstance(sub_value, list):
            print(f"{sub_key}:")
            for item in sub_value:
                print(f"  - {item}")
        else:
            print(f"{sub_key}: {sub_value}")
merged_data = {}

for key, value in data.items():
    if "owner" in key:
        # Get the main key by removing "owner"
        main_key = key.replace("owner", "")
        if main_key in data:
            merged_dict = {}

            # Loop through all key-value pairs in both dictionaries (main and owner)
            for k in set(data[main_key].keys()).union(value.keys()):
                main_val = data[main_key].get(k)
                owner_val = value.get(k)

                if isinstance(main_val, list) and isinstance(owner_val, list):
                    # Merge lists and remove duplicates
                    merged_dict[k] = list(set(main_val + owner_val))
                elif main_val == owner_val:
                    # If values are the same, keep one
                    merged_dict[k] = main_val
                elif main_val is None:
                    # If the main dictionary doesn't have the key, use the owner dictionary's value
                    merged_dict[k] = owner_val
                elif owner_val is None:
                    # If the owner dictionary doesn't have the key, use the main dictionary's value
                    merged_dict[k] = main_val
                else:
                    # If values are different, keep both in a tuple
                    merged_dict[k] = (main_val, owner_val)

            merged_data[main_key] = merged_dict
