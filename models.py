from utilies import *

xg_train, xg_test, yg_train, yg_test = train_test_split(xg1, yg1, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(xg_train, yg_train)
yg_pred = model.predict(xg_test)

x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size=0.2, random_state=42)
modelcls = LogisticRegression()
modelcls.fit(x_train, y_train)
ypredcls = modelcls.predict(x_test)

#tri accura


x_train2, x_test2, y_train2, y_test2 = train_test_split(x2, y2, test_size=0.2, random_state=42)

x_train3, x_test3, y_train3, y_test3 = train_test_split(x3, y3, test_size=0.3, random_state=42)

model2 = LogisticRegression()
model2.fit(x_train2, y_train2)
ypred2 = model2.predict(x_test2)

model3 = LogisticRegression()
model3.fit(x_train3, y_train3)
ypred3 = model3.predict(x_test3)



