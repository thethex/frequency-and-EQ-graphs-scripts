import sys

print("USE : python diff_response_response.py /PATH/TO/your_frequency_response_file.txt /PATH/TO/your_frequency_response_file_to_substract.txt")

measurea = sys.argv[1]
measureb = sys.argv[2]
diff = "sub_"+measureb.replace(".txt","")+"_with_"+measurea

count = 0
# Strips the newline character
with open(measurea) as fa, open(measureb) as fb,open(diff,"w") as o:
  for linea, lineb in zip(fa, fb):
    if not(linea.startswith("*")):
        valuesa = linea.strip().split(",")
        valuesb = lineb.strip().split(",")
        count += 1
        floata=float(valuesa[1])
        floatb=float(valuesb[1])
        valuediff=(floatb-floata)
        print("Line{}: '{}' '{}' - '{}' = {}".format(count,valuesa[0],valuesb[1],valuesa[1],valuediff))
        o.write("{},{}\n".format(valuesa[0],valuediff))

