from flask import Flask, render_template, request, redirect,flash,url_for,session
from wtforms import Form, FloatField, validators
from forms import stockInput, goBack
from stockTicker import stockTicker, mmdict,stockExists
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import BoxSelectTool, BoxZoomTool,ResetTool,WheelZoomTool,LassoSelectTool
import pandas as pd 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e256803842b0ac38c491bc4ff193e809587b1ef2b6915b9cd746b46b8978883a'

@app.route('/', methods = ['GET','POST'])
def index():
    form = stockInput()
    if form.validate_on_submit():
        flash(f'Fetching data for {form.symbol.data}!','success')
        session['symbol']=form.symbol.data
        session['month']=mmdict(form.month.data)
        session['year']=form.year.data
        return redirect(url_for('figure'))
    return render_template("index.html",form=form)

@app.route('/figure',methods = ['GET','POST'])
def figure():
    from bokeh.plotting import figure, output_file, show
    back = goBack()
    d = stockTicker(session['symbol'],session['month'],session['year'])
    stock = session['symbol']
    stock = stock.upper()
    month = session['month']
    year = session['year']
    if month != '12':
        next_month = str(int(month)+1)
        next_year = year
    else:
        next_month = '01'
        next_year = str(int(year)+1)
    ymin = min(d.set_index(d['date'])[month+'-'+year:month+'-'+year]['close'])
    ymin = ymin-(ymin*.025)
    ymax = max(d.set_index(d['date'])[month+'-'+year:month+'-'+year]['close'])
    ymax = ymax+(ymax*.025)
    p = figure(plot_width=600, plot_height=400,x_axis_type='datetime',title='Closing price of {} for {}/{}'.
        format(stock,session['month'],session['year']),
        x_range = (pd.to_datetime(year+'-'+month+'-'+'01',format='%Y-%m-%d'),
            pd.to_datetime(next_year+'-'+next_month+'-'+'01',format='%Y-%m-%d')),
        y_range = (ymin,ymax))
    p.line(d['date'], d['close'], line_width=2)
    p.xaxis.axis_label = "Date"
    p.yaxis.axis_label = "Closing Price (USD)"
    script,div = components(p)
    if back.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('figure.html', script=script, div=div,form=back)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)