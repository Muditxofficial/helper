def compare_first_third_and_sign(first_list, second_list):
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

    # Compare "first", "third", and "sign" values for matching keys
    for key in first_dict:
        if key in second_dict:
            match = True
            for idx, (first_sub_dict, second_sub_dict) in enumerate(
                zip(first_dict[key], second_dict[key])
            ):
                # Check "first", "third", and "sign" values only
                if (
                    first_sub_dict.get("first") != second_sub_dict.get("first")
                    or first_sub_dict.get("third") != second_sub_dict.get("third")
                    or second_sub_dict.get("sign") != True
                ):  # Check if sign is True
                    match = False
                    break
            comparison_result[key] = match

    return comparison_result


# Get comparison result
result = compare_first_third_and_sign(first_list, second_list)
