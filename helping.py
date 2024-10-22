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
        "0999owner": {"FOWN": "claire", "LOWN": "Freuen"},
        "0999": {
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
        "0999owner": {"FOWN": "claire", "LOWN": "Freuen"},
        "0999": {
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
        },
        "0999": {
            "FOWN": "claire",
            "LOWN": "Freuen",
            "FINS": "claire",
            "LINS": "Freuen",
            "date": "09/30/2024",
            "VALID_DATE": True,
            "AGENT_CODE": "708",
        },
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
        },
        "0999": {
            "FOWN": "claire",
            "LOWN": "Freuen",
            "FINS": "claire",
            "LINS": "Freuen",
            "date": "09/30/2024",
            "VALID_DATE": True,
            "AGENT_CODE": "708",
        },
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
    },
    "0999": {
        "FOWN": "claire",
        "LOWN": "Freuen",
        "FINS": "claire",
        "LINS": "Freuen",
        "date": "09/30/2024",
        "VALID_DATE": True,
        "ADMIN": "CAPS",
        "AGENT_CODE": "708",
        "INTENT": ["NAMECHG", "ADRCHG"],
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

merged_dict = {}

# Iterate through the input dictionary
for intent, entries in input_dict.items():
    # Initialize a dictionary to hold merged data for each intent
    merged_data = {}

    # Iterate through each key-value pair in the intent's entries
    for value in entries.values():
        for k, v in value.items():
            # Only add the key-value pair if the key is not already present
            if k not in merged_data:
                merged_data[k] = v

    # Assign the merged data to the respective intent in merged_dict
    # Using the first key as a reference for the new structure
    first_key = list(entries.keys())[0]
    merged_dict[intent] = {first_key: merged_data}
