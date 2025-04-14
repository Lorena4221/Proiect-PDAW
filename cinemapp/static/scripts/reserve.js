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

var dropbutton = document.getElementById("dropbutton");
dropbutton.addEventListener('click', function()
{
    document.getElementById("dropcontent").classList.toggle("contentshow");
});

var dropcontent = document.querySelector(".dropcontent");
var dropelements = dropcontent.querySelectorAll("a");

dropelements.forEach(function(a){
    a.addEventListener("click", function()
    {
        dropbutton.textContent = a.textContent;
        document.getElementById("formularinch").style.display = "flex";
    });
});

window.onclick = function(event){
    if (!event.target.matches('.dropdownbutton'))
    {
        if (dropcontent.classList.contains("contentshow"))
        {
            dropcontent.classList.remove("contentshow");
        }
    }
}

var months = document.getElementById("month");
var years = document.getElementById("year");
var days = document.getElementById("day");

function onChange() {
  var value = months.value;
  var text = months.options[months.selectedIndex].text;
    days.selectedIndex = 0;
    for (i = 28; i<=31; i++)
    {
        if (days.options[i].classList.contains("contenthide"))
            days.options[i].classList.remove("contenthide");
    }
    if (value == "februarie")
    {
        days.options[31].classList.toggle("contenthide");
        days.options[30].classList.toggle("contenthide");
        if (years.value % 4 != 0)
        days.options[29].classList.toggle("contenthide");
    } 
    if (value == "aprilie")
    {
        days.options[31].classList.toggle("contenthide");
    } 
    if (value == "iunie")
    {
        days.options[31].classList.toggle("contenthide");
    } 
    if (value == "septembrie")
    {
        days.options[31].classList.toggle("contenthide");
    } 
    if (value == "noiembrie")
    {
        days.options[31].classList.toggle("contenthide");
    }  
}

months.onchange = onChange;
years.onchange = onChange;
onChange();




