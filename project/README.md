## File description  <br>
DATA603_Alex_final proj.ipynb: main program, all needed toolkits are included, it can be directly run withou any setting up, ML train process will take over 20mins.<br>
host_train.csv.zip: data set, origin one's size is too big, so it converts into a zip file.<br>
presentation.pdf: PPT file.<br>
README.md: file you are reading.<br>



## Explanation about changing the content of the project <br>
At first I chose a question about covid and unemployment for my project, but after I observed and analyzed the data, the results were very boring, and because the effect of covid was so huge that it resulted in a curve that matched the unemployment rate and the number of covid very well, I didn't know what more analysis I could do.

## Why I chose this data <br>
So I looked for another data on hospital treatment of covid to predict the number of days a patient needs to be treated. This makes a lot of sense because it will help doctors come up with better treatment plans, which will ease the strain on our healthcare system.

## Final results and explain <br>
After a series of adjustments to the parameters and training, I improved the accuracy from 20% to 40%. I also compared my results to those using other algorithms and there was little difference in the final results. The final predictions were visualized with the data and did not identify a large number of predictions with obvious errors, as most of the predictions basically fell to the left or right of the truth. The main prediction errors appear inside the 2 columns of 41-70 years old. Since the characteristics of these data are not very prominent, the decision tree gives more conservative predictions at depths of 5 and 10. If I had more time for me to solve this problem, I think I would use pruning to improve the accuracy.

**Parameters of DecisionTreeClassifier**<br>
Impurity - Gini<br>
maxBins - 24,32<br>
minInfoGain - 0.0, 0.2<br>
maxDepth - 5,10<br>
Cross-validator 10 fold<br>


**result:**<br>
Accuracy = 0.391596 <br>
F1 = 0.350377 <br>
Test Error = 0.608404 <br>
True Positive Rate By Label = 0.685592 <br>
False Positive Rate By Label = 0.402116 <br>
Precision By Label = 0.394414 <br>
Recall By Label = 0.685592 <br>
FMeasure By Label = 0.500751 <br>
Weighted Recall = 0.391596 <br>
Weighted Precision = 0.359063 <br>
Weighted True Positive Rate = 0.391596 <br>
Weighted FMeasure = 0.350377 <br>
Log Loss = 1.78592 <br>
Hamming Loss = 0.608404 <br>
