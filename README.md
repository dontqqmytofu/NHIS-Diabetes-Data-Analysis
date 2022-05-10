# Data Analyses Project Using Python
This project demonstrates some data analysis capabilties using Python to read, process, and create visualizations. The dataset used is the 2020 NHIS survey.
## Data Manipulations
There are 2 files used in creating the full dataset: The raw survey data, and a PDF file containing information that links the coded (numerical) data from the survey to the corresponding answers.
The raw survey data was too large to upload to github as one file, so I have split them, and changed the code separately to join them when run.
```python
import glob
import os

path = r"C:/Users/syang/Documents/CDC_NHIS_Data/splits"
files = glob.glob(os.path.join(path , "*.csv"))
li = []
for filename in files:
	df = pd.read_csv(filename, index_col = None, header=0)
	li.append(df)

fullData = pd.concat(li, axis=0, ignore_index=True)
```
The next step involves re-assigning the actual survey answers to their code in the raw data.
```python
replace1 = fullData.replace({'INTV_MON':{1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}, 
..., 'BMICAT_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"}
})
```
After this, if we want to create a new output file, we can filter the dataset for attributes relevant to the work we want to perform.
```python
filteredReplaced = replace1[['HHX', 'INTV_MON', 'AGEP_A', 'SEX_A', 'HISP_A', 'HISPALLP_A', 'HISDETP_A', 'RACEALLP_A', 'PHSTAT_A',
				  'HYPEV_A', 'HYPDIF_A', 'HYP12M_A', 'HYPMED_A', 'CHLEV_A', 'CHL12M_A', 'CHLMED_A', 'CHDEV_A', 'ANGEV_A', 'MIEV_A', 'STREV_A', 'PREDIB_A', 'GESDIB_A', 'DIBEV_A', 'DIBREL_A', 'PREGNOW_A', 'WEIGHTLBTC_A', 'BMICAT_A', 'DIBTYPE_A',
				  'ADVACTIVE_A', 'ADVEAT_A', 'ADVWGTPRG_A', 'NOWACTIVE_A', 'NOWEAT_A', 'NOWWGTPRG_A',
				  'FAMINCTC_A', 'POVRATTC_A', 'INCGRP_A']]
```
## Visualizations
### Figure 1 - Individuals with Diabetes
![Figure_1](https://user-images.githubusercontent.com/44685741/167742916-e393c70b-adcd-499e-a8f8-9e5c23326fa1.png)

### Figure 2 - Individuals with High Cholestrol and Diabetes
![Figure_2](https://user-images.githubusercontent.com/44685741/167742970-ef18d46b-f687-4768-bde2-52c1de47696a.png)

### Figure 3 - Rates of Diabetes Among Individuals with: High Cholestrol, Hypertension, Angina
![Figure_3](https://user-images.githubusercontent.com/44685741/167743024-c3e86194-1125-426b-b0f0-9a57ca56a0d4.png)
