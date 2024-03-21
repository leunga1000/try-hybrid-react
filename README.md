
# React + a wider site

How to bridge to react components from a pre-existing website.


Uses vite - implements the vite development mode, so allows hot module reloading, and then you can customise the rollup options to output one js bundle file. 

Then you get HMR even with the browser mode import. 

Will need to add development only clause around your html imports.

Needs the react preamble to occur before the vite imports.

Haven't solved the issue with serving assets yet, think its some rewiring on the server side to point to the relevant folder in dev mode and prod mode.


If you're happy for a full stack solution then you could also consider astro.js. But if you want to retain the basics up approach then can try this.


The use of the react modules is shown in the public/index.html file which is served by the web server.




