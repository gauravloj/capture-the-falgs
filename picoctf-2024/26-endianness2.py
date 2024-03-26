filename = 'challengefile'

outfile = open(f"{filename}.jpg", 'wb')
with open(filename, 'rb') as f:

    while True:
        data = f.read(4)
        if not data:
            break
        data = data[::-1]
        outfile.write(data)



# image shows picoCTF{cert!f1Ed_iNd!4n_s0rry_3nDian_b039bc14}

