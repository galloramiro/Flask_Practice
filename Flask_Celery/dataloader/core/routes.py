from flask import render_template, request, Blueprint
from dataloader.core.forms import DataLoaderForm
from dataloader.core.utils import csvToDb

core = Blueprint('core', __name__, template_folder='templates/core/')


@core.route('/')
@core.route('/home')
def home():
    form = DataLoaderForm()
    if form.validate_on_submit():
        d = csvToDb(form.picture.data)
        print(d['gen'][1])
        """ 

        for x in len(d):
            df
        
        """
    return render_template('home.html', form = form)

