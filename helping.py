def compare_nested_dicts(first_list, second_list):
    comparison_result = {}
    
    # Helper function to flatten the list of dictionaries into a dictionary of lists
    def flatten_list(input_list):
        flat_dict = {}
        for item in input_list:
            for dictionary in item:
                for key, value in dictionary.items():
                    flat_dict[key] = value
        return flat_dict

    # Flatten both lists
    first_dict = flatten_list(first_list)
    second_dict = flatten_list(second_list)

    # Compare dictionaries where keys match
    for key in first_dict:
        if key in second_dict:
            comparison_result[key] = {}
            
            # Compare each sub-dictionary inside the matching key
            for idx, (first_sub_dict, second_sub_dict) in enumerate(zip(first_dict[key], second_dict[key])):
                sub_result = {}
                all_keys = set(first_sub_dict.keys()).union(second_sub_dict.keys())
                
                # Compare each unique sub-key
                for sub_key in all_keys:
                    first_value = first_sub_dict.get(sub_key, None)
                    second_value = second_sub_dict.get(sub_key, None)
                    sub_result[sub_key] = {
                        "first_list_value": first_value,
                        "second_list_value": second_value,
                        "match": first_value == second_value
                    }
                comparison_result[key][f"comparison_{idx+1}"] = sub_result

    return comparison_result

# Get comparison result
result = compare_nested_dicts(first_list, second_list)
