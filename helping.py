# Parse XML
root = ET.fromstring(xml_data)

# Namespace handling (if needed)
ns = {'soap': 'xy', 'me': 'me'}  # Adjust namespaces as required

# Check if TxResult is "Success"
tx_result = root.find('.//{me}Response/{me}TxResult', ns)
if tx_result is not None and tx_result.text.strip().lower() == "success":
    admin = root.find('.//{me}ADMIN', ns).text if root.find('.//{me}ADMIN', ns) is not None else None
    data_list = []
    
    for person in root.findall('.//{me}TCRMCONPRBOBJ', ns):
        role = person.find('./{me}Role', ns).text if person.find('./{me}Role', ns) is not None else None
        first_name = person.find('.//{me}FirstName', ns).text if person.find('.//{me}FirstName', ns) is not None else None
        last_name = person.find('.//{me}LastName', ns).text if person.find('.//{me}LastName', ns) is not None else None
        identify = person.find('.//{me}Identify', ns).text if person.find('.//{me}Identify', ns) is not None else None
        
        data_list.append({
            "Admin": admin,
            "Role": role,
            "FirstName": first_name,
            "LastName": last_name,
            "Identify": identify
        })

    print(data_list)  # Output the extracted data
else:
    print("Transaction result is not Success.")
