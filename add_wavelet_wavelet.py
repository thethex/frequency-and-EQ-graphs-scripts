import sys

print("USE : python convert_wavelet_response.py /PATH/TO/your_wavelet_graphic_EQ_file.txt /PATH/TO/your_second_wavelet_graphic_EQ_file.txt ")

wavelet_a = sys.argv[1]
wavelet_b = sys.argv[2]


with open(wavelet_a) as wa, open(wavelet_b) as wb,open(wavelet_a.replace(".txt",".squiged.txt") +"_plus_"+wavelet_b,"w") as o:

    res="GraphicEQ:"
    la=wa.readline().strip().split(":")[1].split(";")
    lb=wb.readline().strip().split(":")[1].split(";")
    for i in range(len(la)):
        las=la[i].split(" ")
        lbs=lb[i].split(" ")
        res= res+" {0:} {1:.1f};".format(las[1],(float(las[2])+float(lbs[2])))
        print(res)
    res = res[:-1] #remove last ;
    o.write(res)
