var prev = sessionStorage.getItem('lan');



var languageRadio = document.getElementsByClassName("toggle_option");
var en_text = document.getElementsByClassName("en-text");
var ru_text = document.getElementsByClassName("ru-text");

for(let i = 0; i < languageRadio.length; i++){
    languageRadio[i].addEventListener("click", function() {
        change_lan(this.value);
    });
}

if(prev != null && prev != 'EN'){
    for(let i = 0; i < languageRadio.length; i++){
        if(languageRadio[i].value == prev){
            languageRadio[i].checked = true;
        }
    }
}


change_lan(prev);

function change_lan(value){
    let en_display = "inline-block", ru_display= "none";
    if(value === "RU"){
        en_display = "none";
        ru_display = "inline-block";
    }
    for(let i = 0; i < en_text.length; i++){
        en_text[i].style.display = en_display;
    }
    for(let i = 0; i < ru_text.length; i++){
        ru_text[i].style.display = ru_display;
    }
    sessionStorage.setItem('lan', value);
}



function create_list(){
    var courses = document.getElementsByClassName("course-list");
    for(let i = 0; i < courses.length; i++){
        console.log(courses[i]);
        courses[i].href = courses[i].href + '?value=' + courses[i].id;
    }
}
create_list();

function list(){
    var courses = document.getElementsByClassName("list");
    for(let i = 0; i < courses.length; i++){
        console.log(courses[i]);
        courses[i].href = courses[i].href + '?theory=' + courses[i].id;
    }
}
list();

function homework(){
    var courses = document.getElementsByClassName("homework");
    for(let i = 0; i < courses.length; i++){
        console.log(courses[i]);
        courses[i].href = courses[i].href + '?homework=' + courses[i].id;
    }
}
homework();
