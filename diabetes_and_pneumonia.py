def diabetes():
	count=0
	for i in symp:
		if i=='4':
			count+=1
		if i=='12':
			count+=1
		if i=='15':
			count+=1
		else:
			continue
	if count>=2:
		print("Patient has DIABETES!")
		print("Medication:\n Statin\n Insulin\n Exercising and maintaining diet")
diabetes()

def pneumonia():
	count=0
	for i in symp:
		if i=='1':
			count+=1
		if i=='4':
			count+=1
		if i=='9':
			count+=1
		if i=='10':
			count+=1
		if i=='5':
			count+=1
		else:
			continue
	if count>=4:
		print("Patient has been affected with PNEUMONIA!")
		print("Medication:\n Antibiotics\n Fluoroquinolones\n Tetracyclines")
