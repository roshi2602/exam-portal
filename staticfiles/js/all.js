$(function(){
var gal=$(".gallery").find("img").first();
var images=[
    //2 images ke path copy kie hai
    'https://www.ndtv.com/education/cache-static/media/presets/625X400/presets/900X600/article_images/2021/2/18/exam001.webp',
   'https://thumbs.dreamstime.com/z/final-exam-results-test-reading-books-words-concept-79093620.jpg'
];
//use javascript  fun in it
var i=0;
setInterval(function(){
        i=(i+1) %images.length; // for image format 0 ,1 ,2,0,1,2
        gal.fadeOut(function(){
            $(this).attr("src", images[i]);
            $(this).fadeIn();
         

         }); 
         console.log(gal.attr("src"));
}, 2000);
});
//images animations me show ho rahi hai aur fade in bhi ho rahi hai while changing




