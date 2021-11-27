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
        
        metadata_drenthe = BaseDataSet.from_config({
            "dataset_id": "data_drenthe_mockup",
            "url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/15fb29ae372b3b610ad34e33c79aa68f621213ba/data/data_drenthe_mockup.csv",
            #"url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/data/data_drenthe_mockup.csv",
            "img_url": "https://www.provincie.drenthe.nl/publish/pages/120213/logo-provincie-drenthe.png",
            "link": "https://www.ftm.nl/dossier/shell-papers",
            "license": "",
            "title": "Drenthe (Mock-up)",
            "authors": [
            "FTM"
            ],
            "year": 2021,
            "topic": ""
        }
        )

        assen = BaseVersionedDataSet("test1", [metadata_assen], "test2")
        drenthe = BaseVersionedDataSet("test3", [metadata_drenthe], "test4")      


        super(YourDataGroup, self).__init__(assen, drenthe)
        # pass multiple datasets to init if there are more datasets
