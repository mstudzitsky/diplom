def ikomek_accuracy(y_true, y_pred, **kwargs):
    accuracy = 0.0
    for i in range(0, y_pred.shape[0]):
        if y_true.array[i] == y_pred[i]:
            accuracy += 1
        elif (y_pred[i] == 10 or y_pred[i] == 4) and y_true.array[i] == 14:
            accuracy += 0.5
        elif y_pred[i] == 14 and (y_true.array[i] == 10 or y_true.array[i] == 14):
            accuracy += 0.5
    return accuracy/y_pred.shape[0]