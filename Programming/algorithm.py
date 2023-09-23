def update_file(import_file, remove_list):

    # Statement to read in the initial contents of the file
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # Convert `ip_addresses` from a string to a list
    ip_addresses = ip_addresses.split()

    # Iterative statement
    for element in ip_addresses:

        # Conditional statement
        if element in remove_list:

            # then current element should be removed from `ip_addresses`
            ip_addresses.remove(element)

    # Convert `ip_addresses` back to a string so that it can be written into the text file
    ip_addresses = "\n".join(ip_addresses)

    # Rewrite the original file
    with open(import_file, "w") as file:
        file.write(ip_addresses)


# A list of IP addresses to be removed from file
update_file("Programming/data/whitelist.txt",
            ["192.168.145.158", "192.168.3.252", "192.168.15.110"])

with open("Programming/data/whitelist.txt", "r") as file:
    text = file.read()

print(text)
