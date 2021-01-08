//commint section
var cls=document.getElementsByClassName('commint')
var cls2=document.getElementsByClassName('commint_back')

console.log('cls2',cls2)
console.log('cls',cls)
for(var i=0; i<cls.length;i++){
    
cls[i].addEventListener('click',function (e){
    e.preventDefault()
    for(var j=0;j<cls2.length;j++){
        cls2[j].classList.toggle('show')
    }//end for j
}//end function
)//end litener
}//end for
//end commint section