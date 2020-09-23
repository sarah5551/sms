import requests

_phone = input("Enter number: ")

a = requests.get("https://avtobzvon.ru/request/makeTestCall",
  params={"to": "("+ _phone[0] + "" + _phone[1] + "" + _phone[2] +") "+ _phone[3] + ""+_phone[4] +""+_phone[5]+"-"+_phone[6]+""+_phone[7]+"-"+_phone[8]+""+_phone[9]+""}
        )
print("Answer 1: ")
print(a.text)

c = requests.post('https://autodozvon.ru/test/makeTestCall',
    params={"to": "("+ _phone[0] + "" + _phone[1] + "" + _phone[2] +") "+ _phone[3] + ""+_phone[4] +""+_phone[5]+"-"+_phone[6]+""+_phone[7]+"-"+_phone[8]+""+_phone[9]+""}
    )
print("Answer 2: ")

print(c.text)