from itertools import product
from unicodedata import name
from flask import Flask, render_template, request, redirect
from models.products import Product
from models.suppliers import Supplier
from flask import Blueprint
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template ("/products/index.html", all_products=products)

@products_blueprint.route("/products/<id>")
def show(id):
    product = product_repository.select(id)
    return render_template("/products/show.html", product=product)

@products_blueprint.route("/products/<id>/edit", methods=["POST"])
def edit(id):
    product = product_repository.select(id)
    suppliers = supplier_repository.select_all()
    return render_template('/products/edit.html', product=product, all_suppliers=suppliers)

@products_blueprint.route('/products/<id>', methods=['POST'])
def update(id):
    name = request.form['name']
    stock_quantity = request.form['stock_quantity']
    buyer_cost = request.form['buyer_cost']
    resale_price = request.form['resale_price']
    description = request.form['description']
    supplier_id = request.form['supplier_id']
    supplier = supplier_repository.select(supplier_id)
    product = Product(name, description, stock_quantity, buyer_cost, resale_price, supplier, id)
    product_repository.update(product)
    return redirect('/products/'+ id)

@products_blueprint.route('/products/new')
def new():
    suppliers = supplier_repository.select_all()
    return render_template('/products/new.html', all_suppliers = suppliers)

@products_blueprint.route('/products', methods = ['POST'])
def create():
    name = request.form['name']
    stock_quantity = request.form['stock_quantity']
    buyer_cost = request.form['buyer_cost']
    resale_price = request.form['resale_price']
    description = request.form['description']
    supplier_id = request.form['supplier_id']
    supplier = supplier_repository.select(supplier_id)
    product = Product(name, description, stock_quantity, buyer_cost, resale_price, supplier)
    product_repository.save(product)
    return redirect('/products')

@products_blueprint.route('/products/<id>/delete', methods = ['POST'])
def delete(id):
    product_repository.delete(id)
    return redirect('/products')