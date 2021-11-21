function dropdown() {
    if (document.getElementById('dropdownlogout').style.zIndex == -5) {
        document.getElementById('logoutdropping').style.background = "#5CE1E6";
        document.getElementById('dropdownlogout').style.zIndex = 5;
        document.getElementById('dropdownlogout').style.opacity = 1;
        document.getElementById('logoutdropping').style.color = "white";        
        document.getElementById('arrow').innerHTML = "&#9650";        
    }
    else {
        document.getElementById('dropdownlogout').style.zIndex = -5;
        document.getElementById('dropdownlogout').style.opacity = 0;
        document.getElementById('logoutdropping').style.background = "#F6F3F3";
        document.getElementById('logoutdropping').style.color = "black";
        document.getElementById('arrow').innerHTML = "&#9660"; 
    };
};

function dropup() {
    if (document.getElementById('dropdownlogout').style.zIndex == 5) {
        document.getElementById('dropdownlogout').style.zIndex = -5;
        document.getElementById('logoutdropping').style.background = "#F6F3F3";
        document.getElementById('logoutdropping').style.color = "black";
        document.getElementById('arrow').innerHTML = "&#9660"; 
    };
};

function pullLeft() {
    if (document.getElementById('left').style.left == '-35vw') {   
        document.getElementById('left').style.left = '0vw';    
    }
    else {
        document.getElementById('left').style.left = '-35vw';
    };
};

function pushLeft() {
    if (document.getElementById('left').style.left == '0vw') {
        document.getElementById('left').style.left = '-35vw';
        
    }
    else {
        return none
    }
    
};

function drop() {
    if (document.getElementById('mdrop').style.zIndex == -5) {
        document.getElementById('mdrop').style.zIndex = 5;
        document.getElementById('mdrop').style.opacity = 1;      
    }    
    else {
        document.getElementById('mdrop').style.zIndex = -5;
        document.getElementById('mdrop').style.opacity = 0;
    }
}
