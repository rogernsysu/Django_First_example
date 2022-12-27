from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import os
import json
from sklearn.linear_model import LinearRegression

def index(request):
    return HttpResponse("Hello, world. Django is too difficult.")
# Create your views here.

def dataframe(request):
    os.chdir(f'C:/Users/roger/Desktop/Study/PATHLOSS_DISTANCE/Salt')
    template = pd.read_csv('NT_PATHLOSS_9104.csv')
    template = template.rename(columns={'-115':'Pathloss_Distance','-120':'Pathloss_Distance_120','-125':'Pathloss_Distance_125','-130':'Pathloss_Distance_130','-135':'Pathloss_Distance_135','-140':'Pathloss_Distance_140'})
    json_records = template.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'table.html', context)