from joblib import load
from utils import ikomek_accuracy


class Models(object):
    def __init__(self):
        self.model = load('models/nb.joblib')
        self.model4 = load('models/nb4.joblib')
        print('Model is ready!!!')

    def predict(self, text: str) -> tuple:
        pred = self.model.predict([text])
        if pred[0] == 0:
            pred = self.model4.predict([text])
        labels = {
            0: 'Другие',
            4: 'Сантехник',
            10: 'Электрик',
            14: 'Муж на час',
            13: 'Ремонт компьютеров',
            9: 'Уборка помещений',
            24: 'Видеонаблюдение',
            25: 'Автоматические ворота, рольставни',
            61: 'Ремонт стиральных машин'
        }
        return pred[0], labels[pred[0]]
