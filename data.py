from flask import Flask
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt
import os
current_dir = os.getcwd()
src = current_dir
dest = os.path.join(current_dir, "static")


# SETTING UP APP AND DB
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoice.db'
db = SQLAlchemy(app)


# function to find the monthly totals QUIZ1
def monthly_totals():
    jan2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Jan2019 FROM invoices WHERE [*invoicedate] LIKE "%/1/2019"', con=db.engine).to_dict()["Jan2019"][0]

    feb2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Feb2019 FROM invoices WHERE [*invoicedate] LIKE "%/2/2019"', con=db.engine).to_dict()["Feb2019"][0]

    mar2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Mar2019 FROM invoices WHERE [*invoicedate] LIKE "%/3/2019"', con=db.engine).to_dict()["Mar2019"][0]

    apr2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Apr2019 FROM invoices WHERE [*invoicedate] LIKE "%/4/2019"', con=db.engine).to_dict()["Apr2019"][0]

    may2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS May2019 FROM invoices WHERE [*invoicedate] LIKE "%/5/2019"', con=db.engine).to_dict()["May2019"][0]

    jun2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Jun2019 FROM invoices WHERE [*invoicedate] LIKE "%/6/2019"', con=db.engine).to_dict()["Jun2019"][0]

    jul2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Jul2019 FROM invoices WHERE [*invoicedate] LIKE "%/7/2019"', con=db.engine).to_dict()["Jul2019"][0]

    aug2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Aug2019 FROM invoices WHERE [*invoicedate] LIKE "%/8/2019"', con=db.engine).to_dict()["Aug2019"][0]

    sep2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Sep2019 FROM invoices WHERE [*invoicedate] LIKE "%/9/2019"', con=db.engine).to_dict()["Sep2019"][0]

    oct2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Oct2019 FROM invoices WHERE [*invoicedate] LIKE "%/10/2019"', con=db.engine).to_dict()["Oct2019"][0]

    nov2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Nov2019 FROM invoices WHERE [*invoicedate] LIKE "%/11/2019"', con=db.engine).to_dict()["Nov2019"][0]

    dec2019 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Dec2019 FROM invoices WHERE [*invoicedate] LIKE "%/12/2019"', con=db.engine).to_dict()["Dec2019"][0]

    jan2020 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Jan2020 FROM invoices WHERE [*invoicedate] LIKE "%/1/2020"', con=db.engine).to_dict()["Jan2020"][0]

    feb2020 = pd.read_sql('SELECT SUM([*unitamount] * [*quantity]) AS Feb2020 FROM invoices WHERE [*invoicedate] LIKE "%/2/2020"', con=db.engine).to_dict()["Feb2020"][0]

    monthly = {
        "first": jan2019,
        "second": feb2019,
        "third": mar2019,
        "forth": apr2019,
        "fifth": may2019,
        "sixth": jun2019,
        "seventh": jul2019,
        "eighth": aug2019,
        "ninth": sep2019,
        "tenth": oct2019,
        "eleventh": nov2019,
        "twelveth": dec2019,
        "thirteenth": jan2020,
        "forteenth": feb2020 
    }
    return monthly


def top_customers():
    top2019 = pd.read_sql('SELECT [*contactname], [*quantity] * [*unitamount] AS amount FROM invoices WHERE [*invoicedate] LIKE "%2019" ORDER BY amount DESC LIMIT 5', con=db.engine).to_dict()["*ContactName"]

    top2020 = pd.read_sql('SELECT [*contactname], [*quantity] * [*unitamount] AS amount FROM invoices WHERE [*invoicedate] LIKE "%2020" ORDER BY amount DESC LIMIT 5', con=db.engine).to_dict()["*ContactName"]

    customers = {
        "one": top2019[0],
        "two": top2019[1],
        "three": top2019[2],
        "four": top2019[3],
        "five": top2019[4],
        "six": top2020[0],
        "seven": top2020[1],
        "eight": top2020[2],
        "nine": top2020[3],
        "ten": top2020[4]
    }
    return customers


def thirty_days():
    days30 = pd.read_sql('SELECT SUM([*quantity] * [*unitamount]) AS total, * FROM invoices WHERE [*InvoiceDate] BETWEEN "1/11/2019" AND "29/11/2019" GROUP BY [*InvoiceDate]', con=db.engine).to_dict()["total"]

    day0 = days30[0]
    day1 = days30[1] + day0
    day2 = days30[2] + day1
    day3 = days30[3] + day2
    day4 = days30[4] + day3
    day5 = days30[5] + day4
    day6 = days30[6] + day5
    day7 = days30[7] + day6

    barC = pd.read_sql('SELECT [*contactname], [*quantity] * [*unitamount] AS amount FROM invoices ORDER BY amount DESC LIMIT 5', con=db.engine).to_dict()["*ContactName"]

    barA = pd.read_sql('SELECT [*contactname], [*quantity] * [*unitamount] AS amount FROM invoices ORDER BY amount DESC LIMIT 5', con=db.engine).to_dict()["amount"]

    y0 = barC[0]
    y1 = barC[1]
    y2 = barC[2]
    y3 = barC[3]
    y4 = barC[4]

    x0 = barA[0]
    x1 = barA[1]
    x2 = barA[2]
    x3 = barA[3]
    x4 = barA[4]

    plt.style.use("seaborn")
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle("GRAPHICAL PRESENTATIONS")
    ax1.plot(["Nov7","Nov10","Nov14","Nov15","Nov19","Nov20","Nov24","Nov29"],[day0,day1,day2,day3,day4,day5,day6,day7])

    ax2.barh([y4,y3,y2,y1,y0], [x4,x3,x2,x1,x0], height=.8, color="blue")

    plt.savefig('graph.png')

    if not os.path.isfile(dest + '/graph.png'):
        os.rename(src + "/graph.png", dest + "/graph.png")
    return


def general_top_five():
    top5 = pd.read_sql('SELECT [*contactname] FROM invoices  ORDER BY [*quantity] DESC LIMIT 5', con=db.engine).to_dict()["*ContactName"]

    oneQ = top5[0]
    twoQ = top5[1]
    threeQ = top5[2]
    fourQ = top5[3]
    fiveQ = top5[4]

    general = {
        "one": oneQ,
        "two": twoQ,
        "three": threeQ,
        "four": fourQ,
        "five": fiveQ,
    }
    return general