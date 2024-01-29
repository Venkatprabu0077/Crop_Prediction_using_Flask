from flask import Flask, redirect, url_for, request, render_template
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
app = Flask(__name__)

@app.route('/success/<m1>/<m2>/<m3>/<m4>/<m5>/<m6>/<m7>')
def success(m1,m2,m3,m4,m5,m6,m7):
    DS=pd.read_csv(r'C:\Users\Ashok Kumar\Desktop\crop prediction project\Crop-prediction-project-main\Crop-prediction-project-main\crop.csv')
    v=DS['label']
    g=[]
    for t in v:
        if t not in g:
            g.append(t)
    for i in range(0,22):
        for j in range(1):
            DS=DS.replace(g[i],i)
    x=DS.drop(['label'],axis=1)
    y=DS['label']   
    x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.70,random_state=0)
    DT = DecisionTreeClassifier()
    DT.fit(x_train,y_train)
    y_pred2 = DT.predict([[m1,m2,m3,m4,m5,m6,m7]]) 
    value=g[y_pred2[0]]
    k=["https://assets.thehansindia.com/h-upload/feeds/2019/07/13/195638-paddy-crop.jpg","https://seed2plant.in/cdn/shop/products/maizeseeds_800x.jpg?v=1604034397","https://i0.wp.com/post.medicalnewstoday.com/wp-content/uploads/sites/3/2022/04/chickpeas_closeup_1296x728_header-1024x575.jpg?w=1155&h=1528","https://i0.wp.com/images-prod.healthline.com/hlcmsresource/images/AN_images/kidney-beans-1296x728-feature.jpg?w=1155&h=1528","https://thumbs.dreamstime.com/b/lot-pigeon-pea-background-uses-30186612.jpg","https://tiimg.tistatic.com/fp/1/006/986/dried-moth-bean-817.jpg","https://www.wellandgood.com/wp-content/uploads/2014/11/Stocksy-Mung-Bean-Julie-Rideout.jpg","https://4.imimg.com/data4/HG/FS/MY-23833905/black-gram-seeds-500x500.jpeg","https://www.wikihow.com/images/thumb/e/ec/Make-Lentils-Step-1-Version-2.jpg/v4-460px-Make-Lentils-Step-1-Version-2.jpg","https://images.healthshots.com/healthshots/en/uploads/2021/09/27184641/pomegranate-1600x900.jpg","https://www.daysoftheyear.com/cdn-cgi/image/dpr=1%2Cf=auto%2Cfit=cover%2Cheight=650%2Cq=70%2Csharpen=1%2Cwidth=956/wp-content/uploads/banana-day1-scaled.jpg","https://www.netmeds.com/images/cms/wysiwyg/blog/2019/04/Raw_Mango_898.jpg","https://assets.epicurious.com/photos/55e4c39fcf90d6663f727a74/16:9/w_4592,h_2583,c_limit/shutterstock_209917372.jpg","https://www.syngenta.co.in/sites/g/files/kgtney376/files/styles/syngenta_large_4_3/public/media/image/2022/05/27/watermelon-landing-page-banner.jpg?itok=H3wLGfaj","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrutPoPYxvVNXh1R6p4l8EN3mH9IpMNHDarw&usqp=CAU","https://cdn.britannica.com/22/187222-050-07B17FB6/apples-on-a-tree-branch.jpg","https://cdn.britannica.com/24/174524-050-A851D3F2/Oranges.jpg","https://t4.ftcdn.net/jpg/05/41/44/55/360_F_541445577_1i2kIGN20SH2Jy9gkkuIfPO2yWsOXNEQ.jpg","https://cdn.xxl.thumbs.canstockphoto.com/coconut-tree-stock-images_csp8060765.jpg","https://cdn.shopify.com/s/files/1/2694/3724/articles/Blog_Title_3_ba3adee4-747e-4de0-81a1-d0f08931f119_600x.jpg?v=1630947563","https://thumbs.dreamstime.com/z/jute-plant-field-cultivation-assam-india-green-tall-plants-leaves-agricultural-crops-agriculture-asia-asian-background-154951730.jpg","https://i0.wp.com/post.medicalnewstoday.com/wp-content/uploads/sites/3/2022/04/can_coffee_cause_cancer_1296x728_header-1024x575.jpg?w=1155&h=1528"]
    g=k[y_pred2[0]]
    return render_template("index.html",value=value,g=g)

@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      v1= int(request.form['n1'])
      v2= int( request.form['n2'])
      v3= int(request.form['n3'])
      v4= int(request.form['n4'])
      v5= int(request.form['n5'])
      v6= int(request.form['n6'])
      v7= int(request.form['n7'])
      return redirect(url_for('success',m1=v1,m2=v2,m3=v3,m4=v4,m5=v5,m6=v6,m7=v7))
  

if __name__ == '__main__':
   app.run(debug = True)
