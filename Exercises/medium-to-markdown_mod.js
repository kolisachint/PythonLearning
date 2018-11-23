const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl("https://medium.com/@kolisachint/test-b6c7c2e59abb").then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});