# Define the two dictionaries
Values_API = {
    "NAMECHG": {
        "1234owner": {"FOWN": "claire", "LOWN": "Freuen"},
        "1234": {
            "FINS": "claire",
            "LINS": "Freuen",
            "ADMIN": "CAPS",
            "AGENT_DETAILS": [["srm", "708"]],
        },
    },
    "ADRCHG": {
        "1234owner": {"FOWN": "claire", "LOWN": "Freuen"},
        "1234": {
            "FINS": "claire",
            "LINS": "Freuen",
            "ADMIN": "CAPS",
            "AGENT_DETAILS": [["srm", "708"]],
        },
    },
}

Values_VS = {
    "NAMECHG": {
        "1234": {
            "FOWN": "claire",
            "LOWN": "Freuen",
            "FINS": "claire",
            "LINS": "Freuen",
            "date": "09/30/2024",
            "VALID_DATE": True,
            "AGENT_CODE": "708",
        }
    },
    "ADRCHG": {
        "1234": {
            "FOWN": "claire",
            "LOWN": "Freuen",
            "FINS": "claire",
            "LINS": "Freuen",
            "date": "09/30/2024",
            "VALID_DATE": True,
            "AGENT_CODE": "708",
        }
    },
}
merged = {
    "1234": {
        "FOWN": "claire",
        "LOWN": "Freuen",
        "FINS": "claire",
        "LINS": "Freuen",
        "date": "09/30/2024",
        "VALID_DATE": True,
        "ADMIN": "CAPS",
        "AGENT_CODE": "708",
        "INTENT": ["NAMECHG", "ADRCHG"],
    }
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


# Create a new dictionary by merging Values_API and Values_VS
merged_dict = {}

# First, copy all key-value pairs from Values_API to merged_dict
for key, value in Values_API.items():
    merged_dict[key] = value

# Now, handle merging for the '1234' key specifically
for key, value in Values_VS.items():
    if key in merged_dict:
        # Initialize an empty list for INTENT
        intent_list = []
        for item in value:
            if "INTENT" in item:
                intent_list.append(item["INTENT"])

        # Update the existing dictionary in merged_dict
        merged_dict[key].update({"AGT": "", "INTENT": intent_list})
    else:
        merged_dict[key] = value
merged = {}

# Iterate over the intents in Values_VS
for intent, vs_data in Values_VS.items():
    for key, vs_values in vs_data.items():
        # Check if VALID_DATE is True
        if vs_values.get("VALID_DATE") and key in Values_API[intent]:
            api_values = Values_API[intent][key]

            # Check if the required fields match
            if (
                vs_values["FOWN"] == api_values.get("FOWN")
                and vs_values["LOWN"] == api_values.get("LOWN")
                and vs_values["FINS"] == api_values.get("FINS")
                and vs_values["LINS"] == api_values.get("LINS")
                and vs_values["AGENT_CODE"] == api_values["AGENT_DETAILS"][0][1]
            ):  # Match AGENT_CODE with AGENT_DETAILS

                # Merge the values into the final dictionary
                merged[key] = {
                    **vs_values,  # Start with the Values_VS values
                    **api_values,  # Add Values_API values
                    "INTENT": merged.get(key, {}).get("INTENT", [])
                    + [intent],  # Add intent to INTENT list
                }
