from sklearn.base import TransformerMixin, BaseEstimator


class SAXDiscretizer(TransformerMixin, BaseEstimator):
    """ Discretizer that is based on the default implementation of  Symbolic Aggregate approXimation algorithm
    """

    def __init__(self, params=None):
        pass

    def fit(self, X, y):
        return self

    def transform(self, X):
        return None
