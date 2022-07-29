from flask import Flask ,render_template, request, redirect
from repositories import product_repository, supplier_repository
from models.suppliers import Supplier
from models.products import Product
from flask import Blueprint

suppliers_blueprint = Blueprint("suppliers", __name__)
 