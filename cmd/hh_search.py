#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import json

# from tabulate import tabulate
import pandas as pd
import requests


# from transliterate import translit
class HhSearcher:
    def __init__(self):
        self.headers = {'user-agent': 'api-test-agent'}
        self.q = 'python'
        self.area = '2'  # SPb
        self.money = '1000'
        self.period = '30'
        self.ar_vac = []
        self.list_vac_name = []
        self.list_vac_money_from = []
        self.list_vac_money_cur = []
        self.list_vac_money_to = []
        self.list_city = []
        self.list_employer_name = []
        self.list_employer_url = []
        self.list_employer_url_vacancy = []
        self.list_addr_metro = []
        self.list_addr_street = []
        self.list_addr_build = []
        self.list_addr_lng = []
        self.list_addr_lat = []
        self.dict_data_pandas = []

    # Парсим вакансии на странице
    def req_parse_page(self, page_num):
        url = 'https://api.hh.ru/vacancies?text=%s&area=%s&salary=%s&period=%s&only_with_salary=true&per_page=10&page=%s&type=open' % (
            self.q, self.area, self.money, self.period, page_num)
        r = requests.get(url, headers=self.headers)
        vac_dic = json.loads(r.text)
        print('Parse page #', page_num, ' Vacancy count:', len(vac_dic['items']))
        
        # Проходим по всем вакансиям.
        for vac in vac_dic['items']:
            #employer = vac['employer']
            employer_name = vac['employer']['name']
            # employer_name = employer_name.encode('utf8')
            employer_url = ''
            try:
                employer_url = vac['employer']['url']
            except:
                pass
            employer_url_vacancy = vac['alternate_url']
            vac_name = vac['name']
            vac_money_from = vac['salary']['from']
            vac_money_to = vac['salary']['to']
            vac_money_cur = vac['salary']['currency']
            city = vac['area']['name']
            #address = vac['address']
            #snip = vac['snippet']
            #snip_req = vac['snippet']['requirement']
            #snip_res = vac['snippet']['responsibility']
            addr = vac['address']
            addr_lng = ''
            addr_lat = ''
            addr_metro = ''
            addr_street = ''
            addr_build = ''
            if addr != None:
                addr_lng = vac['address']['lng']
                addr_lat = vac['address']['lat']
                if addr['metro'] != None:
                    addr_metro = vac['address']['metro']['station_name']
                addr_street = vac['address']['street']
            if (addr != None) and ('building' in addr):
                addr_build = addr['building']
            # print addr
            #print("%s) %s [%s - %s]" % (str(page_num+1), vac_name, vac_money_from, vac_money_to))
            # snip_req, snip_res
            vac_num = page_num + 1
            self.ar_vac.append(
                [vac_num, vac_name, vac_money_from, vac_money_cur, vac_money_to, city, employer_name, employer_url,
                 employer_url_vacancy, addr_metro, addr_street, addr_build, addr_lng,
                 addr_lat])  # добавляем построчно сразу все параметры в список
            # добавляем каждый параметро в отдельный список. Это нужно для обработки в pandas
            # vac_name = translit(vac_name, "ru", reversed=True)
            # city = translit(city, "ru", reversed=True)
            # employer_name = translit(employer_name, "ru", reversed=True)
            # addr_metro = translit(addr_metro, "ru", reversed=True)
            # addr_street = translit(addr_street, "ru", reversed=True)
            # addr_build = translit(addr_build, "ru", reversed=True)
            # addr_build = translit(addr_build, "ru", reversed=True)
            self.list_vac_name.append(vac_name)
            self.list_vac_money_from.append(vac_money_from)
            self.list_vac_money_cur.append(vac_money_cur)
            self.list_vac_money_to.append(vac_money_to)
            self.list_city.append(city)
            self.list_employer_name.append(employer_name)
            self.list_employer_url.append(employer_url)
            self.list_employer_url_vacancy.append(employer_url_vacancy)
            self.list_addr_metro.append(addr_metro)
            self.list_addr_street.append(addr_street)
            self.list_addr_build.append(addr_build)
            self.list_addr_lng.append(addr_lng)
            self.list_addr_lat.append(addr_lat)
            # pandas data dict
            self.dict_data_pandas = {
                'vac_name': self.list_vac_name,
                'vac_money_from': self.list_vac_money_from,
                'vac_money_to': self.list_vac_money_to,
                'vac_money_cur': self.list_vac_money_cur,
                'city': self.list_city,
                'employer_name': self.list_employer_name,
                'employer_url': self.list_employer_url,
                'employer_url_vacancy': self.list_employer_url_vacancy,
                'addr_metro': self.list_addr_metro,
                'addr_street': self.list_addr_street,
                'addr_build': self.list_addr_build,
                'addr_lng': self.list_addr_lng,
                'addr_lat': self.list_addr_lat,
            }

    # Узнаем количество найденных вакансий
    def req_get_count(self, headers, q, area, money, period):
        url = 'https://api.hh.ru/vacancies?text=%s&area=%s&salary=%s&period=%s&only_with_salary=true&per_page=0&page=0&type=open' % (
            self.q, self.area, self.money, self.period)
        r = requests.get(url, headers=headers)
        vac_dic = json.loads(r.text)
        vac_count = vac_dic['found']
        return vac_count

    # Проходим по списку вакансий
    def loop_pages(self, vac_count):
        pages_count = vac_count // 10   # целове число вакансий
        div_count = vac_count % 10      # остаток от деления
        
        if div_count > 0:
            pages_count = pages_count + 1
        
        for p in range(0, pages_count):
            # print p
            self.req_parse_page(p)

    # Ищем вакансии по запросу q
    def find_vacancy(self, q, period, money, file_rez):
        if q != '':
            self.q = q
        if period != '':
            self.period = period
        if money != '':
            self.money = money
        print("\n")
        print('#' * 30)
        print('#' * 11, 'SEARCH', '#' * 11)
        print('Search:', self.q)
        print('Days spend:', self.period)
        print('Money:', self.money)
        print('#'*30)

        vac_count = self.req_get_count(self.headers, self.q, self.area, self.money, self.period)

        print("[*] Number of vacancies = %d" % (vac_count))
        # ReqParseAllPages(headers, q, area, money, period, pages_count)
        print('Please wait...')
        self.loop_pages(vac_count)

        # выводим в виде красивой таблици
        # сохраняем в файл
        print('Save file:', file_rez)
        if file_rez != '':
            f = open(file_rez, 'w')
            for stroka in self.ar_vac:
                # print stroka
                stroka2 = ''
                for s in stroka:
                    if isinstance(s, str):
                        # print 'String', s
                        s2 = s.encode("utf8")
                        if stroka2 == '':
                            stroka2 = s2
                        else:
                            stroka2 = str(stroka2) + ";\t" + str(s2)
                    elif isinstance(s, int):
                        s2 = str(s)
                        s2 = s2.encode("utf8")
                        if stroka2 == '':
                            stroka2 = s2
                        else:
                            stroka2 = stroka2 + ";\t" + str(s2)
                f.write(str(stroka2) + '\n')
            f.close()

        # создание csv в pandas
        df = pd.DataFrame(self.dict_data_pandas)  # , columns = ['num', 'vac_name', 'vac_money_from', 'vac_money_to']
        # print df.head()
        # print df['vac_name']
        if file_rez != '':
            df.to_csv(file_rez + '.csv', sep=';', encoding='utf-8')

    # Получаем информацию о васании по id
    def VacancyInfo(self, vac_id):
        url = 'https://api.hh.ru/vacancies/%s' % vac_id
        r = requests.get(url, headers=self.headers)
        vac_dic = json.loads(r.text)
        # print type(vac_dic)
        # print "#"*30
        for key, val in vac_dic.iteritems():
            if key == 'employment':
                print('ТИП ЗАНЯТОСТИ-ID: ', val['id'])
                print('ТИП ЗАНЯТОСТИ: ', val['name'])
            elif key == 'area':
                print('URL: ', val['url'])
                print('ГОРОД: ', val['name'])
            elif key == 'employer':
                print('ЛОГО: ', val['logo_urls']['original'])
                print('НАЗВАНИЕ РАБОТОДАТЕЛЯ: ', val['name'])
            elif key == 'type':
                print('ТИП ВАКАНСИИ-ID', val['id'])
                print('ТИП ВАКАНСИИ', val['name'])
            elif key == 'description':
                print(val)
            elif key == 'building_type':
                print('ТИП ЗДАНИЯ-ID: ', val['id'])
                print('ТИП ЗДАНИЯ: ', val['name'])
            elif key == 'salary':
                print('ОТ: ', val['from'])
                print('ДО: ', val['to'])
                print('ВАЛЮТА: ', val['currency'])
            elif key == 'billing_type':
                print('БИЛИНГ-ID: ', val['id'])
                print('БИЛИНГ: ', val['name'])
            elif key == 'experience':
                print('ОПЫТ-ID', val['id'])
                print('ОПЫТ-ОПИСАНИЕ', val['name'])
            elif key == 'schedule':
                print('ГРАФИК-ID:', val['id'])
                print('ГРАФИК:', val['name'])
            else:
                print(key, val)


parser = argparse.ArgumentParser(description='Work search api:')
parser.add_argument('--request', '-r')
parser.add_argument('--money', '-m')
parser.add_argument('--period', '-p')
parser.add_argument('--vacancy', '-v')
parser.add_argument('--output', '-o')

args = parser.parse_args()
# print("Request: {}".format(args.request))
if str(args.request) != 'None':
    if (str(args.money) != 'None') and (str(args.period) != 'None'):
        hh = HhSearcher()
        if str(args.output) != 'None':
            file_rez = str(args.output)
            hh.find_vacancy(args.request, args.period, args.money, file_rez)
        else:
            hh.find_vacancy(args.request, args.period, args.money, '')
elif str(args.vacancy) != 'None':
    print('Vacancy: ', args.vacancy)
    hh = HhSearcher()
    hh.VacancyInfo(args.vacancy)

'''
python hh_search.py -r 'python' -m 50000 -p 10
'''
