from time import strftime


from flask import Flask, render_template, request, redirect, session,jsonify
from DBConnection import Db

app = Flask(__name__)
app.secret_key="hi"

staticpath="C:\\Users\\91918\\PycharmProjects\\OMR\\static\\"

@app.route('/')
def login():
    return render_template("Admin/login.html")

@app.route('/mailcheck')
def mailcheck():
    username=request.args.get('cc')
    qry="select * from login where username='"+username+"'"
    db=Db()
    res=db.selectOne(qry)
    if res is not None:
        return jsonify(status="no")
    else:
        return jsonify(status="yes")

@app.route('/logout')
def logout():
    session ['lid']=''
    return redirect("/")

@app.route('/a')
def a():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        return render_template("admin/a.html")

@app.route('/loginpost',methods=['post'])
def loginpost():
        username=request.form['username']
        password=request.form['password']
        db=Db()
        qry="select * from login WHERE username='"+username+"'and password='"+password+"'"
        res=db.selectOne(qry)
        if res is None:
            return '''<script>alert("incorrect password or username");window.location="/"</script>'''
        elif res['type']=='admin':
            session['lid']=res['lid']
            return redirect('/a')
        elif res['type']=='staff':
            session['lid']=res['lid']
            return redirect('/b')

        else:
            return '''<script>alert("Incorrect password or username");window.location="/"</script>'''





@app.route('/admin_add_winners')
def admin_add_winners():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        return render_template("Admin/add winners.html")

@app.route('/addwinnerpost',methods=['post'])
def addwinnerpost():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        name=request.form['winnername']
        photo= request.files['winnerphoto']
        details= request.form['winnerdet']
        dateofpass=request.form['winnerpass']
        s=strftime("%y%m%d-%H%M%S")+".jpg"
        photo.save(staticpath+"winner\\"+photo.filename)
        path="/static/winner/"+photo.filename

        db=Db()
        qry="INSERT INTO winner (`name`,photo,details,date_of_passout) VALUES('"+name+"','"+path+"','"+details+"','"+dateofpass+"')"
        db.insert(qry)
        return '''<script>alert('Added successfully...');window.location='/admin_add_winners#about'</script>'''

@app.route('/editwinner/<id>')
def editwinner(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db = Db()
        qry = "select * from winner where winner_id='"+id+"'"
        res = db.selectOne(qry)
        return render_template("Admin/editwinner.html", data=res)

@app.route('/editwinnerpost',methods=['post'])
def editwinnerpost():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        idr=request.form['id']
        name=request.form['winnername']
        details= request.form['winnerdet']
        dateofpass=request.form['winnerpass']
        db=Db()
        if 'winnerphoto' in request.files:
            photo = request.files['winnerphoto']
            if photo.filename!="":
                s = strftime("%y%m%d-%H%M%S") + ".jpg"
                photo.save(staticpath + "winner\\" + photo.filename)
                path = "/static/winner/" + photo.filename
                qry = "update winner set name='" + name + "',details='" + details + "',date_of_passout='" + dateofpass + "',photo='" + path + "' where winner_id='" + idr + "'"
                db.update(qry)
                return redirect('/admin_view_winners')
            else:
                qry = "update winner set name='" + name + "',details='" + details + "',date_of_passout='" + dateofpass + "' where winner_id='" + idr + "'"
                db.update(qry)
                return redirect('/admin_view_winners')
        else:
            qry = "update winner set name='" + name + "',details='" + details + "',date_of_passout='" + dateofpass + "' where winner_id='" + idr + "'"
            db.update(qry)
            return redirect('/admin_view_winners')



@app.route('/admin_add_staff')
def admin_add_staff():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        return render_template("Admin/Admin(add staff).html")

@app.route('/staffpost',methods=['post'])
def staffpost():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        name=request.form['staffname']
        gender=request.form['RadioGroup1']
        place= request.form['staffplace']
        post= request.form['staffpost']
        disttrict= request.form['staffdist']
        e_mail= request.form['staffmail']
        phone= request.form['staffphone']
        photo= request.files['staffphoto']
        qualification= request.form['staffqua']
        s = strftime("%Y%m%d-%H%M%S") + ".jpg"
        photo.save(staticpath + "staff\\" + s)
        path = "/static/staff/" + s
        qry="insert into login(username,password,type)VALUES ('"+e_mail+"','"+phone+"','staff')"
        db=Db()
        res=db.insert(qry)
        qry1="INSERT INTO staff (staff_lid,`name`,gender,place,post,district,email,phone,photo,qualification) VALUES ('"+str(res)+"','"+name+"','"+gender+"','"+place+"','"+post+"','"+disttrict+"','"+e_mail+"','"+phone+"','"+path+"','"+qualification+"')"
        res1=db.insert(qry1)

        return '''<script>alert('Added successfully...');window.location='/admin_add_staff'</script>'''

@app.route('/deletestaff/<id>')
def deletestaff(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="delete from staff where staff_id='"+id+"'"
        res=db.delete(qry)
        return redirect('/admin_view_staff')

@app.route('/editstaff/<id>')
def editstaff(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db = Db()
        qry = "select * from staff where staff_id='"+id+"'"
        res = db.selectOne(qry)
        return render_template("Admin/editstaff.html", data=res)

@app.route('/editstaff_post',methods=['post'])
def editstaff_post():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        idr=request.form['id']
        name = request.form['staffname']
        gender = request.form['RadioGroup1']
        place = request.form['staffplace']
        post = request.form['staffpost']
        disttrict = request.form['staffdist']
        e_mail = request.form['staffmail']
        phone = request.form['staffphone']
        db=Db()
        qualification = request.form['staffqua']
        if 'staffphoto' in request.files:
            photo = request.files['staffphoto']
            s = strftime("%Y%m%d-%H%M%S") + ".jpg"
            photo.save(staticpath + "staff\\" + s)
            path = "/static/staff/" + s
            if photo.filename != "":
                qry="update staff set name='"+name+"',gender='"+gender+"',place='"+place+"',post='"+post+"',district='"+disttrict+"',email='"+e_mail+"',phone='"+phone+"',photo='"+path+"',qualification='"+qualification+"' where staff_id='"+idr+"'"
                res=db.update(qry)
                return redirect('/admin_view_staff')
            else:
                qry = "update staff set name='" + name + "',gender='" + gender + "',place='" + place + "',post='" + post + "',district='" + disttrict + "',email='" + e_mail + "',phone='" + phone + "',qualification='" + qualification + "' where staff_id='" + idr + "'"
                res = db.update(qry)
                return redirect('/admin_view_staff')
        else:
            qry = "update staff set name='" + name + "',gender='" + gender + "',place='" + place + "',post='" + post + "',district='" + disttrict + "',email='" + e_mail + "',phone='" + phone + "',qualification='" + qualification + "' where staff_id='" + idr + "'"
            res = db.update(qry)
            return redirect('/admin_view_staff')


@app.route('/admin_add_career')
def admin_add_career():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        return render_template("Admin/career.html")



@app.route ('/admincareer',methods=['post'])
def admincareer():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        career=request.form['admincareer']
        description=request.form['admindesc']

        db=Db()
        qry="insert into career(career, description, `date`, `time`)VALUES ('"+career+"','"+description+"',curdate(),curtime())"
        db.insert(qry)
        return '''<script>alert('Added successfully...');window.location='/admin_add_career'</script>'''
@app.route('/admin_view_complaint')
def admin_view_complaint():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry = "SELECT *,date_format(date,'%d-%m-%Y') as dt FROM complaint INNER JOIN student ON student.student_lid=complaint.student_lid"
        res = db.select(qry)
        return render_template("Admin/complaint.html",data=res)


@app.route('/admin_view_feedback')
def admin_view_feedback():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db = Db()
        qry = "SELECT feedback.*,date_format(date,'%d-%m-%Y') as date,`student`.`name` FROM feedback JOIN student ON `feedback`.`feedback_lid`=`student`.`student_lid`"
        res = db.select(qry)
        return render_template("Admin/feedback.html",data=res)


@app.route('/admin_complaint_reply/<id>')
def admin_complaint_reply(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="select * from complaint WHERE complaint_id='"+id+"'"
        res=db.selectOne(qry)
        return render_template("Admin/reply.html",data=res)

@app.route('/admin_search_complaint',methods=['post'])
def admin_search_complaint():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        dt1=request.form['dt1']
        dt2=request.form['dt2']
        db=Db()
        qry="SELECT *,date_format(date,'%d-%m-%Y') as dt FROM complaint INNER JOIN student ON student.student_lid=complaint.student_lid where date BETWEEN '"+dt1+"' and '"+dt2+"'"
        res=db.select(qry)
        return render_template("Admin/complaint.html",data=res)

@app.route('/admincomplaintreply',methods=['post'])
def admincomplaintreply():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        idr=request.form['id']
        reply=request.form['reply']
        db=Db()
        qry = "update complaint set reply='" + reply + "',status='done' where complaint_id='" + idr + "'"
        db.update(qry)
        return redirect('/admin_view_complaint')


@app.route('/admin_send_notification')
def admin_send_notification():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        return render_template("Admin/send notification.html")


@app.route ('/adminnotification',methods=['post'])
def adminnotification():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        notification=request.form['notification']
        db=Db()
        qry="insert into notification(`from_lid`,notification,`date`)VALUES ('"+str(session['lid'])+"','"+notification+"',curdate())"
        db.insert(qry)
        return '''<script>alert('Send successfully...');window.location='/admin_send_notification#about'</script>'''


@app.route('/admin_view_career')
def admin_view_career():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="select * from career"
        res=db.select(qry)
        return render_template("Admin/view career.html",data=res)

@app.route('/admin_search_career',methods=['post'])
def admin_search_career():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        search=request.form['search']
        db=Db()
        qry="select * from career where career like '%"+search+"%'"
        res=db.select(qry)
        return render_template("Admin/view career.html",data=res)



@app.route('/deletecareer/<id>')
def deletecareer(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="delete from career where career_id='"+id+"'"
        res=db.delete(qry)
        return redirect('/admin_view_career')


@app.route('/editcareer/<id>')
def editcareer(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db = Db()
        qry = "select * from career where career_id='"+id+"'"
        res = db.selectOne(qry)
        return render_template("Admin/editcareer.html", data=res)


@app.route ('/editcareer_post',methods=['post'])
def editcareer_post():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        idr=request.form['id']
        career=request.form['admincareer']
        description=request.form['admindesc']
        date=request.form['careerdate']
        time=request.form['careertime']

        db=Db()
        qry="update career set career='"+career+"',description='"+description+"',date='"+date+"',time='"+time+"' where career_id='"+idr+"'"
        db.update(qry)
        return redirect('/admin_view_career')


@app.route('/admin_view_result')
def admin_view_result():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="SELECT `student`.`name`,`result`.*  FROM result JOIN student ON student.student_lid=result.student_id"
        res=db.select(qry)
        return render_template("Admin/view exam result.html",data=res)

@app.route('/admin_search_result',methods=['post'])
def admin_search_result():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        search=request.form['search']
        db=Db()
        qry="SELECT `student`.`name`,`result`.*  FROM result JOIN student ON student.student_lid=result.student_id where student.name like '%"+search+"%'"
        res=db.select(qry)
        return render_template("Admin/view exam result.html",data=res)


@app.route('/admin_view_notification')
def admin_view_notification():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db = Db()
        qry = "SELECT * FROM notification"
        res = db.select(qry)
        return render_template("Admin/view notification.html", data=res)
@app.route('/deletenotification/<id>')
def deletenotification(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="delete from notification where notification_id='"+id+"'"
        res=db.delete(qry)
        return redirect('/admin_view_notification')

@app.route('/admin_view_staff')
def admin_view_staff():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="select * from staff"
        res=db.select(qry)
        return render_template("Admin/view staff.html",data=res)

@app.route('/admin_search_staff',methods=['post'])
def admin_search_staff():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        search=request.form['search']
        db=Db()
        qry="select * from staff where name like '%"+search+"%'"
        res=db.select(qry)
        return render_template("Admin/view staff.html",data=res)


@app.route('/admin_view_student')
def admin_view_student():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="select * from student"
        res=db.select(qry)
        return render_template("Admin/view student.html",data=res)

@app.route('/admin_search_student',methods=['post'])
def admin_search_student():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        search=request.form['search']
        db=Db()
        qry="select * from student where name like '%"+search+"%'"
        res=db.select(qry)
        return render_template("Admin/view student.html",data=res)

@app.route('/admin_view_winners')
def admin_view_winners():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="SELECT * FROM winner"
        res=db.select(qry)
        return render_template("Admin/view winner.html",data=res)

@app.route('/admin_search_winner',methods=['post'])
def admin_search_winner():
    if session['lid'] == '':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        search=request.form['search']
        db=Db()
        qry="select * from winner where name like '%"+search+"%'"
        res=db.select(qry)
        return render_template("Admin/view winner.html",data=res)


@app.route('/deletewinner/<id>')
def deletewinner(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="delete from winner where winner_id='"+id+"'"
        res=db.delete(qry)
        return redirect('/admin_view_winners')
@app.route('/admin_home')
def admin_home():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        return render_template("Admin/home.html")





# ----------------------------------------------------------------------------------------------------------------------------------------------------------staff
@app.route('/staff_add_exam')
def staff_add_exam():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        qry="SELECT * FROM `exam`"
        db=Db()
        res=db.select(qry)
        return render_template("staff/exam.html",val=res)


@app.route('/deleteexam/<id>')
def deleteexam(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="delete from exam where exam_id='"+id+"'"
        res=db.delete(qry)
        return redirect('/staff_add_exam')


@app.route('/staff_add_materials')
def staff_add_materials():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        return render_template("staff/addmaterials.html")

@app.route('/addmaterialpost',methods=['post'])
def addmaterialpost():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        name=request.form['materialname']
        doc=request.files['material']
        s = strftime("%Y%m%d-%H%M%S") + ".pdf"
        doc.save(staticpath + "material\\" +doc.filename)
        path = "/static/material/" +doc.filename
        db=Db()
        qry="insert into material (name,material,date,staff_id) VALUES ('"+name+"','"+path+"',curdate(),'"+str(session['lid'])+"')"
        db.insert(qry)
        return '''<script>alert('Added successfully...');window.location='/staff_add_materials#about'</script>'''

@app.route('/staff_view_material')
def staff_view_material():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="SELECT * FROM material where staff_id='"+str(session['lid'])+"'"
        res=db.select(qry)
        return render_template("staff/materials.html",data=res)


@app.route('/deletematerial/<id>')
def deletematerial(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="delete from material where material_id='"+id+"'"
        res=db.delete(qry)
        return '''<script>alert('Deleted successfully...');window.location='/staff_view_material#about'</script>'''

@app.route('/staff_add_questions')
def staff_add_questions():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:

        return render_template("staff/questions add.html")

@app.route('/qstnaddpost', methods=['POST'])
def qstnaddpost():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        question=request.form['question']
        option1=request.form['option1']
        option2 = request.form['option2']
        option3 = request.form['option3']
        option4 = request.form['option4']
        correct = request.form['correct']
        qry="INSERT INTO `question` (`exam_id`,question,`option_1`,`option_2`,`option_3`,`option_4`,`correct_answer`) VALUES('"+str(session['examid'])+"','"+question+"','"+option1+"','"+option2+"','"+option3+"','"+option4+"','"+correct+"')"
        db=Db()
        db.insert(qry)

        return "<script>alert('');window.location='/staff_add_questions#about'</script>"


@app.route('/editquestions/<id>')
def editquestions(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        session['qsid'] = id
        qry = "SELECT * FROM `question` WHERE `question_id`='" + id + "'"
        db = Db()
        res = db.selectOne(qry)
        return render_template("Staff/questions edit.html",data=res)

@app.route('/editqstnpost', methods=['POST'])
def editqstnpost():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        question = request.form['question']
        option1 = request.form['option1']
        option2 = request.form['option2']
        option3 = request.form['option3']
        option4 = request.form['option4']
        correct = request.form['correct']
        db=Db()
        qry="update question set question='" + question + "',option_1='" + option1 + "',option_2='" + option2 + "',option_3='" + option3 + "',option_4='" + option4 + "',correct_answer='" + correct + "' where question_id='" +str(session['qsid'])+ "'"
        db.update(qry)
        return redirect('/staff_add_exam')



@app.route('/viewquestions/<id>')
def viewquestions(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        session['examid'] = id
        qry="SELECT * FROM `question` WHERE `exam_id`='"+str(session['examid'])+"'"
        db=Db()
        res=db.select(qry)
        return render_template("Staff/viewqstions.html",val=res)

@app.route('/deletequestion/<id>')
def deletequestion(id):
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="delete from question where question_id='"+id+"'"
        res=db.delete(qry)
        return redirect('/staff_add_exam')



@app.route('/staff_view_result')
def staff_view_result():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry = "SELECT `student`.`name`,`result`.*,exam.*  FROM result JOIN student ON student.student_lid=result.student_id JOIN exam ON exam.exam_id=result.exam_id"

        res=db.select(qry)
        return render_template("Staff/view exam result.html",data=res)

@app.route('/staff_search_result',methods=['post'])
def staff_search_result():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        search=request.form['search']
        db=Db()
        qry="SELECT `student`.`name`,`result`.*,exam.*  FROM result JOIN student ON student.student_lid=result.student_id JOIN exam ON exam.exam_id=result.exam_id where student.name like '%"+search+"%'"
        res=db.select(qry)
        return render_template("Staff/view exam result.html",data=res)

@app.route('/staff_view_notification')
def staff_view_notification():
    if session['lid'] == '':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="select * from notification"
        res=db.select(qry)
        return render_template("Staff/view notification.html",data=res)

@app.route('/staff_view_profile')
def staff_view_profile():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db = Db()
        qry = "SELECT * FROM `staff` WHERE `staff_lid`='"+str(session['lid'])+"'"
        res = db.selectOne(qry)
    return render_template("staff/view profile.html",data=res)
@app.route('/staff_view_student')
def staff_view_student():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db=Db()
        qry="select * from student"
        res=db.select(qry)
        return render_template("Staff/view student.html",data=res)


@app.route('/staff_search_student',methods=['post'])
def staff_search_student():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        search=request.form['search']
        db=Db()
        qry="select * from student where name like '%"+search+"%'"
        res=db.select(qry)
        return render_template("Staff/view student.html",data=res)

@app.route('/staff_home')
def staff_home():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        return render_template("Staff/home.html")



@app.route('/staff_change_password')
def staff_change_password():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        return render_template('Staff/changepass.html')

@app.route('/change_pswrd_post', methods=['post'])
def change_pswrd_post():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        cp = request.form['p1']
        np = request.form['p2']
        cnp = request.form['p3']
        db = Db()
        qry = "SELECT * FROM `login` WHERE `password`='"+cp+"'"
        res = db.selectOne(qry)
        if res is not None:
            if np==cnp:
                qry = "UPDATE `login` SET `password`='"+str(cnp)+"' WHERE `lid`='"+str(session['lid'])+"'"
                res=db.update(qry)
                return redirect('/')
            else:
                return '''<script>alert('Invalid');window.location='/staff_change_password'</script>'''
        else:
            return '''<script>alert('Invalid');window.location='/staff_change_password'</script>'''




@app.route('/addexam')
def addexam():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        return render_template("Staff/addexam.html")

@app.route('/addexampost', methods=['POST'])
def addexampost():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        db = Db()
        exam=request.form['exam']
        date=request.form['date']
        qry="INSERT INTO `exam` (`exam`,`date`) VALUES('"+exam+"','"+date+"')"
        db.insert(qry)
        qry1="INSERT INTO `notification`(`from_lid`,`notification`,`date`) VALUES ('"+str(session['lid'])+"','"+exam+"','"+date+"')"
        res=db.insert(qry1)
        return '''<script>alert('Added successfully...');window.location='/addexam#about'</script>'''

@app.route('/b')
def b():
    if session['lid']=='':
        return '''<script>alert('Login again to Continue...');window.location='/'</script>'''
    else:
        return render_template("staff/b.html")




#================+++++++++++++++++++++++++++++++++++==============Android========================================================================================================

@app.route('/and_reg_post',methods=['post'])
def and_reg_post():
    name=request.form['name']
    gender=request.form['gender']
    place=request.form['place']
    post=request.form['post']
    district=request.form['district']
    email=request.form['email']
    phone=request.form['phone']
    photo=request.form['photo']
    qualification=request.form['qualification']
    db = Db()
    chk="select * from login WHERE username='"+email+"'"
    feed=db.selectOne(chk)
    if feed is None:
        import base64
        from datetime import datetime
        b=datetime.now().strftime("%y%m%d-&H%M%S%f")+".jpg"
        sp="D:\\OMR\\static\\student\\"
        a=base64.b64decode(photo)
        with open(sp+b,'wb') as fh:
            fh.write(a)
        path="/static/student/"+b

        qry1="INSERT INTO login (`username`,`password`,`type`) VALUES ('"+email+"','"+phone+"','student')"
        res1=db.insert(qry1)
        qry="INSERT INTO student (`student_lid`,`name`,`gender`,`place`,`post`,`district`,`email`,`phone`,`photo`,`qualification`) VALUES ('"+str(res1)+"','"+name+"','"+gender+"','"+place+"','"+post+"','"+district+"','"+email+"','"+phone+"','"+path+"','"+qualification+"' )"
        res=db.insert(qry)
        return jsonify(status="ok")
    else:
        return jsonify(status="No")


@app.route('/and_login_post',methods=['post'])
def and_login_post():
    username=request.form['username']
    password=request.form['password']
    db=Db()
    qry="SELECT * FROM login WHERE `username`='"+username+"' AND `password`='"+password+"'"
    res=db.selectOne(qry)
    if res is None:
        return jsonify(status="not")
    elif res['type'] == 'student':
        return jsonify(status="ok",lid=res['lid'],type='student')
    else:
        return jsonify(status="not")
@app.route('/and_changepass_post',methods=['post'])
def and_changepass_post():
    lid=request.form['lid']
    password1=request.form['p1']
    newpass=request.form['np']
    cnfrmpass=request.form['cp']
    db=Db()
    qry="SELECT * FROM login WHERE `password`='"+password1+"' AND `lid`='"+lid+"'"
    res = db.selectOne(qry)
    if res is not None:
         if newpass == cnfrmpass:
                    qry = "UPDATE `login` SET `password`='"+newpass+"' WHERE `lid`='"+lid+"'"
                    res = db.update(qry)
                    return jsonify(status="ok")
         else:
                    return jsonify(status="not")
    else:
                    return  jsonify(status="not")

@app.route('/and_editprofile_post',methods=['post'])
def and_editprofile_post():
    lid=request.form['lid']
    name = request.form['name']
    gender = request.form['gender']
    place = request.form['place']
    post = request.form['post']
    district = request.form['district']
    email = request.form['email']
    phone = request.form['phone']
    photo = request.form['photo']
    qualification = request.form['qualification']
    db = Db()
    if len(photo)>0:

        import base64
        from datetime import datetime
        b = datetime.now().strftime("%y%m%d-&H%M%S%f") + ".jpg"
        sp = "D:\\OMR\\static\\student\\"
        a = base64.b64decode(photo)
        with open(sp + b, 'wb') as fh:
            fh.write(a)
        path = "/static/student/" + b
        qry="UPDATE student SET `name`='"+name+"',`gender`='"+gender+"',`place`='"+place+"',`post`='"+post+"',`district`='"+district+"',`email`='"+email+"',`phone`='"+phone+"',`photo`='"+path+"',`qualification`='"+qualification+"' WHERE `student_lid`='"+lid+"'"
        res=db.update(qry)
        return jsonify(status="ok")
    else:
        qry = "UPDATE student SET `name`='" + name + "',`gender`='" + gender + "',`place`='" + place + "',`post`='" + post + "',`district`='" + district + "',`email`='" + email + "',`phone`='" + phone + "',`qualification`='" + qualification + "' WHERE `student_lid`='" + lid + "'"
        res = db.update(qry)
        return jsonify(status="ok")


@app.route('/and_complaint_post',methods=['post'])
def and_complaint_post():
    lid=request.form['lid']
    complaint=request.form['complaint']
    db=Db()
    qry="INSERT INTO complaint (`date`,`complaint`,`student_lid`,`reply`,`status`) VALUES (curdate(),'"+complaint+"','"+lid+"','pending','pending')"
    res=db.insert(qry)
    return jsonify(status="ok")

@app.route('/and_sendfeedback_post',methods=['post'])
def and_sendfeedback_post():
    lid=request.form['lid']
    feedback=request.form['feedback']
    db=Db()
    qry="INSERT INTO feedback (`feedback_lid`,`feedback`,`date`) VALUES ('"+lid+"','"+feedback+"',curdate())"
    res=db.insert(qry)
    return jsonify(status="ok")

@app.route('/and_viewprofile_post',methods=['post'])
def and_viewprofile_profile():
    lid=request.form['lid']
    db=Db()
    qry="SELECT * FROM student WHERE `student_lid`='"+lid+"'"
    res=db.selectOne(qry)
    return jsonify(status="ok",data=res,name=res['name'],gender=res['gender'],place=res['place'],post=res['post'],district=res['district'],email=res['email'],phone=res['phone'],photo=res['photo'],qualification=res['qualification'])

@app.route('/and_exmnotification_post',methods=['post'])
def and_exmnotification_post():
    db=Db()
    qry="SELECT `notification`.*,`staff`.name FROM `notification` JOIN `staff` ON `staff`.`staff_lid`=`notification`.`from_lid`"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_notification_post',methods=['post'])
def and_notification_post():
    db=Db()
    qry="SELECT * FROM `notification` WHERE `from_lid`='1'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_exmresult_post',methods=['post'])
def and_exmresult_post():
    lid=request.form['lid']
    db=Db()
    qry="SELECT `result`.*,`exam`.* FROM `exam` JOIN `result` ON `result`.`exam_id`=`exam`.`exam_id` WHERE `result`.`student_id`='"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_material_post',methods=['post'])
def and_material_post():
    db=Db()
    qry="SELECT *,`material`.`name` AS mname FROM `material` JOIN `staff` ON `staff_lid`=`material`.`staff_id`"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/and_career_post',methods=['post'])
def and_career_post():
    db=Db()
    qry="SELECT * FROM career"
    res = db.select(qry)
    return jsonify(status="ok",data=res)





@app.route('/and_view_reply_post', methods=['POST'])
def and_view_reply_post():
    lid=request.form['lid']
    qry="SELECT * FROM `complaint` WHERE `student_lid`='"+lid+"'"
    db=Db()
    res=db.select(qry)
    return jsonify(status="ok", data=res)














if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
