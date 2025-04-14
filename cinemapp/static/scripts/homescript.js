var menu = document.querySelector('.menu');
var menuItems = menu.querySelectorAll('.linkitems');
menuItems.forEach(function(a)
{
    a.addEventListener('mouseover', function(){
      this.style.color = 'rgb(179, 0, 255)';
    });
    a.addEventListener('mouseout', function(){
      this.style.color = 'white';
    });
});

var filmHourDivs = document.querySelectorAll('li .filmhours');

filmHourDivs.forEach(function(div)
{
    div.addEventListener('mouseover', function() {
        this.style.backgroundColor = 'rgb(108, 0, 154)';
      });
    
      div.addEventListener('mouseout', function() {
        this.style.backgroundColor = 'rgb(179, 0, 255)';
      });
});

var tableFilms = document.querySelector('.tablefilms')
var trFilms = tableFilms.querySelectorAll('tr');

trFilms.forEach(function(tr){
    tr.addEventListener('mouseover', function(){
      var tdFilms = this.querySelectorAll('td:not(.tablefilmstd)');
      tdFilms.forEach(td => {
        this.classList.remove('unhoverTR');
        this.classList.add('hoverTR');
      });
    });

    tr.addEventListener('mouseout', function() {
      var tdFilms = this.querySelectorAll('td:not(.tablefilmstd)');
      tdFilms.forEach(td => {
        this.classList.remove('hoverTR');
        this.classList.add('unhoverTR');
      });
    });
});