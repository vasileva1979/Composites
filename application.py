from tkinter import *
import numpy as np
from tensorflow import keras

import joblib
scaler = joblib.load('scaler') 

root = Tk()
root.geometry("600x500")
root.title('Cоотношение матрица-наполнитель')
model = keras.models.load_model('saved_model/my_model')

labl_title=Label(text ='Прогнозное значение параметра \nСоотношение матрица-наполнитель', font='Arial 18')
labl_title.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

labl_plotn=Label(text ='Плотность, кг/м3', font='Arial 12')
labl_plotn.grid(sticky = W, row=1, column=0, padx=10, pady=3)
plotn_var=StringVar()
entry_plotn = Entry(textvariable=plotn_var)
entry_plotn.grid(sticky = W, row=1, column=1, padx=10, pady=3)

labl_modupr=Label(text ='Модуль упругости, ГПа', font='Arial 12')
labl_modupr.grid(sticky = W, row=2, column=0, padx=10, pady=3)
modupr_var=StringVar()
entry_modupr = Entry(textvariable=modupr_var)
entry_modupr.grid(sticky = W, row=2, column=1, padx=10, pady=3)

labl_otverd=Label(text ='Количество отвердителя, м.%', font='Arial 12')
labl_otverd.grid(sticky = W, row=3, column=0, padx=10, pady=3)
otverd_var=StringVar()
entry_otverd = Entry(textvariable=otverd_var)
entry_otverd.grid(sticky = W, row=3, column=1, padx=10, pady=3)

labl_epox=Label(text ='Содержание эпоксидных групп, %_2', font='Arial 12')
labl_epox.grid(sticky = W, row=4, column=0, padx=10, pady=3)
epox_var=StringVar()
entry_epox = Entry(textvariable=epox_var)
entry_epox.grid(sticky = W, row=4, column=1, padx=10, pady=3)

labl_temp=Label(text ='Температура вспышки, С_2', font='Arial 12')
labl_temp.grid(sticky = W, row=5, column=0, padx=10, pady=3)
temp_var=StringVar()
entry_temp = Entry(textvariable=temp_var)
entry_temp.grid(sticky = W, row=5, column=1, padx=10, pady=3)

labl_poverh=Label(text ='Поверхностная плотность, г/м2', font='Arial 12')
labl_poverh.grid(sticky = W, row=6, column=0, padx=10, pady=3)
poverh_var=StringVar()
entry_poverh = Entry(textvariable=poverh_var)
entry_poverh.grid(sticky = W, row=6, column=1, padx=10, pady=3)

labl_upr_ras=Label(text ='Модуль упругости при растяжении, ГПа', font='Arial 12')
labl_upr_ras.grid(sticky = W, row=7, column=0, padx=10, pady=3)
upr_ras_var=StringVar()
entry_upr_ras = Entry(textvariable=upr_ras_var)
entry_upr_ras.grid(sticky = W, row=7, column=1, padx=10, pady=3)

labl_pro_ras=Label(text ='Прочность при растяжении, МПа', font='Arial 12')
labl_pro_ras.grid(sticky = W, row=8, column=0, padx=10, pady=3)
pro_ras_var=StringVar()
entry_pro_ras = Entry(textvariable=pro_ras_var)
entry_pro_ras.grid(sticky = W, row=8, column=1, padx=10, pady=3)

labl_smola=Label(text ='Потребление смолы, г/м2', font='Arial 12')
labl_smola.grid(sticky = W, row=9, column=0, padx=10, pady=3)
smola_var=StringVar()
entry_smola = Entry(textvariable=smola_var)
entry_smola.grid(sticky = W, row=9, column=1, padx=10, pady=3)

labl_ugol=Label(text ='Угол нашивки, град', font='Arial 12')
labl_ugol.grid(sticky = W, row=10, column=0, padx=10, pady=3)
ugol_var=StringVar()
entry_ugol = Entry(textvariable=ugol_var)
entry_ugol.grid(sticky = W, row=10, column=1, padx=10, pady=3)

labl_shag=Label(text ='Шаг нашивки', font='Arial 12')
labl_shag.grid(sticky = W, row=11, column=0, padx=10, pady=3)
shag_var=StringVar()
entry_shag = Entry(textvariable=shag_var)
entry_shag.grid(sticky = W, row=11, column=1, padx=10, pady=3)

labl_plotn_nash=Label(text ='Плотность нашивки', font='Arial 12')
labl_plotn_nash.grid(sticky = W, row=12, column=0, padx=10, pady=3)
plotn_nash_var=StringVar()
entry_plotn_nash = Entry(textvariable=plotn_nash_var)
entry_plotn_nash.grid(sticky = W, row=12, column=1, padx=10, pady=3)

labl_result=Label(text ='Результат:', font='Arial 12')
labl_result.grid(sticky = W, row=13, column=0, padx=10, pady=3)

def calc():
	a1=float(plotn_var.get())
	a2=float(modupr_var.get())
	a3=float(otverd_var.get())
	a4=float(epox_var.get())
	a5=float(temp_var.get())
	a6=float(poverh_var.get())
	a7=float(upr_ras_var.get())
	a8=float(pro_ras_var.get())
	a9=float(smola_var.get())
	a10=float(ugol_var.get())
	a11=float(shag_var.get())
	a12=float(plotn_nash_var.get())
	x=np.array([[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]])
	
	x_norm=scaler.transform(x)
	y=model.predict(x_norm)
	labl_result.config(text = f'Результат: {y[0][0]}')



btn_calc=Button(text="Спрогнозировать", command=calc)
btn_calc.grid(row=13, column=2, padx=10)
root.mainloop()