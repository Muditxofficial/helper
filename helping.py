root = ET.fromstring(xml_data)

# Namespace handling
ns = {"ns": "me"}  # Change this if your XML has a different namespace

# Check if TxResult is "Success"
tx_result = root.find(".//TxResult")
if tx_result is not None and tx_result.text.strip() == "Success":
    # Extract admin
    admin = root.find(".//ADMIN").text.strip()

    # Extract user details
    users = []
    for user in root.findall(".//TCRMCONPRBOBJ"):
        role = user.find("Role").text.strip()
        firstname = user.find(".//FirstName").text.strip()
        lastname = user.find(".//LastName").text.strip()
        identify = user.find(".//Identify").text.strip()
        
        users.append({
            "role": role,
            "firstname": firstname,
            "lastname": lastname,
            "identify": identify
        })

    # Final output dictionary
    result = {"admin": admin, "users": users}
    print(result)
else:
    print("Transaction was not successful.")
