var menu=document.getElementsByClassName('all-option')
var option=document.getElementsByClassName('base')
console.log('option:',option)

option[0].addEventListener('click',function(){ 
    menu[0].classList.toggle("display-option")
    
    console.log( this.children[1].textContent)
    
})