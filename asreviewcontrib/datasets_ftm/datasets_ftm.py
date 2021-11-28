from asreview.datasets import BaseVersionedDataSet, BaseDataSet
from asreview.datasets import BaseDataGroup
from pathlib import Path

class YourDataGroup(BaseDataGroup):
    group_id = "your_data_group"
    description = "Data files containing Mock-up data of the Shell-files."

    def __init__(self):

        metadata_assen = BaseDataSet.from_config({
            "dataset_id": "data_assen_demo",
            "url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/data/data_assen_demo.csv",
            "img_url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/images/assen.png",
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
            "dataset_id": "data_drenthe_demo",
            "url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/data/data_drenthe_demo.csv",
            "img_url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/images/drenthe.PNG",
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

        
        metadata_amsterdam = BaseDataSet.from_config({
            "dataset_id": "data_amsterdam_demo",
            "url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/data/data_amsterdam_demo.csv",
            "img_url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/images/amsterdam.PNG",
            "link": "https://www.ftm.nl/dossier/shell-papers",
            "license": "",
            "title": "Amsterdam (Mock-up)",
            "authors": [
            "FTM"
            ],
            "year": 2021,
            "topic": ""
        }
        )


        metadata_nh = BaseDataSet.from_config({
            "dataset_id": "data_nh_demo",
            "url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/data/data_nh_demo.csv",
            "img_url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/images/nh.PNG",
            "link": "https://www.ftm.nl/dossier/shell-papers",
            "license": "",
            "title": "Noord-Holland (Mock-up)",
            "authors": [
            "FTM"
            ],
            "year": 2021,
            "topic": ""
        }
        )
        
        metadata_minfin = BaseDataSet.from_config({
            "dataset_id": "data_minfin_demo",
            "url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/data/data_minfin_demo.csv",
            "img_url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/images/minfin.PNG",
            "link": "https://www.ftm.nl/dossier/shell-papers",
            "license": "",
            "title": "Ministerie van Financien (Mock-up)",
            "authors": [
            "FTM"
            ],
            "year": 2021,
            "topic": ""
        }
        )
        
        metadata_minienw = BaseDataSet.from_config({
            "dataset_id": "data_minienw_demo",
            "url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/data/data_minienw_demo.csv",
            "img_url": "https://raw.githubusercontent.com/asreview-ftm-hackathon/ASReview-plugin-FTM/main/images/minienw.PNG",
            "link": "https://www.ftm.nl/dossier/shell-papers",
            "license": "",
            "title": "Ministerie van Infrastructuur en Waterstaat (Mock-up)",
            "authors": [
            "FTM"
            ],
            "year": 2021,
            "topic": ""
        }
        )
        assen = BaseVersionedDataSet("test1", [metadata_assen], "test2")
        drenthe = BaseVersionedDataSet("test3", [metadata_drenthe], "test4")      
        amsterdam = BaseVersionedDataSet("test5", [metadata_amsterdam], "test6")
        nh = BaseVersionedDataSet("test7", [metadata_nh], "test8")
        minfin = BaseVersionedDataSet("test9", [metadata_minfin], "test10")
        minienw = BaseVersionedDataSet("test11", [metadata_minienw], "test12")    

        super(YourDataGroup, self).__init__(assen, drenthe, amsterdam, nh, minfin, minienw)
        # pass multiple datasets to init if there are more datasets
