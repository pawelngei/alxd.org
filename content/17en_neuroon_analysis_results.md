Title: NeuroOn analysis - results and discussion
Date: 2016-12-19
Slug: neuroon-analysis-results
Lang: en
Tags: neuroon, signal analysis, science, open notebook
Translation: false

Updated twice, last on 21 December 2016. Notes below.

### tl;dr - So, does it work?!

[NeuroOn](https://neuroon.com/), the self-proclaimed *"world's first smart sleep mask"* isn't a medical grade device, but it's much better than a coin toss.

Its total accuracy in detecting sleep stages is **65%**.

One of the biggest problems with NeuroOn is that when used as an alarm clock almost every third time (**31.6%**) it will choose the worst possible moment for waking, assuring lack of energy and grogginess[^groggy-and-tired] after awakening.

Comparing NeuroOn's sleep stage results to a professional polysomnography[^PSG] scored by a human expert:

<a
    href="/images/17_neuroon_analysis_summary/intro_wake.png"
    target="_blank">
<img
    title="Should you be woken up?"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/intro_wake.png"
    style="width: 400px; height: auto; margin: 2em auto 2em;">
</a>

When polysomnography detects a sleep phase suitable for waking up, NeuroOn agrees in **73.8%** of the cases. In the rest **26.2%** it isn't a big deal, since it will just wait until the next good opportunity to wake you up.

<a
    href="/images/17_neuroon_analysis_summary/intro_sleep.png"
    target="_blank">
<img
    title="Should you stay asleep?"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/intro_sleep.png"
    style="width: 400px; height: auto; margin: 2em auto 2em;">
</a>

When polysomnography says not to wake the user up, NeuroOn agrees in **68.4%**. In the rest **31.6%** - nearly a third of all cases - it could try to wake the user, resulting in grogginess and complete lack of energy till the end of the day[^groggy-and-tired]. **This is a big deal** and may defeat the purpose of NeuroOn's alarm clock altogether.

And for the people who would like to understand what actually happened here...

### Long awaited results

This post is part of a series[^analysis] dedicated to NeuroOn sleep mask and its scientific viability. The full code and all signal samples are available on Github[^notebook].

Months after the first estimates I would like to present you the results of the NeuroOn experiment in a form accessible to laymen. The analysis took nearly four months due to my stubbornness in assuring that it's scientifically sound, completely open and reproducible at different machines. After roughly two months of dedicating every weekend to it, I realized my own understanding of mathematic, statistical analysis and SciPy / NumPy stack falls short for this challenge and asked Ryszard Cetnarski[^ryscet] for help. Together we have been able to create a coherent Jupyter Notebook and open it for peer review on the Internet[^notebook]. In November 2016 we presented a scientific poster[^poster]at the Aspects of Neurosciences[^neuroaspects] conference in Warsaw. Until the publication of this blogpost the only feedback we gathered regarded only small sample size and graph descriptions. If you have any additional suggestions, please send them to me[^email].

I'd like to thank Intelclinic[^intelclinic] for providing us a test unit of NeuroOn, Ryszard Cetnarski[^ryscet] for his tremendous help, as well as everybody who contributed to this analysis (in random order): [Michal Kawalec](https://github.com/mkawalec/), [Adam Golinski](http://adamgol.me/), [Bartosz Krol](https://github.com/BartKrol), [Jaroslaw Hirniak](http://www.hirniak.com/), [Karolina Stosio](https://twitter.com/karaszka), [Karol Benq Siek](https://www.linkedin.com/in/karol-siek-6424487a), [Dawid Laszuk](https://laszukdawid.com/), [Lorenzo Braschi](https://github.com/Lornebradia) and [Piotr Migdal](http://p.migdal.pl/).

### What did the experiment measure?

Our initial experimental hypothesis - *"Signal gathered by the NeuroOn mask is of a good enough quality to detect a sleep stage in real time, given processing power of an average smartphone"* proved to be too complex for a simple analysis, and while we could infer a lot from the signal's quality (discussed later), we were forced to change it.

Our final hypothesis was *"NeuroOn achieves medical-grade results in sleep staging as compared to a human expert working on a PSG signal"*, as claimed by IntelClinic[^medical-grade] (even though they backed out of that at some point[^near-medical-grade]).

EEG-based polysomnographs are the best medical- and scientific- grade devices for analyzing sleep and sleep stages, used widely in hospitals and research. We used Aura PSG [^AURA] used in clinical trials in Poland - and we will be considering it a single source of truth, being as close to the original brain signals as possible.

We analyzed signal from A1-F1 electrodes of the EEG (detailed description and electrode placement is available in the analysis blogpost[^analysis]), pre-cleaned by the Aura PSG amplifier[^AURA] and sleep staging performed by a human technician.

It is worth noting that there are only two nights (roughly 16 hours) of recordings captured on a healthy[^healthy] caucasian male[^sex-bias-neuroscience] in his 25s. To achieve any significant results we should conduct experiments on a more varied population `n > 30` for more than 14 nights, including people with known sleep disorders.

For NeuroOn we used the signal gathered by the three electrodes (single differential channel) on the device pressed to patient's head so firmly they left marks the next day[^marks]. The sleep staging was performed by offline (not real-time) algorithm executed on an external machine afterwards. The software used to do it was provided to us by Intelclinic on the 08.03.2016 under a condition that we will not try to reverse engineer[^reverse-engineer] it, to which we obliged.

We do not have any information about algorithm implementations on mobile devices used with end-user NeuroOn masks or their possible limitations.

### NeuroOn's time delay

First, we assumed that both NeuroOn's and PSG's signals do correlate and compared them. It turns out that the devices' clocks were desynchronized, with NeuroOn's running roughly `160.5 seconds late` and having a slowly growing delay on the course of the 8-hour recording. For the second night the device's clock was `160.7 seconds late`. Both of these results were acquired using cross correlation between the signals as discussed in a Jupyter Notebook[^correlation].

<a
    href="/images/17_neuroon_analysis_summary/correlation_heatmap.png"
    target="_blank">
<img
    title="NeuroOn / PSG correlation heatmap from the first night"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/correlation_heatmap.png"
    style="width: 600px; height: auto; margin: 2em auto 2em;">
</a>

After finding the delays from both nights we assumed that the hypnograms - sleep staging graphs from both devices do correlate and decided to analyze their time shift. It turns out that in addition to `160 seconds` of signal delay, NeuroOn hypnogram had an additional `90 seconds` delay in detecting a sleep phase. This hypnogram was acquired by running the Intelclinic's algorithms offline, using developer's scripts - we currently have no data on delays in real-time taking place on mobile devices, as intended for end users.

<a
    href="/images/17_neuroon_analysis_summary/hypnogram_comparison.png"
    target="_blank">
<img
    title="NeuroOn / PSG hypnogram comparison - Night 1"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/hypnogram_comparison.png"
    style="width: 600px; height: auto; margin: 2em auto 2em;">
</a>

### Total accuracy in detecting sleep phases

With the clock synchronization no longer an issue, we could start comparing sleep staging between the two sources. The Jupyter Notebook[^hypnogram-comparison] is a good read for anyone interested in the code itself.

Since usage of EEG-based polysomnography[^PSG] and human-conducted sleep staging are at the moment of writing both academical and industrial standard, we assumed that PSG sleep stages are our single source of truth to which we compared NeuroOn's hypnograms.

We used Cohen's kappa coefficient analysis[^cohens-kappa]. Heatmaps represent confusion matrices[^confusion-matrix] normalized by rows ("Given a sleep stage detected by PSG, what was probability of NeuroOn to detect it as...?") and joint probability matrices[^joint-probability] which can give insight in the frequency of respective sleep phases.

```
             precision    recall  f1-score   support

        rem       0.70      0.60      0.64      4033
         N1       0.00      0.00      0.00      2190
         N2       0.57      0.91      0.70     10050
         N3       0.62      0.50      0.56      6690
       wake       0.28      0.01      0.03      2238

avg / total       0.53      0.60      0.53     25201

accuracy: 0.60
```

<a
    href="/images/17_neuroon_analysis_summary/night_01_all_stages.png"
    target="_blank">
<img
    title="Night 01 - sleep stages confusion matrix (normalized by rows)"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/night_01_all_stages.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

<a
    href="/images/17_neuroon_analysis_summary/night_01_all_stages.png"
    target="_blank">
<img
    title="Night 01 - sleep stages joint probability matrix"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/night_01_all_stages_joint.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>


And the second night:

```
             precision    recall  f1-score   support

        rem       0.80      0.85      0.82      6030
         N1       0.00      0.00      0.00      1181
         N2       0.70      0.70      0.70     10640
         N3       0.64      0.76      0.70      6750
       wake       0.31      0.14      0.19       600

avg / total       0.67      0.70      0.68     25201

accuracy: 0.70
```

<a
    href="/images/17_neuroon_analysis_summary/night_02_all_stages.png"
    target="_blank">
<img
    title="Night 02 - sleep stages confusion matrix (normalized by rows)"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/night_02_all_stages.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

<a
    href="/images/17_neuroon_analysis_summary/night_02_all_stages.png"
    target="_blank">
<img
    title="Night 02 - sleep stages joint probability matrix"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/night_02_all_stages_joint.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

What's interesting, NeuroOn's staging algorithm never detected N1 sleep stage, which affected its total score.

Accuracy[^accuracy] describes all sleep stages detected by NeuroOn compared to those detected by human in PSG signal. Average value of NeuroOn's accuracy from both nights is `0.65`, **putting it far below any requirements for medical usage.** It doesn't have to disqualify NeuroOn from personal use however.

To illustrate how different NeuroOn's results are different from a purely random "coin toss", here's a bootstrapped[^bootstrap] analysis from the second night:

<a
    href="/images/17_neuroon_analysis_summary/accuracy_permutation_test.png"
    target="_blank">
<img
    title="Night 02 - All stages"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/accuracy_permutation_test.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

If NeuroOn's sleep staging was truly random, the score would fall much closer to the randomly permuted sleep scores.

### Specific tests and current promises

After initial campaign marketing NeuroOn as a medical-grade device[^medical-grade] allowing tracking multiple sleep scores and helping in polyphasic sleep[^polyphasic-sleep] the company has backed off from their promises[^near-medical-grade], replacing them with something much more manageable. Maybe they don't need overall accuracy to deliver them?

Most users may be interested in these two questions:

 - Will NeuroOn wake me up when it has an opportunity to?
 - Will NeuroOn not wake me up when it shouldn't?

Basing on *Tassi, P., & Muzet, A. (2000). Sleep inertia. Sleep Medicine Reviews, 4(4), 341–353.*[^groggy-and-tired] we can select WAKE, N1 and N2 sleep stages as those allowing wake up call, and N3 and REM as those during which NeuroOn's user should not be disturbed.

We aggregated the results of these sleep stages, allowing NeuroOn to misidentify stages within families - WAKE/N1/N2 and N3/REM, since the errors shouldn't be detectable by an end-user.

Normalized and aggregated results from the first night:

<a
    href="/images/17_neuroon_analysis_summary/night_01_simplified.png"
    target="_blank">
<img
    title="Night 01 - Simplified Stages"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/night_01_simplified.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Second night:

<a
    href="/images/17_neuroon_analysis_summary/night_02_simplified.png"
    target="_blank">
<img
    title="Night 02 - Simplified Stages"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/night_02_simplified.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

And mean:

<a
    href="/images/17_neuroon_analysis_summary/both_nights_simplified.png"
    target="_blank">
<img
    title="Waking Matrix with PSG and NeuroOn"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/both_nights_simplified.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

There are two indicators of specific significance:

 - There is `26.2%` chance that NeuroOn will not detect a stage which allows an easy wake up. This isn't harmful to an end-user, since only consecutive misidentification of several stages might cause the alarm clock to go off too late.
 - There is however `31.6%` chance to misidentify a stage which doesn't allow easy wake up in a healthy person. **This may be the single disqualifying feature of NeuroOn**. If a person is woken up in N3 or REM (which NeuroOn interprets as N1, N2 or WAKE), they will suffer from sleep inertia and grogginess.

This means that using NeuroOn's alarm clock - in perfect conditions, keeping it well pressed against one's forehead and while not having any sleep disorders - may result in extremely bad waking up nearly 1/3 of the times.

Since lucid dream induction[^lucid-dream-induction] is quite complex and still discussed by many researchers, we don't feel that discussing its application in NeuroOn's app[^lucid-dreaming-neuroon] is within the scope of this analysis. What we can assess is NeuroOn's ability to detect REM sleep - roughly `72.3%` of PSG-detected REM stages are detected as REM by NeuroOn (mean from both nights).

### Beyond sleep staging - NeuroOn's signal quality

Our initial goal was not only to analyze NeuroOn's staging quality, but also its signal gathered by just 3 dry electrodes on the forehead. Is it possible to create a real-time sleep staging algorithm based that signal?

Answering that question fully would require us to build a perfect and much more advanced version of NeuroOn, de-facto taking on IntelClinic's role in developing the device. We could conduct a much simpler analysis instead, looking for well known EEG indicators within the signal.

EEG waves defined as respective frequencies of EEG signal differ between sleep stages and are one of the most important indicators used in polysomnography. Slow waves between `1Hz` and `3Hz` are called Delta Waves and are used for discriminating deep non-rem sleep phases[^delta-power]. It is reasonable to assume that NeuroOn staging algorithms use these indicators to create its own hypnograms.

With that knowledge we resorted to spectral analysis, studying delta power in NeuroOn's single-channel signal. Full analysis with more details, code and signal samples can be found in our Jupyter Notebook[^spectral-analysis].

Data from the first night:

<a
    href="/images/17_neuroon_analysis_summary/night_01_delta_power_neuroon.png"
    target="_blank">
<img
    title="Night 01 - Delta Power"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/night_01_delta_power_neuroon.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

<a
    href="/images/17_neuroon_analysis_summary/night_01_delta_power_psg.png"
    target="_blank">
<img
    title="Night 01 - Delta Power"
    class="article-img"
    src="/images/17_neuroon_analysis_summary/night_01_delta_power_psg.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

We examined how NeuroOn-recorded delta wave amplitude differs between (PSG-defined) N2 and N3 sleep stages. The results indicate that it is possible to differentiate between those two phases with approximately `75%` accuracy basing on a box-plot distribution.

The delta band powers are similarly distinct in both NeuroOn and PSG, which may imply that the signal gathered can be used for advanced and precise sleep staging - maybe even more precise than the current NeuroOn's[^delta-power]. This invalidates my initial assumption I approached NeuroOn with - that it's impossible to gather signal of good enough quality to reliably discern sleep stages from just 3 electrodes.

### Contrast with current claims

The initial Kickstarter campaign[^kickstarter] was full of unfounded claims, neuro-buzzwords[^neuro-buzzwords] and outright misinformation[^misinformation]. The team even promoted NeuroOn with *"Wanna sleep 2 hours/day ASK ME :)"* t-shirts[^tshirts].
After years in development and Facebook battles with skeptics IntelClinic was forced to back off from many of them.

NeuroOn's *Final* Press Release reads:

>Inteliclinic is a Polish startup whose Neuroon crowdfunding campaign on Kickstarter was a spectacular success. Initially, the project aimed at creating a device that would analyze users’ sleeping patterns and provide tips to people who want to sleep polyphasically (take a few shorter naps instead of a single nightly sleep episode.) After over a year of consultations with leading authorities on sleep medicine, including Christopher Drake, PhD, Director of Sleep Research, Henry Ford Hospital and former Chairman of the Board, National Sleep Foundation, Project Neuroon grew beyond sleep monitoring to include pulse tracking and light therapy. The core functionality of the device is nearly medical-grade sleep measurements and helping people who work shifts, suffer jet lags or have problems falling asleep. The device does not support polyphasic sleep.

I wouldn't say it was growing beyond, but rather realizing that the previous promises made by IntelClinic were completely unfounded in contemporary scientific knowledge. Without spending significant amounts of money on research[^any-papers?] the company wasn't able to deliver, so the startup pivoted and changed scope.

After backing off from "medical grade" device, "near-medical grade" might mean virtually anything.

Intelclinic did register two patents: *"System for polyphasic sleep management, method of its operation, device for sleep analysis, method of current sleep phase classification and use of the system and the device in polyphasic sleep management"* [^polyphasic-patent] and *"System, apparatus and method for treating sleep disorder symptoms"* [^sleep-disorder-patent]. While both of them contain technical overview into the mask's working, I am not aware of any whitepapers showcasing respective functions' feasibility[^any-papers?].

Evaluating its effectiveness of light therapy or jet lag adjustment would require a separate experiment and should be conducted (and released together will all the data) by IntelClinic itself in order to prove its effectiveness.

### Where I was wrong, where I was right

Over two years ago[^original-blogpost] I wrote:

> The NeuroOn sleep mask cannot work exactly as advertised - it cannot utilize a proper EEG signal. While it can detect a REM phase in sleep very roughly, it's very far from reliable sleep analysis. The majority of the population isn't able to achieve polyphasic sleep, since their brains aren't capable of that. A similar thing goes with lucid dreaming. NeuroOn at its best would be not too useful of a gadget to be put away after several uses.

 - `WRONG` Looking at the spectral analysis of NeuroOn's signal above it seems that I have been wrong in saying that it's impossible to reliably discern sleep stages from 3 electrodes located on the forehead. It looks like it should be possible, but requires much more research than IntelClinic has put in NeuroOn.
 - `RIGHT` It holds true that NeuroOn can conduct only a rough (not medical-grade) analysis of the sleep phases.
 - `RIGHT` Polyphasic Sleep isn't supported by NeuroOn, as confirmed by the IntelClinic.
 - `?` We don't know much about lucid dreaming yet, but the research required to change that might be quite costly.

### Addressing possible replies

> NeuroOn staging software you used was several months old. Here's a new version, and look, now the accuracy is better than 95%!

I agree that the software I was sent by IntelClinic was several months old at the time of analysis, but from my understanding it was the version which eventually landed in the consumer units.

Providing any version issued after we published our initial experiment description and sources will not give us any significant results, since it could have been tweaked to match exactly our signals.

The only way to prove that NeuroOn's algorithms have gotten better is to conduct new experiment at a third party's lab (like Sleep Disorders Center at the Institute of Psychiatry and Neurology in Warsaw[^sobieskiego]) and release the hypnograms immediately afterwards.

It'd be a good idea to test it on a patient suffering from sleep disorders, or anyone else than a 25-year-old caucasian male. Preferably several people.

Our code is completely open and should work with newly acquired signals.

> Alarm clock isn't the main functionality now, we're using only REM anyway!

Addressing lucid dreaming and light therapy is beyond the scope of this experiment.

### Startup marketing vs research-based development

(this is my personal opinion)

Winding up several months of research, tweaking the code, trying to make sense of the data, wondering if every method is statistically significant - I can say I'm happy I could have done that. No one paid me - quite the opposite, I rented the hospital lab and PSG with my own money - yet still, it was worth it.

I'd like everyone to make their own opinion on NeuroOn by reading this pretty detailed analysis. If you don't trust it, feel free to re-check all my computations in the Jupyter Notebook[^notebook].

Personally I consider NeuroOn to be a failed project, not researched enough from the start, running mostly on daring marketing promising the impossible.

Real innovation requires research. It's tedious, takes much more time than  the startup community promises. But it's honest - and it's the only way that yields any results.

I view startups similar to Intelclinic as deeply harmful for everyone - customers don't get what they pay for, investors are being misguided about what they support, researchers see their work being abused for the sake of a marketing campaign, and finally the society is being manipulated to see some kind of progress and hope in all that.

At the same time as NeuroOn, another neuro-device was put on Kickstarter - OpenBCI[^openbci]. It's a small open hardware EEG amplifier which allows to conduct experiments much cheaper than with university equipment. It didn't promise to make everyone's life better and it wasn't marketed as well as the IntelClinic's product. Despite earning much less money, OpenBCI delivered a device fulfilling all their promises.

When it comes to real progress and innovation, I'm much more inclined to believe researchers, hackers and makers showing open whitepapers and working prototypes first.

### Updates

In my original blog post I wrongly assumed that NeuroOn's sleep stage detection accuracy may be compared to actigraphy sleep/non-sleep accuracy, which is a much simpler indicator of sleep state. Its current limits are far below any device using EEG signals[^actigraphy-limitations]. These paragraphs are now removed.

I also clarified that sleep inertia is perceptible right after awakening and doesn't necessarily last all day (even though it might affect person's mood).

Added IntelClinic's patents to footnotes.

Previous version of this blogpost may be found on my Github[^blogpost-history].

### Footnotes

[^groggy-and-tired]: [Sleep Intertia on Wikipedia](https://en.wikipedia.org/wiki/Sleep_inertia) or from a publication: *Sleep inertia is a transitional state of lowered arousal occurring immediately after awakening from sleep and producing a temporary decrement in subsequent performance. Many factors are involved in the characteristics of sleep inertia. The duration of prior sleep can influence the severity of subsequent sleep inertia. Although most studies have focused on sleep inertia after short naps, its effects can be shown after a normal 8-h sleep period. One of the most critical factors is the sleep stage prior to awakening. Abrupt awakening during a slow wave sleep (SWS) episode produces more sleep inertia than awakening in stage 1 or 2, REM sleep being intermediate.* - [Tassi, P., & Muzet, A. (2000). Sleep inertia. Sleep Medicine Reviews, 4(4), 341–353.](https://www.ncbi.nlm.nih.gov/pubmed/12531174)

[^PSG]: Polysomnography is the most accurate scientific sleep study available without giving a person a brain implant - more on [Wikipedia](https://en.wikipedia.org/wiki/Polysomnography)

[^analysis]: [NeuroOn analysis - introduction and sources]({filename}/14en_neuroon_analysis_sources.md)

[^notebook]: Jupyter Notebook and all the signal files are available on [Github](https://github.com/pawelngei/sleep_project)

[^ryscet]: MSc Ryszard Cetnarski [github](https://github.com/ryscet/)

[^poster]: "Open-science: validation of neuro-startups" scientific poster is available on [my blog](neuroon-validation-poster)

[^neuroaspects]: Aspects of Neuroscience 2016 - [page](http://neuroaspects.org/conference-2016)

[^email]: alxd (at) alxd (dot) org

[^intelclinic]: Intelclinic is a company which created NeuroOn - [web page](https://inteliclinic.com/)

[^medical-grade]: "The application will also allow its users to access and setup the many features we have introduced so far, such as advanced sleep analytics, heart monitoring, intelligent alarm clock, jet lag, and alertness management, *all with medical-grade accuracy*." [source](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle/posts/925602) and to a lesser extent [source](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle/posts/886714), emphasis mine

[^near-medical-grade]: The core functionality of the device is nearly medical-grade sleep measurements and helping people who work shifts, suffer jet lags or have problems falling asleep. The device does not support polyphasic sleep. [source](https://neuroon.com/news/final-version-neuroon-press-release/)

[^AURA]: [SelectScience review](http://www.selectscience.net/products/aura-psg-ambulatory-systems/?prodID=171717)

[^healthy]: Full examination of my sleep patterns by a certified medical expert is available in Polish from the analysis blogpost[^analysis].

[^sex-bias-neuroscience]: It's a running joke in neuroscience, since a lot of experimental subjects are just campus students - usually caucasian males, which leads to ignoring biodiversity. [Sex Bias in Neuroscience and Biomedical Research, Annaliese K. Beery and Irving Zucker](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3008499/) and [Androcentrism on Wikipedia](https://en.wikipedia.org/wiki/Androcentrism)

[^marks]: The electrodes were pressed to my head so firmly they left visible marks the next day [(photo)](https://alxd.org/images/14_neuroon_signals/examination/electrode_prints.jpg)

[^reverse-engineer]: From [Wikipedia](https://en.wikipedia.org/wiki/Reverse_engineering): *Reverse engineering, also called back engineering, is the processes of extracting knowledge or design information from anything man-made and re-producing it or re-producing anything based on the extracted information. The process often involves disassembling something (a mechanical device, electronic component, computer program, or biological, chemical, or organic matter) and analyzing its components and workings in detail.*

[^correlation]: Cross-correlation computed [here](https://github.com/pawelngei/sleep_project/blob/master/Time_synchronization.ipynb) with various correlation tests available [here](https://github.com/pawelngei/sleep_project/blob/master/Correlation%20test.ipynb)

[^hypnogram-comparison]: Hypnogram comparison description, code and generated graphs are available on [Github](https://github.com/pawelngei/sleep_project/blob/master/Hipnogram_comparison.ipynb)

[^cohens-kappa]: Cohen's kappa on [Wikipedia](https://en.wikipedia.org/wiki/Cohen%27s_kappa)

[^confusion-matrix]: Confusion matrix is defined on [Wikipedia](https://en.wikipedia.org/wiki/Confusion_matrix): *"Each column of the matrix represents the instances in a predicted class while each row represents the instances in an actual class (or vice versa).[2] The name stems from the fact that it makes it easy to see if the system is confusing two classes (i.e. commonly mislabelling one as another)."* The sleep stages are normalized in rows, displaying probability of detecting respective sleep phases by NeuroOn (columns) given that the polysomnograph has detected a given (row) one.

[^joint-probability]: Joint probability distribution on [Wikipedia](https://en.wikipedia.org/wiki/Joint_probability_distribution): *given at least two random variables X, Y, ..., that are defined on a probability space, the joint probability distribution for X, Y, ... is a probability distribution that gives the probability that each of X, Y, ... falls in any particular range or discrete set of values specified for that variable.*

[^accuracy]: Accuracy is a measure of `(True Positives + True Negatives) / (Positives + Negatives)`, as defined in [Evaluation of binary classifiers](https://en.wikipedia.org/wiki/Evaluation_of_binary_classifiers)

[^bootstrap]: As [Wikipedia](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)) defines it, *bootstrapping can refer to any test or metric that relies on random sampling with replacement. Bootstrapping allows assigning measures of accuracy (defined in terms of bias, variance, confidence intervals, prediction error or some other such measure) to sample estimates. This technique allows estimation of the sampling distribution of almost any statistic using random sampling methods. Generally, it falls in the broader class of resampling methods.*

[^polyphasic-sleep]: Initial NeuroOn campaign promised customers polyphasic sleep functionalities on [Kickstarter](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle)

[^lucid-dream-induction]: *In lucid dreams the dreamer is aware of dreaming and often able to influence the ongoing dream content. Lucid dreaming is a learnable skill and a variety of techniques is suggested for lucid dreaming induction. This systematic review evaluated the evidence for the effectiveness of induction techniques. A comprehensive literature search was carried out in biomedical databases and specific resources. Thirty-five studies were included in the analysis (11 sleep laboratory and 24 field studies), of which 26 employed cognitive techniques, 11 external stimulation and one drug application. The methodological quality of the included studies was relatively low. None of the induction techniques were verified to induce lucid dreams reliably and consistently, although some of them look promising. On the basis of the reviewed studies, a taxonomy of lucid dream induction methods is presented. Several methodological issues are discussed and further directions for future studies are proposed.* - [Induction of lucid dreams: A systematic review of evidence - Tadas Stumbrys, Daniel Erlacher, Melanie Schädlich, Michael Schredl](http://www.sciencedirect.com/science/article/pii/S1053810012001614)

[^lucid-dreaming-neuroon]: Lucid Dreaming app for [NeuroOn](https://neuroon.com/lucid-dreaming/)

[^delta-power]: Delta Power in EEG - [Aeschbach, D., & Borbely, A. a. (1993). All-night dynamics of the human sleep EEG. Journal of Sleep Research.](https://www.ncbi.nlm.nih.gov/pubmed/10607074), [Mukai, J., Uchida, S., Miyazaki, S., Nishihara, K., & Honda, Y. (2003). Spectral analysis of all-night human sleep EEG in narcoleptic patients and normal subjects. J Sleep Res, 12(1), 63–71.](https://www.ncbi.nlm.nih.gov/pubmed/12603788)

[^spectral-analysis]: Spectral Analysis Jupyter Notebook can be found on our [Github](https://github.com/pawelngei/sleep_project/blob/master/Spectral%20analysis.ipynb)

[^neuro-buzzwords]: Widespread usage of non-scientific neurological claims by many startups is a well known problem, well described by [NeuroCritic](http://neurocritic.blogspot.com/2014/01/neurocrap-funded-by-masses-neuroon-and.html) and other science journalists.

[^kickstarter]: NeuroOn Kickstarter campaign made many unfounded claims [(link)](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle/description)

[^misinformation]: *Apparently Da Vinci, Tesla, Churchill and even Napoleon used polyphasic sleep to rest. It allowed them to fully regenerate, reducing sleep time to 6.5 hours or sometimes just 2 hours. And those guys got things done!* [NeuroOn's Kickstarter](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle/description) vs [Polyphasic Sleep: Facts and Myths by dr Piotr Wozniak](https://www.supermemo.com/en/articles/polyphasic)

[^tshirts]: T-Shirts worn by IntelClinic team at WebSummit Dublin 2013 [(photo)](https://ksr-ugc.imgix.net/assets/001/341/456/57eb4c010584ad8eb5343ec8ae07df2c_original.jpg?w=680&fit=max&v=1384737341&auto=format&q=92&s=d64354acf07b087cd497c5a07785bf4b)

[^any-papers?]: If you are aware of any whitepapers or peer-reviewed scientific papers by IntelClinic regarding NeuroOn project, please contact me, and I will officially apologize for my previous criticism. IntelClinic mentions their patents on [their homepage](https://neuroon.com/) and in [multiple](http://mamstartup.pl/technologie/8009/neuroon-ma-ponad-piec-tysiecy-zamowien-ta-maska-mierzy-parametry-snu) [interviews](http://pierwszymilion.forbes.pl/neuroon-polski-projekt-z-sukcesem-na-kickstarterze,artykuly,167476,1,1.html#) with startup portals.

[^polyphasic-patent]: *System for polyphasic sleep management, method of its operation, device for sleep analysis, method of current sleep phase classification and use of the system and the device in polyphasic sleep management* on [Google Patents](https://patents.google.com/patent/WO2015111012A1/en), filed 2015-01-26

[^sleep-disorder-patent]: *System, apparatus and method for treating sleep disorder symptoms* on [Google Patents](https://patents.google.com/patent/US20160193442A1/en), filed 2015-01-05

[^original-blogpost]: Original blogpost: NeuroOn: The Emperor is Naked! (only in Polish) on [my blog](neuroon-krol-jest-nagi-pl.html)

[^sobieskiego]: Sleep Disorders Center at the Institute of Psychiatry and Neurology in Warsaw [homepage](http://www.sen-instytut.pl/index_en.html)

[^openbci]: The original OpenBCI Kickstarter campaign from 2013 - [link](https://www.kickstarter.com/projects/openbci/openbci-an-open-source-brain-computer-interface-fo) and their [homepage](http://openbci.com/)

[^actigraphy-limitations]: *Purpose of the investigation was to evaluate the differences of movement density during the sleep stages and waking. 22 diurnally active, healthy, male volunteers of mean age 30.7 (+/-Standard deviation +/- 3.3) years and a Body-Mass-Index 23.6 +/- 3.3 kg/m2 participated in the study. All subjects were recorded in the sleep lab via cardiorespiratory polysomnography and wrist actigraphy (Ambulatory Monitoring, Ardsley, USA) worn on the non-dominant hand, for two consecutive nights. The activity data, consisting of the number of zero crossings (NZC) were recorded in 1-minute periods. Sleep stages were scored visually according to standard criteria. EEG- and actigraphy data were converted to the same data format (European Feature Files). Attaching the actimetry data to the sleep stages was calculated mean NZC for every sleep stage and Wake. In spite of high differences in total individual NZC we observed that most NZC occurred during Wake. NREM 1 movement density was significantly higher in 19 recordings (86%) than in any other sleep stage. In 18 cases (82%) lowest movement density was found in NREM 3/4 with significant difference to all other sleep stages. Within 50% of the recordings were found decreasing activity in the following sequence of stages: Wake > NREM 1 > REM > NREM 2 > NREM 3/4 However, in all other cases there was a varying pattern of activity. Conclusion: Although there is some correlation between motor activity and sleep stages, the predictive value of actimetry data analysis in the assessment of sleep structure appeared to be limited mainly by individual movement density, especially during REM and NREM 2.* [Actigraphy: methodological limits for evaluation of sleep stages and sleep structure of healthy probands - Conradt R, Brandenburg U, Ploch T, Peter JH.](https://www.ncbi.nlm.nih.gov/pubmed/9340625)

[^blogpost-history]: All files used to create this webpage - including raw blogpost texts in Markdown - are stored on my [Github](https://github.com/pawelngei/alxd.org/blob/master/content/17en_neuroon_analysis_results.md)
