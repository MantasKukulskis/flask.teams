from flask import render_template, request, redirect, url_for

from src import app, db
from src.forms import ContactForm

from src.models import Vyras



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/ladies')
def ladies():
    return render_template('ladies.html')


@app.route('/men')
def men():
    vyrai = Vyras.query.all()
    return render_template('men.html', vyrai=vyrai)


# @app.route('/add_mens', methods=['GET', 'POST'])
# def add_mens():
#     if request.method == "POST":
#         print(request.form)
#         vardas = request.form['vardas']
#         amzius = request.form['amzius']
#         ugis = request.form['ugis']
#         svoris = request.form['svoris']
#         vyrai[vardas] = {
#                 'amzius': amzius,
#                 'ugis': ugis,
#                 'svoris': svoris,
#             }
#         return redirect(url_for('men'))
#     return render_template('add_mens.html')



@app.route('/men/<int:id>', methods=['GET', 'POST'])
def vardas(id):
    vardas = Vyras.query.get(id)
    if request.method == "POST":

        return redirect(url_for('delete_man',id=id))
    return render_template('vardas.html', vardas=vardas)



@ app.route('/add_mens', methods=['GET', 'POST'])
def add_mens():
    form = ContactForm()
    if form.validate_on_submit():
        # vyrai[form.vardas.data] = {
        #                 'amzius': form.amzius.data,
        #                 'ugis': form.ugis.data,
        #                 'svoris': form.svoris.data,
        #             }
        vyras = Vyras(vardas=form.vardas.data, team=form.team.data, amzius=form.amzius.data, ugis=form.ugis.data,
        svoris=form.svoris.data)
        db.session.add(vyras)
        db.session.commit()
        return redirect(url_for('men'))
    return render_template('contact_us.html', form=form)

@app.route('/men/<int:id>/delete', methods=['GET', 'POST'])
def delete_man(id):
    vardas = Vyras.query.get(id)
    if request.method == "POST":
         db.session.delete(vardas)
         db.session.commit()
         return redirect(url_for('men'))
    return render_template('delete.html', vardas=vardas)

@app.route('/men/<int:id>/update', methods=['GET', 'POST'])
def update_name(id):
    form = ContactForm()
    vardas = Vyras.query.get(id)
    if request.method == "POST":
        vardas.vardas = form.vardas.data
        db.session.add(vardas)
        db.session.commit()

        return redirect(url_for('men'))
    return render_template('update.html', vardas=vardas, form=form)

