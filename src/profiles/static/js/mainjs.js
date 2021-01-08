
var addViewer=document.getElementsByClassName('AddViewer')
console.log(addViewer)
if (usr =='AnonymousUser'){

    console.log('sorry you dont login plase login and try agin')

}//end if

else{

   for(var i=0 ;i<addViewer.length;i++){
        addViewer[i].addEventListener('click',function(e){
           
           var you=this.dataset.you 
           var slug=this.dataset.slug
           var action=this.dataset.action
           send(you,slug,action)
    
    }//end function
    )//end event listener
   }//end for 

}//end else

function send(you,slug,action){
    url='/library/reciveData/'
    fetch(url,{
        method:'POST',
        headers:{'Content-Type':'application/json','X-CSRFToken':csrftoken},
        body:JSON.stringify({
            'you':you,
            'slug':slug,
            'action':action
    })
    }//end object
    )//end fetch
    .then(
        function(response){
            return response.json()
        }//end function
    )//end then
    .then(
        function(data){
            console.log(data)
            
        }
    )//end then
}//end function


