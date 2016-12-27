## CSS declarations
#


# Dark
dark = """
li, ol, p, ul {
    line-height: 24px;
}
a, button, input, select, textarea {
    margin: 0;
    vertical-align: baseline;
}
a, button:hover {
    text-decoration: none;
}
a, ol, ul {
    padding: 0;
}
hr, td, th {
    text-align: left;
}
body {
    background: #000;
    font-family: Georgia, Palatino, serif;
    color: #EEE;
    line-height: 1;
    padding: 30px;
    margin: auto;
    max-width: 42em;
}
h1, h2 {
    text-align: center;
}
h1, h2, h3, h4 {
    font-weight: 400;
}
h1, h2, h3, h4, h5, p {
    margin-bottom: 24px;
    padding: 0;
}
h1 {
    font-size: 48px;
}
h2 {
    font-size: 36px;
    margin: 24px 0 6px;
}
h3 {
    font-size: 24px;
}
h4 {
    font-size: 21px;
}
h5 {
    font-size: 18px;
}
a {
    color: #61BFC1;
}
a:hover {
    text-decoration: underline;
}
a:visited {
    color: #466B6C;
}
ol, ul {
    margin: 0;
}
li ul {
    margin-left: 24px;
}
ol, p, ul {
    font-size: 16px;
    max-width: 540px;
}
pre {
    padding: 0 24px;
    max-width: 800px;
    white-space: pre-wrap;
}
code {
    font-family: Consolas, Monaco, Andale Mono, monospace;
    line-height: 1.5;
    font-size: 13px;
}
button, input, label, select, textarea {
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
aside {
    display: block;
    float: right;
    width: 390px;
}
blockquote {
    border-left: .5em solid #eee;
    padding: 0 2em;
    margin-left: 0;
    max-width: 476px;
}
blockquote cite {
    font-size: 14px;
    line-height: 20px;
    color: #bfbfbf;
}
blockquote p {
    color: #666;
    max-width: 460px;
}
hr {
    width: 540px;
    margin: 0 auto 0 0;
    color: #999;
}
button::-moz-focus-inner, input::-moz-focus-inner {
    border: 0;
    padding: 0;
}
button, input[type=button], input[type=reset], input[type=submit] {
    cursor: pointer;
    -webkit-appearance: button;
}
input:not([type=image]), textarea {
    -webkit-box-sizing: content-box;
    -moz-box-sizing: content-box;
    box-sizing: content-box;
}
input[type=search] {
    -webkit-appearance: textfield;
    -webkit-box-sizing: content-box;
    -moz-box-sizing: content-box;
    box-sizing: content-box;
}
input[type=search]::-webkit-search-decoration {
    -webkit-appearance: none;
}
input, label, select, textarea {
    font-size: 13px;
    line-height: normal;
    margin-bottom: 18px;
}
input[type=checkbox], input[type=radio] {
    cursor: pointer;
    margin-bottom: 0;
}
input[type=password], input[type=text], select, textarea {
    display: inline-block;
    width: 210px;
    padding: 4px;
    font-size: 13px;
    line-height: 18px;
    height: 18px;
    color: gray;
    border: 1px solid #ccc;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
    -webkit-transition: border linear .2s, box-shadow linear .2s;
    -moz-transition: border linear .2s, box-shadow linear .2s;
    transition: border linear .2s, box-shadow linear .2s;
    -webkit-box-shadow: inset 0 1px 3px rgba(0, 0, 0, .1);
    -moz-box-shadow: inset 0 1px 3px rgba(0, 0, 0, .1);
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, .1);
}
input[type=file], select {
    height: 27px;
    line-height: 27px;
}
textarea {
    height: auto;
}
:-moz-placeholder {
    color: #bfbfbf;
}
::-webkit-input-placeholder {
    color: #bfbfbf;
}
input[type=password]:focus, input[type=text]:focus, textarea:focus {
    outline: 0;
    border-color: rgba(82, 168, 236, .8);
    -webkit-box-shadow: inset 0 1px 3px rgba(0, 0, 0, .1), 0 0 8px rgba(82, 168, 236, .6);
    -moz-box-shadow: inset 0 1px 3px rgba(0, 0, 0, .1), 0 0 8px rgba(82, 168, 236, .6);
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, .1), 0 0 8px rgba(82, 168, 236, .6);
}
button {
    display: inline-block;
    padding: 4px 14px;
    font-size: 13px;
    line-height: 18px;
    -webkit-border-radius: 4px;
    -moz-border-radius: 4px;
    border-radius: 4px;
    -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, .2), 0 1px 2px rgba(0, 0, 0, .05);
    -moz-box-shadow: inset 0 1px 0 rgba(255, 255, 255, .2), 0 1px 2px rgba(0, 0, 0, .05);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, .2), 0 1px 2px rgba(0, 0, 0, .05);
    background-color: #0064cd;
    background-repeat: repeat-x;
    background-image: -khtml-gradient(linear, left top, left bottom, from(#049cdb), to(#0064cd));
    background-image: -moz-linear-gradient(top, #049cdb, #0064cd);
    background-image: -ms-linear-gradient(top, #049cdb, #0064cd);
    background-image: -webkit-gradient(linear, left top, left bottom, color-stop(0, #049cdb), color-stop(100%, #0064cd));
    background-image: -webkit-linear-gradient(top, #049cdb, #0064cd);
    background-image: -o-linear-gradient(top, #049cdb, #0064cd);
    background-image: linear-gradient(top, #049cdb, #0064cd);
    color: #fff;
    text-shadow: 0 -1px 0 rgba(0, 0, 0, .25);
    border: 1px solid #004b9a;
    -webkit-transition: .1s linear all;
    -moz-transition: .1s linear all;
    transition: .1s linear all;
    border-color: #0064cd #0064cd #003f81;
    border-color: rgba(0, 0, 0, .1) rgba(0, 0, 0, .1) rgba(0, 0, 0, .25);
}
button:hover {
    color: #fff;
    background-position: 0 -15px;
}
button:active {
    -webkit-box-shadow: inset 0 3px 7px rgba(0, 0, 0, .15), 0 1px 2px rgba(0, 0, 0, .05);
    -moz-box-shadow: inset 0 3px 7px rgba(0, 0, 0, .15), 0 1px 2px rgba(0, 0, 0, .05);
    box-shadow: inset 0 3px 7px rgba(0, 0, 0, .15), 0 1px 2px rgba(0, 0, 0, .05);
}
button::-moz-focus-inner {
    padding: 0;
    border: 0;
}
mark {
    background-color: #ff69b4;
}
table {
    border-collapse: collapse;
}
td, th {
    border: 1px solid #fff;
    padding: .5rem;
}
.hljs {
    display: block;
    overflow-x: auto;
    padding: .5em;
    background: #2b2b2b;
    color: #bababa;
}
.hljs-emphasis, .hljs-strong {
    color: #a8a8a2;
}
.hljs-bullet, .hljs-link, .hljs-literal, .hljs-number, .hljs-quote, .hljs-regexp {
    color: #6896ba;
}
.hljs-code, .hljs-selector-class {
    color: #a6e22e;
}
.hljs-emphasis {
    font-style: italic;
}
.hljs-attribute, .hljs-keyword, .hljs-name, .hljs-section, .hljs-selector-tag, .hljs-variable {
    color: #cb7832;
}
.hljs-params {
    color: #b9b9b9;
}
.hljs-string {
    color: #6a8759;
}
.hljs-addition, .hljs-built_in, .hljs-builtin-name, .hljs-selector-attr, .hljs-selector-id, .hljs-selector-pseudo, .hljs-subst, .hljs-symbol, .hljs-template-tag, .hljs-template-variable, .hljs-type {
    color: #e0c46c;
}
.hljs-comment, .hljs-deletion, .hljs-meta {
    color: #7f7f7f;
}
"""


# Foghorn
foghorn = """
@import url(http://fonts.googleapis.com/css?family=Vollkorn:400, 400italic, 700, 700italic&subset=latin);
    ol, ul {
    padding-left: 1.2em;
}
body, code, html {
    background: #fff;
}
body, h1 a, h1 a:hover {
    color: #333;
}
a, h1 a, h1 a:hover {
    text-decoration: none;
}
hr, video {
    margin: 2em 0;
}
h1, h2, p#heart {
    text-align: center;
}
table tr td, table tr th {
    border: 1px solid #ccc;
    text-align: left;
    padding: 6px 13px;
    margin: 0;
}
h1, p, table tr td :first-child, table tr th :first-child {
    margin-top: 0;
}
pre code, table, table tr {
    padding: 0;
}
body, html {
    padding: 1em;
    margin: auto;
}
body {
    font: 1.3em Vollkorn, Palatino, Times;
    line-height: 1;
    text-align: justify;
}
h1, h2, h3 {
    font-weight: 400;
}
h3, nav {
    font-style: italic;
}
code, nav {
    font-size: .9em;
}
article, footer, header, nav {
    margin: 0 auto;
}
article {
    margin-top: 4em;
    margin-bottom: 4em;
    min-height: 400px;
}
footer {
    margin-bottom: 50px;
}
video {
    border: 1px solid #ddd;
}
nav {
    border-bottom: 1px solid #ddd;
    padding: 1em 0;
}
nav p {
    margin: 0;
}
p {
    -webkit-hypens: auto;
    -moz-hypens: auto;
    hyphens: auto;
}
ul {
    list-style: square;
}
blockquote {
    margin-left: 1em;
    padding-left: 1em;
    border-left: 1px solid #ddd;
}
code {
    font-family: Consolas, Menlo, Monaco, monospace, serif;
}
a {
    color: #2484c1;
}
a:hover {
    text-decoration: underline;
}
a img {
    border: 0;
}
hr {
    color: #ddd;
    height: 1px;
    border-top: solid 1px #ddd;
    border-bottom: 0;
    border-left: 0;
    border-right: 0;
}
p#heart {
    font-size: 2em;
    line-height: 1;
    color: #ccc;
}
.red {
    color: #b50000;
}
body#index li {
    margin-bottom: 1em;
}
@media only screen and (max-device-width:1024px) {
    body {
    font-size: 120%;
    line-height: 1.4;
}
}
@media only screen and (max-device-width:480px) {
    body {
    text-align: left;
}
article, footer {
    width: auto;
}
article {
    padding: 0 10px;
}
}
table tr {
    border-top: 1px solid #ccc;
    background-color: #fff;
    margin: 0;
}
table tr:nth-child(2n) {
    background-color: #aaa;
}
table tr th {
    font-weight: 700;
}
table tr td:last-child, table tr th :last-child {
    margin-bottom: 0;
}
img {
    max-width: 100%}
code, tt {
    margin: 0 2px;
    padding: 0 5px;
    white-space: nowrap;
    border: 1px solid #eaeaea;
    background-color: #f8f8f8;
    border-radius: 3px;
}
pre code {
    margin: 0;
    white-space: pre;
    border: none;
    background: 0 0;
}
.highlight pre, pre {
    background-color: #f8f8f8;
    border: 1px solid #ccc;
    font-size: 13px;
    line-height: 19px;
    overflow: auto;
    padding: 6px 10px;
    border-radius: 3px;
}
"""


# Github
github = """
body, table tr {
    background-color: #fff;
}
table tr td, table tr th {
    border: 1px solid #ddd;
    padding: 6px 13px;
    margin: 0;
}
pre code, table, table tr {
    padding: 0;
}
hr, pre code {
    background: 0 0;
}
body {
    font: 16px Helvetica, Arial, sans-serif;
    line-height: 1.4;
    color: #333;
    word-wrap: break-word;
    padding: 10px 15px;
}
strong {
    font-weight: 700;
}
table tr th {
    font-weight: bold;
    text-align: left;
}
h1 {
    font-size: 2em;
    margin: .67em 0;
    text-align: center;
}
h2 {
    font-size: 1.75em;
}
h3 {
    font-size: 1.5em;
}
h4 {
    font-size: 1.25em;
}
h1, h2, h3, h4, h5, h6 {
    font-weight: 700;
    position: relative;
    margin-top: 15px;
    margin-bottom: 15px;
    line-height: 1.1;
}
h1, h2 {
    border-bottom: 1px solid #eee;
}
hr {
    height: 0;
    margin: 15px 0;
    overflow: hidden;
    border: 0;
    border-bottom: 1px solid #ddd;
}
a {
    color: #4183C4;
}
a.absent {
    color: #c00;
}
ol, ul {
    padding-left: 15px;
    margin-left: 5px;
}
ol {
    list-style-type: lower-roman;
}
table tr {
    border-top: 1px solid #ccc;
    margin: 0;
    background-color: #fff;
}
table tr:nth-child(2n) {
    background-color: #f8f8f8;
}
table tr td :first-child, table tr th :first-child {
    margin-top: 0;
}
table tr td:last-child, table tr th :last-child {
    margin-bottom: 0;
}
img {
    max-width: 100%}
blockquote {
    padding: 0 15px;
    border-left: 4px solid #ccc;
}
code, tt {
    margin: 0 2px;
    padding: 0 5px;
    white-space: nowrap;
    border: 1px solid #eaeaea;
    background-color: #f8f8f8;
    border-radius: 3px;
}
pre code {
    margin: 0;
    white-space: pre;
    border: none;
}
.highlight pre, pre {
    background-color: #f8f8f8;
    border: 1px solid #ccc;
    font-size: 13px;
    line-height: 19px;
    overflow: auto;
    padding: 6px 10px;
    border-radius: 3px;
}
table {
    display: block;
    width: 100%;
    overflow: auto;
}
"""


# Handwritten
handwriting_css = """
@import url(http://fonts.googleapis.com/css?family=Indie+Flower);
    blockquote: after, blockquote:before {
    color: #000;
    font-size: 2em;
    line-height: .1em;
    vertical-align: -.4em;
}
table tr td, table tr th {
    border: 1px solid #ccc;
    text-align: left;
    padding: 6px 13px;
    margin: 0;
}
pre code, table, table tr {
    padding: 0;
}
body {
    font-family: Indie Flower, Daniel, cursive;
}
h1, h2 {
    text-align: center;
}
blockquote {
    margin: 1.5em 10px;
    padding: .5em 10px;
}
blockquote:before {
    content: open-quote;
    margin-right: .25em;
}
blockquote:after {
    content: close-quote;
    margin-left: .25em;
}
blockquote p {
    display: inline;
}
hr {
    border: 0;
    border-top: dashed 2px gray;
}
table tr {
    border-top: 1px solid #ccc;
    background-color: #fff;
    margin: 0;
}
table tr:nth-child(2n) {
    background-color: #aaa;
}
table tr th {
    font-weight: 700;
}
table tr td :first-child, table tr th :first-child {
    margin-top: 0;
}
table tr td:last-child, table tr th :last-child {
    margin-bottom: 0;
}
code, tt {
    margin: 0 2px;
    padding: 0 5px;
    white-space: nowrap;
    border: 1px solid #eaeaea;
    background-color: #f8f8f8;
    border-radius: 3px;
}
pre code {
    margin: 0;
    white-space: pre;
    border: none;
    background: 0 0;
}
.highlight pre, pre {
    background-color: #f8f8f8;
    border: 1px solid #ccc;
    font-size: 13px;
    line-height: 19px;
    overflow: auto;
    padding: 6px 10px;
    border-radius: 3px;
}
"""


# Markdown
markdown = """
::selection, a::selection {
    background: rgba(255, 255, 0, .3);
}
a, a::selection {
    color: #0645ad;
}
hr, img {
    border: 0;
}
a, ins {
    text-decoration: none;
}
::selection, ins, mark {
    color: #000;
}
dfn, mark {
    font-style: italic;
}
hr, ol, p, ul {
    margin: 1em 0;
}
table tr td, table tr th {
    border: 1px solid #ccc;
    text-align: left;
    padding: 6px 13px;
    margin: 0;
}
hr, pre code, table, table tr {
    padding: 0;
}
pre, pre code {
    white-space: pre;
}
html {
    font-size: 100%;
    overflow-y: scroll;
    -webkit-text-size-adjust: 100%;
    -ms-text-size-adjust: 100%}
body {
    color: #444;
    font-family: Georgia, Palatino, "Palatino Linotype", Times, "Times New Roman", serif;
    font-size: 12px;
    line-height: 1.5em;
    padding: 1em;
    margin: auto;
    max-width: 42em;
    background: #fefefe;
}
a:visited {
    color: #0b0080;
}
a:hover {
    color: #06e;
}
a:active {
    color: #faa700;
}
a:focus {
    outline: dotted thin;
}
a:active, a:hover {
    outline: 0;
}
::-moz-selection {
    background: rgba(255, 255, 0, .3);
    color: #000;
}
a::-moz-selection {
    background: rgba(255, 255, 0, .3);
    color: #0645ad;
}
img {
    max-width: 100%;
    -ms-interpolation-mode: bicubic;
    vertical-align: middle;
}
h1, h2, h3, h4, h5, h6 {
    font-weight: 400;
    color: #111;
    line-height: 1em;
}
b, h4, h5, h6, mark, strong, table tr th {
    font-weight: 700;
}
h1 {
    font-size: 2.5em;
}
h2 {
    font-size: 2em;
}
h3 {
    font-size: 1.5em;
}
h4 {
    font-size: 1.2em;
}
h5 {
    font-size: 1em;
}
h6 {
    font-size: .9em;
}
blockquote {
    color: #666;
    margin: 0;
    padding-left: 3em;
    border-left: .5em #EEE solid;
}
hr {
    display: block;
    height: 2px;
    border-top: 1px solid #aaa;
    border-bottom: 1px solid #eee;
}
code, kbd, pre, samp {
    color: #000;
    font-family: monospace, monospace;
    font-size: .98em;
}
pre {
    white-space: pre-wrap;
    word-wrap: break-word;
}
ins {
    background: #ff9;
}
mark {
    background: #ff0;
}
sub, sup {
    font-size: 75%;
    line-height: 0;
    position: relative;
    vertical-align: baseline;
}
sup {
    top: -.5em;
}
sub {
    bottom: -.25em;
}
ol, ul {
    padding: 0 0 0 2em;
}
li p:last-child {
    margin: 0;
}
dd {
    margin: 0 0 0 2em;
}
table {
    border-collapse: collapse;
    border-spacing: 0;
}
td {
    vertical-align: top;
}
@media only screen and (min-width:480px) {
    body {
    font-size: 14px;
}
}
@media only screen and (min-width:768px) {
    body {
    font-size: 16px;
}
}
@media print {
    blockquote, img, pre, tr {
    page-break-inside: avoid;
}
* {
    background: 0 0!important;
    color: #000!important;
    filter: none!important;
    -ms-filter: none!important;
}
body {
    font-size: 12pt;
    max-width: 100%}
a, a:visited {
    text-decoration: underline;
}
hr {
    height: 1px;
    border: 0;
    border-bottom: 1px solid #000;
}
a[href]:after {
    content: " (" attr(href) ")"}
abbr[title]:after {
    content: " (" attr(title) ")"}
.ir a:after, a[href^="javascript:"]:after, a[href^="#"]:after {
    content: ""}
blockquote, pre {
    border: 1px solid #999;
    padding-right: 1em;
}
img {
    max-width: 100%!important;
}
@page :left {
    margin: 15mm 20mm 15mm 10mm;
}
@page :right {
    margin: 15mm 10mm 15mm 20mm;
}
h2, h3, p {
    orphans: 3;
    widows: 3;
}
h2, h3 {
    page-break-after: avoid;
}
}
table tr {
    border-top: 1px solid #ccc;
    background-color: #fff;
    margin: 0;
}
table tr:nth-child(2n) {
    background-color: #aaa;
}
table tr td :first-child, table tr th :first-child {
    margin-top: 0;
}
table tr td:last-child, table tr th :last-child {
    margin-bottom: 0;
}
code, tt {
    margin: 0 2px;
    padding: 0 5px;
    white-space: nowrap;
    border: 1px solid #eaeaea;
    background-color: #f8f8f8;
    border-radius: 3px;
}
pre code {
    margin: 0;
    border: none;
    background: 0 0;
}
.highlight pre, pre {
    background-color: #f8f8f8;
    border: 1px solid #ccc;
    font-size: 13px;
    line-height: 19px;
    overflow: auto;
    padding: 6px 10px;
    border-radius: 3px;
}
"""


# Metro Vibes
metro_vibes = """
@import url(http://fonts.googleapis.com/css?family=Open+Sans:300italic, 400italic, 600italic, 700italic, 800italic, 400, 300, 600, 700, 800);
    body {
    padding: 20px;
    color: #8e8071;
    font-size: 15px;
    font-family: "Open Sans", AppleSDGothicNeo-Medium, "Segoe UI", "Malgun Gothic", sans-serif;
    background: #fff;
    -webkit-font-smoothing: antialiased;
}
a {
    color: #3269a0;
}
a:hover {
    color: #4183c4;
}
h1, h2, h3, h4, h5 {
    font-weight: 400;
    color: #5c5146;
    letter-spacing: -1px;
}
h2 {
    border-bottom: 1px solid #e6e6e6;
    line-height: 1.7em;
}
h6 {
    color: #777;
}
hr {
    border: 1px solid #e6e6e6;
}
p {
    line-height: 19px;
}
p>code {
    font-family: "Open Sans", AppleSDGothicNeo-Medium, "Segoe UI", "Malgun Gothic", sans-serif;
    color: #e86741;
    font-size: .9em;
}
pre>code {
    font-size: 1em;
    font-family: "Open Sans", AppleSDGothicNeo-Medium, "Segoe UI", "Malgun Gothic", sans-serif;
    letter-spacing: -1px;
    font-weight: 400;
}
blockquote {
    border-left: 4px solid #e6e6e6;
    padding: 0 15px;
    font-style: italic;
    color: #e86741;
}
table {
    background-color: #fafafa;
}
table tr td, table tr th {
    border: 1px solid #e6e6e6;
}
table tr:nth-child(2n) {
    background-color: #f2f2f2;
}
"""


# Metro Vibes Dark
metro_vibes_dark = """
@import url(http://fonts.googleapis.com/css?family=Open+Sans:300italic, 400italic, 600italic, 700italic, 800italic, 400, 300, 600, 700, 800);
    body {
    padding: 20px;
    color: #fff;
    font-size: 15px;
    font-family: "Open Sans", AppleSDGothicNeo-Medium, "Segoe UI", "Malgun Gothic", sans-serif;
    background: #5c5146;
    -webkit-font-smoothing: antialiased;
}
a {
    color: #e5b931;
}
a:hover {
    color: #ebc85e;
}
h1, h2, h3, h4, h5 {
    font-weight: 400;
    letter-spacing: -1px;
}
h2 {
    border-bottom: 1px solid #796a5c;
    line-height: 1.7em;
}
h6 {
    color: #777;
}
hr {
    border: 1px solid #3f3730;
}
p {
    line-height: 19px;
}
p>code {
    font-family: "Open Sans", AppleSDGothicNeo-Medium, "Segoe UI", "Malgun Gothic", sans-serif;
    color: #e86741;
    font-size: .9em;
}
pre>code {
    font-size: 1em;
    font-family: "Open Sans", AppleSDGothicNeo-Medium, "Segoe UI", "Malgun Gothic", sans-serif;
    letter-spacing: -1px;
    font-weight: 400;
}
blockquote {
    border-left: 4px solid #4e443b;
    padding: 0 15px;
    font-style: italic;
    color: #e86741;
}
table {
    background-color: #564c42;
}
table tr td, table tr th {
    border: 1px solid #3f3730;
}
table tr:nth-child(2n) {
    background-color: #4e443b;
}
"""


# Modern
modern_css = """
h1, h2, h3, h4 {
    color: #6495ed;
}
body, table tr {
    background-color: #fff;
}
table tr td, table tr th {
    border: 1px solid #ccc;
    text-align: left;
    padding: 6px 13px;
    margin: 0;
}
pre code, table, table tr {
    padding: 0;
}
body {
    font-family: Helvetica, Arial, sans-serif;
}
h1, h2 {
    text-align: center;
}
blockquote {
    background: #f9f9f9;
    border-left: 10px solid #6495ed;
    margin: 1.5em 10px;
    padding: .5em 10px;
    font-style: italic;
}
blockquote p {
    display: inline;
}
hr {
    clear: both;
    float: none;
    width: 100%;
    height: 2.5px;
    margin: 1.4em 0;
    border: none;
    background: #ddd;
    background: -webkit-gradient(linear, left bottom, right bottom, color-stop(0, #fff), color-stop(.1, #ddd), color-stop(.9, #ddd), color-stop(1, #fff)) #ddd;
    background: -moz-linear-gradient(left center, #fff 0, #ddd 10%, #ddd 90%, #fff 100%) #ddd;
}
table tr {
    border-top: 1px solid #ccc;
    margin: 0;
}
table tr:nth-child(2n) {
    background-color: #aaa;
}
table tr th {
    font-weight: 700;
}
table tr td :first-child, table tr th :first-child {
    margin-top: 0;
}
table tr td:last-child, table tr th :last-child {
    margin-bottom: 0;
}
code, tt {
    margin: 0 2px;
    padding: 0 5px;
    white-space: nowrap;
    border: 1px solid #eaeaea;
    background-color: #f8f8f8;
    border-radius: 3px;
}
pre code {
    margin: 0;
    white-space: pre;
    border: none;
    background: 0 0;
}
.highlight pre, pre {
    background-color: #f8f8f8;
    border: 1px solid #ccc;
    font-size: 13px;
    line-height: 19px;
    overflow: auto;
    padding: 6px 10px;
    border-radius: 3px;
}
"""


# Screen
screen = """
html {
    font-size: 62.5%}
body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 150%;
    line-height: 1.3;
    color: #f6e6cc;
    width: 700px;
    margin: auto;
    background: #27221a;
    position: relative;
    padding: 0 30px;
}
dl, ol, p, pre, table, ul {
    margin-bottom: 1em;
}
ul {
    margin-left: 20px;
}
a {
    text-decoration: none;
    cursor: pointer;
    color: #ba832c;
    font-weight: 700;
}
a:focus {
    outline: dotted 1px;
}
a:focus, a:hover {
    color: #d3a459;
    text-decoration: none;
}
a *, button * {
    cursor: pointer;
}
hr {
    display: none;
}
small {
    font-size: 90%}
button, input, option, select, textarea {
    font-family: Arial, "Lucida Grande", "Lucida Sans Unicode", Arial, Verdana, sans-serif;
    font-size: 100%}
button, input[type=submit], label, option, select {
    cursor: pointer;
}
.group:after {
    content: ".";
    display: block;
    height: 0;
    clear: both;
    visibility: hidden;
}
* html .group {
    height: 1%}
.group {
    display: block;
}
sup {
    font-size: 80%;
    line-height: 1;
    vertical-align: super;
}
button::-moz-focus-inner {
    border: 0;
    padding: 1px;
}
span.amp {
    font-family: Baskerville, "Goudy Old Style", Palatino, "Book Antiqua", serif;
    font-weight: 400;
    font-style: italic;
    font-size: 1.2em;
    line-height: .8;
}
h1, h2, h3, h4, h5, h6 {
    line-height: 1.1;
    font-family: Baskerville, "Goudy Old Style", Palatino, "Book Antiqua", serif;
}
h2 {
    font-size: 22pt;
}
h3 {
    font-size: 20pt;
}
h4 {
    font-size: 18pt;
}
h5 {
    font-size: 16pt;
}
h6 {
    font-size: 14pt;
}
::selection {
    background: #745626;
}
::-moz-selection {
    background: #745626;
}
h1 {
    font-size: 420%;
    margin: 0 0 .1em;
    font-family: Baskerville, "Goudy Old Style", Palatino, "Book Antiqua", serif;
}
h1 a, h1 a:hover {
    color: #d7af72;
    font-weight: 400;
    text-decoration: none;
}
pre {
    background: rgba(0, 0, 0, .3);
    color: #fff;
    padding: 8px 10px;
    border-radius: .4em;
    -moz-border-radius: .4em;
    -webkit-border-radius: .4em;
    overflow-x: hidden;
}
pre code {
    font-size: 10pt;
}
.thumb {
    float: left;
    margin: 10px;
}
table {
    border-collapse: collapse;
}
td, th {
    border: 1px solid #f6e6cc;
    padding: .5rem;
    text-align: left;
}
"""


# Solarized Dark
solarized_dark = """
h1, h2 {
    border-bottom: 1px solid;
}
html a:hover, html pre {
    background-color: #073642;
}
blockquote, body, h1, h2, h3, h4, h5, h6, html, img, li, ol, p, ul {
    margin: 0;
    padding: 0;
    font: inherit;
    vertical-align: baseline;
}
img, ol, p, pre, ul {
    margin-bottom: 20px;
}
html * {
    font-family: ff-din-web-pro-1, ff-din-web-pro-2, sans-serif;
    font-size: 16px;
    line-height: 19.2px;
    color-profile: sRGB;
    color: #839496;
}
body {
    margin: 40px 70px;
}
p {
    font-weight: lighter;
}
strong {
    font-weight: 700;
}
ol, ul {
    margin-left: 2em;
}
ol ol, ol ul, ul ol, ul ul {
    margin-top: 10px;
}
li {
    margin-bottom: 3px;
}
h1, h2, h3, h4, h5, h6 {
    font-weight: lighter;
    text-transform: capitalize;
    margin-top: 20px;
    margin-bottom: 10px;
}
.hljs-strong, h1, mark {
    font-weight: 700;
}
h1, h2 {
    font-size: 24.62px;
    line-height: 29.55px;
}
h3 {
    font-size: 23.44px;
    line-height: 28.13px;
}
h4, h5, h6 {
    font-size: 22.16px;
    line-height: 26.59px;
}
h1 img, h2 img, h3 img, h4 img, h5 img, h6 img, p img {
    margin-bottom: 0;
}
pre {
    white-space: pre;
    white-space: pre-wrap;
    word-wrap: break-word;
    padding: 15px;
}
code, pre {
    font-family: monospace;
}
blockquote {
    border-left: 4px solid;
    padding: 0 15px;
}
blockquote>:first-child {
    margin-top: 0;
}
blockquote>:last-child {
    margin-bottom: 15px;
}
h1 {
    text-transform: uppercase;
}
h3, h4, h5, h6 {
    border-bottom: none;
}
html body {
    background-color: #002b36;
}
html h1, html h2, html h3, html h4, html h5, html h6 {
    border-color: #839496;
}
html pre {
    color: #93a1a1;
}
html a, html a:active, html a:visited, html code.url, html h1, html h2, html h3, html h4, html h5, html h6 {
    color: #b58900;
}
@media print {
    body {
    margin: 0;
}
* {
    color: #000!important;
}
}
table {
    border-collapse: collapse;
}
td, th {
    border: 1px solid #839496;
    padding: .5rem;
    text-align: left;
}
mark {
    background-color: #93a1a1;
    color: #000;
}
.hljs {
    display: block;
    overflow-x: auto;
    padding: .5em;
    background: #002b36;
    color: #839496;
}
.hljs-comment, .hljs-quote {
    color: #586e75;
}
.hljs-addition, .hljs-keyword, .hljs-selector-tag {
    color: #859900;
}
.hljs-doctag, .hljs-literal, .hljs-meta .hljs-meta-string, .hljs-number, .hljs-regexp, .hljs-string {
    color: #2aa198;
}
.hljs-name, .hljs-section, .hljs-selector-class, .hljs-selector-id, .hljs-title {
    color: #268bd2;
}
.hljs-attr, .hljs-attribute, .hljs-class .hljs-title, .hljs-template-variable, .hljs-type, .hljs-variable {
    color: #b58900;
}
.hljs-bullet, .hljs-link, .hljs-meta, .hljs-meta .hljs-keyword, .hljs-selector-attr, .hljs-selector-pseudo, .hljs-subst, .hljs-symbol {
    color: #cb4b16;
}
.hljs-built_in, .hljs-deletion {
    color: #dc322f;
}
.hljs-formula {
    background: #073642;
}
.hljs-emphasis {
    font-style: italic;
}
"""


# Solarized Light
solarized_light = """
h1, h2 {
    border-bottom: 1px solid;
}
html a:hover, html pre {
    background-color: #eee8d5;
}
blockquote, body, h1, h2, h3, h4, h5, h6, html, img, li, ol, p, ul {
    margin: 0;
    padding: 0;
    font: inherit;
    vertical-align: baseline;
}
img, ol, p, pre, ul {
    margin-bottom: 20px;
}
html * {
    font-family: ff-din-web-pro-1, ff-din-web-pro-2, sans-serif;
    font-size: 16px;
    line-height: 19.2px;
    color-profile: sRGB;
    color: #657b83;
}
body {
    margin: 40px 70px;
}
p {
    font-weight: lighter;
}
strong {
    font-weight: 700;
}
ol, ul {
    margin-left: 2em;
}
ol ol, ol ul, ul ol, ul ul {
    margin-top: 10px;
}
li {
    margin-bottom: 3px;
}
h1, h2, h3, h4, h5, h6 {
    font-weight: lighter;
    text-transform: capitalize;
    margin-top: 20px;
    margin-bottom: 10px;
}
.hljs-strong, h1, mark {
    font-weight: 700;
}
h1, h2 {
    font-size: 24.62px;
    line-height: 29.55px;
}
h3 {
    font-size: 23.44px;
    line-height: 28.13px;
}
h4, h5, h6 {
    font-size: 22.16px;
    line-height: 26.59px;
}
h1 img, h2 img, h3 img, h4 img, h5 img, h6 img, p img {
    margin-bottom: 0;
}
pre {
    white-space: pre;
    white-space: pre-wrap;
    word-wrap: break-word;
    padding: 15px;
}
code, pre {
    font-family: monospace;
}
blockquote {
    border-left: 4px solid;
    padding: 0 15px;
}
blockquote>:first-child {
    margin-top: 0;
}
blockquote>:last-child {
    margin-bottom: 15px;
}
h1 {
    text-transform: uppercase;
}
h3, h4, h5, h6 {
    border-bottom: none;
}
html body {
    background-color: #fdf6e3;
}
html h1, html h2, html h3, html h4, html h5, html h6 {
    border-color: #657b83;
}
html pre {
    color: #586e75;
}
html a, html a:active, html a:visited, html code.url, html h1, html h2, html h3, html h4, html h5, html h6 {
    color: #b58900;
}
@media print {
    body {
    margin: 0;
}
* {
    color: #000!important;
}
}
table {
    border-collapse: collapse;
}
td, th {
    border: 1px solid #657b83;
    padding: .5rem;
    text-align: left;
}
.hljs {
    display: block;
    overflow-x: auto;
    padding: .5em;
    background: #fdf6e3;
    color: #657b83;
}
.hljs-comment, .hljs-quote {
    color: #93a1a1;
}
.hljs-addition, .hljs-keyword, .hljs-selector-tag {
    color: #859900;
}
.hljs-doctag, .hljs-literal, .hljs-meta .hljs-meta-string, .hljs-number, .hljs-regexp, .hljs-string {
    color: #2aa198;
}
.hljs-name, .hljs-section, .hljs-selector-class, .hljs-selector-id, .hljs-title {
    color: #268bd2;
}
.hljs-attr, .hljs-attribute, .hljs-class .hljs-title, .hljs-template-variable, .hljs-type, .hljs-variable {
    color: #b58900;
}
.hljs-bullet, .hljs-link, .hljs-meta, .hljs-meta .hljs-keyword, .hljs-selector-attr, .hljs-selector-pseudo, .hljs-subst, .hljs-symbol {
    color: #cb4b16;
}
.hljs-built_in, .hljs-deletion {
    color: #dc322f;
}
.hljs-formula {
    background: #eee8d5;
}
.hljs-emphasis {
    font-style: italic;
}
"""


custom_css = ''

css = github # Github is the default style (css) applied to the markdown

# End of CSS declarations
