var close=document.getElementsByClassName('close')
var cls2=document.getElementsByClassName('commint_back')
console.log('close',close)

for(var i=0;i<close.length;i++){
    close[i].addEventListener('click',function(e){
        for(var j=0;j<cls2.length;j++){
            cls2[j].classList.remove('show')
            

        }//end for j
    }//end function
    )//end event listener
}//end for