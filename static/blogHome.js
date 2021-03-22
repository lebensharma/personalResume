function dropdown() {
    if (document.getElementById('dropdownlogout').style.zIndex == -5) {
        document.getElementById('logoutdropping').style.background = "#5CE1E6";
        document.getElementById('dropdownlogout').style.zIndex = 5;
        document.getElementById('logoutdropping').style.color = "white";        
        document.getElementById('arrow').innerHTML = "&#9650";        
    }
    else {
        document.getElementById('dropdownlogout').style.zIndex = -5;
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