from flask import Flask, render_template, request, redirect
from models.products import Product
from models.suppliers import Supplier
from flask import Blueprint
import repositories.product_repository as product_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template ("products/index.html", all_products=products)

