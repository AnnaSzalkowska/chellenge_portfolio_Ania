#  Zadanie: konfiguracja oprogramowania

### Podzadanie 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?

Zdecydowałam się wziąć udział, ponieważ znalazłam tu to, czego szukałam. Od złożonego kursu przez mentoring.  
Duższy czas temu zaczynając tworzyć aplikacje od strony wizualnej (skończyłam studia graficzne) poszłam o krok dalej i zaciekawił mnie cały proces tworzenia.   
Interesuję się testowaniem manualnym, ale bardzo chcę zrozumieć proces testowania automatycznego.   
Czuję, że rzucam się trochę na głęboką wodę, ale powrót do systematycznej nauki i nowe wyzwania dobrze mi zrobią 😊 

### &nbsp; Anna Szałkowska 

&nbsp;
&nbsp;

### Zadanie dla chętnych. Nie samymi testami automatycznymi człowiek żyje
### &nbsp; &nbsp; &nbsp; 8 punktów 
___
#  Zadanie 2: selektory
**Scotus_Panel**
* //*[text()="Scouts Panel"]  
* //*[@id="__next"]/form/div/div[1]/h5  
* //h5   `nie wiem czy nie za malo konkretny 😅 `  
* //h5[@class="MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom"]  

**Login_Label**  
* //*[@id="login-label"]  
* //label[@id="login-label"]  
* //div/form/div/div[1]/div[1]/label

**Password_Label**  
* //*[@id="password-label"]  
* //label[@id="password-label"]  
* //div/form/div/div[1]/div[2]/label  

**Listbox_English**  
* //*[@id="__next"]/form/div/div[2]/div/div  
* //*[@aria-haspopup="listbox"]  
* //*[text()="English"]  

**Button_Label_Sign_In**  
* //*[text()="Sign in"]  
* //*[@class="MuiButton-label"]  
* //span[1]  

**Blue_Button**
* //span[2]
* //span[@class="MuiTouchRipple-root"]
* //*[contains(@class,"MuiTouchRipple-root")]

**Elevation1_Root**
* //*[@id="__next"]/form/div
* //*[contains(@class, "elevation1")]
* //*[@class="jss1"]/div