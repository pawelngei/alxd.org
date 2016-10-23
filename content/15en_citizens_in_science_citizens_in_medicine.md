Title: Hackers, researchers, biohackers
Date: 2016-07-27
Slug: hackers-researchers-biohackers
Lang: en
Tags: citizen science, hackerspaces, biolabs
Translation: false

***Note***: *I am still working on NeuroOn signal analysis. You can expect to see the hypnogram[^hypnogram] comparisons first together with time-synchronized signal files and all the code in an open Jupyter Notebook[^jupyter]*

<a 
    href="https://www.flickr.com/photos/madlabuk/7090137567/"
    target="_blank">
<img
    title="Photo CC BY-SA 2.0 madlabuk"
    class="article-img"
    src="/images/15_biolabs/pcr.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

### Hackerspaces and biology

As a long time Citizen Science and Open Source supporter I love the idea of Hackerspaces[^hackerspace] - collaboration workspaces allowing individuals to work on their own technical projects, sharing tools and knowledge. I consider them a vital counterpart to Academic research labs, where people are not bound by strict rules and grants. Hackerspaces excel in very disorganized research and development of various IT and electronic projects, producing a lot of open designs and proof of concepts[^hackaday].

Many researchers point out that it is possible only due to the nature of IT and electronics allowing rapid prototyping and near-instantaneous results - something which couldn't be replicated in more time-consuming experimental sciences such as chemistry and biology. I'd like to disagree with that point. While it is impossible to achieve the same speed of prototyping as in IT or electronics, there is a lot to be gained by changing our approach to said research.

### iGEM

<a 
    href="https://www.flickr.com/photos/igemhq/5167673278/"
    target="_blank">
<img
    title="Photo CC BY-SA 2.0 iGEM and Justin Knight."
    class="article-img"
    src="/images/15_biolabs/igem.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Staying on the very verge of Academia, IGEM - International Genetically Engineered Machine Competition[^igem] allows its participants to use synthetic biology to build organisms serving a specific purpose - like cleaning waste from water or extracting valuable elements from used electronics. To gain speed they use pre-defined building blocks chosen by the iGEM Foundation, allowing much simpler modeling and testing of their organisms. The competition itself was designed for undergrad- and graduate biologists, Student Science Clubs operating in a very hacker-space'y way, with far less strictness than a regular research team - and was deemed a success.[^igem success] Sadly, over time the cost of taking part in the competition rose to over $600 per person[^igem cost], virtually disallowing students without some kind of grant to take part and gathering heavy criticism from multiple communities.

### Citizen Science

Going a step further from formal structures there are a lot of projects happening in biological Citizen Science. This month Copernicus Science Center in Warsaw hosted a SPARKS exhibition "Citizens in Medicine"[^Kopernik]/"Beyond the Lab: The DIY Science Revolution" detailing several of them:

 - Bento Lab[^BentoLab] is a kit for amateur biolabs and citizen scientists based on Arduino and Raspberry Pi idea of standardized kits allowing DIY projects. It lowers the price of a DNA extracting, copying and visualizing equipment to about $920, making it possible to show real DNA experiments at schools, and science fairs - or to conduct basic research.

 - OpenPCR[^openPCR] is doing a similar thing for PCR Thermocyclers - 100% open source and open hardware.

 - Patient Innovation[^Patient Innovation] is a database of patient-submitted devices and procedures which could help in treatment of chronic conditions. It contains DIY devices, suggested way of dealing with problems or just life hacks in a form of layman-accessible articles.

 - Timothy Omer[^Tim Omer] is a hacker who decided to create his own artificial pancreas by combining several medical devices and making his insulin pump act automatically based on an algorithm he devised. 

 - Mosquito Atlas[^Mosquito Atlas] using crowd source to catalog mosquitoes from all over Germany.

 - Sara Riggare[^Sara Riggare], a self-caring Parkinson patient using quantified self devices and her medical knowledge to stave off her disease's progress

- Mapping For Change[^Mapping For Change] is a crowd sourced project to measure the air pollution in different areas of London

### Biolabs

<a 
    href="https://counterculturelabs.org/"
    target="_blank">
<img
    title="Picture CC BY-SA 4.0 https://counterculturelabs.org/"
    class="article-img"
    src="/images/15_biolabs/flasks-logo.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>


Despite multiple legal problems, biological Hackerspaces - called Biolabs[^Biolab] - are sprouting around the world. In multiple countries they are not able to conduct actual research, serving as an education space showcasing simple experiments such as DNA extraction. You can learn a lot about them from a journalistic project showcasing stories from multiple biolabs around the world called BioHacking Safari[^Biohacking Safari]. 

There's a whole ecosystem growing around these self-organized labs, helping them get used equipment from Universities or private research facilities, make repairs and share knowledge on how to operate them in a best way. One of such places is BioLinkDepot[^BioLinkDepot] operating as a NGO within a BioLink[^BioLink] network in the USA. While not as formal and focused more on a hands-on approach, DIY BIO[^DIYBio] constitutes another valuable network for biohackers. 

Several BioHackerspaces, such as Counter Culture Labs in Oakland[^CounterCultureLabs] and BioCurious in Sunnyvale, CA[^BioCurious] carry several serious research projects. In addition to taking part in IGEMs mentioned earlier, they are working on Open Insulin Project[^OpenInsulin] trying to create a patent-less, open way to acquire insulin for people suffering from diabetes. One of their more eccentric, yet no less important ambitions is to create Vegan Cheese[^VeganCheese] produced by bacteria instead of animals. The project was successfully funded on Experiment[^experiment], a crowdfunding platform for researchers.

If you're not sure if a loosely organized lab consisting of people working there part-time, mostly during evenings and weekends is able to achieve sufficient quality - please read on. During my stay in California I had a chance to visit OmniCommons hackerspace(s) and CounterCultureLab together with my friend - Marcin Ziemniak, biochemistry PhD. He agreed to share his findings and conclusions regarding Open Insulin process.

<a 
    href="https://motherboard.vice.com/read/meet-the-gynepunks-pushing-the-boundaries-of-diy-gynecology"
    target="_blank">
<img
    title="Photo Paula Pin/Creative Commons"
    class="article-img"
    src="/images/15_biolabs/speculum.jpeg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

On the other side of "formality" spectrum lie anarchist biolabs and hackerspaces, such as Gynepunks located in Spain[^GynePunks] interested mainly in DIY medicine and gynecology[^GynePunks article]. Their focus on underserved women and field medicine may be extremely valuable in warzones and disaster sites lacking not only doctors and nurses, but also medical equipment. The efforts of hackers and makers may reduce the cost of humanitarian action[^humanitarian aid], such as with Sierra Leone's latest Ebola Epidemic[^EbolaHackers] or refugee camps in Greece[^Daedalus].

Each of these 'spaces and projects serve different purpose supporting a specific area of life with their research. With more and more biological and chemical research being closed behind paywalls and corporate trade secrets I think we should appreciate and support open research done by citizen scientists much more - even if not on par with traditional research institutions.

### Open Insulin Project in Counter Culture Labs

<a 
    href="https://omnicommons.org/"
    target="_blank">
<img
    title="OmniCommons photo copyleft by Omni Oakland Collective"
    class="article-img"
    src="/images/15_biolabs/omnicommons.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Counter Culture Labs[^CounterCultureLabs] is a biolab functioning as a part of OmniCommons community center[^OmniCommons] in Oakland, CA, USA. The Commons are a kind of umbrella organization for about 14 collectivResourceses[^OmniCommons Resources] sharing a building, including the Sudo Room[^Sudo Room] hackerspace, Food Not Bombs chapter or a small poetry press. It's one of the biggest 'Spaces in the Bay area, neighboring Noisebridge[^Noisebridge], Liberating Ourselves Locally[^LOL] and others.

Personally I have no idea how such a large collective exists and is *stable* - and I respect its coordinators deeply. While visiting Oakland and San Francisco I've heard many stories of OmniCommons problems with (non-hacker) neighbors and their possible prejudices.

<a 
    href="https://counterculturelabs.org/"
    target="_blank">
<img
    title="Photo CC-BY-SA 4.0 Counter Culture Labs"
    class="article-img"
    src="/images/15_biolabs/ccl.png"
    style="width: auto; max-width: 500px; height: auto; margin: 2em auto 2em;">
</a>

We've arrived in the Omni on Sunday, 24th April 2016, just in time to look at the Open Insulin Project session. The lab is a space within the main room excluded from the rest of the rooms by tape and not much else. All its participants work there in their own spare time, and according to my understanding no one is paid to manage the project.

Counter Culture members mentioned to me that they may withdraw from this- or next- year IGEM due to the high admission cost, and they are trying to focus on projects outside of the Academia. The nature of the project is a subject of many brainstorms, with examples like a bacterial sunscreen. They are also collaborating with open biolabs, like BioCurious[^BioCurious].

<a 
    href="/images/15_biolabs/cclabs-projects.jpg"
    target="_blank">
<img
    title="Photo CC-BY 4.0 Pawel alxd Chojnacki"
    class="article-img"
    src="/images/15_biolabs/cclabs-projects.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

With that introduction I'd like to give voice to an expert, Marcin Ziemniak PhD, who agreed to share his opinions and conclusions on the process:

Can you please tell us more about yourself, Marcin?

> I am a young scientist who recently finished his PhD in biochemistry/organic chemistry under supervision of prof. Jacek Jemielity at University of Warsaw (Faculty of Physics). My research project was aimed at synthesis of nucleotides and their applications in biochemical and structural studies on proteins involved in mRNA degradation in eukaryotic cells.  Now I am a short time visitor in John D. Gross lab at UCSF in San Francisco. During that stay I work on structure and mechanism of action of several protein regulating mRNA metabolism.

<a 
    href="/images/15_biolabs/marcin-ziemniak-s.png"
    target="_blank">
<img
    title="Photo CC-BY-SA-ND 4.0 Marcin Ziemniak"
    class="article-img"
    src="/images/15_biolabs/marcin-ziemniak-s.png"
    style="max-width: 250px; height: auto; margin: 2em auto 2em;">
</a>

> Apart from that I am also interested in growing field of synthetic biology. In 2009, 2013 and 2014 I took part (initially as a student and later as a supervisor) in iGEM competition. IGEM means International Genetic Machine Competition and it is a largest competition dedicated to synthetic biology. During iGEM a number (recently more than 200) of student teams try to build so called “genetic machine” during a summer scientific project. This enigmatic terms simply means a genetically modified organism i.e. bacteria or yeast capable of being useful for certain purposes. It could be detection of toxic compounds in the environment, production of biofuels or applicability in academic research.

> Because of mentioned interest in synthetic biology I was really pleased when I had an occasion to visit a DIY (Do It Yourself) Biology Lab in Oakland. The people who created the lab called it Counter Culture Labs and this working space is a part of bigger initiative called Omni Commons. Visiting this place was undoubtedly an interesting and rewarding experience!

<a 
    href="/images/15_biolabs/insulin-project.jpg"
    target="_blank">
<img
    title="Photo CC-BY 4.0 Pawel alxd Chojnacki"
    class="article-img"
    src="/images/15_biolabs/insulin-project.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

What do you think about Counter Culture Lab we visited?

> One of the strongest point of the lab is an instant access to a vast array of scientific instruments such as automatic pipettes, thermocycler (a machine using for PCR reaction), spectrofotometers, autoclaves and even a hood for work with eukaryotic cells. The workspace is not only well organised but also tidy and clean. During their practical workshop there was a number of people – all of them were actively taking part in laboratory work. Their instructors seemed to be well prepared and they showed practical and theoretical knowledge about basic concept of microbiology, genetics and biochemistry.

> Currently this lab is engaged in several scientific projects. The main one is dedicated to establish an open source method for preparation of insulin (a protein necessary for people suffering from diabetes). This protein is expressed in bacteria, then purified and refolded to its native state in vitro.  Another project is about microbiology – some people here working on different fungal species. I don’t know the details, probably the aim is to characterise (basic genetics and biochemistry) some naturally existing strains of yeast and investigate whether they may find any practical use in biotechnology. The goal of the second, microbiology oriented, project  is to use bacteria to produce a vegan cheese. What is more, people from this lab even managed to take part in IGEM competition in 2014, which itself is an ambitious and demanding task. 

<a 
    href="https://www.flickr.com/photos/amandawoodward/118635508/"
    target="_blank">
<img
    title="Picture CC-BY-NC 2.0 Amanda Woodward"
    class="article-img"
    src="/images/15_biolabs/insulin-pic.jpg"
    style="width: 400px; height: auto; margin: 2em auto 2em;">
</a>

What are your thoughts on the nature of the movement at large? How do they compare to the Academia - or commercial labs?

> I should mention that DIY biology movement gained some impetus in recent years. It was possible because of several factors. First, more and more biological knowledge is treated as an open source material which is accessible for anyone.  Second, currently the access to some basic equipment and labware is easier (some of them can be even bought online), some places also offer some workspace and financial support for people interested in DIY biology. Last but not least people themselves show growing interest in this subject. Unfortunately, at the present day DIY biology movement cannot really compete with neither commercial nor academic research. It is mainly owing  to smaller financial support and still limited access to most advanced technologies and equipment.  Nevertheless some simple experiments (and of course a lot of educational work) can be easily done in a decent DIY biology lab.

Does this project stand a chance, then? Or are the biohackers just playing around?

> Overall my view on this place is very positive, however their ultimate scientific goal (insulin-related project) might be too ambitious. Perhaps it would be better to first try with some proteins which are easier to work with (such as bacterial enzymes or fluorescent proteins since their activity could be easily monitor using simple biochemical assays). What is more, over last 20 years many companies and research institutions have already put a significant effort in insulin-related studies. It may suggests that this field is already well known and it would be very difficult (at least for a small independent team) to make an important contribution.  On the other hand such project could be just a good occasion to improve some biochemical skills and to gain more interest from people interested in “home-made science”. Not mentioning a number of educational possibilities (training of young people interested in science, popularization of biotechnology and improving the general perception and understanding of science).

<a 
    href="https://counterculturelabs.org/"
    target="_blank">
<img
    title="Photo CC-BY-SA 4.0 Counter Culture Labs"
    class="article-img"
    src="/images/15_biolabs/lab-work.jpeg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Would they be able to get any publication out of their work?

> For me it is quite hard to tell if a scientific article write by a DIY biology team, without an academic affiliation, could be published in a respected scientific journal. It strongly depend on an editor of such journal, I guess it would be easier to publish in an open access journal like PLOS ONE. Another idea would be to cooperate with a friendly institution (university or scientific institute), but it might be difficult due to different attitudes toward science.

So what is your general impressions? Would you change anything if you were a part of the project?

> In the end of day my impression is totally positive. Hopefully these projects will be developed further and gain more attention. I am little concerned by some technical details – protein purification should be done on ice or in a cold room to reduce proteolysis and loss of protein activity. However, when I asked them later about this issue I was informed that some crucial steps of protein purification are in fact performed in cold temperature. Still I think it could be great if they would have access to some sort of cold room.

### There is more to come

Biology and chemistry research is slowly spreading outside of the university and corporate labs. More and more scientists are noticing and researching the topic[^hal article], and other branches of science are following its footsteps[^openbci]. It's a good moment to notice that and welcome biohackers, standing perfectly between scientific and hacker communities.

<a 
    href="https://www.flickr.com/photos/gemmerich/6365692655/"
    target="_blank">
<img
    title="Picture CC-BY-SA 2.0 Greg Emmerich"
    class="article-img"
    src="/images/15_biolabs/open-science.png"
    style="width: auto; max-width: 300px; height: auto; margin: 2em auto 2em;">
</a>
 
[^hypnogram]: Wikipedia on [hypnogram](https://en.wikipedia.org/wiki/Hypnogram)
[^jupyter]: Official page of [Jupyter Project](http://jupyter.org/)
[^hackerspace]: Wikipedia is quite comprehensive on [Hackerspaces](https://en.wikipedia.org/wiki/Hackerspace), but there is also an article from [Berkeley](https://people.eecs.berkeley.edu/~bh/hacker.html) and the immortal [Hacker Hotwo](http://www.catb.org/esr/faqs/hacker-howto.html)
[^hackaday]: A magnificent and beautiful catalog of hundreds of hacker projects, [Hackday.io](https://hackaday.io/)
[^igem]: [iGEM Foundation official page](http://igem.org/Main_Page)
[^igem success]: Minireview from [Oxford FEMS Microbiology Letters](http://femsle.oxfordjournals.org/content/362/16/fnv129.abstract)
[^igem cost]: "To put it succinctly: this is an exorbitant price to pay." - [[An iGEM critique]](http://2015.igem.org/Team:Waterloo/Practices/An_iGEM_Critique)
[^Kopernik]: Copernicus Science Center in Warsaw has a terse [note](http://www.kopernik.org.pl/en/projekty-specjalne/european-projects/sparks/obywatele-w-medycynie-wystawa/) on the exhibition.
[^BentoLab]: Official page of [Bento Lab](https://www.bento.bio/)
[^openPCR]: [OpenPCR Project](http://openpcr.org/)
[^Patient Innovation]: Official page of [Patient Innovation](https://patient-innovation.com/)
[^Tim Omer]: Tim Omer has a shiny [webpage](http://www.hypodiabetic.co.uk/) and a [twitter](https://twitter.com/tim_omer)
[^Mosquito Atlas]: There are multiple [articles](https://dna-barcoding.blogspot.be/2013/06/the-german-mosquito-atlas.html) and publications on the topic, but [this seems to be an official webpage](http://www.mueckenatlas.de/)
[^Sara Riggare]: Sara Riggare is sharing her stories and advice on [this blog](http://www.riggare.se/)
[^Mapping For Change]: Mapping For Change [project page](http://mappingforchange.org.uk/projects/citizen-science-used-to-map-community-air-quality/)
[^Biolab]: Wikipedia on [Biolabs](https://en.wikipedia.org/wiki/Biolab)
[^Biohacking Safari]: Daily Laurel and Quitterie Largeteau are doing excellent work showing Biolabs around the world with their [Biohacking Safari](http://biohackingsafari.com/sample-page/)
[^BioLinkDepot]: [Official page](http://biolinkdepot.org/)
[^BioLink]: [BioLink Foundation](http://www.bio-link.org/home2/)
[^DIYBio]: [DIY Bio Roadmap](https://diybio.org/)
[^CounterCultureLabs]: Official page of [CounterCultureLabs](https://counterculturelabs.org/) and all their projects.
[^BioCurious]: [bioCURIOUS](http://biocurious.org/)
[^OpenInsulin]: [Official Page](http://openinsulin.org/), [Popular Science Article](http://www.popsci.com/these-biohackers-are-making-open-source-insulin), [Experiment campaign](https://experiment.com/projects/open-insulin) and complementary [Open Artificial Pancreas System](https://openaps.org/)
[^VeganCheese]: [Real Vegan Cheese Page](https://realvegancheese.org/) had an [IndieGoGo campaign](https://www.indiegogo.com/projects/real-vegan-cheese#/) and [quite a media coverage](https://www.facebook.com/realvegancheese/)
[^experiment]: [experiment](https://experiment.com/how-it-works) is a kickstarter-like portal for crowd-funding projects, such as [open insulin campaign](https://experiment.com/projects/open-insulin)
[^GynePunks]: [Official, yet quite dead page of Gynepunks](https://gynepunk.hotglue.me/)
[^GynePunks article]: A great article on Gynecology Hackers in [Vice](https://motherboard.vice.com/read/meet-the-gynepunks-pushing-the-boundaries-of-diy-gynecology)
[^humanitarian aid]: "How Makerspaces Are Transforming Disaster Relief And Aid Efforts" is a [talk](http://www.prweb.com/releases/2014/10/prweb12236249.htm) given by [Communitere](http://communitere.org/what-we-do/)
[^EbolaHackers]: My favorite talk from 32C3, "How Open Source Software, second hand laptops and hackers helped stop Ebola" on [YouTube](https://www.youtube.com/watch?v=hZ29t_6TS8)
[^Daedalus]: [Daedalus Project Page](https://daedalus.libtech.website/) with their sister project, [RefugeeSupport](https://refugeesupport.net/)
[^OmniCommons]: [Official OmniCommons Page](https://omnicommons.org/)
[^OmniCommons Resources]: A list of all [Collectives](https://omnicommons.org/wiki/Collectives) located in the OmniCommons
[^Sudo Room]: [SudoRoom hackerspace page](https://sudoroom.org/)
[^Noisebridge]: [NoiseBridge hackerspace](https://www.noisebridge.net/), a home to papa hacker himself, [Mitch Altman](https://en.wikipedia.org/wiki/Mitch_Altman)
[^LOL]: [Liberating Ourselves Locally Makerspace](https://oaklandmakerspace.wordpress.com)
[^hal article]: [Domesticating and democratizing science: a geography
of do-it-yourself biology](https://hal.archives-ouvertes.fr/file/index/docid/784685/filename/WP_CSI_032.pdf)
[^openbci]: Low cost, open hardware brain signal amplifier [OpenBCI](http://openbci.com/)
