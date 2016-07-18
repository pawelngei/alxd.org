Title: NeuroOn analysis - introduction and sources
Date: 2016-06-27
Slug: neuroon-analysis-sources
Lang: en
Tags: neuroon, signal analysis, science, open notebook
Translation: true

<a 
    href="/images/14_neuroon_signals/examination/examination_bed.jpg"
    target="_blank">
<img
    title="NeuroOn on the examination bed"
    class="article-img"
    src="/images/14_neuroon_signals/examination/examination_bed.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

### NeuroOn Today

I was intending to start a blog for a long time, kept back by the feeling that I didn't really have anything valuable to share. This changed when I found a Polish startup - NeuroOn[^1] over two years ago. My first post[^2] expressed all the hopes I had for the sleep mask and skepticism at the clear disregard for scientific standards of its creators. Since it consists mostly of quotes I don't want to risk misinterpretation of IntelClinic employees by translating it fully. I ended it with the following paragraph:

> The NeuroOn sleep mask cannot work exactly as advertised - it cannot utilize a proper EEG signal. While it can detect a REM phase in sleep very roughly, it's very far from reliable sleep analysis. The majority of the population isn't able to achieve polyphasic sleep, since their brains aren't capable of that. A similar thing goes with lucid dreaming. NeuroOn at its best would be not too useful of a gadget to be put away after several uses.

This was far from the only voice of skepticism. The sleep mask was criticized by several blogs popularizing neurosciences, including takingcatsapart[^3] and neurocritic[^4] and the Polish sleep scientist Adam Wichniak MD[^5]. The arguments can be divided into two groups:

 - doubting that the mask can gather signal useful for analysis
 - claiming that the majority of the population cannot achieve polyphasic sleep

In the following two years NeuroOn has managed to finally hit the market and pivot, abandoning its claims to polyphasic sleep[^6], which were replaced by light therapy, jetlag-coping application and general sleep analytics[^7]. It was undoubtedly a reasonable decision, taking half of the arguments from the skeptics' hands - yet many NeuroOn clients and supporters felt cheated, as they were promised a polyphasic sleep product[^8].

I don't want to dwell on the feasibility of inducing a deep and satisfying lucid dream[^9] in every NeuroOn user, especially with access to research showing that different individuals may have varying degrees of capability in achieving lucid dreams[^10].

My main argument against NeuroOn is its controversial claim to be able to gather a useful signal from just:

 - three
 - dry electrodes
 - placed just above the supraorbital ridge (eyebrows)
 - in a mask which may be moved during the course of the night

I have to admit that there are examples of successful EEG experiments being carried out in one of these respective conditions (which the Intelclinic team promptly pointed out in replying to my former criticism[^11]). There is however no experiment, to my knowledge, which would combine all these points and still gather any kind of usable and analyzable signal. I am aware that NeuroOn claims to use not only EEG readings, but also an EOG, thermometer, pulse oximeter and accelerometer to detect the sleep stages - yet many of its users describe its detection accuracy as very low[^12]. In the light of all these arguments I remain skeptical if the mask works exactly as advertised.

### NeuroOn Analysis

Over course of the last two years I declared my willingness to conduct full research into NeuroOn - and I invited such an offer from Kamil Adamczyk and the Intelclinic team with great enthusiasm. They agreed to lend me a test unit for an unspecified amount of time - as long as I need for my tests. Even though we disagree on many issues, I have to openly show respect to them.

The developer model of the NeuroOn looks and according to my understanding works exactly as a production model - it's just a PCB board in a silicone casing with several additional cables allowing access to its data ports.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_main_unit_front.jpg"
    target="_blank">
<img
    title="NeuroOn board - front"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_main_unit_front.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Three gold plated electrodes are located at the very top of the board (I haven't checked the exact material so as not to damage the mask, but the product description claims[^13] it's gold). Together they produce one differential channel of combined EEG, EOG and EMG, with the center electrode serving as a ground. The pulse oximeter and thermometer are hidden in a cutout area close to the middle electrode and LEDs are visible in the bottom corners. In the very heart of the board there is the only button serving as an on/off toggle.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_main_unit_back.jpg"
    target="_blank">
<img
    title="NeuroOn board - back"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_main_unit_back.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

There are no interesting elements on the back of the board. I understand "test unit" to be only the signature of pre-production units, with exactly the same specifications as the production models.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_foam_back.jpg"
    target="_blank">
<img
    title="NeuroOn foam - back"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_foam_back.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

The mask itself together with the band that holds it tightly to the user's head. Its length can be regulated by undoing the velcro between the foam and more rigid mask front and just moving the band's holders on the velcro.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_foam_front.jpg"
    target="_blank">
<img
    title="NeuroOn foam - front"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_foam_front.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

The front of the mask unit is made of foam. The PCB board is placed in the opening at its top and is not held by any kind of velcro or additional bands. If the NeuroOn is worn properly it cannot fall of being kept between the user's forehead and the mask - the electrode prints on the skin can be visible even an hour after waking up.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_assembled_noleds.jpg"
    target="_blank">
<img
    title="Assembled NeuroOn"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_assembled_noleds.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

The LEDs are visible exactly in the foam's cutouts.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_assembled_led.jpg"
    target="_blank">
<img
    title="Włączony NeuroOn"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_assembled_led.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

After turning the mask on, a pair of blue LEDs light up. In my very subjective opinion I don't like the wake up mode of the mask, as the LEDs seem blinding after total darkness, and after clawing the mask off my eyes I'm even more blinded by the ambient light in the room, getting an instant headache.

I used the mask in developer mode, using a graphical manager created in Java by the Intelclinic team. According to our agreement I cannot share its code or binary files used for signal analysis. It also means that I haven't used a regular phone app, going to a Bluetooth / data cable debugger instead.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_debug_ground.jpg"
    target="_blank">
<img
    title="Ground in debugging mode"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_debug_ground.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Even though NeuroOn has a microUSB port it isn't connected to the data pin, serving only as a universal charger. In my setup I'm using it as a ground.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_debug_nochannel.jpg"
    target="_blank">
<img
    title="Data pin"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_debug_nochannel.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

The data pin is located as the very first pin on the left side of the board, under the silicone. In order to reach it, I need to prick the outer silicone layer with a specially prepared signal cable.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_debug_data.jpg"
    target="_blank">
<img
    title="Pricking the data pin"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_debug_data.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

The data cable properly put on. It only looks off, it's working.

<a 
    href="/images/14_neuroon_signals/mask/neuroon_debug_full.jpg"
    target="_blank">
<img
    title="NeuroOn assembled for debugging"
    class="article-img"
    src="/images/14_neuroon_signals/mask/neuroon_debug_full.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Now NeuroOn the is ready to be connected to my PC and programmed in debugging mode. It allows access to most phone app modes and most importantly - data gathering and downloading. Sadly, the Java software required changing port permissions or root access to run properly, which forced me to use it only on a dedicated USB sandbox with Ubuntu.

### Examination

After conducting several night-ling signal gathering sessions with NeuroOn I decided to proceed with a proper experiment. My main research question was: *is signal gathered by the mask of a good enough quality to detect a sleep stage in real time, given processing power of an average smartphone?* Intelclinic promised a mask able to wake up its user in an optimal sleep stage - so I'm assuming that it should have knowledge of their state at any given moment.

<a 
    href="/images/14_neuroon_signals/examination/doorsign.jpg"
    target="_blank">
<img
    title="Sleep disorders lab"
    class="article-img"
    src="/images/14_neuroon_signals/examination/doorsign.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

I decided to compare the NeuroOn to a professional polysomnograph at the Sleep Disorders Center at the Institute of Psychiatry and Neurology in Warsaw[^14]. After several months of saving money I could afford to buy a full examination package lasting two nights. During the first of them, following signals were gathered:

 - EEG
 - EOG
 - ECG
 - breath flow
 - oxygen saturation in blood
 - chest movements
 - leg movements

The second night consisted of only:

- EEG
- EOG
- ECG

Of course during both of them I was gathering signal from the NeuroOn as well. Its location of my forehead wasn't a problem - no electrodes in traditional 10-20 based sleep examinations are located so low above eyebrows.

<a 
    href="/images/14_neuroon_signals/examination/examination_bed.jpg"
    target="_blank">
<img
    title="NeuroOn on the polysomnography examination bed"
    class="article-img"
    src="/images/14_neuroon_signals/examination/examination_bed.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

NeuroOn on an examination bed. Since the room wasn't shielded or covered in a Faraday cage, please expect 50Hz band to be cut off from the result signal due to resonance with the electric network.

<a 
    href="/images/14_neuroon_signals/examination/testing_suite.jpg"
    target="_blank">
<img
    title="Setting NeuroOn up for a night"
    class="article-img"
    src="/images/14_neuroon_signals/examination/testing_suite.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Programming the board before the first night, so that it gathers signal for the next eight hours. I was instructed to use the "CLEAR" option before each session, which in my understanding means overwriting the free memory with zeros.

<a 
    href="/images/14_neuroon_signals/examination/amplifier_front.jpg"
    target="_blank">
<img
    title="Apmplifier - front"
    class="article-img"
    src="/images/14_neuroon_signals/examination/amplifier_front.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

During both of the nights AURA PSG by GRASS Technologies[^15] was used. It gathered signals with 200Hz frequency. According to the Sleep Disorders Center it's a standard for professional drug research.

<a 
    href="/images/14_neuroon_signals/examination/amplifier_back.jpg"
    target="_blank">
<img
    title="Amplifier - back"
    class="article-img"
    src="/images/14_neuroon_signals/examination/amplifier_back.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

All signals were saved directly to a computer in the Center, bypassing the device's memory.

<a 
    href="/images/14_neuroon_signals/examination/1020.png"
    target="_blank">
<img
    title="Channels on 10-20 diagram"
    class="article-img"
    src="/images/14_neuroon_signals/examination/1020.png"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Electrodes used in both sessions: A1 and A2, F3 and F4, C3 and C4, O1 and O2, Fz and Cz as ground and reference. In addition to them EOG1 and EOG2 for EOG, CHIN1, CHIN2 and CHIN3 on the chin, for detecting face movements and ECG on the chest.

<a 
    href="/images/14_neuroon_signals/examination/night_1_electrodes_front.jpg"
    target="_blank">
<img
    title="Electrode placement - front"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_1_electrodes_front.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

Night one - electrode placement on the front - EOG1 and EOG2 are visible by the eyes, Fz on the forehead, CHIN1, CHIN2 and CHIN3 under the chin. F3 and F4 just over the (nonexistent) hairline.

<a 
    href="/images/14_neuroon_signals/examination/night_1_electrodes_left.jpg"
    target="_blank">
<img
    title="Electrode placement - left side"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_1_electrodes_left.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

Visible CHIN1, EOG1, F3, C3 and O1. The tape just behind my ear is used only for securing the cables.

<a 
    href="/images/14_neuroon_signals/examination/night_1_electrodes_back.jpg"
    target="_blank">
<img
    title="Electrode placement - back"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_1_electrodes_back.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

Visible O1 and O2 on the back of my skull, Cz on the top of it.

<a 
    href="/images/14_neuroon_signals/examination/night_1_electrodes_right.jpg"
    target="_blank">
<img
    title="Electrode placement - right side"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_1_electrodes_right.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

As on the left: CHIN3, EOG2, F4 and C4, O2.

After trying on the NeuroOn Fz had to be moved a little bit upwards, as otherwise the tape might touch one of its electrodes.

<a 
    href="/images/14_neuroon_signals/examination/night_1_lying.jpg"
    target="_blank">
<img
    title="Lying before the examination"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_1_lying.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Just before putting the mask on - I can honestly say that the full body "armor" for measuring my chest movement is really uncomfortable. I don't have any photos with the NeuroOn from the first night, but there are several from the second one.

Due to the amount of equipment I had on myself my sleep quality was very low, which should be visible both in the signal and its description.

<a 
    href="/images/14_neuroon_signals/examination/night_2_electrodes_front.jpg"
    target="_blank">
<img
    title="Second night"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_2_electrodes_front.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

Second night - gathering only EEG, EOG and ECG signals. I knew that shaving my head and face will help, but completely forgot about ECG. Well, I lost some of my chest hair in the morning.

<a 
    href="/images/14_neuroon_signals/examination/night_2_electrodes_mask.jpg"
    target="_blank">
<img
    title="Putting NeuroOn on - only the foam"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_2_electrodes_mask.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

After putting the NeuroOn foam - the electrode placement is plainly visible.

<a 
    href="/images/14_neuroon_signals/examination/night_2_full_mask.jpg"
    target="_blank">
<img
    title="Putting NeuroOn on - with the board"
    class="article-img"
    src="/images/14_neuroon_signals/examination/night_2_full_mask.jpg"
    style="width: auto; height: 500px; margin: 2em auto 2em;">
</a>

As you can see, the electrodes are pressed firmly to my forehead.

<a 
    href="/images/14_neuroon_signals/examination/electrode_prints.jpg"
    target="_blank">
<img
    title="Electrode prints"
    class="article-img"
    src="/images/14_neuroon_signals/examination/electrode_prints.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

Electrode prints are plainly visible even an hour after waking up.

<a 
    href="/images/14_neuroon_signals/examination/software.jpg"
    target="_blank">
<img
    title="Grass Technologies PSG TWin Software"
    class="article-img"
    src="/images/14_neuroon_signals/examination/software.jpg"
    style="width: 500px; height: auto; margin: 2em auto 2em;">
</a>

The signals were downloaded from the polysomnograph using Grass Technologies PSG TWin 4.5.4 and 4.5.2 to assure that there are no software-derived artifacts.

Even with the latest version of NeuroOn debugging software saving timestamps to the signal files, streams from the mask and the PSG may start and end in different moments. To help synchronize them for the first several minutes of each session I repeatedly closed my eyes, clenched my teeth and moved my jaw, which should leave plainly visible muscle artifacts on both signals.

All files - scans of the medical documents, signals and staging from NeuroOn (.csv) and AURA (.edf), staging for the latter (.xcl, .xsv), as well as photos are available [on my server](https://obsidian.alxd.org/cloud/index.php/s/Qw2Fscjr4UJzFZB). They are all licensed under Creative Commons BY 4.0[^16].

### Summing it up

As a great supporter of Open Access and Open Notebook Science I did my best to document this research in the most comprehensive way. I encourage you all to try and analyze NeuroOn and AURA signals and publish your own findings! I'm also aware that it would be far better to gather signals from 5, 7 or 14 sessions - I just plainly cannot afford renting the lab for so long. The examinations are also quite tiring and hard to conduct with a regular day job.

Since signal analysis should take me at least a month, I don't want to come to any conclusions at this point. I am trying to remain a proper scientific approach, creating a falsifiable hypothesis (or several) and testing them without prejudice or expected results. I'm going to publish all my analysis and findings using ipython notebook - jupyter[^17], so that everyone will be able to follow me step by step and show potential errors.

[^1]: NeuroOn campaign on [Kickstarter](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle)
[^2]: [NeuroOn - król jest nagi [PL]]({filename}/01pl_neuroon_krol_jest_nagi.md)
[^3]: @takingapartcats, a neuroscientist from Zurich [artykuł](https://takingapartcats.wordpress.com/2014/01/13/nonsense-neurogadgets-sleep-edition/)
[^4]: "Deconstructing the most sensationalistic recent findings in Human Brain Imaging, Cognitive Neuroscience, and Psychopharmacology" [article](https://neurocritic.blogspot.co.uk/2014/01/neurocrap-funded-by-masses-neuroon-and.html)
[^5]: Dr hab. n. med. Adam Wichniak, medical psychiatrist, clinical neurophysiologist [(hospital's page)](http://www.sen-instytut.pl/awichniak.html) for Bloomberg Businessweek 37(114)/2014, in article "Halo, halo, pobudka!"
[^6]: Tomasz Kolodziejak, co-founder of Neuroon, hacks your sleep with the intelligent mask | Valley Talks [YouTube](https://www.youtube.com/watch?v=aFGv4BmgjCw&t=04m53s)
[^7]: [NeuroOn's Features](https://neuroon.com)
[^8]: One of displeased client's comments on [Kickstarter](https://www.kickstarter.com/projects/intelclinic/neuroon-worlds-first-sleep-mask-for-polyphasic-sle/comments?cursor=8675981#comment-8675980)
[^9]: Lucid Dreaming: Psychophysiological Studies of Consciousness during REM Sleep by Stephen LaBerge, Ph.D. [source](http://www.lucidity.com/SleepAndCognition.html)
[^10]: The Neuroscience of Lucid Dreams [Scientific American](http://blogs.scientificamerican.com/illusion-chasers/the-neuroscience-of-lucid-dreams/)
[^11]: Sadly, the blogposts were deleted by the Intelclinic team. While "Biological Amplifiers: Why Do We Need Them?" was deleted permanently, "The Ontogeny of Sleep and Its Neurobiological Basis" can still be found on [The Internet Archive](https://web.archive.org/web/20150426104210/https://neuroon.com/the-ontogeny-of-sleep-and-its-neurobiological-basis/)
[^12]: [Kuiga's blog](https://neuroonsleep.wordpress.com/2016/03/07/more-naps-rant-and-rem-incorrecly-detected-as-wake/)
> In my first post I mentioned having asked the support whether the mask hardware is technically capable of detecting the sleep-stage in real time. I got a message from the support today. They did not answer my question directly (or course…) but said that “We may add in the future the option of waking up when in the light sleep”. What I make of this is that it’s hard to implement and not their top priority at the moment.
[^13]: [NeuroOn Technology](https://neuroon.com/technology/)
[^14]: Sleep Disorders Center at the Institute of Psychiatry and Neurology in Warsaw's [official page](http://www.sen-instytut.pl/index_en.html)
[^15]: All official pages of GRASS Technology seem dead, but information about AURA PSG amplifier are available at [SelectScience](http://www.selectscience.net/products/aura-psg-ambulatory-systems/?prodID=171717) and [Sleep Disorders Center's page](http://www.sen-instytut.pl/sleep_laboratory.html) 
[^16]: CC-BY 4.0 - detailed license can be found at [Creative Commons](https://creativecommons.org/licenses/by/4.0/)
[^17]: Open science notebook as a great way of presenting findings - [JuPyTer](http://jupyter.org/)
