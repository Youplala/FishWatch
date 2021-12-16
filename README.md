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



Figure 1 is a plot showing 100k vessel encounters. As stated above, encounters are Authorizations are either known, partially known or unknown. 

Encounters are locations where two vessels, a fishing and a carrier vessel, were within 500 meters for at least two hours and traveling at a median speed or less than 2 knots, while at least 30km away from a coastal anchorage.