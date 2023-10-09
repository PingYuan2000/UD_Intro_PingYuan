{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2a514a78",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: selenium in c:\\users\\jay\\anaconda3\\lib\\site-packages (4.13.0)\n",
      "Requirement already satisfied: urllib3[socks]<3,>=1.26 in c:\\users\\jay\\anaconda3\\lib\\site-packages (from selenium) (1.26.16)\n",
      "Requirement already satisfied: trio~=0.17 in c:\\users\\jay\\anaconda3\\lib\\site-packages (from selenium) (0.22.2)\n",
      "Requirement already satisfied: trio-websocket~=0.9 in c:\\users\\jay\\anaconda3\\lib\\site-packages (from selenium) (0.11.1)\n",
      "Requirement already satisfied: certifi>=2021.10.8 in c:\\users\\jay\\anaconda3\\lib\\site-packages (from selenium) (2023.7.22)\n",
      "Requirement already satisfied: attrs>=20.1.0 in c:\\users\\jay\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (22.1.0)\n",
      "Requirement already satisfied: sortedcontainers in c:\\users\\jay\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (2.4.0)\n",
      "Requirement already satisfied: idna in c:\\users\\jay\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (3.4)\n",
      "Requirement already satisfied: outcome in c:\\users\\jay\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (1.2.0)\n",
      "Requirement already satisfied: sniffio in c:\\users\\jay\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (1.2.0)\n",
      "Requirement already satisfied: cffi>=1.14 in c:\\users\\jay\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (1.15.1)\n",
      "Requirement already satisfied: wsproto>=0.14 in c:\\users\\jay\\anaconda3\\lib\\site-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
      "Requirement already satisfied: PySocks!=1.5.7,<2.0,>=1.5.6 in c:\\users\\jay\\anaconda3\\lib\\site-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
      "Requirement already satisfied: pycparser in c:\\users\\jay\\anaconda3\\lib\\site-packages (from cffi>=1.14->trio~=0.17->selenium) (2.21)\n",
      "Requirement already satisfied: h11<1,>=0.9.0 in c:\\users\\jay\\anaconda3\\lib\\site-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install selenium"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "004b0012",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Selenium and its sub libraries\n",
    "import selenium \n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.support.ui import Select\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "from time import sleep\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "83a910d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "url=\"https://scholar.google.com/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dad3b73c",
   "metadata": {},
   "outputs": [],
   "source": [
    "articles_list= []\n",
    "author_list=[]\n",
    "link_list=[]\n",
    "pdf_list=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ef7bec61",
   "metadata": {},
   "outputs": [],
   "source": [
    "def extract_page_data(driver):\n",
    "    articles=driver.find_elements(\"class name\", \"gs_ri\")\n",
    "    for b in range(len(articles)): \n",
    "        try:          \n",
    "            title = articles[b].find_element(\"class name\",\"gs_rt\").text.replace('[HTML]','').strip()\n",
    "            print(title)\n",
    "            authors=articles[b].find_element(\"class name\",\"gs_a\").text\n",
    "            print(authors)\n",
    "            link = articles[b].find_element(\"link text\",title).get_attribute('href')\n",
    "            print(link)\n",
    "            link_list.append(link)\n",
    "            articles_list.append(title)\n",
    "            author_list.append(authors)\n",
    "            sleep(2)  \n",
    "        \n",
    "        except:\n",
    "            pass\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "01e9b627",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(In) visible Cities: What Generative Algorithms Tell Us About Our Collective Memory Schema\n",
      "E Rico Carranza, SY Huang, J Besems - CAADRIA proceedings, 2023 - discovery.ucl.ac.uk\n",
      "https://discovery.ucl.ac.uk/id/eprint/10177249/\n",
      "Aspects of Middle and Late Triassic palynology. 1. Palynostratigraphical data from the Chiclana de Segura Formation of the Linares-Alcaraz Region (Southeastern …\n",
      "RE Besems - Review of Palaeobotany and Palynology, 1981 - Elsevier\n",
      "https://www.sciencedirect.com/science/article/pii/0034666781900075\n",
      "Bacterial hygromorphs: experiments into the integration of soft technologies into building skins\n",
      "C Ramirez-Figueroa, L Hernan… - Proceedings of the …, 2016 - researchonline.rca.ac.uk\n",
      "https://researchonline.rca.ac.uk/3858\n",
      "De professionele lobbytweet: Twitternetwerken tussen Lobbyisten en Politici\n",
      "R Krijger - 2017 - studenttheses.uu.nl\n",
      "https://studenttheses.uu.nl/handle/20.500.12932/25606\n",
      "Palynological correlation of Carnian humid pulses throughout western Tethys\n",
      "G Roghi, P Gianolla, L Minarelli, C Pilati… - Palaeogeography …, 2010 - Elsevier\n",
      "https://www.sciencedirect.com/science/article/pii/S0031018209004805\n",
      "The Bio Economic Seaweed Model (BESeM) for modelling tropical seaweed cultivation–experimentation and modelling\n",
      "PAJ Van Oort, N Rukminasari, G Latama… - Journal of Applied …, 2022 - Springer\n",
      "https://link.springer.com/article/10.1007/s10811-022-02799-8\n",
      "Triassic paleomagnetic data from the Subbetic and the Malaguide Complex of the Betic Cordilleras (Southeast Spain)\n",
      "GH Mäkel, HE Rondeel, J Vandenberg - Tectonophysics, 1984 - Elsevier\n",
      "https://www.sciencedirect.com/science/article/pii/0040195184900453\n",
      "Aspects of the palynostratigraphy of the Triassic Sardinian sequences (preliminary report)\n",
      "PP Demelia, A Flaviani - Review of Palaeobotany and Palynology, 1982 - Elsevier\n",
      "https://www.sciencedirect.com/science/article/pii/0034666782900069\n",
      "Palynostratigraphy of the Mufara formation (middle-upper Triassic, Sicily)\n",
      "N BURATTI, A CARRILLAT - Rivista Italiana di Paleontologia e …, 2002 - riviste.unimi.it\n",
      "https://riviste.unimi.it/index.php/RIPS/article/view/5458\n",
      "Aspects of Middle and Late Triassic palynology. 6. Palynological investigations in the Ladinian and Lower Karnian of the western Dolomites, Italy\n",
      "J Van der Eem - Review of Palaeobotany and Palynology, 1983 - Elsevier\n",
      "https://www.sciencedirect.com/science/article/pii/0034666783900167\n",
      "Ranges of selected palynomorphs in the Alpine Triassic of Europe\n",
      "H Visscher, WA Brugman - Review of Palaeobotany and Palynology, 1981 - Elsevier\n",
      "https://www.sciencedirect.com/science/article/pii/0034666781900695\n",
      "[PDF] PALYNOSTRATIGRAPHY OF THE MUFARA FORMATION (MIDDLE. UPPER TRIASSIC, SICILY)\n",
      "NBIE CARRILLAT - academia.edu\n",
      "[PDF] Palaeoenvironmental reconstruction of the Mufara Formation (Upper Triassic, Sicily): biostratigraphy, organic facies, sedimentological and geochemical …\n",
      "L Zaninetti, R Martini - 2001 - access.archive-ouverte.unige.ch\n",
      "The Carnian pluvial event in Western Europe: new data from Iberia and correlation with the Western Neotethys and eastern North America–NW Africa regions\n",
      "A Arche, J Lopez-Gomez - Earth-Science Reviews, 2014 - Elsevier\n",
      "https://www.sciencedirect.com/science/article/pii/S0012825213001840\n",
      "Western Tethys continental-marine responses to the Carnian Humid Episode: Palaeoclimatic and palaeogeographic implications\n",
      "J López-Gómez, MJ Escudero-Mozo… - Global and Planetary …, 2017 - Elsevier\n",
      "https://www.sciencedirect.com/science/article/pii/S0921818116302405\n",
      "[图书] Der göttlich besiegte Julian: aus der Lebens-Beschreibung desselben\n",
      "JG Pfeil - 1753 - books.google.com\n",
      "Divergent organohalide-respiring consortia in PCB-contaminated sediments\n",
      "M Mikešová - 2017 - dspace.cuni.cz\n",
      "https://dspace.cuni.cz/handle/20.500.11956/2014\n",
      "Palynological and sedimentological implications of the sauropterygian Upper Triassic site of El Atance (Central Iberian Peninsula)\n",
      "M García-Ávila, R De la Horra… - Review of Palaeobotany …, 2021 - Elsevier\n",
      "https://www.sciencedirect.com/science/article/pii/S0034666721001652\n",
      "Palynostratigraphy of the late Ladinian and Carnian in the southeastern Dolomites\n",
      "E Blendinger - Review of palaeobotany and palynology, 1988 - Elsevier\n",
      "https://www.sciencedirect.com/science/article/pii/0034666788900383\n",
      "[PDF] Modus operandi and the socio-spatial milieu in which immigrant niche markets vis-a-vis informal economic activities\n",
      "J Mhandu, VB Ojong… - Journal of Social …, 2018 - researchgate.net\n"
     ]
    }
   ],
   "source": [
    "driver = webdriver.Chrome()\n",
    "driver.get(url)\n",
    "\n",
    "search_query = driver.find_element(\"name\",\"q\")\n",
    "\n",
    "search_query.send_keys('Julian Besems')\n",
    "search_query.send_keys(Keys.RETURN)\n",
    "sleep(3)\n",
    "for page_num in range(0,2):\n",
    "    extract_page_data(driver)\n",
    "    driver.find_element(\"css selector\", \"#gs_n > center > table > tbody > tr > td:nth-child(12) > a > b\").click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cecdca5f",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['(In) visible Cities: What Generative Algorithms Tell Us About Our Collective Memory Schema', 'Aspects of Middle and Late Triassic palynology. 1. Palynostratigraphical data from the Chiclana de Segura Formation of the Linares-Alcaraz Region (Southeastern …', 'Bacterial hygromorphs: experiments into the integration of soft technologies into building skins', 'De professionele lobbytweet: Twitternetwerken tussen Lobbyisten en Politici', 'Palynological correlation of Carnian humid pulses throughout western Tethys', 'The Bio Economic Seaweed Model (BESeM) for modelling tropical seaweed cultivation–experimentation and modelling', 'Triassic paleomagnetic data from the Subbetic and the Malaguide Complex of the Betic Cordilleras (Southeast Spain)', 'Aspects of the palynostratigraphy of the Triassic Sardinian sequences (preliminary report)', 'Palynostratigraphy of the Mufara formation (middle-upper Triassic, Sicily)', 'Aspects of Middle and Late Triassic palynology. 6. Palynological investigations in the Ladinian and Lower Karnian of the western Dolomites, Italy', 'Ranges of selected palynomorphs in the Alpine Triassic of Europe', 'The Carnian pluvial event in Western Europe: new data from Iberia and correlation with the Western Neotethys and eastern North America–NW Africa regions', 'Western Tethys continental-marine responses to the Carnian Humid Episode: Palaeoclimatic and palaeogeographic implications', 'Divergent organohalide-respiring consortia in PCB-contaminated sediments', 'Palynological and sedimentological implications of the sauropterygian Upper Triassic site of El Atance (Central Iberian Peninsula)', 'Palynostratigraphy of the late Ladinian and Carnian in the southeastern Dolomites']\n"
     ]
    }
   ],
   "source": [
    "print(articles_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "392e3d93",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['https://discovery.ucl.ac.uk/id/eprint/10177249/', 'https://www.sciencedirect.com/science/article/pii/0034666781900075', 'https://researchonline.rca.ac.uk/3858', 'https://studenttheses.uu.nl/handle/20.500.12932/25606', 'https://www.sciencedirect.com/science/article/pii/S0031018209004805', 'https://link.springer.com/article/10.1007/s10811-022-02799-8', 'https://www.sciencedirect.com/science/article/pii/0040195184900453', 'https://www.sciencedirect.com/science/article/pii/0034666782900069', 'https://riviste.unimi.it/index.php/RIPS/article/view/5458', 'https://www.sciencedirect.com/science/article/pii/0034666783900167', 'https://www.sciencedirect.com/science/article/pii/0034666781900695', 'https://www.sciencedirect.com/science/article/pii/S0012825213001840', 'https://www.sciencedirect.com/science/article/pii/S0921818116302405', 'https://dspace.cuni.cz/handle/20.500.11956/2014', 'https://www.sciencedirect.com/science/article/pii/S0034666721001652', 'https://www.sciencedirect.com/science/article/pii/0034666788900383']\n"
     ]
    }
   ],
   "source": [
    "print(link_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "eb311388",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['E Rico Carranza, SY Huang, J Besems - CAADRIA proceedings, 2023 - discovery.ucl.ac.uk', 'RE Besems - Review of Palaeobotany and Palynology, 1981 - Elsevier', 'C Ramirez-Figueroa, L Hernan… - Proceedings of the …, 2016 - researchonline.rca.ac.uk', 'R Krijger - 2017 - studenttheses.uu.nl', 'G Roghi, P Gianolla, L Minarelli, C Pilati… - Palaeogeography …, 2010 - Elsevier', 'PAJ Van Oort, N Rukminasari, G Latama… - Journal of Applied …, 2022 - Springer', 'GH Mäkel, HE Rondeel, J Vandenberg - Tectonophysics, 1984 - Elsevier', 'PP Demelia, A Flaviani - Review of Palaeobotany and Palynology, 1982 - Elsevier', 'N BURATTI, A CARRILLAT - Rivista Italiana di Paleontologia e …, 2002 - riviste.unimi.it', 'J Van der Eem - Review of Palaeobotany and Palynology, 1983 - Elsevier', 'H Visscher, WA Brugman - Review of Palaeobotany and Palynology, 1981 - Elsevier', 'A Arche, J Lopez-Gomez - Earth-Science Reviews, 2014 - Elsevier', 'J López-Gómez, MJ Escudero-Mozo… - Global and Planetary …, 2017 - Elsevier', 'M Mikešová - 2017 - dspace.cuni.cz', 'M García-Ávila, R De la Horra… - Review of Palaeobotany …, 2021 - Elsevier', 'E Blendinger - Review of palaeobotany and palynology, 1988 - Elsevier']\n"
     ]
    }
   ],
   "source": [
    "print(author_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "bdbdb445",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "#Import the library\n",
    "import csv \n",
    "\n",
    "#combine the lists\n",
    "data=zip(articles_list,author_list,link_list)\n",
    "\n",
    "#Write all the data to a csv\n",
    "for i in range(len(link_list)):\n",
    "    with open('googlelearning.csv', 'a',newline='',encoding='utf-8') as csvfile: \n",
    "        writer = csv.writer(csvfile)\n",
    "        writer.writerow([author_list[i],articles_list[i],link_list[i]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7976993",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
