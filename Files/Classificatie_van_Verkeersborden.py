#!/usr/bin/env python
# coding: utf-8

# In[32]:


import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy as np


# In[45]:


from keras.models import load_model
model = load_model('traffic_classifier.h5')


# In[201]:


classes = { 0:'Bebouwde kom [0]',
            1:'Groot wild [1]',
            2:'Maximumsnelheid [2]', 
            3:'Gehandicaptenparkeerplaats [3]', 
            4:'Parkeerverbod [4]', 
            5:'Onverplicht fietspad [5]', 
            6:'Parkeergelegenheid alleen bestemd voor de voertuigcategorie of groep voertuigen die op het bord is aangegeven [6]', 
            7:'Einde erf [7]', 
            8:'Einde van de zone met snelheidslimiet [8]', 
            9:'Fiets/bromfietspad [9]', 
            10:'Gesloten voor alle motorvoertuigen [10]', 
            11:'Gesloten in beide richtingen voor voertuigen, ruiters en geleiders van rij- of trekdieren of vee [11]', 
            12:'Voorrangsweg [12]', 
            13:'Gebod voor alle bestuurders het bord voorbij te gaan aan de zijde die de pijl aangeeft [13]', 
            14:'Start of einde voetgangerszone [14]', 
            15:'Eenrichtingsweg [15]', 
            16:"Gesloten voor vrachtauto's [16]", 
            17:'Zone van Maximumsnelheid [17]', 
            18:'Gesloten voor voertuigen waarvan de aslast hoger is dan op het bord is aangegeven [18]', 
            19:'Parkeergelegenheid [19]', 
            20:'Gebod tot het volgen van de rijrichting die op het bord is aangegeven [20]', 
            21:'Gesloten voor voertuigen die, met inbegrip van de lading, hoger zijn dan op het bord is aangegeven [21]', 
            22:'Voorrangskruispunt [22]', 
            23:'Begin parkeerverbodzone [23]', 
            24:'Gesloten voor ruiters, vee, wagens, landbouw- en bosbouwtrekkers, motorrijtuigen met beperkte snelheid, mobiele machines, brommobielen, fietsen, snorfietsen, bromfietsen en gehandicaptenvoertuigen[24]', 
            25:'Route voor het vervoer van bepaalde gevaarlijke stoffen [25]', 
            26:'Bestuurders uit tegengestelde richting moeten verkeer dat van deze richting nadert voor laten gaan [26]', 
            27:'Adviessnelheid [27]', 
            28:'Eenrichtingsweg, in deze richting gesloten voor voertuigen, ruiters en geleiders van rij- of trekdieren of vee [28]', 
            29:'Kinderen [29]', 
            30:'Eenrichtingsweg [30]', 
            31:'Verleen voorrang aan bestuurders op de kruisende weg [31]',
            32:'S-bocht(en), eerst naar rechts [32]', 
            33:'Verbod voor bestuurders door te gaan bij nadering van verkeer uit tegengestelde richting [33]', 
            34:'Verplicht fietspad [34]', 
            35:'Verkeersdrempel [35]', 
            36:'Erf [36]', 
            37:'S-bocht(en), eerst naar rechts [37]', 
            38:'Maximumsnelheid op een electronisch signaleringsbord [38]', 
            39:'Voetpad [39]', 
            40:'Einde onverplicht fietspad [40]', 
            41:'Einde maximumsnelheid [41]', 
            42:'Gelegenheid bestemd voor het onmiddellijk laden en lossen van goederen [42]', 
            43:'Doodlopende weg [43]',
            44:'Gesloten voor fietsen, bromfietsen en gehandicaptenvoertuigen [44]',
            45:'Parkeerschijf-zone met verplicht gebruik van parkeerschijf, tevens parkeerverbod indien er langer wordt geparkeerd dan de parkeerduur die op het bord is aangegeven [45]',
            46:'Voetgangers [46]',
            47:'Gesloten voor personen- en bedrijfsauto’s, vrachtauto’s of bussen met een dieselmotor vanwege milieuzone [47]',
            48:'Gebod tot het volgen van de rijrichting die op het bord is aangegeven [48]',
            49:'Gesloten voor motorvoertuigen op meer dan twee wielen [49]',
            50:'Verbod stil te staan [50]',
            51:'Voetgangersoversteekplaats [51]',
            52:'Einde bebouwde kom [52]',
            53:'Voetgangersoversteekplaats [53]',
            54:'Fietsers en bromfietsers [54]',
            55:'Gebod tot het volgen van één van de rijrichtingen die op het bord zijn aangegeven [55]',
            56:'Gevaar (de aard van het gevaar is aangegeven op het onderbord [56]',
            57:'Voorrangskruispunt Zijweg rechts [57]',
            58:'Hoogte onderdoorgang [58]',
            59:'Werk in uitvoering [59]',
            60:'Einde fiets/bromfietspad [60]',
            61:'Einde verplicht fietspad [61]',
            62:'Bord mag aan beide zijden worden voorbijgegaan [62]',
            63:'Gesloten voor voetgangers [63]',
            64:'Overweg met slagbomen [64]',
            65:'Rotonde [65]',
            66:'Tegenliggers [66]',
            67:'Verkeerslichten [67]',
            68:'Gevaarlijk kruispunt [68]',
            69:'Voorrangskruispunt Zijweg links [69]',
            70:'Rijbaan of -strook uitsluitend ten behoeve van lijnbussen [70]',
            71:'Autoweg [71]',
            72:'Einde voorrangsweg [72]',
            73:'Rotonde; verplichte rijrichting [73]',
            74:'Gesloten voor voertuigen en samenstellen van voertuigen die, met inbegrip van de lading, langer zijn dan op het bord is aangegeven [74]',  
            75:'Parkeergelegenheid alleen bestemd voor vergunninghouders [75]',
            76:'Start of einde parkeerzone vergunninghouders [76]',
            77:'Gesloten voor landbouw- en bosbouwtrekkers, motorrijtuigen met beperkte snelheid en mobiele machines [77]',
            78:'Start of einde zone gesloten voor vrachtverkeer [78]',
            79:'Bocht naar rechts [79]',
            80:'Verbod fietsen en bromfietsen te plaatsen [80]',
            81:'Overweg met twee of meer sporen [81]',
            82:'Rijbaanversmalling [82]',
            83:'Verbod voor motorvoertuigen om elkaar onderling in te halen [83]',
            84:'empty',
            85:'Einde Autosnelweg [85]',
            86:'Overweg zonder slagbomen [86]',
            87:'Stop; verleen voorrang aan bestuurders op de kruisende weg [87]',
            88:'Vluchthaven [88]',
            89:'Overweg met enkel spoor [89]',
            90:'Einde autoweg  [90]',
            91:'Bocht naar links [91]',
            92:'Einde van alle door verkeersborden aangegeven verboden [92]',
            93:'Gesloten voor voertuigen en samenstellen van voertuigen, waarvan de totaalmassa hoger is dan op het bord is aangegeven [93]',
            94:'Dichtstbijzijnde uitgang of twee dichtstbijzijnde uitgangen in de op het bord aangegeven richting en afstand [94]',
            95:'Einde parkeerschijf-zone met verplicht gebruik van parkeerschijf [95]',
            96:'Rijbaanversmalling links [96]',
            97:'Rijbaanversmalling rechts [97]',
            98:'Autosnelweg [98]',
            99:'Taxistandplaats [99]',
            100:'Ruiterpad [100]',
            101:'Gesloten voor fietsen en voor gehandicaptenvoertuigen zonder motor [101]',
            102:'Beweegbare brug [102]',
            103:'Slipgevaar [103]',
            104:'Gesloten voor motorvoertuigen met aanhangwagen [104]',
            105:'Vee [105]',
            106:'Gesloten voor bromfietsen, snorfietsen en gehandicaptenvoertuigen, met in werking zijnde motor [106]',
            107:'Einde verbod voor motorvoertuigen om elkaar onderling in te halen [107]',
            108:'Gebod tot het volgen van één van de rijrichtingen die op het bord zijn aangegeven [108]',
            109:'Keerverbod [109]',
            110:'Parkeergelegenheid ten behoeve van overstappers op het openbaar vervoer [110]',
            111:'Rijbaan of -strook uitsluitend ten behoeve van vrachtauto’s [111]',
            112:'Start of einde zone parkeerverbod voor (brom-)fietsers [112]',
            113:"Einde verbod voor vrachtauto's om motorvoertuigen in te halen [113]",
            114:'Waarschuwing voor elektrische in- en uitschuifbare paal in de rijbaan (poller) waarmee toegankelijkheid van straten en gebieden kan worden geregeld. [114]',
            115:'Steile helling [115]',
            116:'Losliggende stenen [116]',
            117:'Stop. In het bord kan worden aangegeven door wie of waarom het bord wordt toegepast [117]',
            118:'Einde adviessnelheid [118]',
            119:'Einde voetpad [119]',
            120:'IJzel of sneeuw [120]',
            121:'Inrijden toegestaan [121]',
            122:'Gesloten voor voertuigen die, met inbegrip van de lading, breder zijn dan op het bord is aangegeven [122]',
            123:'verkeerstunnel [123]',
            124:'Parkeergelegenheid ten behoeve van carpoolers [124]',
            125:'Gesloten voor autobussen en vrachtauto’s [125]',
            126:'Gesloten voor voertuigen met bepaalde gevaarlijke stoffen [126]',
            127:'Vooraanduiding verkeersmaatregel voor de aangegeven richting [127]',
            128:'Verbod voor vrachtauto’s om motorvoertuigen in te halen [128]',
            129:'Zijwind [129]',
            130:'Bushalte / tramhalte [130]',
            131:'Gesloten voor motorfietsen [131]',
            132:'Gesloten voor autobussen [132]',
            133:'Einde ruiterpad[133]',
            134:'Noodtelefoon [134]',
            135:'File [135]',
            136:'Verkeersbord geldt alleen voor de aangegeven rijstrook [136]',
            137:'Laagvliegende vliegtuigen [137]',
            138:'Kade of rivieroever [138]',
            139:'Tram(kruising) [139]',
            140:'Brandblusapparaat [140]',
            141:'Vooraanduiding doodlopende weg [141]',
            142:'Rijbaan of -strook uitsluitend ten behoeve van trams [142]',
            143:'Einde geslotenverklaring milieuzone [143]',
            144:'Rijbaan of -strook uitsluitend ten behoeve van lijnbussen en trams [144]',
            145:'Einde rijstrook [145]',
            146:'Voorsorteren [146]',
            147:'Gesloten voor personen- en bedrijfsauto’s, vrachtauto’s of bussen met een dieselmotor vanwege milieuzone [147]',
            148:'Gevaarlijke daling [148]'}


# In[202]:


top=tk.Tk()
top.geometry('1000x900')
top.title('Classificatie van Verkeersborden')
top.configure(background='#116562')
label=Label(top,background='#CDCDCD', font=('baskerville old face',15,'bold'))
sign_image = Label(top)


# In[203]:


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = np.expand_dims(image, axis=0)
    image_array = np.array(image)
    predict_x=model.predict(image_array) 
    classes_x=np.argmax(predict_x,axis=1)
    sign = classes[classes_x[0]]
    print(sign)
    label.configure(foreground='#011638', text=sign) 


# In[204]:


def show_classify_button(file_path):
    classify_b=Button(top,text="Afbeelding Classificeren",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('baskerville old face',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)


# In[205]:


def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


# In[206]:


upload=Button(top,text="Upload Een Afbeelding",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('baskerville old face',10,'bold'))


# In[207]:


upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Ken Uw Verkeersbord",pady=20, font=('baskerville old face',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()


# In[ ]:





# In[ ]:




