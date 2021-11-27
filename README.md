# ASReview-plugin-FTM

In this repository, we will develop a plug-in for the open-source software
[ASReview](www.asreview.ai) inspired by the [CORD19 plug-in](
https://github.com/asreview/asreview-covid19). 

The current repository will contain mock-up datasets based on  the files
available at the website of [Follow the
Money](https://www.ftm.nl/dossier/shell-papers#documenten). A `csv` file
containing these files is available at [Github](
https://github.com/ftmnl/asr), and we randomly created [10
subsets](https://github.com/asreview-ftm-hackathon/Data/tree/main/split_preprocessed)
to resemble the [different expected data
files](https://www.ftm.nl/dossier/shell-papers#wob-verzoeken). 

# Getting Started

Clone the repository, navigate to the folder in the CMD, and install the FTM-pluging with

```bash
pip install .
```

or

```bash
pip install git@github.com:{USER_NAME}/{REPO_NAME}.git
```

and replace `{USER_NAME}` and `{REPO_NAME}` by your own details. 


# Usage

Install ASReview version 0.17 and launh the softare via the CMD.

The mock-up data can be selected under plug-ins:

![alt text](https://user-images.githubusercontent.com/36502709/143719180-6bfb533c-903b-4c74-93ac-da5f2ee74f39.png)

# License
The content in this repository is published under the MIT license.

# Contact
For any questions or remarks, please send an email to asreview@uu.nl.   
