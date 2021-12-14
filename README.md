# FishWatch

This repo is a collection of scripts and notebooks to download, merge and analyze data from [GlobalFishingWatch](https://globalfishingwatch.org/data-download/).

We also process, split and build a classification model to predict wether a vessel encounter is authorized, partially authorized or not authorized.

## Installation

Create an account and download all the `Carriers v*` zips from [GlobalFishingWatch](https://globalfishingwatch.org/data-download/) into a folder called `carriers_data` in the root of the repository.

Run the following command to unzip the files we are interested in:

```
python3 extract_zips.py
```

It will create a new folder called `extracted` that will contain the extracted files, and a file `final.csv` containing the merge of all the files.
The `final.csv` file is the one we will use to train our model.

