# JWT Tokens

# The client will send some credentials, e.g. login + PW
# If the credentials are valid, then a token is produced 
# The token is sent back, and the client then uses this everytime an API request is sent 
# The API checks that the token is valid, and if it is, the info is sent back
# The token is NOT encrypted and contains metadata like: 
# 1) The header, with the algorithm and type. 
# 2) The payload; the info of which is up to the programmer, such as non-sensitive info like the user ID. 
# 3) Verify signature; A combo of the header, payload and a secret. 

