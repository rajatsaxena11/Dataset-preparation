# Dataset-preparation
To prepare an unbiased data set from a given data set for multi-class classification purpose

Given a count 'c', the aim is to extract c number of records of each label from the original dataset and create a new dataset having equal count of all labels. If a label count is less than c, the empty slots for the label are filled by randomly choosing and repeating the records of the label.
The purpose of it was to remvove the bias caused by a label present in huge proportion in the data, which can lead to misinterpretation of the accuracy results during classification. For example, if there are 4 labels A, B, C and D present in 80%, 10%, 5% and 5% ratio in the data set. After training a classifier, there might be a case where only label A is predicted corectly, while all the rest of the labels are predicted incorrectly. In that case, the accuracy achieved is 80%, however, the classifier's performance is very poor.
