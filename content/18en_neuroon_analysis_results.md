Title: NeuroOn analysis - results and discussion
Date: 2016-12-10
Slug: neuroon-analysis-results
Lang: en
Tags: neuroon, signal analysis, science, open notebook
Translation: false
Status: draft

### tl;dr - So, does it work?!

After an experiment conducted in perfect conditions: on 25-year-old caucasian male with no sleep disorders, sleeping nearly motionlessly with electrodes pressed to his head so firmly they left marks the next day[^marks], we are able to conclude:

NeuroOn isn't a medical grade device, but it's much better than a coin toss.

The total accuracy in detecting sleep stages is **65%**. Since this value holds little meaning to an end-user, let's ask two simpler questions:

 - Will NeuroOn wake me up when it has an opportunity to?
 - Will NeuroOn not wake me up when it shouldn't?

Comparing NeuroOn's sleep stage results to a professional polysomnography[^PSG] scored by a human expert:

<a
    href="/images/18_neuroon_analysis_summary/intro_waking_matrix_en.png"
    target="_blank">
<img
    title="Waking Matrix with PSG and NeuroOn"
    class="article-img"
    src="/images/18_neuroon_analysis_summary/intro_waking_matrix_en.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

 - In **73.8%** of cases where PSG detects a sleep phase suitable for waking up, NeuroOn agrees.
 - In **26.2%** it doesn't, meaning that it will wait for the next opportunity. No big deal.
 - In **68.4%** of cases where PSG says not to wake us up, NeuroOn agrees.
 - In **31.6%** of cases where we absolutely shouldn't be woken up, NeuroOn would still do it. **That's a big deal**, since it means that every ~third Night with NeuroOn alarm clock on we will wake up extremely groggy and tired[^groggy-and-tired].

While the results may be viewed as a step in a right direction, it should be kept in mind that accelerometer-only sleep stage analysis may yield better scores[^actigraph]  [^actillume].

And for the people who would like to understand what actually happened here...

### Long awaited results

This post is part of a series[^analysis] dedicated to NeuroOn sleep mask and its scientific viability. The full code and all signal samples are available at Github[^notebook].

Months after first estimates I would like to present you results of the NeuroOn experiment, in a form accessible to laymen. The analysis took nearly four months due to my stubbornness in assuring that it's scientifically sound, completely open, and reproducible at different machines. After roughly two months of dedicating every weekend to it, I realized my own understanding of mathematic, statistical analysis and SciPy / NumPy stack falls short for this challenge and asked MSc Ryszard Cetnarski[^ryscet] for help. Together we have been able to create a coherent Jupyter Notebook and open it for peer review in the Internet[^notebook], as well as a scientific poster[^poster] we presented at the Aspects of Neurosciences conference in Warsaw in November 2016. So far the only feedback we gathered regarded only small sample sizes and graph descriptions. If you have any additional suggestions, please send them to me[^email].

I'd like to thank Intelclinic for providing us a test unit of NeuroOn, as well as everybody who contributed to this analysis (in random order): Michal Kawalec, Adam Golinski, Bartosz Krol, Jaroslaw Hirniak, Karolina Stosio, Karol Benq Siek, Dawid Laszuk and Piotr Migdal.

### What did the experiment measure?

Our initial experimental hypothesis - *"Signal gathered by the NeuroOn mask is of a good enough quality to detect a sleep stage in real time, given processing power of an average smartphone"* proved to be too complex for a simple analysis, and while we could infer a lot from the signal's quality (discussed later), we were forced to change it.

Our final hypothesis was *"NeuroOn achieves medical-grade results in sleep staging as compared to a human expert working on a PSG signal"*, as claimed by IntelClinic[^medical-grade] (even though they backed out of that at some point[^near-medical-grade]).

EEG-based polysomnographs are the best medical- and scientific- grade devices for analyzing sleep and sleep stages, used widely in hospitals and research. We used Aura PSG [^AURA] used in clinical trials in Poland - and we will be considering it a single source of truth, being as close to the original brain signals as possible.

We analyzed signal from A1-F1 electrodes of the EEG (detailed description and electrode placement is available in the analysis blogpost[^analysis]), pre-cleaned by the Aura PSG amplifier[^AURA] and sleep staging performed by a human technician.

It is worth noting that there are only two nights (roughly 16 hours) of recordings captured on a healthy[^healthy] caucasian male in his 25s. To achieve any significant results we shouldn conduct experiments on a more varied population `n > 30` for more than 14 nights, including people with known sleep disorders.

For NeuroOn we used the signal gathered by the three electrodes (single differential channel) on the device and sleep staging performed by offline (not real-time) algorithm executed on an external machine afterwards. The software used to do it was provided to us by Intelclinic on the 08.03.2016 under a condition that we will not try to reverse engineer it, to which we obliged.

### NeuroOn time delay

First, we assumed that both NeuroOn's and PSG's signals do correlate and compared them. It turns out that the devices' clocks were desynchronized, with NeuroOn's running roughly `160.5 seconds late` and having a slowly growing delay on the course of the 8-hour recording. For the second night the device's clock was `160.7 seconds late`. Both of these results were acquired using cross correlation between the signals as discussed in a Jupyter Notebook[^correlation].

After finding the delays from both nights we assumed that the hypnograms - sleep staging graphs from both devices do correlate and decided to analyze their time shift. It turns out that in addition to `160 seconds` of signal delay, NeuroOn hypnogram had an additional `90 seconds` delay in detecting a sleep phase. The result was achieved by running the Intelclinic's algorithms offline, using a developer's scripts - we currently have no data on delays in real-time taking place on mobile devices, as intended for end users.

### Total accuracy in detecting sleep phases

With the clock synchronization no longer an issue, we can start comparing sleep staging between the two sources. The Jupyter Notebook[^hypnogram-comparison] is a good read for anyone interested in the code itself.

Since usage of EEG-based polysomnography[^PSG] and human-conducted sleep staging are at the moment of writing both academical and industrial standard, we assumed that PSG sleep stages are our single source of truth to which we compared NeuroOn's hypnograms.

We used Cohen's kappa coefficient analysis[^cohens-kappa]. Values from the first night:

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
    href="/images/18_neuroon_analysis_summary/night_01_all_stages.png"
    target="_blank">
<img
    title="Night 01 - All stages"
    class="article-img"
    src="/images/18_neuroon_analysis_summary/night_01_all_stages.png"
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
    href="/images/18_neuroon_analysis_summary/night_02_all_stages.png"
    target="_blank">
<img
    title="Night 02 - All stages"
    class="article-img"
    src="/images/18_neuroon_analysis_summary/night_02_all_stages.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

All values on the heatmaps are minutes, not normalized horizontally nor vertically.

What's interesting, NeuroOn's staging algorithm never detected N1 sleep stage, which affected its total score.

Accuracy[^accuracy] describes all sleep stages detected by NeuroOn compared to those detected by human in PSG signal. Average value of NeuroOn's accuracy from both nights is `0.65`, **putting it far below any requirements for medical usage.** It doesn't have to disqualify NeuroOn from personal use however.

To illustrate how different NeuroOn's results are different from a purely random "coin toss", here's a bootstrapped analysis from the second night:

<a
    href="/images/18_neuroon_analysis_summary/accuracy_permutation_test.png"
    target="_blank">
<img
    title="Night 02 - All stages"
    class="article-img"
    src="/images/18_neuroon_analysis_summary/accuracy_permutation_test.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

If NeuroOn's sleep staging was truly random, the score would fall much closer to the randomly permuted sleep scores.

### Specific tests and current promises

After initial campaign marketing NeuroOn as a medical-grade device[^medical-grade] allowing tracking multiple sleep scores and helping in polyphasic sleep[^polyphasic-sleep] the company has backed off from their promises[^near-medical-grade], replacing them with something much more manageable. Maybe they don't need overall accuracy to deliver them?

The most users may be interested in two questions:

 - Will NeuroOn wake me up when it has an opportunity to?
 - Will NeuroOn not wake me up when it shouldn't?

Basing on *Tassi, P., & Muzet, A. (2000). Sleep inertia. Sleep Medicine Reviews, 4(4), 341–353.*[^groggy-and-tired] we can select WAKE, N1 and N2 sleep stages as those allowing wake up call, and N3 and REM as those during which NeuroOn's user should not be disturbed.

We aggregated the results of these sleep stages, allowing NeuroOn to misidentify stages within families - WAKE/N1/N2 and N3/REM, since the errors shouldn't be detectable by an end-user.

Normalized and aggregated results from the first night:

<a
    href="/images/18_neuroon_analysis_summary/night_01_simplified.png"
    target="_blank">
<img
    title="Night 01 - Simplified Stages"
    class="article-img"
    src="/images/18_neuroon_analysis_summary/night_01_simplified.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Second night:

<a
    href="/images/18_neuroon_analysis_summary/night_02_simplified.png"
    target="_blank">
<img
    title="Night 02 - Simplified Stages"
    class="article-img"
    src="/images/18_neuroon_analysis_summary/night_02_simplified.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

And mean:

<a
    href="/images/18_neuroon_analysis_summary/intro_waking_matrix_en.png"
    target="_blank">
<img
    title="Waking Matrix with PSG and NeuroOn"
    class="article-img"
    src="/images/18_neuroon_analysis_summary/intro_waking_matrix_en.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

There are two indicators of specific significance:

 - There is `26.2%` chance, that NeuroOn will not detect a stage which allows an easy wake up. This isn't harmful to an end-user, since only consecutive misidentification of several stages might cause the alarm clock to go off too late.
 - There is however `31.6%` chance to misidentify a stage which doesn't allow easy wake up in a healthy person. **This may be the single disqualifying feature of NeuroOn**. If a person is woken up in N3 or REM (which NeuroOn interpreted as N1, N2 or WAKE), they will suffer from sleep inertia and grogginess for the rest of the day.

This means that using NeuroOn's alarm clock - in perfect conditions, keeping it well pressed against one's forehead and while not having any sleep disorders - may result in extremely bad waking up nearly 1/3 of the times.

Since lucid dream induction [SOURCE] is quite complex and still discussed by many researchers, we don't feel that discussing its application in NeuroOn's app[^lucid-dreaming-neuroon] is within the scope of this analysis. What we can assess is NeuroOn's ability to detect REM sleep, which is quite good - [CALCULATE].

### Beyond sleep staging - NeuroOn's signal quality

Our initial goal was not only to analyze NeuroOn's staging quality, but also its signal gathered by just 3 dry electrodes on the forehead. Is it possible to create a real-time sleep staging algorithm based that signal?

Answering that question fully would require us to build a perfect and much more advanced version of NeuroOn, de-facto taking on IntelClinic's role in developing the device. We could conduct a much simpler analysis instead, looking for well known EEG indicators within the signal.

We resorted to spectral analysis, studying delta power in NeuroOn's single-channel signal. Full analysis with more details, code and signal samples can be found in our Jupyter Notebook[^spectral-analysis].

Delta power, which we define as sum of the power spectral density between `1hz` and `3hz` is a well established EEG measure which can be used to discriminate sleep stages[^delta-power].

Data from the first night:

<a
    href="/images/18_neuroon_analysis_summary/night_01_delta_power_neuroon.png"
    target="_blank">
<img
    title="Night 01 - Delta Power"
    class="article-img"
    src="/images/18_neuroon_analysis_summary/night_01_delta_power_neuroon.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

<a
    href="/images/18_neuroon_analysis_summary/night_01_delta_power_psg.png"
    target="_blank">
<img
    title="Night 01 - Delta Power"
    class="article-img"
    src="/images/18_neuroon_analysis_summary/night_01_delta_power_psg.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

[!!!re-check validity, sources for this paragraph!!!]

The delta band powers are similarly distinct in both NeuroOn and PSG, which may imply that the signal gathered can be used for advanced and precise sleep staging - maybe even more precise than the current NeuroOn's[^delta-power]. This invalidates my initial assumption I approached NeuroOn with - that it's impossible to gather signal of good enough quality to reliably discern sleep stages from just 3 electrodes. Its analysis in real-time may still be very complex, which leaves us with another, maybe simpler option:

### Why use EEG?

Even though NeuroOn's marketing success was largely founded in in usage of neuro-buzzwords[^neuro-buzzwords] one should also ask: if it is best-quality sleep staging for end-user that we're trying to achieve, should we use EEG? Are there different, less uncomfortable and more accurate methods of analyzing sleep? Or do users need to wake up with electrode prints on their forehead every morning to get a proper signal quality?

Research done on clinical-grade wrist-worn devices[^actigraph]  [^actillume] suggests that is is possible to achieve results better than NeuroOn's by focusing on accelerometer analysis only. Respective teams were able to obtain `82-89%` agreement rate with the PSG[^actigraph] and `81%` overall accuracy[^actillume] on much bigger populations than this experiment.

NeuroOn's campaign openly criticized wrist-based accelerometers, claiming that *"The competition? They must be dreaming!" (...) "Accelerometer is less precise than biological signal processing"*  [^kickstarter]. After through analysis - it doesn't seems so.

### Contrast with current claims

The initial Kickstarter campaign[^kickstarter] was full of unfounded claims, neuro-buzzwords and outright misinformation[^misinformation]. The team even promoted NeuroOn with *"Wanna sleep 2 hours/day ASK ME :)* t-shirts[^tshirts].
After years in development and Facebook battles with skeptics IntelClinic was forced to back off from many of them.

NeuroOn's *Final* Press Release reads:

>Inteliclinic is a Polish startup whose Neuroon crowdfunding campaign on Kickstarter was a spectacular success. Initially, the project aimed at creating a device that would analyze users’ sleeping patterns and provide tips to people who want to sleep polyphasically (take a few shorter naps instead of a single nightly sleep episode.) After over a year of consultations with leading authorities on sleep medicine, including Christopher Drake, PhD, Director of Sleep Research, Henry Ford Hospital and former Chairman of the Board, National Sleep Foundation, Project Neuroon grew beyond sleep monitoring to include pulse tracking and light therapy. The core functionality of the device is nearly medical-grade sleep measurements and helping people who work shifts, suffer jet lags or have problems falling asleep. The device does not support polyphasic sleep.

I wouldn't say it was growing beyond, but rather realizing that the previous promises made by IntelClinic were completely unfounded in contemporary scientific knowledge. Without spending significant amounts of money on research[^any-papers?] the company wasn't able to deliver, so the startup pivoted and changed scope.

After backing off from "medical grade" device, "near-medical grade" might mean virtually anything.

Evaluating its effectiveness of light therapy or jet lag adjustment would require a separate experiment and should be conducted (and released together will all the data) by IntelClinic itself in order to prove its effectiveness.

### Where I was wrong, where I was right

Over two years ago[^original-blogpost] I wrote:

> The NeuroOn sleep mask cannot work exactly as advertised - it cannot utilize a proper EEG signal. While it can detect a REM phase in sleep very roughly, it's very far from reliable sleep analysis. The majority of the population isn't able to achieve polyphasic sleep, since their brains aren't capable of that. A similar thing goes with lucid dreaming. NeuroOn at its best would be not too useful of a gadget to be put away after several uses.

 - `WRONG` Looking at the spectral analysis of NeuroOn's signal above it seems that I have been wrong in saying that it's impossible to reliably discern sleep stages from 3 electrodes located on the forehead. It looks like it should be possible, given much more research than IntelClinic has put in NeuroOn.
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

Winding up several months of research, tweaking the code, trying to make sense of the data, wondering if *that* method is statistically significant giving I've just used *that* transform from version 0.15.3 - I can say I'm happy I could have done that. No one paid me - quite the opposite, I rented the hospital lab and PSG with my own money - yet still, it was worth it.

I'd like to show you that real innovation requires research. It's tedious, takes much more time than you've previously expected and it's nothing like the startup community has promised you. But it's honest - and it's the only way that yields any results.

I consider startups and Kickstarter campaigns like IntelClinic's NeuroOn deeply harmful. Promising a product that you haven't even checked is possible to build is just plain lying. Spending more money on marketing campaigns than actual, peer-reviewed research is just scamming.

There are much better aspirations than founding a startup. If you're really interested in changing the world and improving something, think about hackerspaces. Build technology with your own hands, share the knowledge and see the impact it makes.

I hope my next project will help you with that.


### Footnotes

[^marks]: The electrodes were pressed to my head so firmly they left visible marks the next day [(photo)](https://alxd.org/images/14_neuroon_signals/examination/electrode_prints.jpg)

[^ryscet]: MSc Ryszard Cetnarski [github](https://github.com/ryscet/)

[^email]: alxd (at) alxd (dot) org

[^groggy-and-tired]: [Sleep Intertia on Wikipedia](https://en.wikipedia.org/wiki/Sleep_inertia) or from a publication: *Sleep inertia is a transitional state of lowered arousal occurring immediately after awakening from sleep and producing a temporary decrement in subsequent performance. Many factors are involved in the characteristics of sleep inertia. The duration of prior sleep can influence the severity of subsequent sleep inertia. Although most studies have focused on sleep inertia after short naps, its effects can be shown after a normal 8-h sleep period. One of the most critical factors is the sleep stage prior to awakening. Abrupt awakening during a slow wave sleep (SWS) episode produces more sleep inertia than awakening in stage 1 or 2, REM sleep being intermediate.* - [Tassi, P., & Muzet, A. (2000). Sleep inertia. Sleep Medicine Reviews, 4(4), 341–353.](https://www.ncbi.nlm.nih.gov/pubmed/12531174)

[^analysis]: [NeuroOn analysis - introduction and sources]({filename}/15en_neuroon-analysis-sources.md)

[^notebook]: Jupyter Notebook and all the signal files are available on [Github](https://github.com/pawelchojnacki/sleep_project)

[^poster]: "Open-science: validation of neuro-startups" scientific poster is available on [my blog](neuroon-validation-poster)

[^medical-grade]: "The application will also allow its users to access and setup the many features we have introduced so far, such as advanced sleep analytics, heart monitoring, intelligent alarm clock, jet lag, and alertness management, *all with medical-grade accuracy*." [source](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle/posts/925602) and to a lesser extent [source](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle/posts/886714), emphasis mine

[^near-medical-grade]: The core functionality of the device is nearly medical-grade sleep measurements and helping people who work shifts, suffer jet lags or have problems falling asleep. The device does not support polyphasic sleep. [source](https://neuroon.com/news/final-version-neuroon-press-release/)

[^AURA]: [SelectScience review](http://www.selectscience.net/products/aura-psg-ambulatory-systems/?prodID=171717)

[^healthy]: Full examination of my sleep patterns by a certified medical expert is available in Polish from the analysis blogpost[^analysis].

[^correlation]: Cross-correlation computed [here](https://github.com/pawelchojnacki/sleep_project/blob/master/Time_synchronization.ipynb) with various correlation tests available [here](https://github.com/pawelchojnacki/sleep_project/blob/master/Correlation%20test.ipynb)

[^hypnogram-comparison]: Hypnogram comparison description, code and generated graphs are available on [Github](https://github.com/pawelchojnacki/sleep_project/blob/master/Hipnogram_comparison.ipynb)

[^PSG]: Polysomnography is the most accurate scientific sleep study available without giving a person a brain implant - more on [Wikipedia](https://en.wikipedia.org/wiki/Polysomnography)

[^cohens-kappa]: Cohen's kappa on [Wikipedia](https://en.wikipedia.org/wiki/Cohen%27s_kappa)

[^accuracy]: Accuracy is a measure of `(True Positives + True Negatives) / (Positives + Negatives)`, as defined in [Evaluation of binary classifiers](https://en.wikipedia.org/wiki/Evaluation_of_binary_classifiers)

[^polyphasic-sleep]: Initial NeuroOn campaign promised customers polyphasic sleep functionalities on [Kickstarter](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle)

[^lucid-dreaming-neuroon]: Lucid Dreaming app for [NeuroOn](https://neuroon.com/lucid-dreaming/)

[^spectral-analysis]: Spectral Analysis Jupyter Notebook can be found on our [Github](https://github.com/pawelchojnacki/sleep_project/blob/master/Spectral%20analysis.ipynb)

[^delta-power]: Delta Power in EEG - [Aeschbach, D., & Borbely, A. a. (1993). All-night dynamics of the human sleep EEG. Journal of Sleep Research.](https://www.ncbi.nlm.nih.gov/pubmed/10607074), [Mukai, J., Uchida, S., Miyazaki, S., Nishihara, K., & Honda, Y. (2003). Spectral analysis of all-night human sleep EEG in narcoleptic patients and normal subjects. J Sleep Res, 12(1), 63–71.](https://www.ncbi.nlm.nih.gov/pubmed/12603788)

[^neuro-buzzwords]: Widespread usage of non-scientific neurological claims by many startups is a well known problem, well described by [NeuroCritic](http://neurocritic.blogspot.com/2014/01/neurocrap-funded-by-masses-neuroon-and.html) and other science journalists.

[^actigraph]: *Two validation studies were conducted to optimize the sleep-detection algorithm of the Actillume. The first study used home recordings of postmenopausal women (age range: 51 to 77 years), which were analyzed to derive the optimal algorithm for detecting sleep and wakefulness from wrist activity data, both for nocturnal in-bed recordings and considering the entire 24 h. The second study explored the optimal algorithm to score in-bed recordings of healthy young adults (age range: 19 to 34 years) monitored in the laboratory. In Study I, the algorithm for in-bed recordings (n=39) showed a minute-by-minute agreement of 85% between Actillume and polysomnography (PSG), a correlation of .98, and a mean measurement error (ME) of 21 min for estimates of sleep duration. Using the same algorithm to score 24-h recordings with Webster's rules, an agreement of 89%, a correlation of .90, and 1 min ME were observed. A different algorithm proved optimal to score in-bed recordings (n=31) of young adults, yielding an agreement of 91%, a correlation of .92, and an ME of 5 min. The strong correlations and agreements between sleep estimates from Actillume and PSG in both studies suggest that the Actillume can reliably monitor sleep and wakefulness both in community-residing elderly and healthy young adults in the laboratory. However, different algorithms are optimal for individuals with different characteristics.* - [Sleep detection with an accelerometer actigraph: comparisons with polysomnography - Girardin Jean-Louisa, Daniel F Kripkea, Roger J Colec, Joseph D Assmusa, Robert D Langerb](http://www.sciencedirect.com/science/article/pii/S0031938400003553)

[^actillume]: *This study evaluated the Actillume instrument and the modified Action 3 sleep-wake scoring algorithm, in which the scoring factor (P) was set at 0.10, 0.14, 0.20, 0.30, 0.40 and 0.50. Fifteen subjects, each of whom underwent polysomnography with simultaneous wrist actigraphy four times, yielded a total of 60 sleep studies. The sleep data from each subject were divided into four groups. In the high sleep efficiency index groups of the calibration and validation samples, the accuracy of the algorithm significantly differed within six P-values and was highest at P=0.14. In the low sleep efficiency index groups of both samples, however, there were no significant differences in the accuracy. Thus, these results indicate that P=0.14 should be most appropriate for this actigraph and algorithm.* [Evaluation of the Actillume wrist actigraphy monitor in the detection of sleeping and waking. Matsumoto M, Miyagishi T, Sack RL, Hughes RJ, Blood ML, Lewy AJ.](https://www.ncbi.nlm.nih.gov/pubmed/9628126)

[^kickstarter]: NeuroOn Kickstarter campaign made many unfounded claims [(link)](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle/description)

[^misinformation]: *Apparently Da Vinci, Tesla, Churchill and even Napoleon used polyphasic sleep to rest. It allowed them to fully regenerate, reducing sleep time to 6.5 hours or sometimes just 2 hours. And those guys got things done!* [NeuroOn's Kickstarter](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle/description) vs [Polyphasic Sleep: Facts and Myths by dr Piotr Wozniak](https://www.supermemo.com/en/articles/polyphasic)

[^tshirts]: T-Shirts worn by IntelClinic team at WebSummit Dublin 2013 [(photo)](https://ksr-ugc.imgix.net/assets/001/341/456/57eb4c010584ad8eb5343ec8ae07df2c_original.jpg?w=680&fit=max&v=1384737341&auto=format&q=92&s=d64354acf07b087cd497c5a07785bf4b)

[^any-papers?]: If you are aware of any peer-reviewed scientific papers or patents submitted by IntelClinic regarding NeuroOn project, please contact me, and I will officially apologize for my previous criticism. IntelClinic mentions their patents on [their homepage](https://neuroon.com/) and in [multiple](http://mamstartup.pl/technologie/8009/neuroon-ma-ponad-piec-tysiecy-zamowien-ta-maska-mierzy-parametry-snu) [interviews](http://pierwszymilion.forbes.pl/neuroon-polski-projekt-z-sukcesem-na-kickstarterze,artykuly,167476,1,1.html#) with startup portals.

[^original-blogpost]: Original blogpost: NeuroOn: The Emperor is Naked! (only in Polish) on [my blog](neuroon-krol-jest-nagi-pl.html)

[^sobieskiego]: Sleep Disorders Center at the Institute of Psychiatry and Neurology in Warsaw [homepage](http://www.sen-instytut.pl/index_en.html)
