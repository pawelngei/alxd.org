Title: The Story Engine Card Creator
Date: 2020-05-19
Slug: the-story-engine-card-creator
Lang: en
Translation: false
opengraph_image: 31_story_engine_card_creator/screenshot.jpg

![The Story Engine Card Creator](/images/31_story_engine_card_creator/screenshot.jpg)

I've just finished working on an app - [The Story Engine Card Creator](https://cardcreator.storyenginedeck.com/) based on [_The Story Engine_](http://storyenginedeck.com/) by Peter Chiykowski, with its source available on [Github](https://github.com/pawelngei/story-engine-card-creator) on aGPLv3!

## The Story

A few months ago a friend sent me an interesting Kickstarter campaign - _The Story Engine_, a card game of writing prompts, helping people generate new stories or challenge themselves to write short fiction about whatever they draw. It offered five kinds of cards, each presenting you with a few options to choose, even after the initial random drawing happened.

An _Agent_ card (An Artist / A Dancer / A Writer / A Musician), an _Engine_ card (Wants To Finally Tell The Truth About/Is Trying To Spread A Lie About), an _Anchor_ card (A Shrine / A Simulation / A Drug / A Dream), a _Conflict_ card (But Their Family Stands In The Way / But It Will Cost Them The Only Family They Ever Known) and finally, an _Aspect_ (Blighted / Thoughtful / Icy / Brilliant). Drawn those from their separate decks, I can tell a story about

An Brilliant Artist, Who Wants To Spread A Lie About A Shrine, But Their Family Stands In The Way. A well-established iconoclast painter, who wants to deface the symbols of their religious youth, suggesting it was much darker than it really was. They will need to fight their family trying to prove their innocence - and defending their sacred place.

Or

A Musician Who Wants To Finally Tell The Truth About A Blighted Dream, But It Will Cost Them The Only Family They Ever Known. A violinist who will finally admit that their lifelong dream of becoming the best and most inspired destroyed so many things they deemed valuable and beautiful - and who will be shunned by all their colleagues, still believing in it.

<iframe width="640" height="360" src="https://www.kickstarter.com/projects/rockpapercynic/the-story-engine-deck-of-endless-storytelling-prompts-book/widget/video.html" frameborder="0" scrolling="no"> </iframe>

I really liked the idea, but I already invested in a few Kickstarters and didn't have any cash to spare. I'm more invested in full-fledged Role Playing Games than just narrative games.

A few months passed, Covid-19 and the quarantine happened and suddenly it became much harder to get all my friends - spending most their time on their computers, working remotely - to videoconference for four, six hours more over the weekend to play a game. I decided to play with my spouse - but quickly found out that single-player RPGs are too intensive for us - and switched to lighter narrative experiences, like [For The Queen](https://cannibalhalflinggaming.com/2019/08/15/the-independents-for-the-queen/) or [The Quiet Year](https://buriedwithoutceremony.com/the-quiet-year) (both of which I really recommend).

At some point I saw a blogpost of Peter Chiykowski, the creator of _The Story Engine_, sharing the PDFs of the game with all the educators and locked-in families for free! I downloaded them and tried them out - and quickly realized that while they're really well designed, even the _eco_ version is really dark, not adjusted for b/w printers. I wrote to Peter asking if he can share his PSD files to make them really ink-friendly - and we started talking.

After a while we realized that better than making just another version of the deck, we can build a whole card generator webapp together, allowing people to create their own cards and edit existing ones, with different print settings. Peter designed the mockups and card backs & fronts, while I supplied my code.

## The App

You can find the application's source code on [Github](https://github.com/pawelngei/story-engine-card-creator). The code is released under aGPLv3, but the assets are copyrighted by Peter and cannot be used commercially.

It's a TypeScript React app based on a very simple [Create React App](https://reactjs.org/docs/create-a-new-react-app.html) starter.

The whole idea revolves around rendering a static-size A4 page and populating it with cards, then scaling it up and down depending on the user's viewport. This way the page can be printed directly to A4 and look the same - no margins, no funky font size changes or antialiasing. We don't need to generate a PDF out of it - most browsers will be able to do it for us!

I chose [Styled Components](https://styled-components.com/) for CSS after some good experiences working with and maintaining them in a few other projects.

Since I worked mostly on bigger apps before, starting something small with React Starter and designing the whole layout taught me a lot about CSS, especially [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) and how it interacts with [transform: scale()](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/scale) and [transform-origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin). [box-sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing) proved more useful than I expected. `media @print` are the backbone of the whole thing :)

I tried using some [material-ui](https://material-ui.com/) components for easy styling and fancy effect, but quickly learned that they come with a lot of customization overhead for small projects, where I'd like to use just a few buttons.

The overall architecture of the app is quite simple: we have a Card component (which handles all cart logic) on a Page, which is then managed by PagesManager, displaying fronts and backs. On the left there's the LeftMenu controlling card, page, view and deck actions. Speaking of further development, breaking the LeftMenu is probably one of the biggest priorities, since it's quite a huge component.

Card Creator doesn't support mobile - or really small - viewport, since that would require a lot of design work. We could make the Left Menu a drawer and have it slide out on click, but that would stop users from easily seeing the changes they're making. We could scrap the menu totally and edit the cards inline - but that introduces even more design challenges.

I'm pretty happy with Create React App, with only one caveat - it doesn't document the usage of `eslint` well enough. I spent a few hours trying to install proper libraries with yarn and understand _where should I place the config_, until I arrived to what seems to be right: install everything BUT `eslint` package itself and place the `.eslintrc` in root of the project.

I hope that the application will be useful to all of _The Story Engine_ fans, and please contact me if you'd like me to clarify how it works.