# 3 Maart 2026 21:40 - 21:59
Begonnen aan het project. Gestart met de tutorial te volgen en toen besefte ik dat ik niet de juiste Python had geïnstalleerd. Deze was niet compatibel met pygame, dus moest ik de juiste zoeken en installeren. Eerst was dit lastig, omdat hij altijd mijn andere Python bleef herkennen. Uiteindelijk opgelost via Python: Select Interpreter in VS Code.

# 4 Maart 2026 17:00 - 18:15
Ik merk dat ik veel kleine dingen overzie, zoals inputs dubbel typen of komma’s missen. Het is altijd even zoeken om dat te zien, ook al toont de terminal meestal waar de fout ongeveer zit. De oplossing is meestal gewoon beter kijken en de foutmelding rustiger lezen.

# 5 Maart 2026 18:25 - ?
Tijd niet goed bijgehouden. Ik werd opnieuw gefrustreerd omdat mijn kaarten niet op beeld kwamen. Ik ben dan gestopt, omdat ik merk dat ik niet helder denk als ik gefrustreerd ben. Achteraf bleek het weer om een klein detail te gaan.

# 7 Maart 2026 15:17 - ?
Doel was om het foutje te vinden waar ik frustraties bij had. Alweer een klein detail over het hoofd gezien. Ik moet beter opletten bij het typen van commands en waar ik dingen in de code zet. Tijd uit het oog verloren maar zeker 2 uur bezig geweest. In mijn geval zat het probleem bij het berekenen van de kaarten. De oplossing was uiteindelijk de code op de juiste plaats zetten.

# 8 Maart 2026 16:00 - 17:00
Eindelijk afgerond met de tutorial te volgen. Ja, ik kon de code gewoon kopiëren van GitHub, maar ik wou dat liever vermijden zodat ik toch iets leer. Blind volgen zonder echt te begrijpen wat je doet maakt het soms zelfs moeilijker. Mijn focus op het project zal dus zijn dat ik er mijn eigen spin aan geef, maar ook begrijp wat ik juist doe.

# 8 Maart 2026 19:06 - 21: 00
Doel is nu om een Pacman-spel te maken met als basis de blackjack. Ik kies hiervoor omdat Pacman nostalgisch is voor mij en ik de regels van een kaartspel niet zo goed ken. Ik heb de basis al roze gemaakt voor een girly aesthetic, een maze ingevoerd en een aantal blackjack-termen veranderd. De oplossing hier was om de structuur van blackjack te behouden, maar de inhoud te vervangen.

# 9 Maart 2026
Ik was hieraan begonnen op 9 maart, maar ben vergeten mijn logboek-update te saven. Ik heb de basis van het spel gemaakt: maze uitgebreid, Pacman toegevoegd en 1 spookje. Eerst gebruikte ik simpele cirkels voor de karakters. Daarna begon ik collision toe te voegen, omdat mijn Pacman over de muren heen kon. Ook bewoog mijn spookje eerst niet. Dat heb ik opgelost door online op te zoeken hoe beweging en botsingen werken in pygame.

# 13 Maart 2026 17:20 - 22:03
Verder gewerkt aan mijn Pacman-spel op basis van de structuur van mijn blackjack-project. Ik heb de code stap voor stap simpeler gemaakt zodat ik beter snapte wat elke functie deed. Ook heb ik richtingen aangepast naar woorden zoals "right" en "left" in plaats van cijfers, omdat dat duidelijker is. Daarna veel aan de vormgeving gewerkt. Ik heb de pellets veranderd naar hartjes, Pacman groter gemaakt en een zachtere gele kleur gegeven, en de spookjes veranderd van simpele cirkels naar echte spookvormen. Ook extra spookjes toegevoegd en kleuren aangepast zodat ze beter zichtbaar zijn tegenover de roze maze.

Verder heb ik een winconditie toegevoegd waarbij de speler wint als alle pellets op zijn. Ik heb ook fruitjes toegevoegd die een power mode activeren, waardoor de spookjes tijdelijk blauw worden en Pacman ze kan opeten. Dit werkte eerst niet goed, dus ik moest fouten zoeken in mijn collision-logica en hoe ik de spookjes tekende. Uiteindelijk opgelost door die functies aan te passen. Ten slotte heb ik gewerkt aan de presentatie van het spel: een startscherm met de titel PACMAN IN PINKLAND!, een pixel font toegevoegd (gedownload van een andere site), grotere GAME OVER en YOU WIN! teksten, en een pauzemenu gemaakt. Ik merk dat ik functies, variabelen en de main loop nu beter begin te begrijpen, ook al heb ik nog moeite met dingen op de juiste plaats te zetten. 

# 14 Maart 2026
Ik heb de kersen gemaakt door een aparte functie te schrijven die meerdere simpele vormen combineert, zoals cirkels en lijnen. Zo kreeg ik een fruitvorm in plaats van gewoon een rood bolletje. 

# 16 Maart 2026 17:18 - 18:15

Ik heb pacman zijn mondje getekent zodat het een animatie heeft. Ik heb het nog steeds moeilijk met de juiste positie te vinden voor bepaalde codes. Zoals de video die ik gisteren gekeken heb, probeer ik, test ik, en lees ik aandachtig wat de error zegt in het terminaal en probeer ik het zelf te fixen.Ik heb de positie van mijn kersen in de code aangepast. Ik tekende ze na het bord, maar het oogt beter als ik ze boven het bord zet. 

# 16 Maart 18:15 - 19:00 

Geprobeerd om een tweede level toe te voegen. Hiervoor heb ik mijn huidige bord opgesplitst in level_1 en level_2, zodat ik later tussen levels kan wisselen. Ik heb ook gekeken hoe ik dat logisch kon laten gebeuren via check_win() en hoe een nieuw spel terug op level 1 moet starten via reset_game().

In het begin werkte dit niet goed en liep mijn spel vast. Uiteindelijk bleek dat mijn variabelen niet op de juiste plaats stonden in de code. Nadat ik dat had aangepast en board = level_1 op de juiste plek had gezet, werkte het systeem opnieuw zoals bedoeld. Verder ook een level text midden boven aan toegevoegt. Ik wil het niet te veel verder compliceren dan het al is, dus stuur ik dit naar de leerkracht voor feedback.

# 24 Maart 16:37 FEEDBACK 
Feedback gekregen over mijn project. Ik heb het eens na gelezen en ga akkoord met de commentaar. Inderdaad, ik plaats comments voor bepaalde functies terwijl ik de functie zelf gewoon duidelijker had kunnen maken. Ik leer ook uit de kortere, duidelijkere geschreven functie voorbeelden die gegeven werden. 

Er werden een aantal vragen gesteld, waarop ik hier de antwoorden schrijf in het geval dat deze worden gevraagt op het examen zelf.

# Elke ghost is een dictionary met x, y, startpositie, richting en kleur.
# [dn] Waarom een dictionary?
Ik gebruikte een dictionary omdat een ghost meerdere eigenschappen heeft zoals positie, richting en kleur, en die ik gemakkelijk per naam wou opslaan en aanpassen. 

# [dn] Die TILE + TILE // 2 komt heel vaak voor. Waarom geen makkelijker te typen variabele van maken?
Goede opmerking. Ik heb hier zelf niet echt stil bij gestaan en onwetend dingen moeilijker voor mezelf gemaakt. Ik durf niet zo goed dingen 'veranderen', dus blijf ik bij de gecompliceerde versie omdat ik het beter 'ken'. 

Het doel is nu om de feedback te gebruiken om de code qua structuur beter te maken en dit in de toekomst ook te doen.

# Feedback verwerkt: constanten duidelijker gemaakt, kleuren consistent in hoofdletters,
# TILE_CENTER toegevoegd en ghosts omgezet van dictionary naar class.
