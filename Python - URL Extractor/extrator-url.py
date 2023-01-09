# Basic URL info extractor
# Applying basic concepts for strings

# url = "somebank.com/exchage?destinationCurrency=USD&originCurrency=REAL&quantity=100"
url = "  "
print("Root URL = {}".format(url))

# URL Sanitizing
# Another way to take spaces out is by using .replace(" ", "") but strip does it better
url = url.strip()

# URL Validation
if url == "":
    raise ValueError("Invalid URL - Empty Field")

url_regex = re.compile("(http(s)?://)?(www.)?somebank.com(.br)?/exchange")
url_match = url_regex.match("www.somebank.com/exchange")

if not url_match:
    raise ValueError("Invalid URL")

# Print Base URL - Without Parameters

url_base = url[0:20]
print("Base URL = {}".format(url_base))

# Print URL Parameters
url_parameters = url[21:]

print("URL Parameters = {}".format(url_parameters))

# User should input the parameter
search_parameter = "originCurrency"
print("Searching for {}".format(search_parameter))

# Search parameter index on string
parameter_index = url_parameters.find(search_parameter)
print("Your parameter was found on index: {}".format(parameter_index))

# Search for Value Index based on parameter given
# +1 means that we skip the = sign
value_index = parameter_index + len(search_parameter) + 1

# It returns -1 if my separator (&) is BEFORE the value otherwise, it returns the index
separator_index = url_parameters.find("&", value_index)
print("Separator index = {}".format(separator_index))

# Obtaining the value attributed for this parameter the value index based on separator
if separator_index == -1:
    # Returning -1 implies that there is no other statements left, we can search till the end of the url
    parameter_value = url_parameters[value_index:]
else:
    # In the other hand, if we actually find the separator, we set it as the final index]
    parameter_value = url_parameters[value_index:separator_index]

print("Value = {}".format(parameter_value))

