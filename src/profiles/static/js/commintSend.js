var evet=document.getElementsByClassName('forms')



for(var i=0;i<evet.length;i++){
   
   evet[i].addEventListener('submit',function(e){
      e.preventDefault()
      var commint=this.children[2]
      if (commint.value==''){console.log('commint:','empty')}
      else{
         slug=this.children[1].value
         commints=commint.value
         sendInformation(slug,commints)
      }
      
       
   }//end function
   ) //end event listener 
   
       
}//end for

function sendInformation(slug,commints){
   url='/library/create_commint/'
   fetch(url,{
       method:'POST',
       headers:{'Content-Type':'application/json','X-CSRFToken':csrftoken},
       body:JSON.stringify({
           'slug':slug,
           'content':commints
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