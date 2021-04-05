from flask import Flask,render_template,request
import sqlite3 as sql
import base64

app = Flask(__name__)

username = 'admin'
password = 'password'


## Developed by xrwy
    
@app.route('/', methods = ['GET'])
def main():
    return render_template('main.html')

@app.route('/home', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/adminloginpanel', methods = ['GET'])
def adminLoginPanel():
    return render_template('adminLoginPanel.html')

@app.route('/adminpanel', methods = ['GET','POST'])
def adminPanel():
    if request.method == 'POST':
        user_name = request.form.get('u_se_rN_m')
        _password = request.form.get('p_4ssW0_r_xd')
        if user_name == username and password == _password:
            with sql.connect('data.db') as custo_db:
                cursor = custo_db.cursor()
                cursor.execute('SELECT * FROM customer_informations')
                data__ = cursor.fetchall()
                x = []
                z = []
                for value in data__:
                    t_p_leVal = value
                    for val_ in t_p_leVal:
                        valBytes = val_.encode('ascii')
                        b_se4_Val = base64.b64decode(valBytes) 
                        per_Val = b_se4_Val.decode('ascii')
                        x.append(per_Val)
                    z.append(x)
                    x = []
                return render_template('adminPanel.html', customer__ = z) 
        else:  
            return "INTRUSION ATTEMPT"
    else: 
        return render_template('adminLogin.html')
    
    

@app.route('/reservation', methods = ['GET','POST'])
def reservation():
    if request.method == 'POST':
        
        name = request.form.get('name_')
        nameBytes = name.encode('ascii')
        base64_bytes1 = base64.b64encode(nameBytes) 
        
        namePass = base64_bytes1.decode('ascii')
        
        
        surname = request.form.get('surname_')
        surnameBytes = surname.encode('ascii')
        base64_bytes2 = base64.b64encode(surnameBytes)
        
        surnamePass = base64_bytes2.decode('ascii')
        
        email = request.form.get('email_')
        emailBytes = email.encode('ascii')
        base64_bytes3 = base64.b64encode(emailBytes) 
        
        emailPass = base64_bytes3.decode('ascii')
        
        
        phone = request.form.get('phone_')
        phoneBytes = phone.encode('ascii')
        base64_bytes4 = base64.b64encode(phoneBytes) 
        
        phonePass = base64_bytes4.decode('ascii')
        
        adults = request.form.get('adults_')
        adultsBytes = adults.encode('ascii')
        base64_bytes5 = base64.b64encode(adultsBytes) 
        
        adultsPass = base64_bytes5.decode('ascii')
        
        children = request.form.get('children_')
        childrenBytes = children.encode('ascii')
        base64_bytes6 = base64.b64encode(childrenBytes) 
        
        childrenPass = base64_bytes6.decode('ascii')
        
        wifi = request.form.get('check_box_1')
        parking = request.form.get('check_box_2')
        breakfast = request.form.get('check_box_3')
        
        check_In = request.form.get('checkIn')
        checkInBytes = check_In.encode('ascii')
        base64_bytes7 = base64.b64encode(checkInBytes)
        
        check_InPass = base64_bytes7.decode('ascii')
        
        
        
        check_Out = request.form.get('checkOut')
        checkOutBytes = check_Out.encode('ascii')
        base64_bytes8 = base64.b64encode(checkOutBytes)
        
        check_OutPass = base64_bytes8.decode('ascii')
        
        

        if(wifi == "1"):
            wifi = "    "
            wifiBytes = wifi.encode('ascii')
            wifiBs4Bytes_ = base64.b64encode(wifiBytes)
            
            wifiPass = wifiBs4Bytes_ .decode('ascii')
        else:
            wifi = "False"
            wifiBytes = wifi.encode('ascii')
            wifiBs4Bytes_ = base64.b64encode(wifiBytes)
            
            wifiPass = wifiBs4Bytes_.decode('ascii')
            
        if(parking == "1"):
            parking = "True"
            parkingBytes = parking.encode('ascii')
            parkingBs4Bytes_ = base64.b64encode(parkingBytes)
            
            parkingPass = parkingBs4Bytes_.decode('ascii')
        else:
            parking = "False"
            parkingBytes = parking.encode('ascii')
            parkingBs4Bytes_ = base64.b64encode(parkingBytes)
            
            parkingPass = parkingBs4Bytes_.decode('ascii')
            
        if(breakfast == "1"):
            breakfast = "True"
            breakfastBytes = breakfast.encode('ascii')
            breakfastBs4Bytes_ = base64.b64encode(breakfastBytes)
            
            breakfastPass = breakfastBs4Bytes_.decode('ascii')
        else:
            breakfast = "False"
            breakfastBytes = breakfast.encode('ascii')
            
            breakfastBs4Bytes_ = base64.b64encode(breakfastBytes)
            
            breakfastPass = breakfastBs4Bytes_.decode('ascii')
                
                
                
        with sql.connect('data.db') as customer_db:
            cursor = customer_db.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS customer_informations (Name,Surname,Email,Phone,Adults,Children,Wifi,Parking,Breakfast,Check_In,Check_Out)')
            cursor.execute('INSERT INTO customer_informations (Name,Surname,Email,Phone,Adults,Children,Wifi,Parking,Breakfast,Check_In,Check_Out) VALUES(?,?,?,?,?,?,?,?,?,?,?)', [namePass,surnamePass,emailPass,phonePass,adultsPass,childrenPass,wifiPass,parkingPass,breakfastPass,check_InPass,check_OutPass])
            
            return render_template('successful.html')
        
        
        
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    


    





