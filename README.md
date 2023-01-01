# qrcode-generator

This is a project in Python using Django Framework to generate QR codes.

To install the project in your local machine:

1. Clone this repository

2. Create an enviroment in the root folder, like `py -m venv <path>` and activa it.

3. Run `pip install -r requirements.txt`

4. Go where the `manage.py` file is, and run `py manage.py runserver` in your terminal

5. Then, in your browser go to `http://localhost:8000/home`


---
There are two apps in this project, one is the `users` app and the `qr_app`.

The `users` app is the one it manages the user authentication.

`http://localhost:8000/home` is the home page, there you have a nav bar with options to Login or Signup.

![image](https://user-images.githubusercontent.com/70811425/192155112-f956cde0-9719-48fc-80b6-17f183e95a6b.png)

The Sign Up page has a form to register the user.

![image](https://user-images.githubusercontent.com/70811425/192155275-1a54014f-da7e-401e-aa2f-03167ff826df.png)

After the user was registered, he/she will be redirected to the login page.

![image](https://user-images.githubusercontent.com/70811425/192155399-f0ea68ad-9e1c-470b-846d-f6263ac45216.png)

After login, the user has other options in the navigation bar as logout and the QR Generator app, and also it will be available the option to change the password.

![image](https://user-images.githubusercontent.com/70811425/192155468-b6826115-2cdf-4090-a3a3-1b01c440335a.png)


The QR Generator will ask the user to enter a text, press submit to convert the text to a QR code.

![image](https://user-images.githubusercontent.com/70811425/192155594-248ab609-f0e9-4fab-8fd1-4faf1ddd0d13.png)

![image](https://user-images.githubusercontent.com/70811425/192155673-0b224ca5-cc26-4c9c-8a6f-6b240f29c322.png)

This project the file system, every time a QR code is generated, it will create .png file in the `media` folder.
