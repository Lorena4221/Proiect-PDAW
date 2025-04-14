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