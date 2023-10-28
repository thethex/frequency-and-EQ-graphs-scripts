import sys

print("USE : python convert_wavelet_response.py /PATH/TO/your_wavelet_graphic_EQ_file.txt /PATH/TO/template_frequency_response.txt ")

wavelet = sys.argv[1]
pattern = sys.argv[2]
squiged = wavelet.replace(".txt",".squiged.txt")

# Strips the newline character
with open(wavelet) as w, open(pattern) as p,open(squiged,"w") as s:

  wave_content = w.readline().split(';')

  #MEASURES = list([map(float, line.split('\t')) for line in m.readlines()])

  print(wave_content)

  wave_i=0

  linew=wave_content[0].split(' ');
  freqw=float(linew[1])
  floatw=float(linew[2])

  for linep in p:
    lineps = linep.strip().split(",")
    freqp=float(lineps[0])
    floatp=float(lineps[1])

    # If current  pattern frequency is higher than wavelet frequency, go to next wavelet frequency.
    # Added security, you can't overflow wavelet content.
    if((freqp>freqw) and wave_i<(len(wave_content)-1)):
      wave_i+=1
      linew=wave_content[wave_i].split(" ")

    freqw=float(linew[1])
    floatw=float(linew[2])

    floatr=floatp+floatw
    print("{} + {}:'{}'".format(floatp,floatw,floatr))
    s.write("{},{}\n".format(freqp,floatw))
