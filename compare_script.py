from browser import *

maxSpeed = ["298 км/ч","286 км/ч","261 км/ч","246 км/ч"]
acceleration = ["4.8 cек","4.8 cек","5 cек","5.3 cек"]
hP = ["455 л.с","390 л.с","300 л.с","280 л.с"]
weight = ["1490 кг","1506 кг","1385 кг","1430 кг"]

def CarChooser(event):
    get_first = document.getElementById("selcar1").value;
    get_second = document.getElementById("selcar2").value;
    
    if get_first == "Lambo":
        document.getElementById("carpic1").src="pics/countach-main.jpg"
        document.getElementById("name_frst").text="Lamborghini Countach 5000QV"
        document.getElementById("ms1").text=maxSpeed[0]
        document.getElementById("acc1").text=acceleration[0]
        document.getElementById("hp1").text=hP[0]
        document.getElementById("w1").text=weight[0]
    elif get_first == "Ferrari":
        document.getElementById("carpic1").src="pics/testarossa-main.jpg"
        document.getElementById("name_frst").text="Ferrari Testarossa"
        document.getElementById("ms1").text=maxSpeed[1]
        document.getElementById("acc1").text=acceleration[1]
        document.getElementById("hp1").text=hP[1]
        document.getElementById("w1").text=weight[1]
    elif get_first == "Porsche":
        document.getElementById("carpic1").src="pics/911turbo-main.jpg"
        document.getElementById("name_frst").text="Porsche 930"
        document.getElementById("ms1").text=maxSpeed[2]
        document.getElementById("acc1").text=acceleration[2]
        document.getElementById("hp1").text=hP[2]
        document.getElementById("w1").text=weight[2]
    elif get_first == "Nissan":
        document.getElementById("carpic1").src="pics/gtr-main.jpg"
        document.getElementById("name_frst").text="Nissan GT-R (R32)"
        document.getElementById("ms1").text=maxSpeed[3]
        document.getElementById("acc1").text=acceleration[3]
        document.getElementById("hp1").text=hP[3]
        document.getElementById("w1").text=weight[3]
    else:
        document.getElementById("carpic1").src="pics/comp_script/choose.png"
        document.getElementById("name_frst").text="???"
        document.getElementById("ms1").text="???"
        document.getElementById("acc1").text="???"
        document.getElementById("hp1").text="???"
        document.getElementById("w1").text="???"
    
    if get_second == "Lambo":
        document.getElementById("carpic2").src="pics/countach-main.jpg"
        document.getElementById("name_scnd").text="Lamborghini Countach 5000QV"
        document.getElementById("ms2").text=maxSpeed[0]
        document.getElementById("acc2").text=acceleration[0]
        document.getElementById("hp2").text=hP[0]
        document.getElementById("w2").text=weight[0]
    elif get_second == "Ferrari":
        document.getElementById("carpic2").src="pics/testarossa-main.jpg"
        document.getElementById("name_scnd").text="Ferrari Testarossa"
        document.getElementById("ms2").text=maxSpeed[1]
        document.getElementById("acc2").text=acceleration[1]
        document.getElementById("hp2").text=hP[1]
        document.getElementById("w2").text=weight[1]
    elif get_second == "Porsche":
        document.getElementById("carpic2").src="pics/911turbo-main.jpg"
        document.getElementById("name_scnd").text="Porsche 930"
        document.getElementById("ms2").text=maxSpeed[2]
        document.getElementById("acc2").text=acceleration[2]
        document.getElementById("hp2").text=hP[2]
        document.getElementById("w2").text=weight[2]
    elif get_second == "Nissan":
        document.getElementById("carpic2").src="pics/gtr-main.jpg"
        document.getElementById("name_scnd").text="Nissan GT-R (R32)"
        document.getElementById("ms2").text=maxSpeed[3]
        document.getElementById("acc2").text=acceleration[3]
        document.getElementById("hp2").text=hP[3]
        document.getElementById("w2").text=weight[3]
    else:
        document.getElementById("carpic2").src="pics/comp_script/choose.png"
        document.getElementById("name_scnd").text="???"
        document.getElementById("ms2").text="???"
        document.getElementById("acc2").text="???"
        document.getElementById("hp2").text="???"
        document.getElementById("w2").text="???"
    
    
    mms1 = document.getElementById("ms1")
    mms2 = document.getElementById("ms2")
    if mms1.text > mms2.text:
        document.getElementById("ms1").classList.remove('compnames')
        document.getElementById("ms1").classList.add('winnames')
    else:
        document.getElementById("ms1").classList.remove('winnames')
        document.getElementById("ms1").classList.add('compnames')
    if mms2.text > mms1.text:
        document.getElementById("ms2").classList.remove('compnames')
        document.getElementById("ms2").classList.add('winnames')
    else:
        document.getElementById("ms2").classList.remove('winnames')
        document.getElementById("ms2").classList.add('compnames')
        
    aacc1 = document.getElementById("acc1")
    aacc2 = document.getElementById("acc2")
    if aacc1.text < aacc2.text:
        document.getElementById("acc1").classList.remove('compnames')
        document.getElementById("acc1").classList.add('winnames')
    else:
        document.getElementById("acc1").classList.remove('winnames')
        document.getElementById("acc1").classList.add('compnames')
    if aacc2.text < aacc1.text:
        document.getElementById("acc2").classList.remove('compnames')
        document.getElementById("acc2").classList.add('winnames')
    else:
        document.getElementById("acc2").classList.remove('winnames')
        document.getElementById("acc2").classList.add('compnames')
        
    hhp1 = document.getElementById("hp1")
    hhp2 = document.getElementById("hp2")
    if hhp1.text > hhp2.text:
        document.getElementById("hp1").classList.remove('compnames')
        document.getElementById("hp1").classList.add('winnames')
    else:
        document.getElementById("hp1").classList.remove('winnames')
        document.getElementById("hp1").classList.add('compnames')
    if hhp2.text > hhp1.text:
        document.getElementById("hp2").classList.remove('compnames')
        document.getElementById("hp2").classList.add('winnames')
    else:
        document.getElementById("hp2").classList.remove('winnames')
        document.getElementById("hp2").classList.add('compnames')
        
    ww1 = document.getElementById("w1")
    ww2 = document.getElementById("w2")
    if ww1.text < ww2.text:
        document.getElementById("w1").classList.remove('compnames')
        document.getElementById("w1").classList.add('winnames')
    else:
        document.getElementById("w1").classList.remove('winnames')
        document.getElementById("w1").classList.add('compnames')
    if ww2.text < ww1.text:
        document.getElementById("w2").classList.remove('compnames')
        document.getElementById("w2").classList.add('winnames')
    else:
        document.getElementById("w2").classList.remove('winnames')
        document.getElementById("w2").classList.add('compnames')
        
document['btn-1'].bind('click', CarChooser)
