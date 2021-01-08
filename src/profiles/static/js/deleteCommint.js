console.log('delete Commint .js is work')

var t=document.getElementsByClassName('delete')

for(var i=0;i<t.length;i++){
   
    t[i].addEventListener('click',function(e){
       e.preventDefault()
       var commint=this.children[1].value
       deleteCommint(commint)
    }//end function
    ) //end event listener 
    
        
 }//end for
 function deleteCommint(commint){
    url='/library/delete_commint/'
    fetch(url,{
        method:'POST',
        headers:{'Content-Type':'application/json','X-CSRFToken':csrftoken},
        body:JSON.stringify({
            'content':commint
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
            window.location.reload()
            
        }
    )//end then
 }//end function