from flask import Flask, render_template, redirect, request, make_response

app = Flask(__name__)

@app.route('/', methods=['POST'])
def ussd_callback():
	session_id = request.values.get("sessionId", None)
	serviceCode = request.values.get("serviceCode", None)
	phoneNumber = request.values.get("phoneNumber", None)
	text = request.values.get("text", None)

	#serve menus based on text
	if text == "":
		menu_text = "CON What would you want to check \n"
		menu_text += "1. My Account \n"
		menu_text += "2. My phone number \n"
		menu_text += "3. My branch"

	elif text =="1":
		menu_text = "CON Choose the account information that you want to view \n"
		menu_text += "1. My Account balance\n"
		menu_text += "2. My Account number \n"

	elif text =="2":
		menu_text = "END Your phone number is "+phoneNumber

	elif text =="1*1":
		menu_text = "END Your account number is ACOO10SWO2101."

	elif text =="1*2":
		menu_text = "END Your BALANCE  is KES 120/-"

	resp = make_response(menu_text, 200)
	resp.headers['Content-Type'] = "text/plain"
	return resp

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)