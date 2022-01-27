# Francesco Esposito Enero 2022
import pandas
from os import path
import os
data = pandas.read_csv('https://raw.githubusercontent.com/marcusRB/IDbootcamps_DataScience_student_PT_10201/master/dataset/bank_budget_data.csv')
saveFile = path.join(path.dirname(__file__), 'analisis.txt')

def write_to_file(meses, tot, promedio, maxIncrDate, maxIncr, maxDismDate, maxDism, verbose=True):
  with open(saveFile, 'w', encoding='utf-8') as file:
    line0 = 'Análisis financiero\n\n'
    line1 = f'Meses Totales: {meses}\n'
    line2 = f'Total: {tot} $\n'
    line3 = f'Cambio Promedio: {promedio} $\n'
    line4 = f'Mayor Incremento de Utilidades: {maxIncrDate} ({maxIncr} $)\n'
    line5 = f'Mayor Disminución en Utilidades: {maxDismDate} ({maxDism} $)'
    report = line0 + line1 + line2 + line3 + line4 + line5
    file.write(report)
    if verbose: print(report)

def analisis():
    meses = data.shape[0]
    tot = sum(data['Profit/Losses'])
    for n in range(meses-1):
        data.loc[n+1, 'Profit/Losses previus month'] = data.loc[n, 'Profit/Losses']
    data['change'] = data['Profit/Losses'] - data['Profit/Losses previus month']
    promedio = round(data.change.mean(), 2)
    maxIncr = data.change.max()
    maxIncrDate = str(data['Date'][data['change']==maxIncr]).split()[1]
    maxDism = data.change.min()
    maxDismDate = str(data['Date'][data['change']==maxDism]).split()[1]
    write_to_file(meses, tot, promedio, maxIncrDate, maxIncr, maxDismDate, maxDism)

if __name__ == '__main__':
    analisis()

    print(pandas.__version__)
    print(os.getcwd())
    print(os.path.dirname(__file__))


