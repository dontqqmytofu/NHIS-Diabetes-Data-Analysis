import pandas as pd
import matplotlib.pyplot as mpl
import numpy as np
import glob
import os

path = r"C:/Users/syang/Documents/CDC_NHIS_Data/splits"
files = glob.glob(os.path.join(path , "*.csv"))
li = []
for filename in files:
	df = pd.read_csv(filename, index_col = None, header=0)
	li.append(df)

fullData = pd.concat(li, axis=0, ignore_index=True)

#fullData = pd.read_csv("C:/Users/syang/Documents/CDC_NHIS_Data/adult20.csv")
replace1 = fullData.replace({'INTV_MON':{1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}, 
							 'AGEP_A':{85:"85+", 97:'Refused', 98:'Not Ascertained', 99:"Don't Know"},
							 'SEX_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'HISP_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'HISPALLP_A':{1:'Hispanic', 2:'NH White only', 3:'NH Black/African American only', 4:'NH Asian only', 5:'NH AIAN only', 6:'NH AIAN and any other group', 7:'Other single and multiple races', 97:'Refused', 98:'Not Ascertained', 99:"Don't Know"},
							 'HISDETP_A':{1:"Hispanic (Mexican/Mexican American)", 2:"Hispanic (all other groups)", 3:"Not Hispanic", 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'RACEALLP_A':{1:'White only', 2:"Black/African American only", 3:'Asian only', 4:'AIAN only', 5:'AIAN and any other group', 6:'Other single and multiple race', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'PHSTAT_A':{1:'Excellent', 2:'Very Good', 3:'Good', 4:'Fair', 5:'Poor', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'DIBTYPE_A':{1:'Type 1', 2:'Type 2', 3:'Other type of diabetes', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'MODFREQW_A':{0:'Less than once a week', 94:'Never', 95:'Extreme value', 96:'Unable to do this type of activity', 97:'Refused', 98:'Not Ascertained', 99:"Don't Know"},
							 'VIGFREQW_A':{0:'Less than once a week', 94:'Never', 95:'Extreme value', 96:'Unable to do this type of activity', 97:'Refused', 98:'Not Ascertained', 99:"Don't Know"},
							 'STRFREQW_A':{0:'Less than once a week', 94:'Never', 95:'Extreme value', 96:'Unable to do this type of activity', 97:'Refused', 98:'Not Ascertained', 99:"Don't Know"},
							 'PA18-02R_A':{1:'Inactive', 2:'Insufficiently active', 3:'Sufficiently active', 8:'Not Ascertained'},
							 'INCGRP_A':{1:"$0-$34,999", 2:"$35,000-$49,999", 3:"$50,000-$74,999", 4:"$75,000-$99,999", 5:"$100,000 or greater", 8:"Not Ascertained"},
							 'ADVACTIVE_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'ADVEAT_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'ADVWGTPRG_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'NOWACTIVE_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'NOWEAT_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'NOWWGTPRG_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'HYPEV_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'HYPDIF_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'HYP12M_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'HYPMED_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'CHLEV_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'CHL12M_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'CHLMED_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'CHDEV_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'ANGEV_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'MIEV_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'STREV_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'PREDIB_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'GESDIB_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'DIBEV_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'DIBREL_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'PREGNOW_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'WEIGHTLBTC_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 'BMICAT_A':{1:'Yes', 2:'No', 7:'Refused', 8:'Not Ascertained', 9:"Don't Know"},
							 })
#print(replace1)

filteredReplaced = replace1[['HHX', 'INTV_MON', 'AGEP_A', 'SEX_A', 'HISP_A', 'HISPALLP_A', 'HISDETP_A', 'RACEALLP_A', 'PHSTAT_A',
				  'HYPEV_A', 'HYPDIF_A', 'HYP12M_A', 'HYPMED_A', 'CHLEV_A', 'CHL12M_A', 'CHLMED_A', 'CHDEV_A', 'ANGEV_A', 'MIEV_A', 'STREV_A', 'PREDIB_A', 'GESDIB_A', 'DIBEV_A', 'DIBREL_A', 'PREGNOW_A', 'WEIGHTLBTC_A', 'BMICAT_A', 'DIBTYPE_A',
				  'ADVACTIVE_A', 'ADVEAT_A', 'ADVWGTPRG_A', 'NOWACTIVE_A', 'NOWEAT_A', 'NOWWGTPRG_A',
				  'FAMINCTC_A', 'POVRATTC_A', 'INCGRP_A']]
#print(filteredReplaced)
#print(sum(1 for x in filteredReplaced['DIBEV_A'] if x=='Yes'))
#print(len(filteredReplaced[filteredReplaced['DIBEV_A'] == 'Yes']))
#print(type(filteredReplaced))
#print(len(filteredReplaced[(filteredReplaced['CHLEV_A'] == 'Yes') & (filteredReplaced['DIBEV_A'] == 'Yes')]))

#Pie chart of individuals with diabetes
labels = 'Yes', 'No', "Other - Refused, Not Ascertained, Don't Know"
sizes = [len(filteredReplaced[filteredReplaced['DIBEV_A'] == 'Yes']), 
len(filteredReplaced[filteredReplaced['DIBEV_A'] == 'No']), 
len(filteredReplaced[(filteredReplaced['DIBEV_A'] == 'Refused') | (filteredReplaced['DIBEV_A'] == 'Not Ascertained') | (filteredReplaced['DIBEV_A'] == "Don't Know")])] 

fig1, ax1 = mpl.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
mpl.show()

#Pie chart of individuals with high cholestrol and diabetes
labels = 'Yes', 'No', "Other - Refused, Not Ascertained, Don't Know"
sizes = [len(filteredReplaced[(filteredReplaced['CHLEV_A'] == 'Yes') & (filteredReplaced['DIBEV_A'] == 'Yes')]),
		 len(filteredReplaced[(filteredReplaced['CHLEV_A'] == 'Yes') & (filteredReplaced['DIBEV_A'] == 'No')]),
		 len(filteredReplaced[(filteredReplaced['CHLEV_A'] == 'Yes') & ((filteredReplaced['DIBEV_A'] == 'Refused') | (filteredReplaced['DIBEV_A'] == 'Not Ascertained') | 
																  (filteredReplaced['DIBEV_A'] == "Don't Know"))])]

fig2, ax2 = mpl.subplots()
ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax2.axis('equal')
mpl.show()

#Bar chart showing rates of diabetes among individuals with: high cholestrol, hypertension, angina
n = 3
cntDiabY = (len(filteredReplaced[(filteredReplaced['CHLEV_A'] == 'Yes') & (filteredReplaced['DIBEV_A'] == 'Yes')]), len(filteredReplaced[(filteredReplaced['HYPEV_A'] == 'Yes') & (filteredReplaced['DIBEV_A'] == 'Yes')]), len(filteredReplaced[(filteredReplaced['ANGEV_A'] == 'Yes') & (filteredReplaced['DIBEV_A'] == 'Yes')]))
cntDiabN = (len(filteredReplaced[(filteredReplaced['CHLEV_A'] == 'Yes') & (filteredReplaced['DIBEV_A'] == 'No')]), len(filteredReplaced[(filteredReplaced['HYPEV_A'] == 'Yes') & (filteredReplaced['DIBEV_A'] == 'No')]), len(filteredReplaced[(filteredReplaced['ANGEV_A'] == 'Yes') & (filteredReplaced['DIBEV_A'] == 'No')]))

ind = np.arange(n)
width = .35

fig3, ax3 = mpl.subplots()
rects1 = ax3.bar(ind, cntDiabY, width, color = 'r')
rects2 = ax3.bar(ind + width, cntDiabN, width, color = 'b')

ax3.set_ylabel('Count')
ax3.set_title('Diabetes rates among individuals with other health conditions')
ax3.set_xticks(ind + width / 2)
ax3.set_xticklabels(('High Cholestrol', 'Hypertension', 'Angina'))

ax3.legend((rects1[0], rects2[0]), ('Yes', 'No'))

def autolabel(rects):
	for rect in rects:
		height = rect.get_height()
		ax3.text(rect.get_x() + rect.get_width()/2., height,
		  '%d' % int(height),
		  ha = 'center', va = 'bottom')

autolabel(rects1)
autolabel(rects2)

mpl.show()