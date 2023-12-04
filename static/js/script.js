document.querySelector('#card').onclick = () =>{
    document.querySelector('#containered').classList.toggle('active');
  }
  
  document.querySelector('#cancel').onclick = () =>{
    document.querySelector('#containered').classList.remove('active');
  }

  let toggle = document.querySelector('.toggle');
         let navigation = document.querySelector('.navigation');
         let main = document.querySelector('.main');

         toggle.onclick = function(){
            navigation.classList.toggle('active');
            main.classList.toggle('active');
         } 