'''
This file is used to define the functionalities of Traffic API
@author: Anirudh Nagulapalli, Kavya Reddy Vemula
'''

import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import PIL
from PIL import Image
import subprocess
from subprocess import call
import PyPDF2
import webbrowser



def output_graph(hour_of_the_day):
    """
    Gives out a graph of how much traffic can be estimated
    This can only be done by the logged in user.
    :param hour_of_the_day: The graph that needs to be fetched for the respective hour of travel. 
    :type hour_of_the_day: str

    :rtype: None
    """
    if hour_of_the_day == "0":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_1.png').show()
    elif hour_of_the_day == "1":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_2.png').show()
    elif hour_of_the_day == "2":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_3.png').show()
    elif hour_of_the_day == "3":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_4.png').show()
    elif hour_of_the_day == "4":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_5.png').show()
    elif hour_of_the_day == "5":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_6.png').show()
    elif hour_of_the_day == "6":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_7.png').show()
    elif hour_of_the_day == "7":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_8.png').show()
    elif hour_of_the_day == "8":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_9.png').show()
    elif hour_of_the_day == "9":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_10.png').show()
    elif hour_of_the_day == "10":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_11.png').show()
    elif hour_of_the_day == "11":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_12.png').show()
    elif hour_of_the_day == "12":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_13.png').show()
    elif hour_of_the_day == "13":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_14.png').show()
    elif hour_of_the_day == "14":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_15.png').show()
    elif hour_of_the_day == "15":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_16.png').show()
    elif hour_of_the_day == "16":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_17.png').show()
    elif hour_of_the_day == "17":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_18.png').show()
    elif hour_of_the_day == "18":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_19.png').show()
    elif hour_of_the_day == "19":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_20.png').show()
    elif hour_of_the_day == "20":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_21.png').show()
    elif hour_of_the_day == "21":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_22.png').show()
    elif hour_of_the_day == "22":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_23.png').show()
    elif hour_of_the_day == "23":
        Image.open('/Users/Anirudh/4th Semester/Outputs/figure_24.png').show()
    return 'FlyingSaucers view for the required hour'


def predict_time(Choice):
    """
    Analysis of the model
    Enter 1 for the predicted values or 2 for the information about the model.
    :param Choice: Accept input from user
    :type Choice: dict | bytes

    :rtype: None
    """
    #Sets the default browser as Safari
    browser = webbrowser.get('safari')
    
    if Choice == "1":
        #Outputs the SPSS exported values in Safari
        browser.open_new('file:///Users/Anirudh/4th%20Semester/Outputs/tableWithPredictions.txt')
        
    elif Choice == "2":
        browser.open_new('file:///Users/Anirudh/4th%20Semester/Outputs/Prediction.pdf')

    return 'Results displayed!!'
