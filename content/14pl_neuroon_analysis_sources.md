Title: Analiza NeuroOna - źródła
Date: 2016-06-27
Slug: neuroon-analysis-sources
Lang: pl
Tags: neuroon, signal analysis, science, open notebook
Translation: true

### Edycja 29.09.2016

Analiza wraz ze wszystkimi danymi dostępne są na moim [Githubie](https://github.com/pawelchojnacki/sleep_project).

<a 
    href="/images/14_neuroon_signals/examination/examination_bed.jpg"
    target="_blank">
<img
    title="NeuroOn na łóżku do polisomnografii"
    class="article-img"
    src="/images/14_neuroon_signals/examination/examination_bed.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

### NeuroOn dzisiaj

Dość długo nosiłem się z założeniem tego bloga, jednak czułem, że nie miałem nic wartościowego do powiedzenia. Zmieniło się to dopiero, gdy usłyszałem o polskim startupie NeuroOn[^1]. Mój pierwszy post[^2] dotyczył właśnie nadziei jakie wiązałem z maską i sceptycyzmu wobec braku naukowego podejścia twórców. Zakończyłem go słowami:

> Maska NeuroOn z pewnością nie działa tak, jak jest reklamowana - nie używa EEG. Może z bardzo niską dokładnością wykrywać fazę REM, jednak nie pozwoli na rzetelną analizę snu. Ogromna część populacji i tak nie osiągnie snu polifazowego, gdyż ich mózgi po prostu tak nie działają. Maska z pewnością też nie pozwoli na świadome śnienie. Będzie tylko mało przydatną zabaweczką do odłożenia na półkę po kilku nocach.

Nie był to jedyny głos krytyki - o masce sceptycznie wypowiadali się także @takingapartcats[^3], neurocritic[^4] czy dr Adam Wichniak[^5]. Argumentację przeciw obietnicom NeuroOna podzielić można na dwie grupy: wątpiącą w możliwość maski do zebrania wiarygodnego sygnału EEG oraz stwierdzającą, iż sen polifazowy nie jest możliwy dla większości populacji.

Minęły jednak dwa lata, maska weszła na rynek pivotując i porzucając swoje obietnice o śnie polifazowym[^6]. Zastąpione zostały one terapią światłem, pomocą w radzeniu sobie z jetlagiem i zbieraniu analityki snu[^7]. Było to niewątpliwie rozsądne działanie, odbierające połowę argumentów sceptyków działania maski - jednak w oczach wielu klientów całkowicie zaprzepaszczające ideę NeuroOna[^8].

Nie chcę w tym miejscu wdawać się w dyskusje na temat możliwości wywołania głębokiego i satysfakcjonującego efektu świadomego snu[^9] u każdego użytkownika NeuroOna, szczególnie w świetle badań mówiących o osobniczym zróżnicowaniu predyspozycji do niego[^10]. Moim głównym problemem z maską jest wciąż kontrowersyjna jakość sygnału EEG, jaka może być zebrana z:

 - trzech
 - suchych elektrod
 - położonych bezpośrednio nad łukiem brwiowym
 - w masce mogącej poruszać się w trakcie snu

O ile można by było dyskutować z jakością sygnału w każdym z tych podpunktów oddzielnie (co czynił NeuroOn na swoim blogu w odpowiedzi na moje poprzednie zarzuty[^11]), kombinacja wszystkich czterech czynników może skutkować jakością sygnału całkowicie nie nadającą się do analizy EEG. O ile NeuroOn do wykrycia fazy snu korzysta również z EOG - elektrookulogramu (jakość którego również może być wątpliwa), termometru, pulsoksymetru i akcelerometru - wielu użytkowników opisuje[^12] jego działanie jako wyjątkowo niedokładne. W świetle wszystkich tych okoliczności wciąż pozostaję sceptyczny wobec tego, czy NeuroOn naprawdę *działa* w sposób, w jaki jest reklamowany.

### Analiza NeuroOna

Na przestrzeni ostatnich dwóch lat wielokrotnie deklarowałem chęć przeprowadzenia solidnej analizy maski - i z wielkim entuzjazmem przyjąłem zaproszenie Kamila Adamczyka i zespołu Intelclinic, którzy w tym roku użyczyli mi modelu deweloperskiego NeuroOna na potrzeby testów. Jakkolwiek nie zgadzam się z nimi w wielku kwestiach, decyzja ta i otwartość na zewnętrzną analizę są niewątpliwie godne szacunku.

Model deweloperski maski jest tak naprawdę zwykłym egzemplarzem produkcyjnym - płytką PCB zanurzoną w silikonie - z dodatkowymi kabelkami pozwalającymi na przebicie się przez silikon do pinów danych na płytce.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_main_unit_front.jpg"
    target="_blank">
<img
    title="Płytka NeuroOna - przód"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_main_unit_front.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Z przodu widzimy trzy elektrody (wg opisu produktu pokryte warstwą złota[^13] - nie sprawdzałem tego samodzielnie nie chcąc uszkodzić maski), pulsoksymetr i termometr w charakterystycznym wycięciu, LEDy w narożnikach oraz jedyny guzik znajdujący się w samym środku płytki. Elektrody razem dają jeden kanał różnicowy - środkowa jest masą.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_main_unit_back.jpg"
    target="_blank">
<img
    title="Płytka NeuroOna - tył"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_main_unit_back.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Tylna część płytki NeuroOna nie zawiera elementów charakterystycznych. Z mojego rozumienia "test unit" oznacza po prostu model wyprodukowany na potrzeby Intelclinic przed produkcją masową, posiadający identyczne parametry.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_foam_back.jpg"
    target="_blank">
<img
    title="Pianka NeuroOna - tył"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_foam_back.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Maska z gumką, którą NeuroOn przymocowany jest do twarzy użytkownika. <del>Niestety, nie posiada regulacji i dla osób z dużą głową (jak ja) może być obcisła / powodować chęć zmiany pozycji urzadzenia w nocy, co bardzo źle wpłynie na sygnał.</del> Edit: NeuroOn posiada regulację długości gumki - w tym calu należy rozebrać gąbkę, odrywając przypiętą na rzep przednią część i zmienić położenie uchwytu paska (również zamocowanego na rzep). Dzięki Karol!

<a 
    href="/images/14_neuroon_signals/mask/neuroon_foam_front.jpg"
    target="_blank">
<img
    title="Pianka NeuroOna - przód"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_foam_front.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Przód maski wykonany jest z gąbki. Płytka PCB wkładana jest w otwór widoczny na górze, gdzie leży dość dobrze, jednak nie jest przymocowana żadnym rzepami, magnesami czy gumkami. Poprawnie założona nie powinna wypaść w nocy - maska sprawia, że elektrody przylegają bardzo ściśle i zostawiają odciski na skórze (zdjęcia później).

<a 
    href="/images/14_neuroon_signals/mask/neuroon_assembled_noleds.jpg"
    target="_blank">
<img
    title="Złożony NeuroOn"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_assembled_noleds.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Maska z włożoną płytką - LEDy wypadają dokładnie w miejscach wycięć gąbki.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_assembled_led.jpg"
    target="_blank">
<img
    title="Włączony NeuroOn"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_assembled_led.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Po włączeniu płytki zapalają się niebieskie LEDy. Bardzo subiektywnie nie lubię tego, jak działają w trybie wybudzania - kiedy włączają się na kilka minut przed planowanym wybudzeniem światło w ciemności wydaje się oślepiające,natomiast po zdarciu maski z twarzy okazuje się, że pokój z odsłoniętym oknem jest znacznie jasniejszy, przez co dostaję porannego bólu głowy.

Maski używałem w trybie deweloperskim - z graficznym menadżerem napisanym w Javie przez zespół Intelclinic, którego kodem - ani binarkami do analizy danych - nie mogę się jednak podzielić wedle naszej umowy. Oznacza to także, że nie korzystałem z aplikacji NeuroOna na telefon. Zastąpiły mi ją dedykowany moduł bluetooth na USB oraz dwa kabelki podpięte pod debugger.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_debug_ground.jpg"
    target="_blank">
<img
    title="Uziemienie w trybie debugowania"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_debug_ground.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Podłączenie masy pod port microUSB w NeuroOnie. Sam w sobie służy jedynie do ładowania i nie ma podpiętego data pina.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_debug_nochannel.jpg"
    target="_blank">
<img
    title="Pin z danymi"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_debug_nochannel.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Pin danych znajduje się na płytce - jest to pierwszy od lewej pin pod silikonem, przez który należy się przebić (dedykowaną igłą w krokodylku), aby uzyskać dostęp do danych z maski.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_debug_data.jpg"
    target="_blank">
<img
    title="Wkłucie się w pin z danymi"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_debug_data.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Poprawnie założony krokodylek (tylko wygląda na krzywy),

<a 
    href="/images/14_neuroon_signals/mask/neuroon_debug_full.jpg"
    target="_blank">
<img
    title="Cały zestaw do debugowania"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_debug_full.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

NeuroOn gotowy do podpięcia do komputera i wejścia w tryb debugowania. Pozwala on na uruchomienie podstawowych trybów z aplikacji, oraz co najważniejsze - zapisywania i pobierania sygnału. <del>Software niestety wymagał odpalenia go z uprawnieniami roota - czego nie robię dla żadnej graficznej aplikacji której kodu nie da się przejrzeć.</del> W dalszych badaniach posługiwałem się więc dedykowanym pendrive z Ubuntu. Edit: Jak poinformował mnie Witold Granicki z Intelclinic, oprogramowaniu wystarczy dostęp do portów na linuksach, co dałoby się rozwiązać i bez roota.

### Badanie

Po wykonaniu kilku testowych całonocnych nagrań NeuroOnem postanowiłem przeprowadzić rzetelny eksperyment, który pozwoliłby mi z dużą pewnością odpowiedzieć na pytanie: *czy zbierany przez maskę sygnał jest wystarczająco dobrej jakości, by posiadając moc obliczeniową smartphone'a móc w czasie rzeczywistym wykrywać fazę snu na podstawie EEG, EOG, pulsoksymetru, termometru i akcelerometru?* Kickstarterowe obietnice IntelClinic mówiły właśnie o masce będącej w stanie wybudzić nas w odpowiednim momencie - a więc muszącej wiedzieć, w jakiej fazie snu jesteśmy w danej chwili.

<a 
    href="/images/14_neuroon_signals/examination/doorsign.jpg"
    target="_blank">
<img
    title="Pracownia zaburzeń snu"
    class="article-img"
    src="/images/14_neuroon_signals/examination/doorsign.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

W tym celu postanowiłem zestawić NeuroOna z profesjonalnym polisomnografem w warszawskim Ośrodku Medycyny Snu Instytutu Psychiatrii i Neurologii[^14]. Po kilku miesiącach oszczędzania udało mi się wynająć łóżko w Ośrodku na dwie noce - Podczas pierwszej z nich wykonane były:

 - EEG
 - EOG
 - EKG
 - badanie oddechu (flow)
 - nasycenia tlenu w krwi
 - ruchów klatki piersiowej
 - ruchów nóg

Druga noc zawierała już tylko:

 - EEG
 - EOG
 - EKG

Podczas obu zbierałem też równolegle sygnał z NeuroOna, którego umiejscowienie na twarzy nie sprawiało zbytniego problemu - żadne elektrody wykorzystywane w profesjonalnych badaniach nie znajdują się zaraz nad łukiem brwiowym.

<a 
    href="/images/14_neuroon_signals/examination/examination_bed.jpg"
    target="_blank">
<img
    title="NeuroOn na łóżku do polisomnografii"
    class="article-img"
    src="/images/14_neuroon_signals/examination/examination_bed.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

NeuroOn na łóżku, gdzie wykonywane będą badania. Pomieszczenie nie było w żaden sposób ekranowane i nie znajdowało się pod klatką Faradaya, przez co pasmo 50Hz będzie wycięte z końcowego sygnału ze względu na rezonans z siecią elektryczną w ścianach.

<a 
    href="/images/14_neuroon_signals/examination/testing_suite.jpg"
    target="_blank">
<img
    title="Programowanie NeuroOna"
    class="article-img"
    src="/images/14_neuroon_signals/examination/testing_suite.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Programowanie płytki przed pierwszą nocą, aby nie włączała trybu wybudzania przed ośmioma godzinami i zbierała cały sygnał. Przed każdym nagraniem dobrze jest też nadpisać cąłą wolną pamięć zerami (a przynajmniej tak rozumiem opcję CLEAR w oprogramowaniu).

<a 
    href="/images/14_neuroon_signals/examination/amplifier_front.jpg"
    target="_blank">
<img
    title="Wzmacniacz - przód"
    class="article-img"
    src="/images/14_neuroon_signals/examination/amplifier_front.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

Przez obie noce używany był wzmacniacz AURA PSG firmy GRASS[^15] zbierający sygnały z częstotliwością 200Hz. Wedle informacji udzielonych mi przez Ośrodek jest to standard we w pełni profesjonalnych badaniach lekowych.

<a 
    href="/images/14_neuroon_signals/examination/amplifier_back.jpg"
    target="_blank">
<img
    title="Wzmacniacz - tył"
    class="article-img"
    src="/images/14_neuroon_signals/examination/amplifier_back.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Wszystkie sygnały zapisywane były bezpośrednio do komputera w Ośrodku z pominięciem pamięci wewnętrznej urzadzenia.

<a 
    href="/images/14_neuroon_signals/examination/1020.png"
    target="_blank">
<img
    title="Kanały 10-20"
    class="article-img"
    src="/images/14_neuroon_signals/examination/1020.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Elektrody użyte w EEG w obu badaniach: A1 i A2, F3 i F4, C3 i C4, O1 i O2, Fz i Cz jako uziemienie oraz referencyjna. Oprócz nich zostały użyte elektrody EOG1 i EOG2 (EOG), CHIN1, CHIN2 i CHIN3 (na brodzie, do wykrywania grymasów twarzy) oraz ECG na klatce piersiowej.

<a 
    href="/images/14_neuroon_signals/examination/night_1_electrodes_front.jpg"
    target="_blank">
<img
    title="Rozmieszczenie elektrod - przód"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_1_electrodes_front.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

Noc pierwsza - umiejscowienie elektrod z frontu - widoczne są EOG1 i EOG2 przy oczach, Fz na czole, CHIN1, CHIN2 i CHIN3 pod brodą, F3 i F4 tuż nad linią włosów.

<a 
    href="/images/14_neuroon_signals/examination/night_1_electrodes_left.jpg"
    target="_blank">
<img
    title="Rozmieszczenie elektrod - lewa strona"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_1_electrodes_left.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

Widoczne elektrody CHIN1, EOG1, F3, C3 i O1. Kawałek kleju za uchem trzyma jedynie kable.

<a 
    href="/images/14_neuroon_signals/examination/night_1_electrodes_back.jpg"
    target="_blank">
<img
    title="Rozmieszczenie elektrod - tył"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_1_electrodes_back.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

Widoczne O1 i O2 z tyłu głowy, Cz na szczycie czaszki.

<a 
    href="/images/14_neuroon_signals/examination/night_1_electrodes_right.jpg"
    target="_blank">
<img
    title="Rozmieszczenie elektrod - prawa strona"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_1_electrodes_right.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

Analogicznie z prawej strony głowy: CHIN3, EOG2, F4 i C4, O2.

Po przymierzeniu maski Fz należało przesunąć trochę do góry, by plastry przytrzymujące ją nie zasłaniały elektrod NeuroOna. 

<a 
    href="/images/14_neuroon_signals/examination/night_1_lying.jpg"
    target="_blank">
<img
    title="Leżąc przed badaniem"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_1_lying.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Zaraz przed założeniem maski - jestem w stanie powiedzieć, że pełna uprząż do badania ruchów klatki piersiowej jest wyjątkowo niewygodna. Brakuje mi zdjęć z NeuroOnem z pierwszej nocy, pojawiają się jednak następnej. Z uwagi na ilość sprzętu jaką miałem na sobie, jakość mojego snu była na początku bardzo niska, co będzie dobrze widoczne tak w opisie, jak i w sygnale.

<a 
    href="/images/14_neuroon_signals/examination/night_2_electrodes_front.jpg"
    target="_blank">
<img
    title="Druga noc"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_2_electrodes_front.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

Druga noc - i już tylko EEG, EOG i EKG. Wiedziałem, że pozbycie się zarostu z twarzy i skalpu pomoże, zapomniałem jednak o EKG - i straciłem trochę włosów z klatki piersiowej.

<a 
    href="/images/14_neuroon_signals/examination/night_2_electrodes_mask.jpg"
    target="_blank">
<img
    title="NeuroOn na twarzy - sama pianka"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_2_electrodes_mask.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

Po założeniu maski - dość dobrze widać, gdzie będą przylegały elektrody.

<a 
    href="/images/14_neuroon_signals/examination/night_2_full_mask.jpg"
    target="_blank">
<img
    title="NeuroOn na twarzy - wraz z płytką"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_2_full_mask.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

Jak widać, przylegają one do twarzy bardzo mocno.

<a 
    href="/images/14_neuroon_signals/examination/electrode_prints.jpg"
    target="_blank">
<img
    title="Odciski po elektrodach"
    class="article-img"
    src="/images/14_neuroon_signals/examination/electrode_prints.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Odciski widoczne są na twarzy kolejnego dnia - nawet do godziny po zdjęciu.

<a 
    href="/images/14_neuroon_signals/examination/software.jpg"
    target="_blank">
<img
    title="Oprogramowanie Grass Technologies PSG TWin"
    class="article-img"
    src="/images/14_neuroon_signals/examination/software.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Sygnał z obu nocy został zgrany z polisomnografu za pomocą oprogramowania Grass Technologies PSG TWin 4.5.4 oraz 4.5.2 dla upewnienia się, że nie powstaną artefakty pochodzenia software'owego.

Mimo iż nowsza wersja software IntelClinic którą otrzymałem zapisuje w plikach z sygnałem timestampy z NeuroOna, streamy z maski i polisomnografu mogą zaczynać się w różnych momentach. By pomóc wyznaczyć wspólny punkt startu, przez pierwsze kilka minut badań co kilka sekund zamykałem oczy i zaciskałem zęby lub wysuwałem żuchwę, co powinno pojawić się jako bardzo wyraźne artefakty mięśniowe pomagające zsynchronizować oba sygnały. 

Wszystkie pliki - zarówno skany opisu, sygnały z NeuroOna (.csv) i AURY (.edf), staging (.xcl, .csv) jak i zdjęcia można znaleźć [na moim serwerze](https://alxd.org/data/psg_neuroon_raw_data_description.7z). Wszystkie wyżej wymienione materiały objęte są licencją Creative Commons BY 4.0[^16].

### Podsumowanie

Ponieważ od dawna jestem zwolennikiem nauki Otwartego Dostępu, a w szczególności Open Notebook Science, starałem się udokumentować badanie w jak najlepszy sposób. Zachęcam wszystkich chętnych do porównania sygnałów z NeuroOna i AURY i publikacji własnych wyników. Jestem świadom, że znacznie lepiej byłoby zebrać 5, 7 czy 14 próbek - jednak nie stać mnie na wynajęcie Ośrodka na tak długo - a i jest to niesamowicie niewygodne (oprócz badań pracuję też osiem godzin dziennie).

Analiza sygnałów zajmie mi przynajmniej miesiąc, nie chcę więc w tej chwili przesądzać czegokolwiek. Staram się zachować odpowiednio naukowe podejście do tematu, posiadając falsyfikowalną hipotezę, nie uprzedzenia czy nieuzasadnione przekonania. Całość mojej pracy opublikuję na tym blogu, najprawdopodobniej w formie ipython notebooka - jupytera[^17], by każdy z Was miał możliwość prześledzenia moich działań krok po kroku i wytknięcia mi ewentualnych błędów.


[^1]: Kampania NeuroOna [Kickstarter](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle)
[^2]: [NeuroOn - król jest nagi]({filename}/01pl_neuroon_krol_jest_nagi.md)
[^3]: @takingapartcats, a neuroscientist from Zurich [artykuł](https://takingapartcats.wordpress.com/2014/01/13/nonsense-neurogadgets-sleep-edition/)
[^4]: "Deconstructing the most sensationalistic recent findings in Human Brain Imaging, Cognitive Neuroscience, and Psychopharmacology" [artykuł](https://neurocritic.blogspot.co.uk/2014/01/neurocrap-funded-by-masses-neuroon-and.html)
[^5]: Dr hab. n. med. Adam Wichniak, specjalista psychiatra, neurofizjolog kliniczny [(strona szpitala)](http://www.sen-instytut.pl/awichniak.html) w Bloomberg Businessweek 37(114)/2014, artykuł "Halo, halo, pobudka!". Doktor wypowiada się również w programie [Sonda²](http://vod.tvp.pl/24809566/odc-11)l
[^6]: Tomasz Kolodziejak, co-founder of Neuroon, hacks your sleep with the intelligent mask | Valley Talks [YouTube](https://www.youtube.com/watch?v=aFGv4BmgjCw&t=04m53s)
[^7]: Dział Features na [stronie NeuroOna](https://neuroon.com)
[^8]: Jeden z komentarzy niezadowolonych klientów [Kickstarter](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle/comments?cursor=8675981#comment-8675980)
[^9]: Lucid Dreaming: Psychophysiological Studies of Consciousness during REM Sleep by Stephen LaBerge, Ph.D. [source](http://www.lucidity.com/SleepAndCognition.html)
[^10]: The Neuroscience of Lucid Dreams [Scientific American](http://blogs.scientificamerican.com/illusion-chasers/the-neuroscience-of-lucid-dreams/)
[^11]: Niestety, blogposty zostały skasowane ze strony NeuroOna. O ile "Biological Amplifiers: Why Do We Need Them?" zostało usunięte bezpowrotnie, "The Ontogeny of Sleep and Its Neurobiological Basis" można jeszcze znaleźć na [The Internet Archive](https://web.archive.org/web/20150426104210/https://neuroon.com/the-ontogeny-of-sleep-and-its-neurobiological-basis/)
[^12]: [Kuiga's blog](https://neuroonsleep.wordpress.com/2016/03/07/more-naps-rant-and-rem-incorrecly-detected-as-wake/)
> In my first post I mentioned having asked the support whether the mask hardware is technically capable of detecting the sleep-stage in real time. I got a message from the support today. They did not answer my question directly (or course…) but said that “We may add in the future the option of waking up when in the light sleep”. What I make of this is that it’s hard to implement and not their top priority at the moment.
[^13]: [NeuroOn Technology](https://neuroon.com/technology/)
[^14]: Ośrodek Medycyny Snu Instytutu Psychiatrii i Neurologii [strona główna](http://www.sen-instytut.pl/index.html)
[^15]: Wszystkie strony firmy Grass wydają się martwe, natomiast informacje o wzmacniaczu AURA dostępne są na [SelectScience](http://www.selectscience.net/products/aura-psg-ambulatory-systems/?prodID=171717) i [stronie Ośrodka Medycyny Snu](http://www.sen-instytut.pl/sleep_laboratory.html) 
[^16]: CC-BY 4.0 - szczegółowe warunki licencji dostępne są na stronie [Creative Commons](https://creativecommons.org/licenses/by/4.0/deed.pl)
[^17]: Otwarty notes naukowy jako świetna forma do prezentacji swoich badań - [JuPyTer](http://jupyter.org/)
