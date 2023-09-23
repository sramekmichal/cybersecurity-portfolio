import_file = "allow_list.txt"

ip_addresses = "192.168.218.160 \n192.168.97.225 \n192.168.145.158 \n192.168.108.13 \n192.168.60.153 \n192.168.96.200 \n192.168.247.153 \n192.168.3.252 \n192.168.116.187 \n192.168.15.110 \n192.168.39.246"

# Create a `with` statement to write to the text file
with open(import_file, "w") as file:
    file.write(ip_addresses)

# Create a `with` statement to read in the text file
with open(import_file, "r") as file:
    text = file.read()

# Display the contents of `text`
print(text)
