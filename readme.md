# Running
## Train and run the transformer, transformer w/ preprocessing or LSTM (subwords)
Look in the ```/notebooks``` folder to find three jupyter notebooks with instructions on how to run the models (take note that some functionality, like saving and loading from google Drive requires you to run the file via [Google Colab](https://colab.research.google.com).

## Train and run the custom LSTM and Vanilla models
To run the custom-made networks in the ```models``` folder, simply execute the file from the root directory (make sure this root folder is added to your `PYTHONPATH`). An example call to train the LSTM model and generate comments for the validation set is shown below:

```bash
$ export PYTHONPATH = "${PYTHONPATH}:/path/to/our/project/"
$ python3 models/seq2seqLSTM.py
$ python3 models/infer_lstm.py
``` 

## Example outputs
Example outputs for the models can be found in the ```Evaluation``` folder. This folder also contains the generated markdown files used for our expert evaluation for the _subword LSTM_ and _Transformer_ models.  