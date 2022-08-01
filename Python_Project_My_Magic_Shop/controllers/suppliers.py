from flask import Flask ,render_template, request, redirect
from models.suppliers import Supplier
from models.products import Product
from flask import Blueprint
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all()
    return render_template ("/suppliers/index.html", all_suppliers=suppliers)

@suppliers_blueprint.route("/suppliers/<id>")
def show(id):
    supplier = supplier_repository.select(id)
    return render_template("/suppliers/show.html", supplier=supplier)

@suppliers_blueprint.route("/suppliers/<id>/edit", methods=["POST"])
def edit(id):
    supplier = supplier_repository.select(id)
    return render_template('/suppliers/edit.html', supplier=supplier)

@suppliers_blueprint.route('/suppliers/<id>', methods=['POST'])
def update(id):
    company_name = request.form['company_name']
    contact_name = request.form['contact_name']
    human = request.form['human']
    supplier = Supplier(company_name, contact_name, human, id)
    supplier_repository.update(supplier)
    return redirect('/suppliers/'+ id)

@suppliers_blueprint.route('/suppliers/new')
def new():
    return render_template('/suppliers/new.html')

@suppliers_blueprint.route('/suppliers', methods = ['POST'])
def create():
    company_name = request.form['company_name']
    contact_name = request.form['contact_name']
    human = request.form['human']
    supplier = Supplier(company_name, contact_name, human)
    supplier_repository.save(supplier)
    return redirect('/suppliers')