##############################################################################
# TODO: Implementing SIFT + SVM with own data              		                       #
##############################################################################

from sklearn.neural_network import MLPClassifier

def train_MLP(des_array, y_train_list):
  """Train linear SVM"""
# Create a classifier: a support vector classifier
  classifier = MLPClassifier(hidden_layer_sizes=(50), max_iter=100, alpha=1e-4,
                      solver='sgd', verbose=True, random_state=1,
                      learning_rate_init=.1)

  classifier.fit(des_array, y_train_list)
  return classifier

##############################################################################
#                             END OF YOUR CODE                               #
##############################################################################