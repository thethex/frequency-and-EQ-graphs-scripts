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

### merge_wavelet

```python
python merge_wavelet.py
```

### merge_response

```python
python merge_response.py
```

### merge_wavelet_response

```python
python merge_wavelet_response.py
```

## Substract scripts

These scripts calculates the difference between `Frequency Responses`/`Wavelet compatible Graphical EQ`.
It can be used to calculate the difference between to Frequency Responses. Or apply a negative adjustment to a Frequency Response or Graphical EQ.

### diff_response


## Convert scripts

These scripts allows to convert Wavelet Graphical EQ files to Squig.link compatible Frequency Responses files and .

### wavelet_to_frequency_response

```python
python convert_wavelet_response.py /PATH/TO/your_wavelet_graphic_EQ_file.txt /PATH/TO/template_frequency_response.txt
```

Creates a converted file `/PATH/TO/your_wavelet_graphic_EQ_file.squiged.txt`

### frequency_response_to_wavelet
