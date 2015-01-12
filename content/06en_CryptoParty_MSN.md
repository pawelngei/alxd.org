Title: CryptoParty in Museum of Modern Art in Warsaw
Date: 2015-01-11 22:00
Slug: cryptoparty-in-museum-of-modern-art
Lang: en
Translation: false

<a href="http://artmuseum.pl/en/muzeum">
  <img title="Photo copyrighted by Bartosz Stawiarski" class="article-img" src="/images/06_cryptoparty_msn/cryptopartymsn.jpg" style="height: 400px; width:auto;">
</a>

At the very end of the previous year I was invited by a [Museum of Modern Art in Warsaw](http://artmuseum.pl/en/muzeum) to conduct a [CryptoParty](https://en.wikipedia.org/wiki/CryptoParty) at the finissage of "Privacy settings" exhibition. I'm very glad that the organizers thought about educating their guests and showing them a *real* face of the Internet, not only phrased as a contemporary work of art.

Since CryptoParty may mean many things - and I've attended a workshop about it during the [31C3](https://en.wikipedia.org/wiki/Chaos_Communication_Congress) - it was important to have a clear vision in mind. As the form of workshop was unfavorable in the Museum's conditions: more than 40 predicted guests with almost no prior knowledge and only 90 minutes for the event - I decided to go with a lecture in four parts. I tried to design it this way so every section would build on the previous, and each was more optional for a normal user.

The first one - an introduction - answered a question: *why*. What is the threat? For whom? Why is it so? Naming cyber-criminals, corporations and government agencies, telling a little about their targets and techniques, trying not to sound *too* paranoid. From my experience omitting this one is a real deal-breaker for most of attendees.

A good quote and creed for the presentation:

>If you are not paying for it, you're not the customer; you're the product being sold.
>
>[blue_beetle](http://www.metafilter.com/95152/Userdriven-discontent#3256046)

The second covered *online security* and I thought it most vital for a newbie. Up-to-date OS, browser and plugins. Firefox or Chromium (I don't trust Chrome as much). The insecurity of an email. [MITM](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) attacks and HTTPS. Clickjacking and NoScript. Cookies and Disconnect.me. The dangers of default synchronization. A brief mention of TOR (which I consider a tool for people who know they are doing, not for everyday use).

Then, *offline securty*. What does it mean to be encrypted? Why can't we use TrueCrypt anymore? Symmetric and [asymmetric encryption](https://en.wikipedia.org/wiki/Public-key_cryptography). Passwords on files (better than plaintext emails anyway!). Containers. Disk encryption.

The fourth section only for people who are really aware of their digital surroundings, because without that the whole process is pointless. So: communicators and OTR. emails, files and PGP (introduction and invitation for a real CryptoParty workshop). SMS and calls: TextSecure and RedPhone.

And an extra: Android security: Cyanogenmod, app priviliges and disk encryption.

After reviewing the whole thing I noticed that the whole presentation may seem a little bit too paranoid. Maybe we should interact with the audience? MITM attack sounds nice. Together with [piorek](http://piorekf.org/) from Warsaw Hackerspace we designed a small setup of a "YourFavoriteCafe" network, which injected some CSS styles in every page, inverting each `<img>` in the X axis. We used [MITMProxy](https://mitmproxy.org/) and simple word replacement: `<head>` to `<head><style>...</style>`.

So on 4th of January, two days after coming back from aforementioned 31C3 we gave a talk for roughly 50 people, mostly with no technical background - and it seems that we were able to share what we intended. It took about 80 minutes in itself and we had several questions from the audience, both about the talk and other security subjects.

There were some mistakes and things to be improved (all of which I consider rather minor): some technical disagreements between piorek and me, a little too much fuss on TOR's political importance, and my inability to properly convey that the PGP *is* manageable - just requires a little training.

After the presentation I noticed several topics which could have been mentioned as well, namely: different search engines (DuckDuckGo) and distributed social networks (Diaspora, Friendica, Red). It's just important not to overload the audience with too many technical terms they don't understand, and if we're suggesting why to leave the Facebook - list enough credible and important arguments for choosing something far less convenient.

We've already got two or three invitations to schools around Warsaw to go with the same presentation, yet I think that it should be changed to better suit the younger listeners. While they may see the MITM on their smartphones, we should focus on *why is it important to stay private* and *why not to share naked pictures of yourself* instead of dwelling on subjects easily grasped by the youth (like why Internet Explorer is a bad idea).

The presentation itself (sadly, Polish only for now - but a lot of pictures) may be found [here](http://slides.com/pawelchojnacki/cryptopartymsn) or in the `iframe` below (press `F` to fullscreen):

<div style="text-align: center; margin: 1em;">
  <iframe src="//slides.com/pawelchojnacki/cryptopartymsn/embed?style=hidden" width="500" height="420" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
</div>

If you've got any suggestions or comments, feel free to write me an [email](mailto:alxd AT alxd.org).

Thanks to piorek, pozytywny, maupa and Nikola for making both the CryptoParty and this text possible!
