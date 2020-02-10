# IMPORTING FLASK AND ALL DEPENDENCIES OF THE APPLICATION
from flask import Flask, render_template, request
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from data import monthly_totals, top_customers, thirty_days, general_top_five

# SETTING UP APP AND DB
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///invoice.db'
db = SQLAlchemy(app)


# ROUTES AND ENDPOINTS
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data', methods=["POST"])
def transform_view():
    if request.method == 'POST':
        f = request.files['data_file']
        df = pd.read_csv(f, parse_dates=True, usecols=[0, 10, 12, 13, 16, 17, 18], encoding='UTF-16 LE')
        df.to_sql('invoices', con=db.engine, index=False, index_label='id', if_exists='replace')
        return render_template('data.html', monthly_totals=monthly_totals(), customers=top_customers(), general=general_top_five())
    return 'Oops, Try again something went wrong!'


if __name__ == '__main__':
    app.run(debug=True)