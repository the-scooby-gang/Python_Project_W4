#REMEMBER TO LOOK AT OLD NOTES ( Week4 Day3 Full_Task...blah blah is a great example and where you took all your notes)
#Controllers = 
    #Products
        #COMPLETE! HomeRoute - (link to base html)(and show home page with nav links)
        #COMPLETE! ProductsRoute = (link to index html)(and show list of products with manufacturer highlighted and product highlighted)
        #New_ProductRoute = (GET)(link to new html)(and allows us to get to the new form to add a new product)
        #ProductsRoute = (POST) (allow us to submit the details on the form, add the product to the list and then redirect to the Products tab)
        #Products<id>Route = (GET) (link to show html)(allows us to show a single product (contains full class details))
        #PRoducts<id>EditRoute = (GET) (link to edit html)(takes us to the form to edit a product)
        #Products<id>Route = (POST) (allows us to update the product and then return the new edited product)
        #Products<id>DeleteRoute = (POST) = Makes the delete button work
    #Suppliers
        #New_SuppliersRoute = (GET)(link to new html)(and allows us to get to the new form to add a new Supplier)
        #SuppliersRoute = (POST) (allow us to submit the details on the form, add a new supplier to the list and then redirect to the Supppliers tab)
        #Suppliers<id>Route = (GET) (link to show html)(allows us to show a single supplier (contains full class details))
        #Suppliers<id>EditRoute = (GET) (links to edit html)(takes us to the form to edit a supplier)
        #Suppliers<id>Route = (POST) (allows us to update the supplier and then return the new edited supplier)

#CSS - Read Notoes (Don't worry about this too much, we can tinker towards the end)

#COMPLETE:
#DB - Magic Shop contains 1 manufacturer to many products... I.E William the bloody, ring of Armarah, NB Hair gel
    #DROP TABLE IF EXISTS Products
    #DROP TABLE IF EXISTS Suppliers
    #Manufacturers = Company name, Contact name, Human (Boolean)
    #Products = name, description, stock quantity, buying cost, selling price

#COMPLETE
#Models - Suppliers and Products classes
    #See DB notes, remember to pass in self
    #Products needs an if/else for low/out of stock - ask instructors about this

#Repositories
    #Products
        #Save - Complete
        #Select_all - Complete
        #Select (one) (IF) - Complete
        #Delete_all - Complete
        #Delete(one) - Complete
        #Update_Product
    #Suppliers
        #Save - Complete
        #Select_all - Complete
        #Select(one) (IF) - Complete
        #Delete_all - Complete
        #Delete(one) - Complete
        #Update_Supplier
        #add_product_to_Supplier

#Templates (look at tables for ease of styling)
    # Base
    # Index
        #Products
            #edit
            #index
                #Add the if statement for quantity levels (low or no stock here)
            #new
            #show
        #Supplier
            #edit
            #index
            #new
            #show

#COMPLETE:
# #Flask =    FLASK_APP=app.py
#             FLASK_ENV=development
#             FLASK_RUN_HOST=127.0.0.1
#             FLASK_RUN_PORT=4999

#COMPLETE
#App = 
        # from flask import Flask, render_template
        # from controllers.tasks_controller import products_blueprint 
        # app = Flask(__name__)
        # app.register_blueprint(products_blueprint) 
        # @app.route('/')
        # def home():
        #     return render_template('index.html')
        # if __name__ == '__main__':
        #     app.run(debug=True)

#COMPLETE
#Console
    #Delete_All
    #Insert DB info:
    #product1 = Product('blah blah', 'blah blah')
    #Save to Product Repository and same for Supplier
    #Supplier1 = Supplier('blah' , 'blah', 'blah')



