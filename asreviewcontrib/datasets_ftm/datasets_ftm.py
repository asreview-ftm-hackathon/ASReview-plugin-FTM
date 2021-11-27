from asreview.datasets import BaseVersionedDataSet, BaseDataSet
from asreview.datasets import BaseDataGroup
from pathlib import Path

class YourDataGroup(BaseDataGroup):
    group_id = "your_data_group"
    description = "Data files containing Mock-up data of the Shell-files."

    def __init__(self):

        metadata_assen = BaseDataSet.from_config({
            "dataset_id": "data_assen_mockup",
            "url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/data/data_assen_mockup.csv",
            "img_url": "https://www.assen.nl/sites/all/themes/custom/assen/logo.png",
            "link": "https://www.ftm.nl/dossier/shell-papers",
            "license": "",
            "title": "Assen (Mock-up)",
            "authors": [
            "FTM"
            ],
            "year": 2021,
            "topic": ""
        }
        )



        dataset = BaseVersionedDataSet("demo", metadata_assen, "group_title")

        super(YourDataGroup, self).__init__(dataset)
        # pass multiple datasets to init if there are more datasets
