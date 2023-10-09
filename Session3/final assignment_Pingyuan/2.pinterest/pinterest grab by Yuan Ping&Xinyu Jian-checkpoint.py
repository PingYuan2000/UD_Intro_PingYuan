{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2a514a78",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: selenium in c:\\users\\15809\\anaconda3\\lib\\site-packages (4.13.0)\n",
      "Requirement already satisfied: urllib3[socks]<3,>=1.26 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from selenium) (1.26.16)\n",
      "Requirement already satisfied: trio~=0.17 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from selenium) (0.22.2)\n",
      "Requirement already satisfied: trio-websocket~=0.9 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from selenium) (0.11.1)\n",
      "Requirement already satisfied: certifi>=2021.10.8 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from selenium) (2023.7.22)\n",
      "Requirement already satisfied: attrs>=20.1.0 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (22.1.0)\n",
      "Requirement already satisfied: sortedcontainers in c:\\users\\15809\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (2.4.0)\n",
      "Requirement already satisfied: idna in c:\\users\\15809\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (3.4)\n",
      "Requirement already satisfied: outcome in c:\\users\\15809\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (1.2.0)\n",
      "Requirement already satisfied: sniffio in c:\\users\\15809\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (1.2.0)\n",
      "Requirement already satisfied: cffi>=1.14 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from trio~=0.17->selenium) (1.15.1)\n",
      "Requirement already satisfied: wsproto>=0.14 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from trio-websocket~=0.9->selenium) (1.2.0)\n",
      "Requirement already satisfied: PySocks!=1.5.7,<2.0,>=1.5.6 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from urllib3[socks]<3,>=1.26->selenium) (1.7.1)\n",
      "Requirement already satisfied: pycparser in c:\\users\\15809\\anaconda3\\lib\\site-packages (from cffi>=1.14->trio~=0.17->selenium) (2.21)\n",
      "Requirement already satisfied: h11<1,>=0.9.0 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)\n",
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
   "id": "d9dce64e",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: requests in c:\\users\\15809\\anaconda3\\lib\\site-packages (2.31.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from requests) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from requests) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from requests) (1.26.16)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\15809\\anaconda3\\lib\\site-packages (from requests) (2023.7.22)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "004b0012",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "29\n",
      "https://i.pinimg.com/236x/ad/0b/54/ad0b54b778733bc99b29b425c042be78.jpg\n",
      "https://i.pinimg.com/236x/0f/56/c3/0f56c36c88d38b0c3a23bf5bbf5743e9.jpg\n",
      "https://i.pinimg.com/236x/b5/87/ea/b587eaa38c450d33e4e5ddcdab39eeb4.jpg\n",
      "https://i.pinimg.com/236x/14/4b/f7/144bf7fdcdcb4dcc6e3678372ec1addf.jpg\n",
      "https://i.pinimg.com/236x/bf/6e/27/bf6e274ba45d592a12721502450cd557.jpg\n",
      "https://i.pinimg.com/236x/76/51/ad/7651ad848b50fe53e468d04cdc2471ca.jpg\n",
      "https://i.pinimg.com/236x/d4/3f/8e/d43f8e0e2faa9148ab5985181c08418d.jpg\n",
      "https://i.pinimg.com/236x/b9/84/bf/b984bf158633f8903be99455b07fb7b7.jpg\n",
      "https://i.pinimg.com/236x/ec/fc/01/ecfc013051fc2d6b22539d0b13d4a32d.jpg\n",
      "https://i.pinimg.com/236x/ca/9f/fa/ca9ffac74848ad0e92616e8704fcda98.jpg\n",
      "https://i.pinimg.com/236x/b2/a6/39/b2a639983da060be45035b113c273f90.jpg\n",
      "https://i.pinimg.com/236x/1c/4f/b5/1c4fb52207a8a6249c19016524db63e6.jpg\n",
      "https://i.pinimg.com/236x/50/e2/5b/50e25b07d73e0e8f368d6c08fa23b2cc.jpg\n",
      "https://i.pinimg.com/236x/49/ce/89/49ce890805482be1da1beaa26254f487.jpg\n",
      "https://i.pinimg.com/236x/57/da/3e/57da3e8876f2b0ebb8569111ccec9bed.jpg\n",
      "https://i.pinimg.com/236x/08/7f/d1/087fd17c28b06f240ffeec3cb5bf0a87.jpg\n",
      "https://i.pinimg.com/236x/cd/c1/71/cdc1712fe5f6f215864496c991d8cc87.jpg\n",
      "https://i.pinimg.com/236x/41/a0/d5/41a0d51bdd445cec83c63b391ce9942c.jpg\n",
      "https://i.pinimg.com/236x/b9/f5/26/b9f526069744e00ab51409ee762e17a0.jpg\n",
      "https://i.pinimg.com/236x/f2/6c/ee/f26cee9042ce41df2c16dd4ca0a7c9de.jpg\n",
      "https://i.pinimg.com/236x/87/ee/98/87ee982bee1d144ef6359cba81a03c86.jpg\n",
      "https://i.pinimg.com/236x/3c/49/af/3c49afb5852162708f5fc8198279402f.jpg\n",
      "https://i.pinimg.com/236x/cd/45/8c/cd458c5d406f3df7ad3b9cd71c9d32da.jpg\n",
      "https://i.pinimg.com/236x/b7/a3/74/b7a3746f8b02155257cc3873a37c6730.jpg\n",
      "https://i.pinimg.com/236x/f3/8a/93/f38a9397ab947627215817bee51ffa55.jpg\n",
      "https://i.pinimg.com/236x/dc/dd/6b/dcdd6b0ea207fc99f67eeffbebefaa71.jpg\n",
      "https://i.pinimg.com/236x/6c/a5/d6/6ca5d6a1679ecb12ba1d4e7ba18b264b.jpg\n",
      "https://i.pinimg.com/236x/66/f5/57/66f5574e86fe211c11b43f80d48be439.jpg\n",
      "https://i.pinimg.com/236x/1d/c8/ad/1dc8ad159fee307257c2db33994851bd.jpg\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver import ChromeService\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "import requests\n",
    "import os\n",
    "\n",
    "service = ChromeService(executable_path=\"D:\\SOFTWARE\\google driver\\chromedriver(1).exe\")\n",
    "driver = webdriver.Chrome(service=service)\n",
    "driver.execute_cdp_cmd(\"Page.addScriptToEvaluateOnNewDocument\",{\n",
    "    \"source\":\"\"\"\n",
    "    Object.defineProperty(navigator, 'webdriver', {\n",
    "    get: () => undefined\n",
    "    })\n",
    "    \"\"\"\n",
    "})\n",
    "driver.implicitly_wait(10)\n",
    "url=\"https://www.pinterest.com/PinterestUK/\"\n",
    "driver.maximize_window()\n",
    "time.sleep(2)\n",
    "driver.get(url)\n",
    "search_query = driver.find_element(\"name\", \"q\")\n",
    "search_query.send_keys(\"Rem Koolhaas\")\n",
    "search_query.send_keys(Keys.RETURN)\n",
    "time.sleep(1)\n",
    "\n",
    "js_all = 'document.documentElement.scrollTop=document.documentElement.scrollHeight'\n",
    "driver.execute_script(js_all)\n",
    "for i in range(1, 20, 2):\n",
    "    time.sleep(1)\n",
    "    j = i / 19\n",
    "    js_all2 = 'document.documentElement.scrollTop=document.documentElement.scrollHeight * %f' % j\n",
    "    driver.execute_script(js_all2)\n",
    "\n",
    "articles = driver.find_elements(By.CSS_SELECTOR, \"img.hCL.kVc.L4E.MIw\")\n",
    "num = 1\n",
    "print(len(articles))\n",
    "for i in articles:\n",
    "    try:\n",
    "        src = i.get_attribute('src')\n",
    "        print(src)\n",
    "        path = f\"./pinterest_pics\"\n",
    "        os.makedirs(path,exist_ok=True)\n",
    "        img = requests.get(src)\n",
    "        with open(f\"./pinterest_pics/{num}.jpg\",mode='wb') as f:\n",
    "            f.write(img.content)\n",
    "        num += 1\n",
    "    except:\n",
    "        pass\n",
    "driver.quit()"
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
