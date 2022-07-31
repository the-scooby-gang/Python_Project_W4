from flask import Flask, render_template, request, redirect
from repositories import product_repository, supplier_repository
from models.products import Product
from models.suppliers import Supplier
from flask import Blueprint

products_blueprint = Blueprint("products", __name__)


