from rembg import  remove


input_path = "image.jpg"        # girdinin türü her türlü olur farketmez
output_path = "output.png"      # çıktının sonunu .png vermeliyiz arka planı transparan jpg desteklemiyor png destekliyor


with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)