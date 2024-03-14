from flask import render_template, jsonify, request, redirect, url_for, flash
# from flask_login import login_user, current_user, logout_user, login_required

# Forms
# from flaskapp.py_forms.crud_forms import Basic_post


from flaskapp.py_routes.main_routes import main


# LANDING PAGE
# ===================================================================
@main.route('/', methods=['GET', 'POST'])
@main.route('/dashboard', methods=['GET', 'POST'])
# @login_required
def main_dashboard():
    page_title = 'Main page'
    # form = Basic_post()

    if request.method == 'GET':
        return render_template('/index_primary.html', page_title=page_title)




