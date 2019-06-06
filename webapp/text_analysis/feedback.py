import numpy as np
import random


class HybridModel(object):


    def __init__(self, standards, path=None):
        self.standards = standards
        self.path = path
        self.data = self.create(standards)

    def __str__(self):
        return str(self.data)
    

    def create(self, list_of_standards):
        """
        Imaginary blackbox that returns scores per document (now just a random Numpy array)
        """
        blackbox = np.random.uniform(0,100,[5]).round(2).tolist()
        data = {}
        for i, standard in enumerate(list_of_standards):
            data[standard] = (blackbox[i], 0)
        return data


    def update(self, feedback):
        """
        Train model to update with user feedback
        """
        for standard, vote in feedback.items():
            if vote:
                self.data[standard] = (self.data[standard][0], self.data[standard][1]+1)
        return self.data


    def compute(self):
        pass


if __name__ == "__main__":
    """
    Given two features, the unsupervised score (black boxed and randomized here), and a user's selection over time

    black-box-score: 90.3
    user-votes: 2

    How do you rank this?
    global model * user specific
    """
    standards = ["ISO/IEC 17025", "Coast Guard 4323", "IEEE 403403", "ISO 12312312"]
    model = HybridModel(standards)
    print(model.data)
    # User accepts, rejects, or suggests each standard for training 
    for i in range(1,6):
        user_choices = np.random.choice(a=[False, True], size=(5,)).tolist()
        feedback = dict(zip(standards, user_choices))
        print("Iteration %s" % i)
        print(model.data)
        model.update(feedback)
