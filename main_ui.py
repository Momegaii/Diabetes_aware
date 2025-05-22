from models import * 
import warnings 

warnings.help()

def ui():
	uin = input("Welcom to Ms20.sys for diabetes awarness ,please choose a service : type 1  for Glucose pred or type 2 for diabetes prediction")
	if uin == "1" :
		glcin = int(input("Please , provide me with : the peitent last report of in order just numbers Diastolicpressure ,Systolicpress,heartrate,diabetesornot 1 for diabetes and 0 for nodiabetes  "))
		
		glcinx = [[glcin]]
		
		preusrglc = model.predict(glcinx)
		
		print(preusrglc[0])
	
		if preusrglc > 70 : 
			print("the peitent have high level of glucose may cause a blood pressure needs attention ")
		else:
			print("GLC level is normal")
			
	elif uin == "2" :
		diabin = input("Please, provide me with the last report only numbers of : ")
