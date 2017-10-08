import os
import pandas as pd
from pyador.pyador import Pyador
from pyador import local as const

if __name__ == "__main__":
    dev_file = os.path.join(const.DEV_DIR, const.DEV_FILE)
    X = pd.read_csv(dev_file)
    print("training data is %s " % dev_file)
    print("data shape is %s" % (X.shape,))

    # initialize the program with fraud percentage
    clf = Pyador(frac=0.05)
    clf._debug()

    y_predict = clf.fit_predict(X)

    print(y_predict[0:500])
