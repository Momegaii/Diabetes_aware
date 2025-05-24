from models import * 
import warnings
warnings.filterwarnings('ignore')

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
		diabin = input("Please, provide me with the last report only numbers of : Age,BMI,Fasting Glucose (mg/dL),HbA1c (%),Polyuria1/0,Polydipsia1/0,Blurred Vision1/0,Fatigue1/0,Unexplained Weight Loss1/0 ")
		
		dibinx = [[diabin]]
		
		preusrdiab1 = model2.predict(dibnx)
		
		preusrdiab2 = model3.predict(dibnx)
		
		#check on the decoder if it made the yes 0 or one before usin the block below 
		if preusrdiab1 == 0 :
			print("Diabetes")
		elif preusrdiab == 1  :
			print("Normal")
			
		if preusrdiab2 == 0 : 
			print("diabetes")
		elif preusrdiab2 == 1  :
			print("normal")
				
			
ui()
