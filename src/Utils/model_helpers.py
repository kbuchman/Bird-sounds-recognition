from sklearn.model_selection import KFold


def cross_validation(signals: list, folds: int):
    kf = KFold(folds)
    output = []
    for train, test in kf.split(signals):
        output.append((train, test))
    return output