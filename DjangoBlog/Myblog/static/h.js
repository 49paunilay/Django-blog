console.log("I am loaded");
var script = document.createElement('script');
script.type = "text/javascript";
script.src="https://cdn.tiny.cloud/1/b3a8mf173d1g6yr3oa0h7lgol9evcx3jhewqd7983semvfsa/tinymce/5/tinymce.min.js";
document.head.appendChild(script);
script.onload = function(){
  console.log("Loaded");
    tinymce.init({
        selector: '#id_content',  // change this value according to your HTML
        menubar: 'tools',
        plugins: 'code',  
        //toolbar: 'code', 

      });
}
