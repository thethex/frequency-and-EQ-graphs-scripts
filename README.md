# frequency-and-EQ-graphs-scripts

This repository is a compilation of python scripts used to manipulate frequency response and Wavelet Graphical EQ files.

## Requierments

python (tested with python 3.11)

## File Definition

### Wavelet Graphic Filters

* negative number : `-n.n`
* positive number : `n.n`
* round number    : `n.0`

### Squig Frequency Response

## Addition scripts

These scripts calculates the sum of  `Frequency Responses`/`Wavelet compatible Graphical EQ`.
It can be used to apply a positiv adjustment to a Frequency Response or Graphical EQ.

### add_wavelet_wavelet

Add two Wavelet Graphical EQ together:

```python
python add_wavelet_wavelet.py /PATH/TO/your_wavelet_graphic_EQ_file.txt /PATH/TO/your_second_wavelet_graphic_EQ_file.txt
```
Creates a converted file `/PATH/TO/your_wavelet_graphic_EQ_file_plus_your_second_wavelet_graphic_EQ_file.txt`

### add_response_response

```python
python add_response_response.py
```

### add_wavelet_response

To add Wavelet Graphical EQ and Squig Frequency Response, use the convert script `wavelet_to_frequency_response` with the frequency response has template :

```python
python convert_wavelet_response.py /PATH/TO/your_wavelet_graphic_EQ_file.txt /PATH/TO/your_frequency_response.txt
```

## Substract scripts

These scripts calculates the difference between `Frequency Responses`/`Wavelet compatible Graphical EQ`.
It can be used to calculate the difference between to Frequency Responses. Or apply a negative adjustment to a Frequency Response or Graphical EQ.

### diff_wavelet_wavelet



### diff_response_response


## Convert scripts

These scripts allows to convert Wavelet Graphical EQ files to Squig.link compatible Frequency Responses files and .

### wavelet_to_frequency_response

```python
python convert_wavelet_response.py /PATH/TO/your_wavelet_graphic_EQ_file.txt /PATH/TO/template_frequency_response.txt
```

Creates a converted file `/PATH/TO/your_wavelet_graphic_EQ_file.squiged.txt`

### frequency_response_to_wavelet
