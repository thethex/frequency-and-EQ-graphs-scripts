import sys

print("USE : python convert_wavelet_response.py /PATH/TO/your_wavelet_graphic_EQ_file.txt /PATH/TO/template_frequency_response.txt ")

wavelet = sys.argv[1]
pattern = sys.argv[2]
squiged = wavelet.replace(".txt",".squiged.txt")

# Strips the newline character
with open(wavelet) as w, open(pattern) as p,open(squiged,"w") as s:

  wave_content = w.readline().split(';')

  # Output frequency will be between this and the previous index
  wave_i=1 #wavelet next index

  # i-1
  linew=wave_content[0].split(' ');
  freqw=float(linew[1])
  floatw=float(linew[2])

  # i
  linewi=wave_content[wave_i].split(' ');
  freqwi=float(linewi[1])
  floatwi=float(linewi[2])

  for linep in p:
    lineps = linep.strip().split(",")
    freqp=float(lineps[0])
    floatp=float(lineps[1])

    # If current  pattern frequency is higher than wavelet frequency, go to next wavelet frequency.
    # Added security, you can't overflow wavelet content.
    if((freqp>freqwi) and wave_i<(len(wave_content)-1)):

      # index-1 = index
      freqw=freqwi
      floatw=floatwi

      # index = index+1
      wave_i+=1
      linewi=wave_content[wave_i].split(" ")
      freqwi=float(linewi[1])
      floatwi=float(linewi[2])

    # Calculate the output frequency.
    # To do so we calculate the equation of the line going through the 2 wavelet index coordinate
    # And then deduce the Y value corresponding to the x frequency
    # We then add this value to the template value (0).

    floatr= floatp+(((freqp-freqw)*((floatwi-floatw)/(freqwi-freqw)))+floatw)

    print("value template {} + calc wavelet value at frequency {} = '{}'".format(floatp,freqp,floatr))
    s.write("{},{}\n".format(freqp,floatw))
