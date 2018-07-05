Title: TaxBrackets - visualizing tax systems in d3.js
Date: 2016-01-15 18:00
Slug: tax-brackets-visualizing-tax-systems-in-d3-js
Lang: en
Tags: tech, js, d3
Translation: false

Hah, my first technical post on the blog, even if very lame :)

During the last year's elections in Poland a truly leftist party surfaced for the first time in decades, proposing to raise the taxes with a progressive tax system. It turned out that a lot of Poles didn't know how such a system works and became terrified by the thought of a 75% tax for the richest.

That convinced me to create some kind of visualization of various tax systems - be in flat or progressive. This is an early stage effect of my works: TaxBrackets 0.1, available at [my Github](http://github.com/pawelngei/d3-taxBrackets).

<a href="https://www.flickr.com/photos/jakerust/16825349671/">
  <img title="Taxes CC-BY http://www.gotcredit.com/" class="article-img" src="/images/11_taxbrackets/taxes.jpg" style="width: 500px; height: auto; margin: 2em auto;">
</a>

I've been meaning to sit down and work it out for months, and starting wasn't easy - the most important factor was a clear and simple design. It had to present an average person how the tax brackets are distributed in their gross salary. Iterating between versions with varying level of details I finally settled on relative simple one, which shouldn't feel crowded.

I wanted to create two view modes: 'general', showcasing the sum of all the taxes paid for gross income and the 'detailed' one, divided into respective tax brackets. You can alternate between them with a click (Should there be a side button? Do users want to copy the legend text?),

A little demo (all the config code inline, feel free to peek):

<div>
    <svg id="taxBrackets"></svg>
</div>

<input id="salary"
       type="number"
       value="6000">

<style>
  .salary {
    fill: rgba(0,0,255,0.25);
  }
  .tax {
    fill: rgba(255,0,0,0.5);
  }
  .net {
    fill: rgba(0,255,0,0.4);
  }
  text {
    font-family: sans;
  }
  .d3-tooltip {
    line-height: 1;
    font-family: sans;
    padding: 6px;
    background: rgba(0, 0, 0, 0.8);
    color: #fff;
    border-radius: 2px;
  }
</style>

<script src="scripts/11_taxbrackets/d3.min.js"></script>
<script src="scripts/11_taxbrackets/d3-tip.js"></script>
<script src="scripts/11_taxbrackets/jquery.min.js"></script>
<script type="text/javascript"
      src="scripts/11_taxbrackets/taxBrackets.js"
      charset="utf-8"></script>

<script>
var taxRazem = {
  name: 'Progressive',
  constantFee: 0,
  brackets: [
    {
      limit: 1000,
      taxValue: 0,
    },
    {
      limit: 5000,
      taxValue: 22,
    },
    {
      limit: 10000,
      taxValue: 33,
    },
    {
      limit: 20833,
      taxValue: 44,
    },
    {
      limit: 41667,
      taxValue: 55,
    },
    {
      limit: -1, /* inf */
      taxValue: 75,
    }
  ]
};

var taxCurrent = {
  name: 'Current',
  constantFee: 0,
  brackets: [
    {
      limit: 257.58,
      taxValue: 0
    },
    {
      limit: 7127.33,
      taxValue: 18
    },
    {
      limit: -1,
      taxValue: 32
    }
  ]
}

var taxNowoczesna = {
  name: 'Flat 16%',
  constantFee: 0,
  brackets: [
    {
      limit: 257.58,
      taxValue: 0
    },
    {
      limit: -1,
      taxValue: 16,
    }
  ]
}

var tbInstance = new TaxBrackets('#taxBrackets',
        [taxCurrent, taxRazem, taxNowoczesna],
        {outerWidth: $('#taxBrackets').parent().width()});
tbInstance.initGraph($('#salary').val());

$('#salary').on('keyup', function (event) {
  var value = $('#salary').val();
  tbInstance.initGraph(value);
});
</script>

Feel free to change the number above - it represents a monthly income in PLN.

I hope this little lib will prove useful to somebody even in this state - I will continue working on it in my spare time.

### How it works

[d3.js](http://d3js.org/) was rather an obvious choice for an implementation. Since it was my first go with the library, it took me a moment to get used to the concepts - yet I'm very pleased by the results, especially the transitions.

Everything is written in [ES2015](https://babeljs.io/docs/learn-es2015/) precompiled with [babelJS](https://babeljs.io/) and [gulpJS](http://gulpjs.com/). I've tried making it into a class, which may not have been the best design choice...

Since I wanted this little lib to be as reusable as possible, at the moment of creating your `taxBracket` object you can feed it an arbitrary number of TaxSystem objects, structured like:

    var taxFlat = {
      name: 'Flat 16%',
      constantFee: 0, // not implemented, TODO
      brackets: [
        {
          limit: 257.58, // upper tax bracket limit
          taxValue: 0 // tax-free
        },
        {
          limit: -1, // no limit
          taxValue: 16, // in percent
        }
      ]
    }

The year/monthly income depends on the `limit` parameter set in the `taxSystem`, so there's no need to alternate between the modes in the code itself.

### TODO

This is just an early alpha version, which probably needs a redesign as well as a refactoring. Pointing out:

1. Showing full labour costs instead of just income tax would be beneficial. Right now the `constantFee` remains unimplemented, and in several tax systems (including Polish) it can vary between a flat rate and a percentage of the income. That's a major redesign.

2. Splitting the library into several files, probably using webpack should be a good idea - especially the business logic (calculating the taxes) should be in a different module than rendering.

3. Better tooltips - and not displaying them when the legend is visible on a bar. That one has been bugging me for some time and I haven't been able to find a clean implementation of the solution so far.

4. Major ECMAScript overhaul with a lot more `const` will be needed.

5. More sophisticated documentation.

6. Packaging it into a standardized d3 module, maybe?

I will try to keep you updated about [my progress](http://github.com/pawelngei/d3-taxBrackets) - maybe this will keep me motivated to finish this project before the next elections ;)

If you have any comments - please [contact me](mailto:a%6C%78%64 (A%54) %61%6Cxd.org) about it!
