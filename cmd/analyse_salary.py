#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

import pandas as pd

DIR_DUMP = 'dump'


def analyseMinMax(df):
    '''Show min and max values'''
    dfRubles = df.loc[df['vac_money_cur'] == 'RUR']
    dfNoRubles = df.loc[df['vac_money_cur'] != 'RUR']

    print("\n### MAX & MIN")
    print('RUBLES:')
    print('Minimal salary(from): ', dfRubles['vac_money_from'].min())
    print('Maximal salary(from): ', dfRubles['vac_money_from'].max())
    print('Minimal salary(to): ', dfRubles['vac_money_to'].min())
    print('Maximal salary(to): ', dfRubles['vac_money_to'].max())

    print('NO-RUBLES($):')
    print('Minimal salary(from): ', dfNoRubles['vac_money_from'].min())
    print('Maximal salary(from): ', dfNoRubles['vac_money_from'].max())
    print('Minimal salary(to): ', dfNoRubles['vac_money_to'].min())
    print('Maximal salary(to): ', dfNoRubles['vac_money_to'].max())


def analyseAverage(df):
    '''Show avarage values'''
    dfRubles = df.loc[df['vac_money_cur'] == 'RUR']
    dfNoRubles = df.loc[df['vac_money_cur'] != 'RUR']

    print("\n### AVERAGE")
    print('RUBLES:')
    print('Average salary(from): ', dfRubles['vac_money_from'].mean())
    print('Average salary(to): ', dfRubles['vac_money_to'].mean())

    print('NO-RUBLES($):')
    print('Average salary(from): ', dfNoRubles['vac_money_from'].mean())
    print('Average salary(to): ', dfNoRubles['vac_money_to'].mean())


def analyseMedian(df):
    '''Show medians'''
    dfRubles = df.loc[df['vac_money_cur'] == 'RUR']
    dfNoRubles = df.loc[df['vac_money_cur'] != 'RUR']

    print("\n### MEDIAN")
    print('RUBLES:')
    print('Median salary(from): ', dfRubles['vac_money_from'].median())
    print('Median salary(to): ', dfRubles['vac_money_to'].median())

    print('NO-RUBLES($):')
    print('Median salary(from): ', dfNoRubles['vac_money_from'].median())
    print('Median salary(to): ', dfNoRubles['vac_money_to'].median())


def main():
    if len(sys.argv) != 2:
        print("Use: script.py file-name.csv")
        sys.exit()

    fileName = sys.argv[1]
    print('File name: ', fileName)
    appPath = os.path.abspath(os.getcwd())
    fileAbsPath = os.path.join(appPath, DIR_DUMP, fileName)
    df = pd.read_csv(fileAbsPath, sep=';')

    analyseMinMax(df)
    analyseAverage(df)
    analyseMedian(df)


if __name__ == "__main__":
    main()
