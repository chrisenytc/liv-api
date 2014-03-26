# -*- coding: utf-8 -*-

""""
ProjectName: liv-api
Repo: https://github.com/chrisenytc/liv-api
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
import uuid
import os
import threading
from api import app, mail
from hashlib import sha1
from flask import request, copy_current_request_context
from flask import jsonify as JSON
from flask_mail import Message
from api.models.user import User
from api.models.activate import Activate
from api.models.forgot import Forgot
from api.errors.invalid_request import InvalidRequest
from cors import cors


@app.route('/signup', methods=['POST'])
@cors(origin='*', methods=['POST'])
def users_signup():
    # Create new user
    data = request.get_json()
    new_user = User()
    new_user.name = data['name']
    new_user.email = data['email']
    new_user.password = sha1(data['password']).hexdigest()
    new_user.token = str(uuid.uuid4())
    new_user.save()
    create_activate_token = Activate(
        email=new_user.email, token=str(uuid.uuid4()))
    create_activate_token.save()
    # Message
    msg = Message("Welcome to Liv",
                  recipients=[new_user.email])
    msg.html = """
    <h2>Hi, %s</h2>
    <h4>Welcome to Liv</h4>
    <p>
    To start using the Liv, you need to activate your account. 
    Click the link to activate your account.
    </p>
    <p>
        <a href="https://livia.herokuapp.com/signup/activate?token=%s" target="_blank">Activate your Liv account</a>
    </p>
    """ % (new_user.name, create_activate_token.token)

    @copy_current_request_context
    def send_message(message):
        mail.send(message)

    sender = threading.Thread(
        name='mail_signup_sender', target=send_message, args=(msg,))
    sender.start()
    # Returns a response
    return JSON(message='An email with the your activation token has been sent to your email.')


@app.route('/signin', methods=['POST'])
@cors(origin='*', methods=['POST'])
def users_signin():
    # Retorn a user data
    data = request.get_json()
    user_info = User.objects(email=data['email'], password=sha1(
        data['password']).hexdigest())
    if user_info.count():
        return JSON(token=user_info.get().token, roles=user_info.get().roles)
    else:
        return JSON(message='User not found')


@app.route('/signup/activate')
@cors(origin='*')
def users_activate_user():
    activate_info = Activate.objects(token=request.args.get('token', ''))
    if activate_info.count():
        user_info = User.objects(email=activate_info.get().email)
        if user_info.count():
            user_info.update(set__status=True)
            activate_info.delete()
            # Message
            msg = Message("Your Account is Activated",
                          recipients=[user_info.get().email])
            msg.html = """
            <h2>Hi, %s</h2>
            <p>
            Your new access token was successfully generated.
                <p>
                    <b>Access Token: </b> %s
                </p>
            </p>
            """ % (user_info.get().name, user_info.get().token)

            @copy_current_request_context
            def send_message(message):
                mail.send(message)

            sender = threading.Thread(
                name='mail_activate_sender', target=send_message, args=(msg,))
            sender.start()
            # Returns a response
            return JSON(message='An email with the your new token has been sent to your email.')
        else:
            raise InvalidRequest('User not found!')
    else:
        raise InvalidRequest('Activate Token is invalid!')


@app.route('/forgot', methods=['POST'])
@cors(origin='*', methods=['POST'])
def users_forgot():
    data = request.get_json()
    user_info = User.objects(email=data['email'])
    if user_info.count():
        create_forgot_token = Forgot(
            email=user_info.get().email, token=str(uuid.uuid4()))
        create_forgot_token.save()
        # Message
        msg = Message("Forgot Password",
                      recipients=[user_info.get().email])
        msg.html = """
        <h2>Hi, %s</h2>
        <p>
        You requested a password change. Use the link below to create a new password.
        </p>
        <p>
            <a href="https://livia.herokuapp.com/forgot/reset?token=%s" target="_blank">Reset Password</a>
        </p>
        """ % (user_info.get().name, create_forgot_token.token)

        @copy_current_request_context
        def send_message(message):
            mail.send(message)

        sender = threading.Thread(
            name='mail_forgot_sender', target=send_message, args=(msg,))
        sender.start()
        # Returns a response
        return JSON(message='An email with the password reset link has been sent to your email.')
    else:
        raise InvalidRequest('User not found!')


@app.route('/forgot/reset')
@cors(origin='*')
def users_reset():
    forgot_info = Forgot.objects(token=request.args.get('token', ''))
    if forgot_info.count():
        user_info = User.objects(email=forgot_info.get().email)
        if user_info.count():
            randompass = os.urandom(16).encode("base64")[:10]
            user_info.update(set__password=sha1(randompass).hexdigest())
            forgot_info.delete()
            # Message
            msg = Message("Your new Password",
                          recipients=[user_info.get().email])
            msg.html = """
            <h2>Hi, %s</h2>
            <p>
            Your new password was successfully generated.
            </p>
            <p>
                <b>Password: </b> %s
            </p>
            """ % (user_info.get().name, randompass)

            @copy_current_request_context
            def send_message(message):
                mail.send(message)

            sender = threading.Thread(
                name='mail_reset_sender', target=send_message, args=(msg,))
            sender.start()
            # Returns a response
            return JSON(message='An email with the new password has been sent to your email.')
        else:
            raise InvalidRequest('User not found!')
    else:
        raise InvalidRequest('Forgot Token is invalid!')
