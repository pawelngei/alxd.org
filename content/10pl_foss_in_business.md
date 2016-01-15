Title: Wolne i otwarte oprogramowanie w biznesie [pl]
Date: 2016-01-14 18:00
Slug: foss-in-business
Lang: pl
Translation: false

Artykuł ten został napisany na prośbę działu Technologii Finansowych Wprost.pl i objęty jest licencją [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.pl) pozwalającą również na użycie komercyjne. Byłbym wdzięczny za poinformowanie mnie, jeżeli zostałby wykorzystany poza tym blogiem i wprost.pl.

<a href="https://www.flickr.com/photos/duhhquagliato/4478349112/">
  <img title="Tux by Eduardo Quagliato" class="article-img" src="/images/10_foss/logo.jpg" style="width: 500px; height: auto; margin: 2em auto;">
</a>

Przeciętny użytkownik komputera nie poświęca wiele uwagi licencjom oprogramowania, jakiego używa. Jest dla niego zupełnie naturalne, że pewne - jak system Windows czy pakiet antywirusowy - powinien zakupić, inne zaś może legalnie ściągnąć z Sieci. Część z nich będzie wyświetlała reklamy, inne przy instalacji podrzucą też do systemu dodatkowy toolbar czy aplikację partnera. Jest jednak i oprogramowanie, które mimo że bezpłatne - nie posunie się do żadnej z tych rzeczy. Należy do niego większość przeglądarek internetowych - być może najważniejszych dla zwykłego użytkownika aplikacji.

Przeglądarki te - jak [Mozilla Firefox](https://firefox.com/) czy [Chromium](https://www.chromium.org/) (znana większości pod marką [Google Chrome](https://www.google.pl/chrome/browser/desktop/)) objęte są licencjami z rodziny open source. Ich kod źródłowy jest dostępny dla każdego - co oznacza, że są one nie tylko darmowe dla użytkownika końcowego, ale możliwe do zmodyfikowania czy dostosowania do swoich potrzeb przez każdego dewelopera. Za ich rozwój odpowiedzialne są najczęściej fundacje i konsorcja nie przynoszące bezpośredniego zysku - a jednak na licencjach otwartych oparty jest niejeden model biznesowy nawet największych graczy, jak Google, Amazon czy Intel.

FOSS - ang. Free and Open-Source Software, Wolne i Otwarte Oprogramowanie obejmuje szereg licencji, które zawsze jednak zapewniają użytkownikowi cztery podstawowe [wolności](https://www.gnu.org/philosophy/free-sw.pl.html):

0. Wolność do użytkowania w dowolny sposób i w dowolnym celu.
1. Wolność do badania i modyfikacji programu (wymaga dostępu do kodu źródłowego).
2. Wolność do wytwarzania dowolnej ilości kopii i rozpowszechniania ich.
3. Wolność do dystrybuowania kopii swoich modyfikacji programu.

Dzieli się ono na dwa nurty, stawiające nacisk właśnie na Otwartość lub Wolność:

### Inżynierska otwartość

Jednym z najważniejszych orędowników oprogramowania po prostu otwartego jest Linus Torvalds, twórca przełomowego dla technologii i biznesu jądra systemu Linux. Głównym motywem do otworzenia kodu jest dla niego kunszt techniczny - nic nie gwarantuje tak wysokiej jakości oprogramowania jak przejrzenie go przez kilku niezależnych ekspertów. Jednym z powodów bardzo wysokiego bezpieczeństwa systemów z rodziny GNU/Linux jest właśnie transparencja i unikanie tzw. "security through obscurity", czyli zatajania mechanizmów zabezpieczeń mając nadzieję, że nie zostaną odkryte przez atakujących.

Do licencji "otwartych" zwanych również "zezwalającymi" należą między innymi, [MIT](https://opensource.org/licenses/MIT), [Apache](https://opensource.org/licenses/Apache-2.0) czy [BSD](https://opensource.org/licenses/BSD-3-Clause). Pozwalają one na dokonywanie modyfikacji objętego nimi oprogramowania bez późniejszej publikacji kodu, a więc i włączenie do oprogramowania zamkniętego i późniejsze odsprzedawanie tak długo, jak przy produkcie końcowym znajdzie się informacja o wszystkich autorach. Zrzekają się oni praw majątkowych do stworzonego kodu, ceniąc jego rozpowszechnienie ponad zyski materialne.

Otwarte oprogramowanie tworzone jest często przez programistów chcących zareklamować swoje umiejętności czy firmy promujące własne ekosystemy (w końcu nikt nie będzie świadczył tak dobrego wsparcia jak twórca pakietu). Pomaga ono w szybkim rozwoju konkretnych technologii do komercyjnego wykorzystania, na przykład narzędzi webowych pisanych w JavaScriptcie ([AngularJS](https://angularjs.org/) na MIT czy [ReactJS](https://facebook.github.io/react/) na BSD). Wiele z konsorcjów decyduje się też na wybór analogicznej licencji dla opracowywanych wspólnie produktów, jak w przypadku [OpenStacka](https://www.openstack.org/).

Można otwarcie powiedzieć, że sam Bitcoin nie zyskałby nawet części obcecnej popularności, gdyby nie jego całkowita otwartość (klient [Bitcoin Core](https://github.com/bitcoin/bitcoin) objęty jest licencją MIT). To właśnie transparentność i możliwość dostosowania do własnych potrzeb zapewniły kryptowalucie - jako infrastrukturze - oszałamiająco szybki rozwój.

### Wolność i niezależność

Drugim znaczącym nurtem w FOSS są właśnie licencje wolne (ang. "free as in freedom"), reprezentowane między innymi przez [GNU/GPL i Affero GPL](https://www.gnu.org/licenses/licenses.pl.html). Każdą modyfikację takiego oprogramowania musimy udostępnić na analogicznej licencji, co zmusiłoby nas do publikacji wszystkich źródeł naszego projektu w przypadku włączenia do niego wolnego kodu. Wciąż mamy jednak prawo do sprzedaży (z pominięciem praw majątkowych twórców kodu GPL/aGPL), pod warunkiem dołączenia do każdego egzemplarza pełnego źródła oprogramowania.

Głównym celem istnienia tych licencji jest niezależność oprogramowania od jakichkolwiek podmiotów, które mogłyby chcieć wprowadzić na rynek swoje własne, zmodyfikowane i własnościowe wersje. Są one bardzo często wybierane w celu zapewnienia neutralności infrastrukturze - jak w przypadku samego jądra [Linuksa](https://www.kernel.org/category/faq.html) na GNU/GPLv2, stanowiącego podwaliny tak samej Sieci, jak i nowopowstającego Internetu Rzeczy.

Sam termin "wolnego oprogramowania" ukuty został w 1985 roku przez [Richarda Stallmana](https://www.gnu.org/gnu/initial-announcement.html), purystę i założyciela Free Software Foundation. Wielokrotnie podkreśla on, że jedynie oprogramowanie w pełni wolne daje gwarancję bezpieczeństwa, wolności i niezależności użytkownikowi - robiąc dokładnie i jedynie to, do czego jest przeznaczone. W ostatnich latach między innymi [Chiny](http://qz.com/505383/a-first-look-at-the-chinese-operating-system-the-government-wants-to-replace-windows/), [Rosja](http://www.astra-linux.com/sertivikat.html) - a w mniejszym stopniu [Niemcy](http://www.itworld.com/article/2716115/operating-systems/switching-to-linux-saves-munich-over--11-million.html) i [Włochy](http://www.networkworld.com/article/2984318/opensource-subnet/forza-open-source-italian-military-to-adopt-libreoffice.html) zdecydowały się przenieść infrastrukturę publiczną na rozwiązania wolne, niezależne od Microsoftu czy Apple powiązanymi blisko ze Stanami Zjednoczonymi.

### FOSS w biznesie

Wolne i otware oprogramowanie pełni kilka istotnych funkcji w biznesie. Nie jest to próba oszczędzenia na licencjach komercyjnych (które to rozwiązania mogą, acz nie zawsze muszą być tańsze), a świadoma decyzja przy tworzeniu biznesplanu.

Firmy zajmujące się FOSS używają go głównie do celów wewnętrznych - budowy infrastruktury, z której korzystają budując produkty i usługi niekoniecznie zawierające w sobie otwarte oprogramownaie, jak na przykład analizy rynku czy Video on Demand. Wśród tych, których produkt objęty jest licencją otwartoźródłową służy on raczej do zbudowania wygodnego dla klientów ekosystemu - zyski zaś czerpią ze świadczenia wsparcia do niego (jak [Canonical](http://www.canonical.com/) czy [Red Hat](https://www.redhat.com/)).

Otwartość kodu świadczy także o kunszcie inżynieryjnym firmy, będąc [bardzo istotnym czynnikiem](https://blog.intercom.io/inbound-recruiting-engineers/) w przyciągnięciu zdolnych i ambinych programistów. Do firm, które między innymi w tym celu postanowiły stworzyć swoje portfolio otwartych narzędzi należą między innymi znane w branży finansowej [Jane Street](https://github.com/janestreet), [Tsuru Capital](https://github.com/tsurucapital) czy [Palantir](https://palantir.github.io).

### Regulacje i hakerzy

W najbliższych latach możemy zobaczyć coraz większy wzrost popularności oprogramowania na licencjach FOSS. Jednym ze skutków afery spalinowej [Volkswagena](http://www.consumerreports.org/cro/cars/vw--audi-cited-by-epa-for-cheating-on-diesel-emissions-tests) było też nasilenie się głosów na temat poddania producentów samochodów [obowiązkiem ujawnienia kodu](https://www.totaralms.com/blog/volkswagen-scandal-avoidable-open-source) działającego w komputerach pokładowych w celu jego weryfikacji tak przez komisje, jak i osoby trzecie. Może się to okazać zaskakująco... zyskowne dla branży motoryzacyjnej. Dlaczego?

Bardzo wielu przedsiębiorców nie docenia znaczenia hakerów, czy też "badaczy bezpieczeństwa" na rynku. Są to osoby niezwiązane z firmą, które we własnym zakresie przeprowadzają analizę oprogramowania danej firmy - znajdując błędy i luki bezpieczeństwa, po czym zgłaszając je do poprawki zanim jeszcze wywołają znaczący i kosztowny kryzys. Giganci tacy jak [Google](https://www.google.com/about/appsecurity/reward-program/) czy [Facebook](https://www.facebook.com/whitehat/) od lat prowadzą już programy "bug bounty", wypłacające nagrody za takie działania.

Może się też okazać, że entuzjasta technologii bawiąc się wieczorami symulowanym silnikiem Volkswagena wpadnie na pomysł optymalizacj, o której nie pomyśleli inżynierowie firmy - zmniejszając zużycie paliwa o kilka procent. Przyniesie więc zysk firmie - a nagroda dla niego będzie znacznie niższa niż budżet RnD, który mógłby stworzyć podobne usprawnienie.

### Poza oprogramowaniem

Licencje pozwalające na dowolne (tak otwarte, jak i wolne) użytkowanie twórczości pojawiają się też poza oprogramowaniem. Jedną z najpopularniejszych jest dziś [Creative Commons](http://creativecommons.org/), wykorzystywana między innymi jako podstawa istnienia [Wikipedii](https://en.wikipedia.org/wiki/Wikipedia:Copyrights). W Polsce [Radio Wolne Media](http://radio.wolnemedia.net/) zapewnia muzykę o licencjach pozwalających także na wykorzystanie komercyjne, bez potrzeby uzyskiwania jakichkolwiek zgód od organizacji zbiorowego zarządzania.

Bardzo ciekawym zagadnieniem jest też rosnąca potrzeba na zaistnienie podobnego rozwiązania w świecie patentów. Systemy prawne całego świata przez dziesięciolecia kształtowane były z myślą o umożliwieniu tworzenia portfolio patentowego i szantażu konkurencji, ktore doprowadziły w końcu do [Wojen Patentowych](http://www.pcmag.com/article2/0,2817,2399098,00.asp) (i około [250 tysięcy patentów](https://www.techdirt.com/blog/innovation/articles/20121017/10480520734/there-are-250000-active-patents-that-impact-smartphones-representing-one-six-active-patents-today.shtml) dotyczących jednego urządzenia - smartfona).

Gdy w zeszłym roku Elon Musk postanowił "[uwolnić](https://www.teslamotors.com/blog/all-our-patent-are-belong-you)" część należących do swojej firmy patentów w celu stworzenia neutralnej infrastruktury dla samochodów elektrycznych, [nie istniały](https://gigaom.com/2014/06/14/what-elon-musk-did-and-did-not-do-when-he-opened-teslas-patents/) gotowe narzędzia prawne, które zagwarantowałyby firmom chcących z nich skorzystać pełne bezpieczeństwo. W przypadku zmiany CEO przez Teslę (co jest teoretycznie możliwe), decyzja Muska mogłaby być podważona, a patenty wciąż pozostające w portfolio firmy użyte przeciwko konkurencji, która już przeznaczyła miliony dolarów na badania tego segmentu rynku.

Dobrze byłoby więc zacząć traktować ruch Wolnego i Otwartego Oprogramowania nie tylko jako ciekawostkę, ale również istotną taktykę w zdobywaniu rynku.

<p class="small">Za pomoc w tworzeniu (mam nadzieję) zrozumiałego artykułu bardzo dziękuję ryśkowi, Ani i Szymkowi.</p>
