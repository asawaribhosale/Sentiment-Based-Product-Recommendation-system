from flask import Flask,render_template,request
import model as mymodel
import pdb

app = Flask(__name__, template_folder='templates')


@app.route('/',methods = ['POST','GET'])
def home():
    product_name_list=[]
    #pdb.set_trace()
    if request.method == 'POST':
        username = request.form['Name']
        product_name_list=mymodel.get_recommendations(username)
        
    return render_template('index.html',product_name_list = product_name_list)


if __name__ == "__main__":
    app.run()

