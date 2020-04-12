from flask import Flask, render_template, redirect, request, make_response

app = Flask(__name__)

@app.route('/', methods=['POST'])
def ussd_callback():
	session_id = request.values.get("sessionId", None)
	serviceCode = request.values.get("serviceCode", None)
	phoneNumber = request.values.get("phoneNumber", None)
	text = request.values.get("text", None)
	pin_entered = False

	#serve menus based on text
	if text == "":
		menu_text = "CON Welcome to RMU eVoucher \n"
		menu_text += "1. Ghanaian Student \n"
		menu_text += "2. International Student \n"

	elif text =="1":
		menu_text = "CON The voucher will cost GHC 100.00 \n"
		menu_text += "1. My Press 1 to continue\n"

	elif text =="2":
		menu_text = "CON The voucher will cost GHC 100.00 \n"
		menu_text += "1. My Press 1 to continue\n"

	elif text =="1*1":
		menu_text = "CON Enter your email to receive your voucher \n"

	elif text =="1*2":
		menu_text = "CON Enter your email to receive your voucher \n"

	elif '@' in text:
		menu_text = "CON Enter your MoMo pin to authenticate the transaction \n"
		pin_entered = True

	if pin_entered:
		menu_text = "END The transaction was successful! Check your email for your eVoucher"



	resp = make_response(menu_text, 200)
	resp.headers['Content-Type'] = "text/plain"
	return resp

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)