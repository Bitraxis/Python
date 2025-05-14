r Ucinky elektrtickeho prudu na ludsky organizmus
[*-*] Uraz => ak ludksym telom prechadza elektricky prud vacsi ako bezpecny, sposobuje fiziologicke zmeny v ludskom organizme => zavisi na case a velkosti ele. prudu.
[*-*] Bezpecny prud = (jednsomerny prud) - 25 mA,
                  = (striedavy prud) /\ 10 mA.   
[*-*] Smrtelny prud = (jednsomerny aj strediavy) - /\ 100 mA.
[?] Uraz moze nastat ak => 1. Dotyk zo zivou castou {Ziva cast je za normalnych podmienok pod napatim}.
                           2. Pri dotyku z nezivou castou, na ktoru sa dostalo napatie pri poruche. {Neziva case je za normalnych podmienok nie je pod napatim}.
[!] Nasledky urazu => 1. Ohrozujuce bez prostredne zivot cloveka (Zastava srdca a dychania, strata vedomia, porucha krvneho obehu).
					  2. Bez prostredne neohruzuju zivot cloveka (Krce, popaleniny, rozklad buniek).
## Odpor ludskeho tela
- Sucha pokozka = 5k� ohmov.
- Mokra pokozka = 2k� ohmov.
[*-*] Cinitele ktore ovplyvnuju odpor cloveka => - stav organizmu,
                                                 - vek,
												 - stav pokozky,
												 - vonkajsie/vnutorne prostriedie.
### Priestory medzi zemou a vodicom :
| Priestory  | Streidave napatie | Jednosmerne napatie |
| ---------- | ----------------- | ------------------- |
| Bezpecne   | do 50 V           | do 100 V            |
| Nebezpecne | do 24 V           | do 60 V             |
| Zv. nebez. | do 12 V           | do 24 V             |

# Prva pomoc pri uraze el. prudu
1. Vyslobodit doticneho z el. obvodu => vypnutim el.prudu pomocou vypinaca alebo vyskrutkovat poistku, vysekat kabel z skerou/kliestami z izolovanymi ruckami,
                                     => osetrit silno krvacajuce miesta a privolat lekara.
									 => Pulz a dychanie, ak nie 30:2
									 
## Hasenie poziaru el. zariadeni
- do 400 voltov:
  [-] Prasok,
  [-] Oxid uhlicity,
  [-] Freon,
  [-] Penou alebo vodou (100% isty ze zariadenie je vypnute a nieje pod napatim.
- do 1000 voltov:
  [-] Prasok,
  [-] Oxid uhlicity.
- do 10000 voltov:
  [-] Oxid uhlicity.
  
# Elektricka Praca
- Oznacenie ***W**
- Jednotka **J = Joule**
[*-*] El. praca je mierou premey el. energie na ine druhy energie.
[*-*] Vykonava sa ak presuvame naboj Q medzi dvoma miestami, medzi ktorymi je napatie.
[?] W = Q x U , W = U x I x t 
       (C)     (J) (V) (A) (s)
## Priklad
| U = 24 V | Q = 2 C |
| I = 2.1 A | U = 1200 V |
| t = 0.41 h (25 min) | W= ? J |
| ------------------- | ---- |
| W = ? J | W = Q x U |
| W = U x I x t | W = 2 x 1200 |
| W = 24 x 2.1 x 0.41 | W = 2400 J |
| W = 20.6 Wh | W = 24 kJ |
| 1 Wh = 3600 J | W = 2400 x 3600 |
| W = 20.6 x 3600 | W = 8�640�000 Wh |
| W = 74160 J | W = 864 kWh |

# Elektricky Vykon
- Oznacenie ***P**
- Jednotka **W = Watt**
[*-*] El. vykon je praca vykonana za urcity cas
[?] P = W / t
   (W) (J) (s)
[*-*] El. vykon pri stalom jednosmernom prude v obvode sa rovna sucinu prudu prechadzajuceho vodicom a napatia medzi koncami vodica.
[?] 1 W je vykon pri ktorom sa rovnomerne vykona praca 1 J za 1 s. Meriame ho wattmetrom alebo multimetrom. 
[?!] P (1W) = W (1J) / t (1s) 
[*-*] Udaj o vykone najdeme na rezistoroch, uvadza sa nim stratovy vykon, ktory sa v rezistor moze zmenit na teplo.
[*-*] Dlhodobe prekrocenie stavoveho vykonu vedie k zniceniu rezistora.

# Rezistory
[*-*] Patri medzi pasivne prvky el. obvodu.
[*-*] Zakladna vlastnostou je jeho odpor = Fyz. vlastnost , tora je dana stukturou materialu a jeho rozmermi. 
[*-*] Ich zakladnou funkciou je klast odpor pretekajucemu prudu. Cim vacsi odpor tym prud mensi.
[?] Pouzivaju sa na obmedzenie prudu a napatia, pripadne na ich regulaciu.

## Charakteristike vlastnosti:
[*-*] Menovita hodnota: | pismenovy kod | farebny kod |
                        | ------------- | ----------- |
                        | - 1k2 = 1200 Ohmov | 4 kruzkovy |
                        | - 0.1 M = 0.1 MOhmu | 5 kruzkovy |

[*-*] Skutocna hodnota: je hodnota odporu zistena meranim ktora sa moze lisit od danej menovitej hodnoty pomocou danej toleracie od vyrobcu.
[*-*] Elektricka pevnost: urcuje maximalne napatie na ktore moze byt rezistor napojeny abi sa neposkodil a sucasne nezmenil menovitu hodnotu. 
[*-*] Menovita zatazitelnost (Stratovy vykon): hodnota vykonu vo wattoch, ktoru udava vyrobca, aky maximalny prud moze pretekat rezistorom bez toho aby sa rezistor neposkodil.
[?] P = R x I^2 I = *^2 P/R (1/150) = I =  0.0816 A 
[*-*] Teplotny sucinitel: vyjadruje zmenu hodnoty odpuru vplyvom teploty, pri zvyseni teplotu sa moze menit aj odpor rezistora.

### Delenie rezistorou
- Linearne Rezistory: Su to rezistory pri ktorych hodnota zostava konstantna aj ked sa menia hodnoty v obvode.
- Nelinearne Rezistory: Su to rezistory ktore sa na zakladne hodnout v obvode menia (Svetlo,teplo,napatie).
    - Thermistor: Jeho odpor sa zavysle meni od teploty. Rozdelenie: | Kladny teplotny sucinitel | Zaporny teplotny sucitinel |
                                                                     | ------------------------- | -------------------------- |
                                                                     | Oznacenie: PTC | Oznacenie:  NTC |
                                                                     | Hodnota odporu rastie od teploty | Hodnota klesa od teploty |
    - Fotorezistor: Hodnota odporu zavisy od osvetlenia, cim viac svetla tym hodnota odporu klesa.
    - Varistor: Hodnota odporu sa meni od zavislosti velkosti napatia. 


### P�jkovanie
- Rozdelenie
    - M�kk� na sp�jkovacie body kde nie je spoj machanicky nam�han� a nen� vystaven� vzsok�m teplot�m. Vyzna�uje sa st�limy a dobr�mi el. vlastnostami.
    - Tvrd� nad 450C
- Sp�jkova�ki
    - Pi�to�ov� (transformatorov�) = hrot sa r�chlo zahreje. Mal� mno�stvo sp�jky bez toho aby sa to prep�lilo. S� ve�mi hrub�.
    - Mikro = s� v�ade (odporov�)
- Pr�prava p�jkovania = hrot mus� by� o�isten�
- Sp�jka kovov� materi�l (c�n a olovo)
- Tavidla halvn� �loha je odstr�nit oxidov� povlak z povrchu oxidov�ch �ast� tavidlo musi mat v priemere nizsiu teplotu tavenia nez o 100C ako spajka aby sa spajkovane plochy ocistili skor nez sa spajka roztavy. Kolofonia je najcastejsie tavidlo, ked ochladne tak vznikne skrupinka
#### Priprava spajkovanych casti pred spajkovanim
    - Spajkovane plochy su tie casti materialu, ktore sa pri spajkovani netavia
### Spajanie do dosky plosnych spojov (DPS)
    - Suciastky sa zapajaju od najjednoduchsich (pasivnych) po zlozite (aktivne), smerom hore. 3-4s sa spajkuje

# Dioda
anoda +
kathoda -
material> kremikove / germaniove
vyhotovenie> hrotova, plosna, dioda s privarenym zlatym hrotom
pouzitie> usmernovacia, stabilizacna (zemerova), tunelova, kapacitna (varikap)
oznacenia> A=dioda vseobecne B=kapacitna E=tunelova P=photodiody/phototransistory R=viacvrstvove diody Z=zemerova Y=usmernovacia
Zemerova= zaverny smer po zvyseny napatia k nedeskruktivnemu prierezu (skoro neznicitelna), na stabilizaciu napatia, po prekroceni sa zaverny prud rychlo zvacsuje, ale napatie privedene na diodu cez ochranny rezistor sa meni malo

# Polovodi�e
- Germani�m �tr�ktura do kry�t�u (pravidelne usporiadan�), spr�va sa ako izolant
- Fyzikalna podstata cinnosti polovodicovych obvodovoych suciastok
- Charakteristicky znak: velka zavislot merneho odporu od cistoty latky
- Z rastucov teplotov stupa a podstatne zavisi od pritomnosti cudzich prvkov v kristalovej mriezke polovodica.
- Polovodice: Diody, tranzistory, integrovane obvody
## Vlastny
- atomy GE a kremika su 4 mocne, pravidelne usporiadane v kristalovej mriezke, kazdy atom susedi z 4 dalsimi atomamy
- Dvojica susediacich atomov ma vzdy 2 spolocne atomy
- Pri nizkej teplote velkej mriezky nie su volne elektorny, a kristal cisteho germania a kremika sa sprava ako izolant
## Nevlastne
- V tychto polovodicoch sa cast atomov kristqalovej mriezky vlastneho polovodica nahradza atomamamy primesi
## Donor (Patmocne) - darca volnych elektronov - Arzen (As)
## Akceptory (Trojmocne) - prijemnca volnych elektronov - Indium (In)
- Germanium z primesou patmocneho prvku, ma 5 valecnych elektronov, prevladajuce nositele su zaprone nabyte, takyto nevlastny ma elektronovu vodisvost a nazyvame ho polovodic N.
- Germanium z primesou trojmocneho prvku, vznika v kristalovej mriezke jednu neobsadenu vazbu do ktorej moze prejst iny volny elektron, je nositel kladneho ele. naboja, volame ho polovodic P.
- Usmernovacia dioda usmernuje striedavy na jednosmerny
# Tranzistory
- Maju 2 priechody PN
- Stavy bipolarnych tranzistorov - 1. PNP
                                   2. NPN
- Druhy tranzistorov : 1. bipolarne > obidve polarity
                       2. unipolarne > riadene ele. polom
- Struktura tranzistora sklada z 3 oblasti typu PN ktore mozu byt usporiadane v poradi PNP a NPN
- Tranzistor zhotovime tak ze na protilahle strany dosticky vodica N nanesieme proti sebe malemnozstvo trojmocneho prvku.
- Po jeho roztopeni a zliati z materialom zakladnej dosticky vytvoria oblasti z vodivostou P a an rozhrani vzniknu 2 PN priechody.
- Zamenou materialou vznikne tranzistor NPN>
- PN priechod na strane kolektora je rozmerovo vacsi, lebo na strane kolektora sa pracuje s vacsimi vykonmi

# Kondez�tor
    - zvitkov� m� polaritu, dlh�ia plus
    - keramick� m� rovnako dlh� no�i�ky
    - Je dvojp�lov� reaktan�n� s��iastka, ktor� realizuje elektrick� veli�inu - kapacitu, �o je schopnos� akumulova� ele. n�boj
## Princ�p fungovania kondez�toru
    - sklad� sa z dvoch vodiv�ch dosiek odelen�ch dielektrikom (izolant)
    - na ka�d� z dosiek sa priv�dzaj� el. n�boje opa�nej polarity, ktor� sa navz�jom pri�ahuj� el. silou
    - dielektrikum medzi doskami nedovol� aby sa �astice z n�bojom dostali do kontaktu a t�m do�lo k vybitiu ele. n�boja
### Z�kladn� vlastnosti
    - kapacita - mno�stvo n�boje ktor� je schopn� kondez�tor nahromadi� pri hromadnom nap�t�
    - reaktancia - kondez�tor trvale jednosmern� pr�d nevedie / neprep��ta, kladie mu nekone�n� odpor. Striedav�mu pr�du kladie kone�n� / kvalitat�vne in� odpor
    - nap�tie - rovnak� ako je aj na zdroji
#### Typy:
    1. Elektrolitick� - medzi dve hlinikov� f�lie (elektrod�dy) je odlo�en� pijav� materi�l (Papier) napusten� elektrolitom. Celok je zrolovan� a je vlo�en� do valcov�ho hlinikov�ho p�zdra z dvoma v�vodmi, nespr�vne zapojenie polarity po�kod� s��iastku
    2. Keramick� - tenk� pl�t kermaick�ho dielektrika je potiahnut� z dvoch str�n kovovou vrstvou, celok je zapojen� kontaktov je zaliati to izola�nej hmoty, nemaj� ur�en� polaritu
    3. Tantalov�
    4. F�lov�
    5. Premenliv�

# Zosil�ova�e
## Sp�tn� v�zba
 - D�le�it� vlastnos� sp�tnej v�zby - ��m m� zosil�ova� **v俿ie zosilnenie �o znamen�, �e tranzistorov� bloky maj� ve�k� rozkmit nap�tia**, *pohybuj� sa ich pracovn� body nie po priamke ale po krivke*. Ka�d� pohyb pracovn�ho bodu je ***nechcen�***, preto pri n�vrhu zosil�ova�a sa sna��me rozdeli� nap�tov� zosilnenie na ***viac*** zosil�ovac�ch blokov a zn��i� celkov� zosilnenie. -> Pou�itie ***viac*** tranzistorov, a t�m st�pa aj zlo�itos� zapojenia. 
 - **EXTRA JEDNODUCH� ZOSIL�OVA�** = nem��e dosiahnu� excelentn�ch vlastnost�, preto kvalitn� koncov� zosil�ova�e obsahuj� aj 70 tranzistorov na jeden kan�l.
### Rozdelenie:
    1. Pod�a typu:
        a. Kladn�
        b. Z�porn�
    2. Pod�a frekvencie:
        a. Frekven�ne nez�visl�
        b. Frekven�ne z�visl�
    3. Pod�a obvodovej veli�iny:
        a. Nap�ov�
        b. Pr�dov�
    4. Pod�a zapojenia:
        a. S�riov�:
            Nap�ov�
            Pr�dov�
        b. Parareln�:
            Nap�ov�
            Pr�dov�
    5. Pod�a pou�it�ho prvku:
        a. Kapacitn�: Kondez�tor (Capacitor - Kapacita)
        b. Induk�n�: Cievka (Ele.mag. indukcia)
        c. Odporov�: Rezistor (Odpor)
    6. Pod�a p�sobenia: 
        a. Priama (100% v�konu)
        b. Nepriama (nen� na 100%)
 - V koncovom zosil�ova�i sa vyu��va Priama, Z�porn�, Frekven�ne z�visl� a Pararelne nap�ov� 
## Koncov� stupe�
 - Jeho �lohou je zosilni� sign�l pr�dovo.
 - V�eobecne je tvoren� bipol�rnymi & unipol�rnimi tranzistormi.
 - **Komplement�rne**: S� tvoren� dvoma tranzistormi = NPN + PNP. -> ***�ASTO POU��VAN�***
 - **Quasikomplement�rne**: Tvoren� dvoma tranzistormi rovnak�ho typu = 2 NPN alebo 2 PNP (�astej�ie). -> ***U� NIE TAK� �AST�***
## Satur�cia
 - Nekone�n� zosilnenie neznamen�, �e na v�stupe je nekone�no ale znamen� to, �e viac ako pod minimum alebo nad maximum v�stup �s� nem��e, **ke� sa dosiahne minimum alebo maximum hovor�me, �e zosil�ova� je saturovan�** -> sign�l sa *orez�va*.
 - V�aka nej m��eme opera�n� zosil�ova� zapoji� ako **Kompar�tor** ==> obvod pomocou ktor�ho m��eme indikova� �asov� okamih, v ktorom ur�it� sign�l nadonudne ur�it� stanoven� nap�ov� hladinu. 

# �asovac NE 555
- Je to integrovan� obvod, ktor� sa naj�astej�ie pou��va ako �asovac
- Obvod je vysoko univerz�lny, a okrem �asovania je ho mo�ne pou�i� na generovanie zvuku, meranie kmito�tov, blikania a podobne.
- Ozna�ie NE 556 => 2x NE 555
- Obvod sa sklad� z jedn�ho klopn�ho obvodu, ktor� je na v�stupe a dvoch kompar�torov, klopn� obvod = je to ele. obvod, ktor� m��e nadob�da� dva odli�n� nap�ov� stavy, v zmene jedn�ho stavu do druh�ho doch�dza skokovo.
- GND = Ground = uzemnenie
- TRIG = Trigger = sp���anie
- OUT = Output = výstup
- RESET = Reset = vynulovanie toho predch�dzaj�ceho stavu
- CTRL = Control = riadenie napätia
- THR = Threshold = prah, minimálne napätie potrebné na funkčnosť
- DIS = Discharge = vybýjanie
- Vcc = kladné napätie, 4,5V ~ 15V


