from tkinter.tix import Form
#from flask import Blueprint, redirect, render_template, request
#from flask_login import current_user, login_required
#from app.Trainers.forms import PostForm
#from app.models import Post, db

#Trainers = Blueprint('Trainers', __name__, template_folder= 'TrainTemp' )

#@Trainers.route('/catch', methods=["GET","POST"])
#@login_required
#def createPost():
    #form = PostForm()
    #if request.method == "POST":
        #if form.validate():
            #title = form.title.data
            #img_url = form.img_url.data
            #caption = form.caption.data

            #post = Post(title, img_url, caption, current_user.id)
            #post.save()
           # flash('Successfully Caught!', 'success')
       # else:
           # flash('Invalid form. Please fill out the form correctly.', 'danger')
  #  return render_template('createpost.html', form=form)


