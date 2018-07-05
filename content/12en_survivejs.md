Title: SurviveJS - a guide to modern web development with React and Webpack
Date: 2016-01-31 18:00
Slug: survivejs-a-guide-to-modern-web-development
Lang: en
Tags: tech, js, react, webpack
Translation: false

This time I wish to share a recommendation. For two years I've been developing in JavaScript in Angular, using various in-house habits and techniques of my respective employers. I have tried vanilla JS and CoffeeScript, Grunt and Gulp, Jasmine and Mocha, various deployment models. I have been learning various tools on my own, but I always seemed to lack the understanding of what is their specific place and strength in a project.

I never really got what's so good in [React](https://facebook.github.io/react/) and [Webpack](https://webpack.github.io/), even though I've completed the tutorials before. I got myself to understand [ES6 and BabelJS](https://babeljs.io/), but never intuitively realized the potential of `const` and modules, even though my [taxBrackets](https://github.com/pawelngei/d3-taxBrackets) project uses a lot of their functions.

<a href="http://survivejs.com/">
  <img title="SurviveJS" class="article-img" src="/images/12_survivejs/title.png" style="width: auto; height: auto; margin: 2em auto;">
</a>

There are lots of great tutorials and showcases of various tools, showing how each of them can simplify and speed up the development. Still - nothing can replace seeing an experienced professional make most of his toolbox and guide you through their work process.

Recently I've seen such a guide, creating a simple yet representative app in React, Webpack and ES2015[^ES2015] - [SurviveJS](http://survivejs.com/). Most of it is available [for free](http://survivejs.com/webpack_react/introduction/) - this version easily covers building a work environment and creating the application itself. You can check the table of contents there or browse the [book source on GitHub](https://github.com/survivejs/webpack_react).

If you want to spare $20 to $24 dollars (depending on where you live), you can buy a [full version](https://leanpub.com/survivejs_webpack_react) in PDF/epub/mobi (no DRM). In the additional chapters you can find a guide for static typing, linting and testing React.

What I like about it is the fact that it never shows *the only way* to achieve something, describing each of the tools and approaches instead. It covers Webpack, but also talks about Grunt and Gulp. It uses ES2015, but TypeScript is an option. React Flux implementation? [Alt](http://alt.js.org/), but read also about [Redux](https://github.com/rackt/redux) and all the others. The book is full of links and references, which make a great context, enriching every developer's knowledge.

The application itself is just a Kanban/ToDo demo, available [online](http://survivejs.com/demos/08_building_kanban/). I really encourage you to try going after the author step by step, commiting each subchapter and seeing all the errors you will get after forgetting that semicolon. Thanks to this approach I feel I really understood what's the role of a `const` and modules (including libraries) in an ES6 app, I began to love Webpack which seemed bloated and unintuitive so far. I will certainly have some ideas how to rewrite my taxBrackets with this knowledge.

The only thing I feel uneasy about is the whole variety of Flux implementations - such as [alt](http://alt.js.org/) used in the project. The sheer number of them and differences between the very concepts of respective libraries leave me confused. I could definitely use rewriting the SurviveJS application with [redux](https://github.com/rackt/redux) for example.

While I can see how the modular architecture and other ES6 features are great (and I am going to use them in future projects), I also want to learn the [TypeScript](http://www.typescriptlang.org/) a lot of people have been talking about, especially in the context of [Angular 2](https://angular.io/). Expect a GitHub project soon ;)

If you are wondering if you should buy the book - try the free version first. If the concept of going step-by-step into app development helps you learn, invest $24 in browsing some more advanced approaches. Of course, you could easily browse the tutorials of [ESLint](http://eslint.org/) and [Flow](http://flowtype.org/) yourself, but the additional chapters should give you a more comprehensible outlook on their competitors - and their usage with Webpack.

Summing it up, I liked the book a lot. Thanks to seeing the actual process and understanding the architecture of a modern web application, reading the comments and discussions on available approaches - I feel much more competent to create one myself. I'm able to do much more than just repeat the patterns I learned at previous jobs and from small tutorials.

If you have any suggestions for the book (which [**is**](https://github.com/survivejs/webpack_react/) licensed under Creative Commons), feel free to drop them in the [AMA section](https://github.com/survivejs/ama/issues). I had some minor recommendations on the Webpack configs, and the author seemed to like them.

[^ES2015]: It's basically ES6 with some experimental additions from ES7 and other proposals such as python-like decorators, available through [BabelJS](https://babeljs.io/).
