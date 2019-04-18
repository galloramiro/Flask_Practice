from dataloader import db
from flask import render_template, request, Blueprint, flash
from dataloader.core.forms import DataLoaderForm
from dataloader.core.utils import dataToDb

core = Blueprint('core', __name__, template_folder='templates/core/')


@core.route('/', methods=['GET', 'POST'])
@core.route('/home', methods=['GET', 'POST'])
def home():

    form = DataLoaderForm()
    if form.validate_on_submit():
        dataToDb(form.gen_data.data)
        flash('The data has been upload', 'success')
        return render_template('home.html', form = form)

    return render_template('home.html', form = form)