# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["0","7","-1"],
        ["Dame un numero=","0!=1","Dame un numero=","7!=5040","Dame un numero=","-1!=Error!"],
        "Debe salir\nHello World!"
    )
]
