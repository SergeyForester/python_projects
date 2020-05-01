# coding:utf-8
import datetime

import numpy
from django.conf import settings


def convert_filters():
    prod_filters = settings.PRODUCT_FILTERS
    res = {k: [[el for el in prod_filters[k][0]], []] for k in prod_filters.keys()}
    print(res)

    for k, v in prod_filters.items():
        data = prod_filters[k][1]
        for el in data:
            el = el.split(",")
            temp = []

            for length in el:
                if '-' in length:
                    mn, mx = length.split('-')
                    for n in numpy.arange(float(mn), float(mx), 0.1):
                        temp.append(round(n, 1))
                else:
                    temp.append(float(length))

            res[k][1].append(temp)

    return res
