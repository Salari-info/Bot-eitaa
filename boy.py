import requests 
from time import sleep


chat_id = "8459908"
token = "99534:6a6b78ef-264c-42af-9a33-fda65778e361"

requests.get(f"https://eitaayar.ir/api/{token}/getMe")
a = 0
while True:
	try:
		a  = a+1
		requests.post(f"https://eitaayar.ir/api/bot{token}/sendMessage", json={
			'chat_id': chat_id,
			'text': requests.get("http://api.codebazan.ir/jok").text + "\n\n  چنل اصلی :  \n 🆔 @tyro_code ",
			}
		)
		print(f"send jok {a} ✅")
		sleep(10)
	except:
		pass
	
