from collections import OrderedDict

def runLengthEncode (plainText):
	res=''
	a=''
	for i in plainText:
		if a.count(i)>0:
			a+=i
		else:
			if len(a)>4:
				res+="/" + str(len(a)) + a[0][:1]
			else:
				res+=a
				a=i
	return(res)


def Formula_RLE(inputan):
	data=OrderedDict.fromkeys(inputan, 0)
	for char in inputan:
		data[char] += 1
	hasil = ''
	paket_RLE = 0
	bytes = 0
	for char,nilai in data.items():
		hasil = hasil + char + str(nilai)
		paket_RLE += 1
		bytes = bytes + nilai
	hasil_akhir = [hasil, paket_RLE, bytes]
	return hasil_akhir

def Formula_RLE_Standart_CCITT(inputan):
	data=OrderedDict.fromkeys(inputan, 0)
	for char in inputan:
		data[char] += 1
	hasil = ''
	for char,nilai in data.items():
		if char == "0" or char == "1":
			hasil = hasil + str(nilai) + " "
		else:
			return ("error")
	return hasil

inputan = input("Masukkan String : ")
hasil = runLengthEncode(inputan)
print ("Dengan RLE di encode menjadi : " , hasil)

#inputan = input("Masukkan String : ")
#hasil = Formula_RLE(inputan)
#print ("RLE : ")
#print ("Dengan RLE di encode menjadi : " , hasil[0])
#print (hasil[1] , " paket RLE")
#print (hasil[2] , " bytes")
#print ()

#inputan = input("Masukkan String : ")
#hasil = Formula_RLE_Standart_CCITT(inputan)
#print ("RLE Standard CCITT No. 2 dan 4 : ")
#print ("Hasil encode : " , hasil)

