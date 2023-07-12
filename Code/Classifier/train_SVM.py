##############################################################################
# TODO: Implementing SIFT + SVM with own data              		                       #
##############################################################################

from sklearn import svm

def train_rbf_SVM(hist_array, y_train_list):
# Create a classifier: a support vector classifier
  classifier = svm.SVC(kernel='rbf', gamma=0.7)
  classifier.fit(hist_array, y_train_list)
  return classifier

##############################################################################
#                             END OF YOUR CODE                               #
##############################################################################