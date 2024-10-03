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
